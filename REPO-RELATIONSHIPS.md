# Repository relationships

The ten repositories this profile is built around share one spine. This file exists because the
repo names alone do not tell you which one to reach for, and because several pairs are easy to
mistake for each other: the two `axiomize` lines, the two `scientific-computing-system` lines, the
two deterministic gates (`plan-auditor` and `nomosguard`), the two MCP servers (`scientific-toolkit`
and `literature-evidence-mcp`), and `eq-layer`, which is frequently read as a truth checker even
though it is a dialogue controller.

## The spine

```
                 scientific-computing-system          (pure Python, zero runtime deps)
                        |                                        |
                        | numeric kernels                      | modeling discipline
                        v                                        v
             scientific-computing-system-2.0  <--            axiomize
                (NumPy/SciPy rebuild)                     (Model IR, 15 lenses, benchmarks)
                                                                |
                                                                v
                                        axiomize-quantum-skills-2.0
                                          (+ quantum-inspired multi-branch reasoning)
                                                    |
                    standalone primitive ------------+
                    (no modeling engine)        quantum-reasoning-skill

        orthogonal axis: agent work verification  ->  plan-auditor
```

Around the spine sit two more layers, which are not new engines:

```
        MCP surface (integration and provenance)
             scientific-toolkit        -> one endpoint in front of several repos,
                                          local stdio + bearer-token Streamable HTTP
             literature-evidence-mcp   -> 32-tool evidence provenance: source and quote
                                          audits, independent evidence logs, optional BM25
                                          and offline experimental NLI

        guardrail axis (deterministic, fail-closed)
             plan-auditor   -> did the agent do what it claims it did?
             nomosguard     -> is this security posture safe to act on? deny-by-default gate
             eq-layer       -> which conversational move comes next? not a truth judgment
```

## Which one do I want?

| If you want to… | Use | Why not the others |
|---|---|---|
| Run numerics with **no dependencies** | `scientific-computing-system` | `-2.0` needs NumPy/SciPy |
| Run numerics **fast**, at scale | `scientific-computing-system-2.0` | the pure-Python twin is slower by design |
| Turn an **idea** into a rigorous model | `axiomize` | not a numerical library |
| Get the same modeling **plus** branching reasoning | `axiomize-quantum-skills-2.0` | superset of `axiomize` |
| Just the branching **primitive**, lightweight | `quantum-reasoning-skill` | no modeling engine, no benchmark reports |
| Verify an **agent's** work with real evidence | `plan-auditor` | orthogonal to everything above |
| Gate an action on **security posture** | `nomosguard` | `plan-auditor` checks agent claims, not CVE and log reasoning |
| Steer a **conversation** (repair, routing, policy) | `eq-layer` | it chooses moves; it does not judge facts |
| Put several repos behind **one MCP endpoint** | `scientific-toolkit` | a gateway runs the others, it does not contain them |
| Trace a **claim back to a quote** in the literature | `literature-evidence-mcp` | evidence provenance, not modeling or numerics |

## Active vs. early-stage

| Repo | Status | Note |
|---|---|---|
| `axiomize` | **Active, v1 line** | the stable, widely-referenced modeling engine |
| `axiomize-quantum-skills-2.0` | **Active, v2 line** | adds multi-branch reasoning; the two are maintained in parallel, `axiomize` is not frozen |
| `quantum-reasoning-skill` | **Active, narrow** | deliberately standalone; overlaps conceptually with the v2 reasoning layer but ships no engine |
| `scientific-computing-system` | **Active** | the pure-Python original |
| `scientific-computing-system-2.0` | **Active** | NumPy/SciPy sibling, independently versioned (v5.x) |
| `plan-auditor` | **Active** | no overlap with the rest; different problem domain |
| `scientific-toolkit` | **Active, integration only** | its deployment checks prove wiring, not scientific correctness; external-client login is not verified and OAuth is not configured |
| `literature-evidence-mcp` | **Active, exploratory** | the NLI challengers and their measured numbers are exploratory; no clinically validated fact-checking and no confirmed superiority |
| `nomosguard` | **Early-stage** | reasoning core and gate are deterministic and testable; scenarios are reproducible and containment planning is opt-in, with no unattended action by default |
| `eq-layer` | **Early-stage** | development evaluations are preliminary; explicitly **not** a factual truth checker |

Nothing here is archived. Where two repos overlap, the newer one is an extension, not a
replacement — `axiomize` remains the v1 reference and `quantum-reasoning-skill` stays a
deliberately small standalone.

## The ones that get confused

**`axiomize` vs `axiomize-quantum-skills-2.0`.** Same 15 perspective lenses and the same
8-phase report structure. v2 adds a quantum-inspired reasoning layer (score / prune / revive /
collapse over branches) and expands the benchmark suite from 12 to 29 reports. Different PyPI
distributions, so both can be installed side by side.

**`axiomize-quantum-skills-2.0` vs `quantum-reasoning-skill`.** Both do multi-branch
reasoning. The 2.0 repo bundles it inside the full modeling engine; `quantum-reasoning-skill`
is just the reasoning primitive, roughly 200 KB, for when you want the branch logic without
Model IR, the lens suite, or the benchmark harness.

**`scientific-computing-system` vs `-2.0`.** Same problem domain, completely different
engineering tradeoff. The first is zero-runtime-dependency pure Python that you can read
end to end. The second is the NumPy/SciPy/pandas rebuild for speed. Independent version lines
(2.x vs 5.x) — not a v1/v2 pair despite the names.

**`plan-auditor` vs `nomosguard`.** Both are deterministic, both keep a hash-chained evidence
ledger, and in both an LLM may explain evidence but never crosses the decision boundary. They
answer different questions: `plan-auditor` takes a sealed execution contract and returns
PASS / FAIL / UNKNOWN about work an agent claims to have done; `nomosguard` ingests CVE and log
evidence, derives attack paths, and returns a deny-by-default policy verdict. Verification of
behaviour is not assessment of risk.

**`scientific-toolkit` vs `literature-evidence-mcp`.** Both speak MCP, and neither is a new
compute engine. The toolkit is a *gateway*: provider-neutral wiring that puts several of these
repositories behind one endpoint over local stdio or bearer-token-authenticated Streamable HTTP,
without merging their code. `literature-evidence-mcp` is a *tool*: a 32-server surface of
evidence-provenance operations over sources, quotes and independent logs. If you are asking "how
do I reach the repos", that is the gateway; if you are asking "is this sentence supported by that
paper", that is the evidence server.

**`eq-layer` vs the verification repos.** `eq-layer` tracks affect and intent and routes the next
action through Bayesian risk, then audits the response structure. It belongs to the guardrail axis
because it decides *what to say or do next in a dialogue*, not because it judges whether a claim
is true. Factual evidence work goes to `literature-evidence-mcp`, `plan-auditor` or `nomosguard`.

## Private research repos

Several private repos (`*-TEORISI`, `*-Hipotezi`, `Dongusel-evren-fikri`) hold unreleased
theory work and are intentionally not described here. They are excluded from the public
profile on purpose.
