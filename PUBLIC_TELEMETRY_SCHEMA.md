# Public Telemetry Schema

Schema identifier: `obscura-public-telemetry-v1`

The public renderer accepts only an exact allow-list. Extra columns are rejected
rather than ignored, preventing an accidental internal-state spill.

## Public fields

| Group | Fields |
|---|---|
| Time | `time_s` |
| Quantum | `qfi_baseline`, `qfi_showcase` |
| Classical | `capture_ratio`, `capture_normalized`, `shadow_error`, `shadow_normalized` |
| Composite | `invisibility_index`, `throughput` |
| Lifecycle | `source_power_W`, `absorbed_power_W`, `healing_power_nW`, `oxidation_state`, `damage_rate_per_s` |
| Pose | `x_m`, `y_m`, `z_m`, `roll_deg`, `pitch_deg`, `yaw_deg` |
| Eye | `focus_target_m`, `focus_m`, `dof_near_m`, `dof_far_m` |
| Material summary | `cloak_quality`, `residual_scatter`, `positive_index_counterfactual_scatter` |
| Dispersion | `dispersion_rms_m`, `dispersion_axis_1_m`, `dispersion_axis_2_m`, `dispersion_axis_3_m` |
| Controller proxies | `objective_proxy`, `gradient_proxy`, `step_proxy` |
| Noise | `shot_sigma`, `thermal_sigma`, `quantum_sigma`, `total_sigma` |
| Finite topology | `beta0`, `beta1` |

## Explicitly excluded

- Material control coordinates and actuator commands
- Constitutive tensor components and per-wavelength fitted parameters
- Objective decomposition and private reward weights
- SPSA perturbations, moments, candidate scores, and acceptance decisions
- Random seeds used for private benchmark claims
- Full complex fields, density matrices, and private channel parameters
- API, authentication, or access-control data

## Validation

```bash
python scripts/verify_public_telemetry.py data/public_telemetry.csv
```
