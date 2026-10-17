<img src="assets/profile-banner.svg" width="100%" alt="Furox — Scientific computing, mathematical modeling, AI reasoning and verification"/>

<p align="center">
  <strong>Independent researcher & developer building rigorous, auditable systems for scientific computing, mathematical modeling, AI reasoning, and verification.</strong><br>
  Reproducible computation · explicit assumptions · deterministic verification · falsifiable models
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/Furox-Art?style=flat-square&logo=github&label=Stars" alt="Stars"/>
</p>

---

## About

Independent developer and researcher working across **AI systems** and **scientific computing**, mostly on software where the reasoning is explicit rather than implicit: numerical algorithms you can read end to end, models whose assumptions are written down, and AI agents whose claims are checked by deterministic machinery instead of trust.

The work runs along two threads:

- **Scientific computing from first principles** — from-scratch numerical libraries with zero runtime dependencies, where the algorithm *is* the documentation, alongside a NumPy/SciPy production line for accelerated and optionally GPU-backed work.
- **Deterministic verification for AI** — turning model output and agent plans into sealed contracts, hash-chained evidence, and PASS / FAIL gates, so that *done* means *here is the command output that proves it*.

Everything is built openly and tested: property, fuzz, oracle, cross-platform, and benchmark-regression suites run in CI, with provenance attestations carried on published artifacts where the packaging supports it.

---

## Featured Projects

