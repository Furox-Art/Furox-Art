<img src="assets/profile-banner.svg" width="100%" alt="Furox — Scientific computing, mathematical modeling, AI verification"/>

<p align="center">
  <strong>Independent researcher & developer building rigorous, auditable systems for scientific computing, mathematical modeling, and AI verification.</strong><br>
  Readable implementations · deterministic tests · explicit assumptions · reproducible workflows
</p>

---

## Projects

<table>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/Furox-Art/plan-auditor">plan-auditor</a></h3>
<p>An independent, multi-layered verification supervisor for AI coding agents. It reviews implementation plans, seals verification criteria against weakening, tracks evidence, runs deterministic checks, and gates completion with PASS / FAIL / UNKNOWN.</p>
<p><code>AI verification</code> · <code>plan sealing</code> · <code>deterministic auditing</code></p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/Furox-Art/axiomize">Axiomize</a></h3>
<p>An agent skill for turning vague ideas into rigorous mathematical models: decomposition, parameter tables, assumptions, fifteen modeling perspectives, validation code, model comparison, and falsifiability criteria.</p>
<p><code>mathematical modeling</code> · <code>15 lenses</code> · <code>falsifiability</code></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/Furox-Art/scientific-computing-system-2.0">scientific-computing-system-2.0</a></h3>
<p>A production-oriented scientific computing platform built on NumPy, SciPy, pandas, and matplotlib, covering linear algebra, statistics, optimization, signals, machine learning, information theory, chaos, Bayes, geometry, finance, and reinforcement learning.</p>
<p><code>NumPy/SciPy</code> · <code>42 modules</code> · <code>scientific Python</code></p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/Furox-Art/scientific-computing-system">scientific-computing-system</a></h3>
<p>A pure-Python scientific computing platform implemented from scratch with zero runtime dependencies. It includes quantum simulation, statistics, signal processing, optimization, ODE solvers, machine learning, symbolic tools, and structured hypothesis generation.</p>
<p><code>pure Python</code> · <code>zero runtime deps</code> · <code>from scratch</code></p>
</td>
</tr>
</table>

---

## How the projects connect

```text
idea
  ↓
Axiomize
  ↓
rigorous mathematical model
  ↓
scientific-computing-system / scientific-computing-system-2.0
  ↓
tested computation
```

```text
AI implementation plan
  ↓
Plan Auditor
  ↓
sealed criteria + deterministic verification + evidence
  ↓
verified completion
```

Together, the repositories focus on one theme: making technical work easier to inspect, test, reproduce, and challenge instead of treating models or agent output as black boxes.

---

## Engineering principles

- **Auditability over black boxes** — important behavior should be inspectable and testable.
- **Behavior-first verification** — checks should demonstrate what the software actually does.
- **Explicit assumptions** — models and systems should expose constraints and failure conditions.
- **Reproducibility** — code, tests, and documentation should make results repeatable.
- **Minimal hidden machinery** — prefer clear mechanisms over unnecessary abstraction.

<details>
<summary><strong>Stack</strong></summary>

`Python 3.10+` · `pytest` · `mypy --strict` · `ruff` · `GitHub Actions` · `MkDocs Material` · `NumPy` · `SciPy` · `pandas` · `matplotlib`

</details>
