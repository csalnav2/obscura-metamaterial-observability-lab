# Scientific validation plan

## Recommendation

Ship the current code as a **research software benchmark**, not as a predictive invisibility model. The next scientific milestone should be a reproducible validation matrix rather than another visual feature.

## Tier 0: Repository integrity

- Compile `obscura.py` and `u.py`.
- Verify the source SHA-256.
- Run AST inventory checks.
- Scan notebooks and tracked files for secrets.
- Record Python and dependency versions.

## Tier 1: Deterministic internal checks

Run:

```bash
python -u u.py --self-test
python -u u.py --verify-quantum-backends
```

Required invariants:

- Density matrix trace equals one.
- Density matrix is Hermitian and positive semidefinite within tolerance.
- NumPy finite-difference QFI agrees with JAX finite difference.
- JAX autodiff QFI agrees with finite difference over a step-size sweep.
- QuTiP parity agrees when available.
- Quaternion norm remains one.
- Rotation matrix remains orthonormal with determinant near one.
- `R + A + S + T = 1` at every sampled node.
- Candidate evaluations do not mutate lifecycle state.
- Display smoothing never changes exported raw data.

## Tier 2: Numerical convergence

### Time step

Compare at least:

\[
\Delta t \in \{0.40, 0.20, 0.10, 0.05\}\ \mathrm{s}.
\]

Track:

- QFI maximum and time integral.
- Capture and shadow maxima.
- Objective integral.
- Acquisition time and suppression lifetime.
- Oxidation state and dose.
- Controller accepted-step norm.

The exact OU and critically damped updates remove important explicit-Euler instability, but the coupled optical/control process still needs an empirical convergence study.

### Spectral resolution

Compare 9, 15, 21, and 31 nodes. Report whether the worst wavelength and pass/fail result stabilize.

### Wave grid

Compare odd grids 33, 49, and 65 with fixed physical extent. Report field NMSE, phase RMSE, modal crosstalk, OAM closure, and trace distance.

### Monte Carlo packets

Compare at least 1,200, 2,400, and 4,800 packets over repeated seeds. Separate visualization convergence from detector-statistics convergence.

## Tier 3: Causal and optimizer ablations

Run paired seeds for:

- Controller disabled.
- Projected SPSA baseline.
- Momentum SPSA.
- RMSProp-SPSA.
- Adam-SPSA.
- QFI-guard SPSA.
- Ensemble hump-guard SPSA.
- MSGA-SPSA.

Ablate one objective family at a time:

- QFI penalty.
- Capture penalty.
- Shadow penalty.
- Throughput guard.
- Absorption guard.
- Wave/channel penalties.
- Spectral hump term.
- Degradation and healing terms.

Report median paired change, confidence interval, failure rate, and worst seed. Do not select only visually attractive trajectories.

## Tier 4: Counterfactual physics checks

- Negative-index branch versus the implemented positive-index counterfactual.
- Ideal active benchmark versus the generic anisotropic comparator.
- Named material platforms only within their declared validity bands.
- Ambient-only versus laser-only versus conserved mixed-source tests.
- Coherent versus Gaussian-Schell versus incoherent sources.
- Gaussian, LG, HG, and finite BG0 probes.

## Tier 5: External solver comparison

Create a simplified geometry that can be represented both in OBSCURA and in an independent FDTD or FEM tool. Compare:

- Reflection and transmission.
- Angular scattering pattern.
- Phase delay.
- Polarization transformation.
- Field overlap at a downstream plane.

Fit no parameters on the test cases. Separate calibration cases from held-out validation cases.

## Tier 6: Material calibration and experiment

Before material-specific prediction:

- Replace literature-shaped defaults with measured ellipsometry or conductivity data.
- Propagate parameter uncertainty.
- Include fabrication tolerances and temperature dependence.
- Validate actuator dynamics and power.
- Measure detector response and background noise.
- Pre-register success criteria.

Only after this tier should “experimental cloaking” enter the title.
