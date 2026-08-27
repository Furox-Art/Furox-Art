# Hi, I'm Furkan 👋

I write numerical algorithms **from scratch, in readable Python** — no NumPy
underneath, no compiled extension you have to take on faith. Open
[`math_utils/linalg.py`](https://github.com/Furox-Art/scientific-computing-system/blob/main/src/cds/math_utils/linalg.py)
and the QR decomposition is right there as Householder reflections, cited to
the 1958 paper.

That is a deliberate trade — SciPy is faster and I am not competing with it.
It buys three things instead:

- **The implementation is the explanation.** Useful if you are learning the
  method, teaching it, or checking that it does what the textbook says.
- **It installs anywhere CPython runs.** Zero runtime dependencies and no
  binary wheels, so Pyodide/WASM, locked-down CI and embedded interpreters
  are not special cases.
- **It is auditable.** No layer you cannot read when a solver returns
  something surprising.

## 🔭 Projects

### [scientific-computing-system](https://github.com/Furox-Art/scientific-computing-system) — the pure-Python line

**22 modules, zero runtime dependencies**, on
[PyPI](https://pypi.org/project/scientific-computing-system/).

![PyPI](https://img.shields.io/pypi/v/scientific-computing-system.svg)
![CI](https://github.com/Furox-Art/scientific-computing-system/actions/workflows/tests.yml/badge.svg)
![Coverage](https://codecov.io/gh/Furox-Art/scientific-computing-system/branch/main/graph/badge.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

- 🎛 Quantum circuit simulation — single/multi-qubit, Bell/GHZ states
- 📈 Statistics — t-tests, ANOVA, effect sizes, nonparametric rank tests,
  bootstrap CIs, power analysis, time-series analysis
- 🤖 Machine learning — PCA, k-means, k-NN, decision trees, logistic/linear
  regression, ensembles, neural networks, even a mini-GPT with its own
  autograd engine
- 🌊 Signal processing — radix-2 FFT, Butterworth filter design, power spectra
- ⏱ ODE/PDE solvers — RK4/RK45 plus implicit stiff solvers (backward Euler,
  Crank–Nicolson)
- 🧮 The math underneath — incomplete gamma/beta via Numerical Recipes,
  LU/QR/Cholesky, Monte Carlo, symbolic differentiation

Readable does not mean unverified: **2,368 tests · 100% statement *and*
branch coverage (enforced CI gate) · `mypy --strict` · signed releases with
build provenance.**

### [scientific-computing-system-2.0](https://github.com/Furox-Art/scientific-computing-system-2.0) — when you want the speed

The same ideas rebuilt on NumPy/SciPy/pandas/matplotlib with C accelerators:
**41 modules**, 1,277 tests, the same 100% coverage gate. Adds domains v1 does
not cover — Bayesian inference, chaos, information theory, metaheuristics,
computational geometry and RL.

![PyPI](https://img.shields.io/pypi/v/scientific-computing-system-2.0.svg)
[Docs](https://furox-art.github.io/scientific-computing-system-2.0/)

### [axiomize](https://github.com/Furox-Art/axiomize) — idea → mathematical model

An AI agent skill that turns a plain-language idea into a rigorous model:
problem decomposition, parameter tables, **15 modeling perspectives**
(deterministic, stochastic, control, game-theoretic, causal, …), runnable
validation code and falsifiability criteria. Ships 11 worked examples,
10 benchmark reports and 6 domain packs.

[Docs](https://furox-art.github.io/axiomize/)

## 🌱 Good first issues

Want to contribute to open-source scientific Python?
[scientific-computing-system has curated starter tasks →](https://github.com/Furox-Art/scientific-computing-system/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

## 🛠 Stack

`Python 3.10+` · `pytest + hypothesis` · `mypy --strict` · `ruff` ·
`GitHub Actions` · `MkDocs Material`

## 📫 Reach me

Open an issue or a discussion on any of my repositories — I read everything.
