<img src="assets/profile-banner.svg" width="100%" alt="Furox — Scientific computing, mathematical modeling, AI reasoning and verification"/>

<p align="center">
  <strong>Independent researcher & developer building rigorous, auditable systems for scientific computing, mathematical modeling, AI reasoning, and verification.</strong><br>
  Reproducible computation · explicit assumptions · deterministic verification · falsifiable models
</p>

<p align="center">
  <img src="assets/stars/total.svg" alt="total stars" height="28"/>
</p>

---

## About

Independent developer and researcher working across **AI systems** and **scientific computing**, mostly on software where the reasoning is explicit rather than implicit: numerical algorithms you can read end to end, models whose assumptions are written down, and AI agents whose claims are checked by deterministic machinery instead of trust.

The work runs along two threads:

- **Scientific computing from first principles** — from-scratch numerical libraries with zero runtime dependencies, where the algorithm *is* the documentation, alongside a NumPy/SciPy production line for accelerated and optionally GPU-backed work.
- **Deterministic verification for AI** — turning model output and agent plans into sealed contracts, hash-chained evidence, and PASS / FAIL gates, so that *done* means *here is the command output that proves it*.

Everything is built openly and tested: property, fuzz, oracle, cross-platform, and benchmark-regression suites run in CI, with provenance attestations carried on published artifacts where the packaging supports it.

---

The star counts below are generated into [`assets/stars/`](assets/stars) by [`scripts/update_star_badges.py`](scripts/update_star_badges.py) and refreshed daily by `star-badges.yml`, so the column never depends on a third-party badge service — a shields.io `429`, cached by the image proxy, used to leave individual cells showing bare alt text while their neighbours looked fine.

## Featured Projects