| Project / GitHub release | ⭐ | Stack | What it does |
| --- | --- | --- | --- |
| [**scientific-computing-system**](https://github.com/Furox-Art/scientific-computing-system) · [![Latest release](https://img.shields.io/github/v/release/Furox-Art/scientific-computing-system?style=flat-square&label=release&cacheSeconds=300)](https://github.com/Furox-Art/scientific-computing-system/releases/latest) | [![GitHub stars](https://badgen.net/github/stars/Furox-Art/scientific-computing-system)](https://github.com/Furox-Art/scientific-computing-system/stargazers) | Python · MIT | Zero-runtime-dependency pure-Python numerical computing: linear algebra, ODE/PDE solvers, Monte Carlo, signal processing, statistics, and uncertainty analysis. Optional NumPy/SciPy backends. Published on PyPI; npm provides a Python CLI launcher, not a separate JavaScript numerical engine. CI and provenance documented. |
| [**axiomize**](https://github.com/Furox-Art/axiomize) · [![Latest release](https://img.shields.io/github/v/release/Furox-Art/axiomize?style=flat-square&label=release&cacheSeconds=300)](https://github.com/Furox-Art/axiomize/releases/latest) | [![GitHub stars](https://badgen.net/github/stars/Furox-Art/axiomize)](https://github.com/Furox-Art/axiomize/stargazers) | Python · MIT | Scientific **modeling layer**, distinct from the numerical library: versioned Model IR, mandatory units, dimensional/numerical validation, calibration, uncertainty analysis, and SBML/CellML/Modelica export. Python, CLI, REST, and MCP interfaces; PyPI/npm distributions and documented CI. |
| [**scientific-computing-system-2.0**](https://github.com/Furox-Art/scientific-computing-system-2.0) · [![Latest release](https://img.shields.io/github/v/release/Furox-Art/scientific-computing-system-2.0?style=flat-square&label=release&cacheSeconds=300)](https://github.com/Furox-Art/scientific-computing-system-2.0/releases/latest) | [![GitHub stars](https://badgen.net/github/stars/Furox-Art/scientific-computing-system-2.0)](https://github.com/Furox-Art/scientific-computing-system-2.0/stargazers) | Python · MIT | The **NumPy/SciPy build of scientific-computing-system**, not a separate product. Adds guided fitting, held-out diagnostics, replay manifests and dependency/confidence-interval drift checks, optional compiled C kernels and CuPy GPU execution. Published on PyPI; npm is a Python launcher. Repository documents extensive tests and branch coverage. |
| [**plan-auditor**](https://github.com/Furox-Art/plan-auditor) · [![Latest release](https://img.shields.io/github/v/release/Furox-Art/plan-auditor?style=flat-square&label=release&cacheSeconds=300)](https://github.com/Furox-Art/plan-auditor/releases/latest) | [![GitHub stars](https://badgen.net/github/stars/Furox-Art/plan-auditor)](https://github.com/Furox-Art/plan-auditor/stargazers) | Python · MIT | Independent, LLM-free behavioral verification of AI agents' work: sealed execution contracts, SHA-256 hash-chained evidence, HMAC-authenticated completion gates, STRIPS/PDDL reachability, and fail-closed PASS / FAIL / UNKNOWN results. Available through PyPI, an npm Python launcher, and a GitHub Action. |
| [**quantum-reasoning-skill**](https://github.com/Furox-Art/quantum-reasoning-skill) · [![Latest release](https://img.shields.io/github/v/release/Furox-Art/quantum-reasoning-skill?style=flat-square&label=release&cacheSeconds=300)](https://github.com/Furox-Art/quantum-reasoning-skill/releases/latest) | [![GitHub stars](https://badgen.net/github/stars/Furox-Art/quantum-reasoning-skill)](https://github.com/Furox-Art/quantum-reasoning-skill/stargazers) | Python · MIT | Model-agnostic Agent Skill for maintaining competing hypotheses, checking evidence, and reviving alternatives. Includes a branch controller and deterministic benchmark harness; distributed through PyPI and npm. **Quantum-inspired, not quantum computing.** Baseline-versus-skill model performance has **not** been established. |
| [**eq-layer**](https://github.com/Furox-Art/eq-layer) · [![Latest release](https://img.shields.io/github/v/release/Furox-Art/eq-layer?style=flat-square&label=release&cacheSeconds=300)](https://github.com/Furox-Art/eq-layer/releases/latest) | [![GitHub stars](https://badgen.net/github/stars/Furox-Art/eq-layer)](https://github.com/Furox-Art/eq-layer/stargazers) | Python · MIT | Early-stage dialogue-control system with affect/intent tracking, Bayesian-risk action routing, conversation repair, policy steering, and structural response audits. Packaged as an Agent Skill for multiple coding-agent ecosystems. Development evaluations are preliminary; it is **not** a factual truth checker. |
| [**nomosguard**](https://github.com/Furox-Art/nomosguard) · [![Latest release](https://img.shields.io/github/v/release/Furox-Art/nomosguard?style=flat-square&label=release&cacheSeconds=300)](https://github.com/Furox-Art/nomosguard/releases/latest) | [![GitHub stars](https://badgen.net/github/stars/Furox-Art/nomosguard)](https://github.com/Furox-Art/nomosguard/stargazers) | Python · Apache-2.0 | Early-stage, deterministic security reasoning: hash-chained evidence ledger, CVE/log ingestion, rule-derived attack paths, and a deny-by-default policy gate. LLMs can explain or propose evidence but cannot decide. Reproducible test/benchmark scenarios and opt-in containment planning are documented; no unattended action by default. |
| [**scientific-toolkit**](https://github.com/Furox-Art/scientific-toolkit) · [![Latest release](https://img.shields.io/github/v/release/Furox-Art/scientific-toolkit?style=flat-square&label=release&cacheSeconds=300)](https://github.com/Furox-Art/scientific-toolkit/releases/latest) | [![GitHub stars](https://badgen.net/github/stars/Furox-Art/scientific-toolkit)](https://github.com/Furox-Art/scientific-toolkit/stargazers) | Python · Apache-2.0 | Provider-neutral MCP gateway connecting **seven independent repositories**, not merging their code. Supports local stdio and bearer-token-authenticated Streamable HTTP; published as a PyPI package. Verified loopback deployment checks cover integration only, **not** scientific correctness or external-client login; OAuth is not configured. |

---

## Open Source Contributions

All 20 merged pull requests in repositories outside this account, highest-starred first:

<table>
<tr>
<th>Repository</th>
<th>Stars</th>
<th>Contribution</th>
</tr>
<tr>
<td><a href="https://github.com/coollabsio/coolify"><code>coollabsio/coolify</code></a></td>
<td>63k</td>
<td><a href="https://github.com/coollabsio/coolify/pull/12066">#12066</a> — fix(api): respect service_name query param in application logs endpoint</td>
</tr>
<tr>
<td><a href="https://github.com/pingdotgg/t3code"><code>pingdotgg/t3code</code></a></td>
<td>27.9k</td>
<td><a href="https://github.com/pingdotgg/t3code/pull/16838">#16838</a> — fix(server): a directory no longer resolves as the resource monitor binary</td>
</tr>
<tr>
<td><a href="https://github.com/TabularisDB/tabularis"><code>TabularisDB/tabularis</code></a></td>
<td>5.2k</td>
<td><a href="https://github.com/TabularisDB/tabularis/pull/1076">#1076</a> — feat(command-palette): add a toggle editor word wrap command (closes #1036)</td>
</tr>
<tr>
<td><a href="https://github.com/libredb/libredb-studio"><code>libredb/libredb-studio</code></a></td>
<td>1.2k</td>
<td><a href="https://github.com/libredb/libredb-studio/pull/1637">#1637</a> — docs: add missing libSQL row to test-database table</td>
</tr>
<tr>
<td><a href="https://github.com/Mudlet/Mudlet"><code>Mudlet/Mudlet</code></a></td>
<td>916</td>
<td><a href="https://github.com/Mudlet/Mudlet/pull/10780">#10780</a> — fix: keep Lua autocomplete popup from stealing editor focus</td>
</tr>
<tr>
<td><a href="https://github.com/vaadin/web-components"><code>vaadin/web-components</code></a></td>
<td>584</td>
<td><a href="https://github.com/vaadin/web-components/pull/13064">#13064</a> — docs: add online IDE reproduction link to bug report template</td>
</tr>
<tr>
<td><a href="https://github.com/Dokploy/templates"><code>Dokploy/templates</code></a></td>
<td>231</td>
<td><a href="https://github.com/Dokploy/templates/pull/1171">#1171</a> — feat: add VersityGW template</td>
</tr>
<tr>
<td><a href="https://github.com/issuerd/issuerd"><code>issuerd/issuerd</code></a></td>
<td>51</td>
<td><a href="https://github.com/issuerd/issuerd/pull/18">#18</a> — test: add proptest suites for issuerd-protocol parsers</td>
</tr>
<tr>
<td><a href="https://github.com/TheVicky1/Pact_OS"><code>TheVicky1/Pact_OS</code></a></td>
<td>28</td>
<td><a href="https://github.com/TheVicky1/Pact_OS/pull/554">#554</a> — feat(ui): add animated loading state to data export button</td>
</tr>
<tr>
<td><a href="https://github.com/Fristail27/vocab-bloom-hub"><code>Fristail27/vocab-bloom-hub</code></a></td>
<td>14</td>
<td><a href="https://github.com/Fristail27/vocab-bloom-hub/pull/598">#598</a> — i18n(pt): review the site interface texts</td>
</tr>
<tr>
<td><a href="https://github.com/Movalabs-crew/mova-store"><code>Movalabs-crew/mova-store</code></a></td>
<td>11</td>
<td><a href="https://github.com/Movalabs-crew/mova-store/pull/408">#408</a> — Fix/stellar browser uint8array</td>
</tr>
<tr>
<td><a href="https://github.com/nedpals/pwa-karaoke"><code>nedpals/pwa-karaoke</code></a></td>
<td>8</td>
<td><a href="https://github.com/nedpals/pwa-karaoke/pull/60">#60</a> — docs: add code of conduct and issue/PR templates</td>
</tr>
<tr>
<td><a href="https://github.com/HafidIdrissi/Time-Tracker"><code>HafidIdrissi/Time-Tracker</code></a></td>
<td>7</td>
<td><a href="https://github.com/HafidIdrissi/Time-Tracker/pull/367">#367</a> — docs: add portable upgrade walkthrough</td>
</tr>
<tr>
<td><a href="https://github.com/crazy-goat/xdbg"><code>crazy-goat/xdbg</code></a></td>
<td>3</td>
<td><a href="https://github.com/crazy-goat/xdbg/pull/124">#124</a> — fix: fall back to len(children) on malformed numchildren</td>
</tr>
<tr>
<td><a href="https://github.com/Finntegrate/tapio"><code>Finntegrate/tapio</code></a></td>
<td>2</td>
<td><a href="https://github.com/Finntegrate/tapio/pull/214">#214</a> — docs: define a status convention for specifications</td>
</tr>
<tr>
<td><a href="https://github.com/hoslift/ranu.js"><code>hoslift/ranu.js</code></a></td>
<td>2</td>
<td><a href="https://github.com/hoslift/ranu.js/pull/215">#215</a> — docs: add bash and zsh autocompletion recipe</td>
</tr>
<tr>
<td><a href="https://github.com/Sall25/folio"><code>Sall25/folio</code></a></td>
<td>2</td>
<td><a href="https://github.com/Sall25/folio/pull/256">#256</a> — fix(ui): keep formula editor within the viewport on small screens</td>
</tr>
<tr>
<td><a href="https://github.com/GDGCampusAEC/gdgc-aec-website"><code>GDGCampusAEC/gdgc-aec-website</code></a></td>
<td>1</td>
<td><a href="https://github.com/GDGCampusAEC/gdgc-aec-website/pull/49">#49</a> — perf(images): replace raw &lt;img&gt; with next/image across the site</td>
</tr>
<tr>
<td><a href="https://github.com/protocorn/Clippy-vision_RAN_BY_GROK_BOT"><code>protocorn/Clippy-vision_RAN_BY_GROK_BOT</code></a></td>
<td>1</td>
<td><a href="https://github.com/protocorn/Clippy-vision_RAN_BY_GROK_BOT/pull/9">#9</a> — docs: add MCP setup guides for Claude Desktop and LM Studio</td>
</tr>
<tr>
<td><a href="https://github.com/ktrubilo9/edge-proxy"><code>ktrubilo9/edge-proxy</code></a></td>
<td>0</td>
<td><a href="https://github.com/ktrubilo9/edge-proxy/pull/65">#65</a> — test: cover public and operational HTTP endpoints</td>
</tr>
</table>

