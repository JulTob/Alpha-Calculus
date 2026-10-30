# Transported arithmetic

Use this topic when a model's observations are easier to combine in a
different coordinate. First specify the generator, its image and inverse;
then calculate in ordinary coordinates and recover the observable.

This topic contains the reusable scalar helper, its tests, bounded formula
checks and [source annotations](local_annotations.md). The
[reference catalogue](references.md) maps each concept to exact sources.

## From the situation to the calculation

For a bijection `alpha: R -> A`, transport an ordinary operation `*` by

$$x *_\alpha y
=\alpha\left(\alpha^{-1}(x)*\alpha^{-1}(y)\right).$$

1. State the observable's domain and units. Use dimensionless values where
   the generator requires them; do not take logarithms of a physical unit.
2. Choose a supported generator and check that both inputs lie in its image.
3. Inspect the returned input coordinates and result coordinate.
4. Recover the observable and explain what operation it represents.
5. Compare the interpretation and cost with a competent conventional method.

The [helper](alpha_transport.py) implements four scalar operations for
three generators:

| Generator | Image `A` | Ordinary coordinate | Additive identity in `A` |
| --- | --- | --- | --- |
| Identity | Real numbers | `x` | `0` |
| Exponential | Positive real numbers | `log(x)` | `1` |
| Inverse logit | Probabilities strictly between 0 and 1 | `log(p/(1-p))` | `0.5` |

The implementation uses finite Python `int`/`float` inputs, excluding
`bool`; its numerical range is narrower than these exact real domains.
Division excludes the generator's additive identity, since its ordinary
coordinate is zero. An `OperationTrace` exposes the intermediate values.

For exponential transport, adding the coordinates of `2` and `3` returns
`6`: transported addition is ordinary multiplication. With inverse-logit
transport, adding `0.2` and `0.3` returns approximately `3/31`: it multiplies
odds. Independent-event union gives `0.44` and answers a different question.

## Run the scripts

From the repository root:

```sh
python3 -B topics/transported_arithmetic/alpha_transport.py
python3 -B topics/transported_arithmetic/test_alpha_transport.py
python3 -B topics/transported_arithmetic/check_formulas.py
```

The helper prints three worked traces. The formula checker writes
[its results](results/formula-results.json) beside this topic, regardless
of the current working directory. No third-party packages are required.

`calculate()` rejects unsupported enum values, invalid domains, non-finite
inputs, coordinate overflow and results that round to excluded image
boundaries. It raises `UnrepresentableResult` rather than clipping a
probability or silently returning a zero exponential result.

## What the checks establish

The 14 [unit tests](test_alpha_transport.py) cover operations, identities,
exact reference examples, invalid inputs, the excluded divisor and
floating-point representation failures. The formula checker supports these
bounded, separately interpreted examples:

| Check | Interpretation and limit |
| --- | --- |
| Function transport and `alpha=exp` | Recover the correct composition order; show a domain failure in the reversed expression. |
| Power-law derivative | Constant elasticity becomes a constant exponential Alpha derivative; see [the power-law topic](../power_laws/README.md). |
| `artanh` and integral factor | Check the [local annotation](local_annotations.md) with finite differences and quadrature. |
| Cube generator at zero | The direct transported derivative can exist when an expanded ordinary chain rule is unavailable. |
| Logit and event union | Exact fractions distinguish transported addition from probability union. |
| Logistic and cloglog links | Ordinary response derivatives and interval-risk ratios retain their own domains and interpretations. |
| Log-odds and Shannon information | Log-odds is a difference of surprisals, distinct from binary entropy. |
| Positive parallel resistance | A restricted reciprocal transport; see [the resistance topic](../parallel_resistance/README.md). |

Finite differences and numerical quadrature support the displayed cases;
they are not proofs of general differentiation or integration theorems.
The checker does not fit a GLM, implement information-theory inference or
solve a general circuit. The scalar helper does not differentiate functions,
accept arbitrary generators or implement symbolic algebra.

The [execution record](results/verification.json) identifies the fresh
commands, runtime and source hashes for the published files. It is evidence
for this revision and these inputs, rather than a full-book validation.
The helper supplies a transparent representation; no exclusive algorithmic
advantage over the same conventional coordinate calculation is claimed.