<table>
  <tr>
    <th width="180" align="left">Project</th>
    <th width="115" align="center">⭐</th>
    <th width="140" align="left">Stack</th>
    <th align="left">What it does</th>
  </tr>
  <tr>
    <td><a href="https://github.com/Furox-Art/polyglot-python"><strong>polyglot-python</strong></a></td>
    <td align="center"><a href="https://github.com/Furox-Art/polyglot-python/stargazers"><img src="assets/stars/polyglot-python.svg" alt="polyglot-python stars"/></a></td>
    <td>Python · MIT</td>
    <td>A deterministic keyword transpiler: write Python with localized keywords in 20 locales — Turkish, Spanish, Portuguese, German, French, Chinese, Hindi, Arabic, Russian, Italian, Dutch, Polish, Indonesian, Vietnamese, Japanese, Korean, Ukrainian, Romanian, Swedish and Greek — and it maps them to real Python and hands the result to CPython. No AI, no network, no randomness. <strong>Not a prose-to-code translator.</strong> PyPI + npm wrapper; Python 3.12+.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Furox-Art/scientific-computing-system"><strong>scientific-computing-system</strong></a></td>
    <td align="center"><a href="https://github.com/Furox-Art/scientific-computing-system/stargazers"><img src="assets/stars/scientific-computing-system.svg" alt="scientific-computing-system stars"/></a></td>
    <td>Python · MIT</td>
    <td>Pure-Python computational science platform with <strong>zero runtime dependencies</strong>: linear algebra, ODE/PDE solvers, Monte Carlo, statistics, signal processing, uncertainty and dimensional analysis, reproducible workflows. Published on PyPI; npm ships a Python CLI launcher, not a JavaScript engine. Python 3.11+.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Furox-Art/axiomize"><strong>axiomize</strong></a></td>
    <td align="center"><a href="https://github.com/Furox-Art/axiomize/stargazers"><img src="assets/stars/axiomize.svg" alt="axiomize stars"/></a></td>
    <td>Python · MIT</td>
    <td>The scientific <strong>modeling layer</strong> (the numerical library lives in scientific-computing-system): explicit, versioned Model IR, mandatory units, dimensional/numerical validation, calibration, uncertainty analysis, SBML/CellML/Modelica export. CLI, REST and MCP (<code>axiomize mcp</code>); <code>pip install axiomize</code>.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Furox-Art/scientific-computing-system-2.0"><strong>scientific-computing-system-2.0</strong></a></td>
    <td align="center"><a href="https://github.com/Furox-Art/scientific-computing-system-2.0/stargazers"><img src="assets/stars/scientific-computing-system-2.0.svg" alt="scientific-computing-system-2.0 stars"/></a></td>
    <td>Python · MIT</td>
    <td>The <strong>NumPy build</strong> of scientific-computing-system — not a separate product: the NumPy/SciPy/pandas/matplotlib line with guided fitting, held-out diagnostics, replay manifests, drift checks, optional compiled C kernels and CuPy GPU execution. PyPI + npm.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Furox-Art/scientific-reasoning-auditor"><strong>scientific-reasoning-auditor</strong></a></td>
    <td align="center"><a href="https://github.com/Furox-Art/scientific-reasoning-auditor/stargazers"><img src="assets/stars/scientific-reasoning-auditor.svg" alt="scientific-reasoning-auditor stars"/></a></td>
    <td>Python · Node.js · MIT</td>
    <td>Audits scientific-manuscript reasoning with source-linked claim/evidence/method/assumption/inference graphs, review-risk flags, semantic-review templates and reproducibility fingerprints; independently recalculates supported two-group Welch t-tests. Findings are review signals, not scientific verdicts or proof of semantic entailment.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Furox-Art/polyglot-code-guard"><strong>polyglot-code-guard</strong></a></td>
    <td align="center"><a href="https://github.com/Furox-Art/polyglot-code-guard/stargazers"><img src="assets/stars/polyglot-code-guard.svg" alt="polyglot-code-guard stars"/></a></td>
    <td>Python · MIT</td>
    <td>Fail-closed test gate for AI-generated code: detects Python, Rust, Go, JavaScript/TypeScript, Java, C#, PHP, Ruby, Swift and C/C++ projects, then runs configured test/build commands. Returns PASS only when every required check succeeds. Includes a coding-agent skill and TOML overrides; PASS is test evidence, not proof of correctness.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Furox-Art/plan-auditor"><strong>plan-auditor</strong></a></td>
    <td align="center"><a href="https://github.com/Furox-Art/plan-auditor/stargazers"><img src="assets/stars/plan-auditor.svg" alt="plan-auditor stars"/></a></td>
    <td>Python · MIT</td>
    <td>Makes an agent's <em>done</em> mean <em>here is the command output that proves it</em>: LLM-free verification with sealed plans, SHA-256 hash-chained evidence, STRIPS/PDDL reachability and a fail-closed PASS / FAIL / UNKNOWN gate. PyPI + npm.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Furox-Art/quantum-reasoning-skill"><strong>quantum-reasoning-skill</strong></a></td>
    <td align="center"><a href="https://github.com/Furox-Art/quantum-reasoning-skill/stargazers"><img src="assets/stars/quantum-reasoning-skill.svg" alt="quantum-reasoning-skill stars"/></a></td>
    <td>Python · MIT</td>
    <td>Model-agnostic Agent Skill that keeps genuinely different hypotheses alive, tests each against evidence, revives alternatives and collapses to the best-supported answer. <strong>Quantum-inspired metaphor, not quantum computing.</strong> Status: protocol and controller benchmark published; model evaluation pending. PyPI + npm.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Furox-Art/eq-layer"><strong>eq-layer</strong></a></td>
    <td align="center"><a href="https://github.com/Furox-Art/eq-layer/stargazers"><img src="assets/stars/eq-layer.svg" alt="eq-layer stars"/></a></td>
    <td>Python · MIT</td>
    <td>A control layer that decides how an LLM should speak before it speaks: affect/intent tracking, Bayesian-risk action routing, conversation repair, policy steering. Early stage; evaluations preliminary; <strong>not a factual truth checker.</strong></td>
  </tr>
  <tr>
    <td><a href="https://github.com/Furox-Art/nomosguard"><strong>nomosguard</strong></a></td>
    <td align="center"><a href="https://github.com/Furox-Art/nomosguard/stargazers"><img src="assets/stars/nomosguard.svg" alt="nomosguard stars"/></a></td>
    <td>Python · Apache-2.0</td>
    <td>Deterministic security reasoning core: <strong>LLMs produce evidence; deterministic machinery decides.</strong> Append-only hash-chained evidence ledger, rule-derived threat/access paths, fail-closed deny-by-default policy gate. Models never cross the decision boundary.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Furox-Art/literature-evidence-mcp"><strong>literature-evidence-mcp</strong></a></td>
    <td align="center"><a href="https://github.com/Furox-Art/literature-evidence-mcp/stargazers"><img src="assets/stars/literature-evidence-mcp.svg" alt="literature-evidence-mcp stars"/></a></td>
    <td>Python · TypeScript · Rust · Go · C++ · Apache-2.0</td>
    <td>Scientific literature and evidence-provenance MCP server: multi-provider search, citation and retraction checks, quote verification, evidence logs. v0.5.1 is a bibliographic/traceability and evidence-audit toolset — <strong>not</strong> an automated peer reviewer, meta-analysis engine or scientific truth oracle.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Furox-Art/scientific-toolkit"><strong>scientific-toolkit</strong></a></td>
    <td align="center"><a href="https://github.com/Furox-Art/scientific-toolkit/stargazers"><img src="assets/stars/scientific-toolkit.svg" alt="scientific-toolkit stars"/></a></td>
    <td>Python · Apache-2.0</td>
    <td>Provider-neutral <strong>MCP gateway for nine existing public repositories</strong>; upstream packages stay independent with their own names and versions. Published on PyPI as scientific-toolkit-mcp; local stdio and Streamable HTTP transports. An integration hub, not a source merge.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Furox-Art/axiomize-quantum-skills-2.0"><strong>axiomize-quantum-skills-2.0</strong></a></td>
    <td align="center"><a href="https://github.com/Furox-Art/axiomize-quantum-skills-2.0/stargazers"><img src="assets/stars/axiomize-quantum-skills-2.0.svg" alt="axiomize-quantum-skills-2.0 stars"/></a></td>
    <td>Python · MIT</td>
    <td>Ships <code>axiomize</code> and <code>quantum-reasoning-skill</code> <strong>together</strong> in one package line — not a separate product and not a second MCP registration. Install this one for both; install the upstream repos when you need only one.</td>
  </tr>
