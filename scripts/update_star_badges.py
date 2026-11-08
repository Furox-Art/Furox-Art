#!/usr/bin/env python3
"""Keep the README star badges inside the repository.

The star column used to point at ``img.shields.io``. Shields answers with ``429``
when it is busy, GitHub's image proxy caches that failure, and the cell then
renders as the bare alt text "Stars" -- a handful of rows looked broken while
their neighbours looked fine, with no difference in the markup to explain it.

These badges are generated here instead: one SVG per repository under
``assets/stars/``, refreshed by ``.github/workflows/star-badges.yml`` from the
GitHub API. Nothing external is fetched when a reader opens the page, so the
column cannot half-render.

Usage:
    python scripts/update_star_badges.py            # refresh counts and rewrite README
    python scripts/update_star_badges.py --check    # verify the README is self-hosted
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
BADGE_DIR = ROOT / "assets" / "stars"
OWNER = "Furox-Art"

SHIELDS_STARS = re.compile(
    r'<img src="https://img\.shields\.io/github/stars/'
    r'(?P<owner>[A-Za-z0-9-]+)/(?P<repo>[A-Za-z0-9._-]+)[^"]*"'
    r'\s+alt="(?P<alt>[^"]*)"\s*/?>'
)
#: The account-level badge in the header: total stars across the listed projects.
SHIELDS_TOTAL = re.compile(
    r'<img src="https://img\.shields\.io/github/stars/(?P<owner>[A-Za-z0-9-]+)\?[^"]*"'
    r'\s+alt="(?P<alt>[^"]*)"[^>]*/?>'
)
TOTAL_BADGE = '<img src="assets/stars/total.svg" alt="total stars" height="28"/>'
LOCAL_STARS = re.compile(r'<img src="assets/stars/(?P<repo>[A-Za-z0-9._-]+)\.svg"')

FONT = "Verdana,Geneva,DejaVu Sans,sans-serif"


def badge_svg(count: int) -> str:
    """Render a for-the-badge-style star counter.

    Same shape as the shields badge it replaces (28px tall, rounded, light text
    on a dark plate) so the column keeps the look the rest of the README has.
    """
    visible = f"\u2605 {count}"
    # Bold 11px Verdana runs about 7.2px per character; the plate needs padding
    # on both sides.
    width = max(40, int(len(visible) * 7.2) + 24)
    # The star is written as a numeric entity so the file stays pure ASCII: an
    # SVG fetched without a charset can be decoded as ISO-8859-1, which turns a
    # literal star into mojibake.
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="28" '
        f'role="img" aria-label="{count} stars">\n'
        f"  <title>{count} stars</title>\n"
        f'  <rect width="{width}" height="28" rx="4" fill="#24292f"/>\n'
        f'  <text x="{width / 2:.1f}" y="18.5" fill="#ffffff" font-family="{FONT}" '
        f'font-size="11" font-weight="bold" letter-spacing=".4" '
        f'text-anchor="middle">&#9733; {count}</text>\n'
        "</svg>\n"
    )


def fetch_stars(repo: str, token: str | None) -> int:
    """Star count for ``OWNER/repo``, or 0 when the API cannot answer."""
    request = urllib.request.Request(
        f"https://api.github.com/repos/{OWNER}/{repo}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "furox-art-star-badges",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return int(json.loads(response.read().decode("utf-8"))["stargazers_count"])
    except Exception as error:  # noqa: BLE001 - a badge must never break the build
        print(f"WARN: could not read stars for {repo}: {error}", file=sys.stderr)
        return 0


def rewrite_readme(text: str) -> tuple[str, list[str]]:
    """Point every star badge at the local SVG; return the text and repo names."""
    repos: list[str] = []

    def replace(match: re.Match[str]) -> str:
        repo = match.group("repo")
        if repo not in repos:
            repos.append(repo)
        return f'<img src="assets/stars/{repo}.svg" alt="{repo} stars"/>'

    return SHIELDS_STARS.sub(replace, text), repos


def check() -> int:
    """Fail when the README would fetch a star badge from outside the repository."""
    text = README.read_text(encoding="utf-8")
    problems: list[str] = []
    for match in SHIELDS_STARS.finditer(text):
        problems.append(
            f"README.md still fetches a star badge from img.shields.io for "
            f"{match.group('repo')}; run scripts/update_star_badges.py"
        )
    if SHIELDS_TOTAL.search(text):
        problems.append(
            "README.md still fetches the account-level star badge from img.shields.io; "
            "run scripts/update_star_badges.py"
        )
    referenced = {match.group("repo") for match in LOCAL_STARS.finditer(text)}
    referenced.discard("total")
    on_disk = {path.stem for path in BADGE_DIR.glob("*.svg")}
    on_disk.discard("total")
    if "assets/stars/total.svg" in text and not (BADGE_DIR / "total.svg").is_file():
        problems.append("README.md links assets/stars/total.svg, which does not exist")
    for repo in sorted(referenced - on_disk):
        problems.append(
            f"README.md links assets/stars/{repo}.svg, which does not exist"
        )
    for repo in sorted(on_disk - referenced):
        problems.append(f"assets/stars/{repo}.svg exists but no row uses it")
    for problem in problems:
        print(f"FAIL: {problem}")
    if not problems:
        print(f"OK: {len(referenced)} star badges are generated in assets/stars/")
        print("OK: the header total comes from assets/stars/total.svg")
    return 1 if problems else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify, do not rewrite")
    args = parser.parse_args(argv)

    if args.check:
        return check()

    text = README.read_text(encoding="utf-8")
    updated, repos = rewrite_readme(text)
    # The header badge counts the whole portfolio: the sum of the rows below it.
    updated = SHIELDS_TOTAL.sub(TOTAL_BADGE, updated)
    if not repos:
        repos = sorted(
            {match.group("repo") for match in LOCAL_STARS.finditer(updated)} - {"total"}
        )
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    BADGE_DIR.mkdir(parents=True, exist_ok=True)
    counts: dict[str, int] = {}
    for repo in repos:
        counts[repo] = fetch_stars(repo, token)
        (BADGE_DIR / f"{repo}.svg").write_text(
            badge_svg(counts[repo]), encoding="utf-8"
        )
        print(f"{repo}: {counts[repo]}")
    total = sum(counts.values())
    (BADGE_DIR / "total.svg").write_text(badge_svg(total), encoding="utf-8")
    print(f"total: {total}")
    if updated != text:
        README.write_text(updated, encoding="utf-8")
        print("README.md rewritten to use the local badges")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
