<img src="assets/profile-banner.svg" width="100%" alt="Furox — Scientific computing, mathematical modeling, AI reasoning and verification"/>

<p align="center">
  <strong>Independent researcher & developer building rigorous, auditable systems for scientific computing, mathematical modeling, AI reasoning, and verification.</strong><br>
  Reproducible computation · explicit assumptions · deterministic verification · falsifiable models
</p>

<p align="center">
  <a href="https://github.com/Furox-Art"><img src="https://img.shields.io/badge/GitHub-Furox--Art-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a>
  <a href="https://x.com/FuroxArt"><img src="https://img.shields.io/badge/X-@FuroxArt-000000?style=flat-square&logo=x&logoColor=white" alt="X"/></a>
  <a href="https://pypi.org/project/scientific-computing-system/"><img src="https://img.shields.io/badge/PyPI-scientific--computing--system-3775A9?style=flat-square&logo=pypi&logoColor=white" alt="PyPI"/></a>
  <img src="https://img.shields.io/github/followers/Furox-Art?style=flat-square&logo=github&label=Followers" alt="Followers"/>
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

| Project | ⭐ | Stack | What it does |
| --- | --- | --- | --- |
| [**scientific-computing-system**](https://github.com/Furox-Art/scientific-computing-system) | 16 | Python · MIT | Pure-Python computational science with **zero runtime dependencies**: 35 modules exporting 505 names — linear algebra, ODE/PDE solvers, quadrature, Monte Carlo/MCMC, statistics, signal processing, quantum simulation, uncertainty & sensitivity analysis, dimensional analysis, and falsifiable hypothesis generation. Optional NumPy/SciPy backends are opt-in extras. |
| [**axiomize**](https://github.com/Furox-Art/axiomize) | 4 | Python · MIT | Reproducible scientific modeling engine and agent skill built around a versioned **Model IR**: explicit units, dimensional and numerical validation, calibration, sensitivity and uncertainty analysis, causal/Bayesian inference, and portable export through CLI, REST, and MCP. |
| [**plan-auditor**](https://github.com/Furox-Art/plan-auditor) | 1 | Python · MIT | Deterministic, LLM-free verification supervisor for AI coding agents: sealed execution contracts, SHA-256 hash-chained evidence, STRIPS/PDDL reachability and exact recompilation, and PASS / FAIL / UNKNOWN completion gating. |
| [**nomosguard**](https://github.com/Furox-Art/nomosguard) | 0 | Python · Apache-2.0 | Deterministic security reasoning core: hash-chained evidence ledger, attack-path rule engine, and a fail-closed policy gate. LLMs produce evidence and explain decisions; they never cross the decision boundary. |
| [**eq-layer**](https://github.com/Furox-Art/eq-layer) | 0 | Python · MIT | A control layer that decides how an LLM should speak before it speaks. |
| [**quantum-reasoning-skill**](https://github.com/Furox-Art/quantum-reasoning-skill) | 1 | Python · MIT | Model-agnostic reasoning protocol for ambiguous, multi-step problems: maintain materially different candidate paths, verify them independently with evidence, detect shared assumptions and contradictions, reallocate compute, preserve dormant branches, and collapse only when one result is supported. Quantum-*inspired*, not quantum computing. |
| [**scientific-toolkit**](https://github.com/Furox-Art/scientific-toolkit) | 0 | Python · Apache-2.0 | Unified open-source scientific toolkit integrating seven research and AI software projects through the **Model Context Protocol (MCP)**. |
| [**scientific-computing-system-2.0**](https://github.com/Furox-Art/scientific-computing-system-2.0) | 2 | Python · MIT | The NumPy/SciPy/pandas production line: 40+ scientific domains, guided model fitting with uncertainty and held-out validation, residual diagnostics and reproducibility manifests, compiled C acceleration kernels with safe fallbacks, optional CuPy GPU execution, and scikit-learn-compatible estimators. |

<p align="center"><em>Also maintained: <a href="https://github.com/Furox-Art/axiomize-quantum-skills-2.0">axiomize-quantum-skills-2.0</a> — the modeling engine plus the quantum-inspired multi-branch reasoning skill in one package.</em></p>

<p align="center"><sub>Star counts, licenses, and PyPI releases are live GitHub / PyPI data, checked 12 October 2026. The project cards below describe each repository in depth and were written against earlier release tags.</sub></p>

---

## Public Projects

<table>
<tr>
<td colspan="2" valign="top">
<h3><a href="https://github.com/Furox-Art/quantum-reasoning-skill">Quantum Reasoning Skill</a></h3>
<p>A model-agnostic reasoning protocol for difficult, ambiguous, and multi-step problems. Instead of committing early to one answer, it maintains materially different candidate paths, verifies them independently with evidence and tools, detects shared assumptions and contradictions, reallocates compute as uncertainty changes, preserves recoverable dormant branches, and collapses only when one result is sufficiently supported. It runs on classical AI models and hardware; it is quantum-inspired reasoning, not quantum computation.</p>
<p><code>multi-branch reasoning</code> · <code>falsification</code> · <code>adaptive compute</code> · <code>branch revival</code> · <code>model-agnostic skill</code></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/Furox-Art/plan-auditor">plan-auditor</a></h3>
<p>An independent deterministic verification supervisor for AI coding agents. It turns requirements and implementation plans into auditable execution contracts, tracks dependency/output DAGs, can automatically compile structured plans into conservative STRIPS contracts, verifies reachability and exact recompilation, seals verification state cryptographically, records hash-chained execution evidence, and gates completion across single- or multi-agent work with PASS / FAIL / UNKNOWN.</p>
<p><code>v2.4.0</code> · <code>agent verification</code> · <code>STRIPS/PDDL</code> · <code>cryptographic sealing</code> · <code>evidence chains</code></p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/Furox-Art/axiomize">Axiomize</a></h3>
<p>A versioned scientific modeling engine and Agent Skill built around a machine-readable Model IR. It supports native algebraic, ODE, PDE, DAE, stochastic, optimization, control, network, Bayesian, agent-based, discrete-event, hybrid, multiphysics, and causal modeling workflows, with fitting, uncertainty analysis, causal identification, Bayesian diagnostics, numerical verification, reproducible provenance, portable scientific export, and optional PyMC, JAX, Lean, and FEniCS/DOLFINx integrations.</p>
<p><code>v1.12.2</code> · <code>Model IR</code> · <code>simulation & fitting</code> · <code>causal/Bayesian inference</code> · <code>scientific verification</code></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/Furox-Art/scientific-computing-system-2.0">scientific-computing-system-2.0</a></h3>
<p>A production-oriented scientific computing platform built on NumPy, SciPy, pandas, and matplotlib. Its current 5.x line spans 40+ scientific domains and adds guided model fitting with uncertainty, held-out validation, residual diagnostics and reproducibility manifests; compiled C acceleration kernels with safe fallbacks; optional CuPy GPU execution; NumPy Array API support; scikit-learn-compatible estimators; and property, fuzz, oracle, cross-platform wheel, and benchmark-regression testing.</p>
<p><code>v5.2.4</code> · <code>40+ domains</code> · <code>guided scientific fitting</code> · <code>C/GPU acceleration</code> · <code>scientific Python</code></p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/Furox-Art/scientific-computing-system">scientific-computing-system</a></h3>
<p>A zero-runtime-dependency, pure-Python computational science platform whose algorithms are implemented in readable Python rather than hidden behind compiled numerical libraries. It covers numerical methods, linear algebra, statistics, probability, optimization, interpolation, ODE/PDE solvers, signal processing, machine learning, Monte Carlo/MCMC, quantum simulation, symbolic modeling, dimensional/scientific utilities, knowledge tools, and structured falsifiable hypothesis generation, with optional scientific backends available separately.</p>
<p><code>pure Python</code> · <code>zero runtime dependencies</code> · <code>from-scratch algorithms</code> · <code>numerical science</code> · <code>hypothesis generation</code></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/Furox-Art/eq-layer">eq-layer</a></h3>
<p>A control layer that decides how an LLM should speak before it speaks.</p>
<p><code>LLM control</code> &middot; <code>speech gating</code> &middot; <code>Python</code></p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/Furox-Art/nomosguard">nomosguard</a></h3>
<p>Deterministic security reasoning core: hash-chained evidence ledger, attack-path rule engine, fail-closed policy gate. LLMs produce evidence and explain decisions; they never cross the decision boundary.</p>
<p><code>security reasoning</code> &middot; <code>hash-chained evidence</code> &middot; <code>fail-closed policy</code></p>
</td>
</tr>
<tr>
<td colspan="2" valign="top">
<h3><a href="https://github.com/Furox-Art/scientific-toolkit">scientific-toolkit</a></h3>
<p>A unified open-source scientific toolkit integrating seven research and AI software projects through the Model Context Protocol (MCP).</p>
<p><code>MCP</code> &middot; <code>seven-project integration</code> &middot; <code>scientific tooling</code></p>
</td>
</tr></table>

---



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

<p align="center"><sub>Live GitHub data, verified through the search API on 16 October 2026.</sub></p>
<p align="center">
  <strong>Current focus</strong><br>
  scientific computing · mathematical & computational modeling · quantum-inspired AI reasoning · agent verification · reproducible research software
</p>

<details>
<summary><strong>Technical stack</strong></summary>

`Python 3.10+` · `NumPy` · `SciPy` · `pandas` · `Matplotlib` · `SymPy` · `statsmodels` · `NetworkX` · `Z3` · `CVXPY` · `CasADi` · `pytest` · `mypy --strict` · `ruff` · `GitHub Actions` · optional `PyMC` / `JAX` / `FEniCS` / `CuPy`

</details>

---

## Contact & Links

The most reliable way to reach me is through the repositories themselves — issues and discussions in the project you are asking about get answered fastest.

<p align="center">
  <a href="https://github.com/Furox-Art"><img src="https://img.shields.io/badge/GitHub-Furox--Art-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
  <a href="https://x.com/FuroxArt"><img src="https://img.shields.io/badge/X-@FuroxArt-000000?style=for-the-badge&logo=x&logoColor=white" alt="X"/></a>
  <a href="https://pypi.org/project/scientific-computing-system/"><img src="https://img.shields.io/badge/PyPI-scientific--computing--system-3775A9?style=for-the-badge&logo=pypi&logoColor=white" alt="PyPI"/></a>
  <a href="https://furox-art.github.io/scientific-computing-system/"><img src="https://img.shields.io/badge/Docs-furox--art.github.io-0a7ea4?style=for-the-badge&logo=readthedocs&logoColor=white" alt="Documentation"/></a>
</p>

| Channel | Details |
| --- | --- |
| **GitHub** | [@Furox-Art](https://github.com/Furox-Art) — 75 public repositories, issues and discussions open |
| **X / Twitter** | [@FuroxArt](https://x.com/FuroxArt) |
| **PyPI** | [scientific-computing-system](https://pypi.org/project/scientific-computing-system/) · [scientific-computing-system-2.0](https://pypi.org/project/scientific-computing-system-2.0/) · [axiomize](https://pypi.org/project/axiomize/) |
| **Documentation** | [furox-art.github.io/scientific-computing-system](https://furox-art.github.io/scientific-computing-system/) |
| **Citation** | `CITATION.cff` ships with every scientific repository, for citable releases |

<p align="center">
  <sub>Open source under MIT and Apache-2.0. Bug reports, correctness questions, and research ideas are welcome — prefer the repository's issue tracker or discussions so the context stays public and searchable.</sub>
</p>