</table>

---

## All public repositories

Every project repository owned by this account, grouped by role. The **Featured Projects** table above describes the main ones in detail.

- **Scientific computing** — [scientific-computing-system](https://github.com/Furox-Art/scientific-computing-system) · [scientific-computing-system-2.0](https://github.com/Furox-Art/scientific-computing-system-2.0) · [axiomize](https://github.com/Furox-Art/axiomize) · [axiomize-quantum-skills-2.0](https://github.com/Furox-Art/axiomize-quantum-skills-2.0)
- **Verification, auditing & security** — [plan-auditor](https://github.com/Furox-Art/plan-auditor) · [nomosguard](https://github.com/Furox-Art/nomosguard) · [scientific-reasoning-auditor](https://github.com/Furox-Art/scientific-reasoning-auditor) · [polyglot-code-guard](https://github.com/Furox-Art/polyglot-code-guard)
- **Agent skills & tooling** — [quantum-reasoning-skill](https://github.com/Furox-Art/quantum-reasoning-skill) · [eq-layer](https://github.com/Furox-Art/eq-layer) · [literature-evidence-mcp](https://github.com/Furox-Art/literature-evidence-mcp) · [scientific-toolkit](https://github.com/Furox-Art/scientific-toolkit) · [repocraft](https://github.com/Furox-Art/repocraft) · [polyglot-python](https://github.com/Furox-Art/polyglot-python)

Full, automatically updated list: [github.com/Furox-Art?tab=repositories](https://github.com/Furox-Art?tab=repositories).
