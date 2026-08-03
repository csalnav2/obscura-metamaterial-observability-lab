A Programmable Metamaterial Dual-Observability Lab

Observability Benchmark for Simulated Cloaking Under Reduced-order AdaptationTagline: Simulated cloaking benchmark, not experimental invisibility.



<p align="center">
  <img src="assets/obscura_public_overview.png" alt="OBSCURA public synthetic dashboard overview" width="100%">
</p>

[!IMPORTANT]This is the public showcase edition. It does not contain the privatesimulation engine, constitutive parameter maps, calibration constants,complete controller objective, optimizer guards, stress schedule, raw privatetelemetry, hosted research-agent stack, credentials, or full Colab notebook.The bundled curves are synthetic and cannot support a scientific performanceclaim.

Project description

OBSCURA is a reduced-order, time-dependent programmable-metamaterial controlbenchmark that studies simultaneous suppression of classical detectorobservability and quantum parameter sensitivity under explicit spectral,energy, lifecycle, and channel constraints.

A scientifically careful public description is:

OBSCURA is a time-dependent adaptive-control simulation that suppressesclassical capture and shadow observability while reducing per-probe quantumFisher information below configured thresholds, producing simulateddual-observability concealment within the declared model.

The required qualifier is equally important:

OBSCURA is a reduced-order feasibility benchmark, not an experimental oruniversal demonstration of electromagnetic invisibility.

The phrase dual observability refers to two model families:

Classical observability: noise-aware capture and shadow signatures.

Quantum parameter observability: quantum Fisher information, or QFI, fora declared phase-like parameter in a finite reduced channel.

Low QFI does not mean that every possible quantum detector fails. It means theselected encoded parameter is difficult to estimate from the modeled outputstate. This distinction is foundational, not decorative.

Why the public repository is deliberately limited

A public GitHub repository is excellent for visibility, critique, and findingcollaborators. It is a poor vault. A shortened copy of a 50,000-line researchengine can still expose architecture, objective structure, calibration logic,and enough relationships to reconstruct the important parts.

This repository therefore publishes the presentation plane, not theinvention plane.

Public showcase

Private engine

Synthetic or sanitized telemetry

Full state and raw telemetry

Plot builders and dashboard vocabulary

Complete simulation and control loop

General scientific equations

Exact constitutive mappings and calibration

Declared threshold semantics

Exact objective weights and guard logic

Read-only result schema

SPSA moments, probes, rescue rules, and schedules

Collaboration pathway

Full notebook, API stack, credentials, and prompts

The public code is useful for reviewing the scientific story, exploring themetric relationships, and rendering approved result summaries. It isintentionally insufficient for reproducing the private solver.

Repository architecture

flowchart LR
    A[Private OBSCURA engine] --> B[Private raw telemetry]
    B --> C[Private allow-list sanitizer]
    C --> D[Public telemetry CSV]
    D --> E[Public showcase renderer]
    E --> F[HTML dashboard]
    E --> G[Static README image]
    E --> H[Public result package]

    A -. never committed .-> I[Public GitHub repository]
    B -. never committed .-> I
    I --> J[Collaboration request]
    J --> K[Controlled private access]

A real private run should cross the public boundary only through an explicit,reviewed allow-list. Extra columns are rejected rather than silently ignored.

Quick start

1. Clone and create an environment

git clone https://github.com/csalnav2/obscura-metamaterial-observability-lab.git
cd obscura-metamaterial-observability-lab

python -m venv .venv

Activate the environment:

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS or Linux
source .venv/bin/activate

2. Install the public showcase dependencies

python -m pip install --upgrade pip
pip install -r requirements.txt

3. Generate the synthetic public dashboard

python obscura_showcase.py --output-dir public_output

Generated artifacts:

public_output/
├── obscura_public_showcase.html
├── obscura_public_overview.png
├── public_metadata.json
└── public_telemetry.csv

Open public_output/obscura_public_showcase.html in a browser.

4. Validate the public release boundary

python scripts/audit_public_release.py .
pytest

The audit fails when it detects private artifact hashes, oversized notebookcells, core private implementation identifiers, credentials, private keys, ormagic-access URLs.

Public threshold convention

The currently declared public boundaries are

$$F_Q \leq 0.020, \qquad C \leq 0.020, \qquad S \leq 0.080,$$

where

$F_Q$ is per-probe QFI for the selected modeled parameter,

$C$ is the noise-aware capture ratio,

$S$ is the shadow error.

Define the threshold-normalized classical severity

$$O_C(t)=\max\left[\frac{C(t)}{C_{\mathrm{lim}}},\frac{S(t)}{S_{\mathrm{lim}}}\right].$$

The public classical pass boundary is therefore

$$O_C(t)\leq 1.$$

A sampled robust assessment is conceptually stricter:

$$\max_{\lambda\in\Lambda}F_Q(\lambda)\leq F_{Q,\mathrm{lim}},$$

$$\max_{\lambda\in\Lambda}C(\lambda)\leq C_{\mathrm{lim}},\qquad\max_{\lambda\in\Lambda}S(\lambda)\leq S_{\mathrm{lim}},$$

with additional scattering, absorption, material-validity, throughput, andapplicable wave/channel gates.

[!NOTE]Passing a finite sampled set $\Lambda$ is evidence only for that declared set.It is not a proof over every wavelength, direction, polarization, mode,detector, material specimen, or perturbation.

Dashboard guide and mathematics

The private dashboard contains eleven primary scientific views plus additionalwave and wavelength audits. The public showcase preserves their vocabulary andinterpretation while replacing the enabling engine with synthetic or sanitizedinputs.

Plot 1: Optimizer comparison

What it displays

The comparison contains three stacked panels:

QFI per detected probe.

Classical capture and shadow observability.

Composite concealment and throughput.

The decisive QFI is conservatively summarized as

$$F_Q^{\star}(t)=\max\left[F_Q^{\mathrm{measured}}(t),\max_{\lambda\in\Lambda}F_Q(t,\lambda)\right].$$

A good controlled run should show all of the following:

$F_Q^{\star}$ remains below its declared boundary.

Capture and shadow remain below their normalized boundary.

Throughput does not collapse.

Absorption does not become the hidden mechanism of apparent concealment.

Improvement persists over time rather than appearing at one favorable sample.

Display smoothing may be used only for causal presentation. Raw exported valuesmust remain unchanged, and visual filtering must never be presented as physicalevidence.

What is withheld

The public repository does not publish the complete private objective,coefficient weights, candidate horizon, guard thresholds, coordinate-rescuelogic, or optimizer state.

Plot 2: Degradation and lifecycle

What it displays

Oxidation or bounded damage state.

Scattering and absorption stress.

Incident, intercepted, absorbed, nonlinear, and healing power.

Damage formation, net rate, accumulated dose, and healing expenditure.

A general bounded formation-healing model is

$$\frac{dD}{dt}=k_f(1-D)-k_hD,$$

with

$$k_f=k_{\mathrm{photo}}+k_{\mathrm{environment}}.$$

For rates held constant over one step $\Delta t$, the exact update is

$$D_{n+1}=D_{\infty}+\left(D_n-D_{\infty}\right)\exp\left[-(k_f+k_h)\Delta t\right],$$

where

$$D_{\infty}=\frac{k_f}{k_f+k_h}.$$

A bounded healing actuator can be assigned a quadratic energetic cost,

$$P_h=P_{h,\max}u_h^2,\qquad 0\leq u_h\leq 1.$$

A low-observability state is scientifically weak when it requires rapidlyincreasing damage, excessive healing power, rising absorption, or survives foronly a negligible interval.

The private rate constants are accelerated surrogate parameters unless fittedto a specific specimen. They are not public lifetime predictions.

Plot 3: Photon scene

What it displays

The programmable outer cube.

The solid inscribed focus cube.

A downstream observer representation.

Incident, internal, scattered, and post-exit packets.

Geometric observer-coverage vectors.

The visible packets are display particles. They do not resolve optical carrieroscillations and do not travel at the physical speed of light.

For a signed-index ray surrogate, let $\mathbf{i}$ be a normalized incidentdirection and $\mathbf{n}$ the interface normal pointing toward the incidentmedium. The incident tangential component is

$$\mathbf{t}_i=\mathbf{i}+\cos\theta_i,\mathbf{n},\qquad\cos\theta_i=-\mathbf{i}\cdot\mathbf{n}.$$

A signed transmitted tangential component is

$$\mathbf{t}_t=\frac{n_1}{n_2}\mathbf{t}_i.$$

Define

$$k=1-\lVert\mathbf{t}_t\rVert^2.$$

For $k\geq 0$, a transmitted direction can be written

$$\mathbf{d}_t=\mathbf{t}_t-\sqrt{k},\mathbf{n}.$$

For $k<0$, the reduced ray model returns a reflected branch. A negative $n_2$reverses the tangential sign in this surrogate, representing negativerefraction. This remains a ray-level approximation, not a solution of fullMaxwell boundary conditions.

Plot 4: Rank-3 tensor lattice or tensor slices

What it displays

The plot represents all 27 components of an effective coupling tensor

$$T_{ijk}, \qquad i,j,k\in{x,y,z}.$$

It may appear as a three-dimensional coefficient lattice or three heatmap slicesfor $k=x,y,z$.

Under a body-to-world rotation $R$, a rank-3 tensor transforms as

R_{ia}R_{jb}R_{kc}T^{\mathrm{body}}_{abc}.$$

The Frobenius norm is

\sqrt{\sum_{i,j,k}T_{ijk}^2}.$$

A directional contraction is

$$(\mathbf{v}_T)i=T{ijk}d_jd_k,$$

or compactly

$$\mathbf{v}_T=T:\mathbf{d}\otimes\mathbf{d}.$$

The object is an effective dimensionless coupling tensor. It is not a retrievedexperimental susceptibility tensor.

Plot 5: Photon flag-complex topology

What it displays

A finite sample of packet positions.

Mutual-nearest-neighbor edges.

Filled triangular 2-simplices.

Betti numbers $\beta_0$ and $\beta_1$ at one spatial scale $\epsilon$.

An edge $(i,j)$ is retained when the points are mutual neighbors and

$$d_{ij}\leq\epsilon.$$

A triangle is added when all three pairwise edges exist. For the resultingfinite clique complex,

$$\beta_0=\text{number of connected components},$$

and

|E|-|V|+\beta_0-\operatorname{rank}_{\mathbb{F}_2}(\partial_2).$$

Interpretation:

Larger $\beta_0$ indicates more disconnected packet groups.

Larger $\beta_1$ indicates more independent unfilled loops.

These are exact invariants of the displayed finite complex at one scale. Theyare not persistent-homology barcodes, continuum invariants, or evidence of atopologically protected material phase.

Plot 6: Cube pose

What it displays

Translation $x,y,z$ in metres.

Roll, pitch, and yaw in degrees.

A bounded stochastic target may use an exact Ornstein-Uhlenbeck update,

\mu+e^{-\Delta t/\tau}(X_n-\mu)+\sigma\sqrt{\frac{\tau}{2}\left(1-e^{-2\Delta t/\tau}\right)},\xi,$$

where $\xi\sim\mathcal{N}(0,1)$.

A smooth critically damped follower satisfies

$$\ddot{x}+2\omega\dot{x}+\omega^2(x-x_\star)=0.$$

For a target held over one interval, define

$$y=x-x_\star,\qquadc=v+\omega y.$$

Then

$$x_{n+1}=x_\star+(y+c\Delta t)e^{-\omega\Delta t},$$

$$v_{n+1}=(v-\omega c\Delta t)e^{-\omega\Delta t}.$$

Using the closed-form follower avoids the timestep-dependent alternatingovershoot associated with a coarse explicit-Euler update. Orientation should beadvanced with normalized quaternions rather than independent Euler-angleincrements.

Plot 7: Retinal projection

What it displays

Packet positions are projected onto the observer's dynamic focal plane. Markersize or opacity may represent blur relative to an accepted circle of confusion.

The thin-lens relation is

$$\frac{1}{f}=\frac{1}{u}+\frac{1}{v},$$

where $u$ is object distance, $v$ is retina distance, and $f$ is focal length.Thus,

$$f=\left(\frac{1}{u}+\frac{1}{v}\right)^{-1}.$$

For pupil radius $a$, focus distance $s$, object distance $u$, and fixed retinadistance $v$, a geometric defocus radius is

$$r_b=av\left|\frac{1}{s}-\frac{1}{u}\right|.$$

This is a geometric retinal model. The classical pass decision comes from thecapture and detector-noise model, not from visual appearance alone.

Plot 8: Eye focus and accommodation

What it displays

Target distance.

Current focus distance.

Near and far depth-of-field limits.

Accommodation demand.

Signed focus error.

For acceptable blur radius $c$, define

$$\delta=\frac{c}{av}.$$

The corresponding near and far object distances are

$$u_{\mathrm{near}}=\frac{1}{1/s+\delta},$$

$$u_{\mathrm{far}}=\frac{1}{1/s-\delta},$$

when the far denominator is positive. The accommodation-demand proxy is

$$A\approx\frac{1}{s}$$

in dioptres when $s$ is measured in metres. This is not a complete biomechanicalmodel of the human lens.

Plot 9: Material trajectory

What it displays

Programmed and realized material-coordinate summaries.

Quality, residual scatter, and a positive-index counterfactual.

Active effort, phase compensation, angular width, and lifecycle controls.

A bounded normalized coordinate $x_i\in[-1,1]$ can be mapped to a physicalinterval by

\theta_{i,\min}+\frac{x_i+1}{2}\left(\theta_{i,\max}-\theta_{i,\min}\right).$$

The public abstraction of cloak quality is a weighted geometric mean,

w_{-n}\prod_{r\in\mathcal{M}}M_r^{\alpha_r},\qquad\sum_r\alpha_r=1,$$

where the matching factors may represent index, anisotropy, phase, impedance,and loss quality. The exact private factors, weights $\alpha_r$, calibrationmaps, and actuator semantics are not distributed.

A generic residual-scatter abstraction is

\sigma_{\mathrm{raw}}\left(1-s_cQ_c\right)G_{\mathrm{size}}.$$

A sign-specific counterfactual can be summarized as

\sigma_{+|n|}-\sigma_{-|n|}.$$

This tests the role of the signed-index branch inside the model. It does notprove that a fabricated material will produce the same response.

Plot 10: Photon dispersion and tensor diagnostics

What it displays

Scattered-packet RMS radius.

Three covariance principal radii.

Tensor norm and directional contraction summaries.

For packet positions $\mathbf{r}_p$,

\frac{1}{N}\sum_{p=1}^{N}\mathbf{r}_p,$$

\frac{1}{N}\sum_{p=1}^{N}(\mathbf{r}_p-\bar{\mathbf{r}})(\mathbf{r}_p-\bar{\mathbf{r}})^T.$$

The RMS radius is

$$r_{\mathrm{RMS}}=\sqrt{\operatorname{tr}\Sigma}.$$

If $\lambda_1,\lambda_2,\lambda_3$ are the covariance eigenvalues, the principalradii are

$$\sqrt{\lambda_1},\qquad\sqrt{\lambda_2},\qquad\sqrt{\lambda_3}.$$

Strong inequality among these radii indicates directional dispersion. Smallpacket dispersion alone does not establish low detector observability.

Plot 11: Controller and detector-noise diagnostics

What it displays

Objective, gradient, and accepted-step summaries.

Composite concealment index.

Residual and counterfactual scattering.

Throughput and shadow.

Shot, thermal, residual quantum, and total noise.

For expected signal count $N_s$ and Fano factor $F$,

$$\sigma_{\mathrm{shot}}=\sqrt{FN_s}.$$

Independent noise terms combine as

\sqrt{\sigma_{\mathrm{shot}}^2+\sigma_{\mathrm{thermal}}^2+\sigma_{\mathrm{quantum}}^2}.$$

A significance-aware detector may compare the excess count against$z\sigma_{\mathrm{total}}$ before forming a reported capture ratio.

Define normalized severities

$$q=\frac{F_Q}{F_{Q,\mathrm{lim}}},\qquadc=\frac{C}{C_{\mathrm{lim}}},\qquads=\frac{S}{S_{\mathrm{lim}}},\qquad\nu=\mathrm{SNR}.$$

A bounded display index can be formed from

$$\chi=\frac{1}{2}\sqrt{q^2+c^2+s^2+\nu^2},$$

$$I_{\mathrm{conceal}}=\frac{1}{1+\chi}.$$

This is a derived dashboard score. It is not a fundamental physical observableand should never replace the underlying channels.

Additional scientific audits

Audit 12: Standalone dual-visibility atlas

This view places the decisive QFI, capture, shadow, composite index, and captureSNR in one evidence-oriented panel. It is useful for verifying that a highcomposite score is not hiding a breach in one raw channel.

Audit 13: Sampled vector-paraxial wave atlas

For an applicable directional probe, the audit may report:

Field normalized mean-square error.

Phase RMSE.

Polarization leakage.

Modal crosstalk.

OAM infidelity and resolved closure.

State trace distance and finite-basis channel distances.

A field NMSE can be written

\frac{\lVert E_{\mathrm{cloak}}-E_{0}\rVert_2^2}{\lVert E_0\rVert_2^2}.$$

For a normalized input polarization $|p\rangle$ and normalized output coherencymatrix $J$, polarization fidelity and leakage are

$$F_{\mathrm{pol}}=\langle p|J|p\rangle,\qquadL_{\mathrm{pol}}=1-F_{\mathrm{pol}}.$$

For retained target-mode power $P_0$,

$$X_{\mathrm{modal}}=1-P_0.$$

An OAM comparison should report both fidelity inside the resolved basis and theresolved closure. These are separate gates so one finite-basis truncation is notpenalized twice.

For two density operators,

$$D(\rho,\sigma)=\frac{1}{2}\lVert\rho-\sigma\rVert_1.$$

Under equal priors, the optimal binary Helstrom error is

$$P_{e}^{\star}=\frac{1}{2}\left(1-D(\rho,\sigma)\right).$$

For the default incoherent all-sky source, a single global complex field, phase,modal state, and OAM state are not defined. Those coherent audits are thereforenot applicable unless a directional probe is selected.

Audit 14: Wavefront or angular representation

A directional coherent probe can support detector-plane complex-field andpolarization maps. An incoherent all-sky intensity ensemble cannot be assigned asingle global phase without inventing coherence that the source does not have.Its public representation should remain angular or intensity-based.

Audit 15: Rolling wavelength severity

A time-by-wavelength observability severity is

\max\left[\frac{F_Q(t,\lambda)}{F_{Q,\mathrm{lim}}},\frac{C(t,\lambda)}{C_{\mathrm{lim}}},\frac{S(t,\lambda)}{S_{\mathrm{lim}}}\right].$$

A loss severity is

\max\left[\frac{\mathcal{S}(t,\lambda)}{\mathcal{S}{\mathrm{lim}}},\frac{\mathcal{A}(t,\lambda)}{\mathcal{A}{\mathrm{lim}}}\right].$$

At a sampled node, values at or below one pass the corresponding normalizedcriterion.

Quantum Fisher information

The private engine evaluates a finite reduced density operator $\rho(\phi)$ fora declared parameter $\phi$. The public repository intentionally does notpublish the complete material-to-channel map

$$\boldsymbol{\theta}\longmapsto\rho(\phi;\boldsymbol{\theta}).$$

For a spectral decomposition

$$\rho=\sum_i\lambda_i|i\rangle\langle i|,$$

QFI is

\sum_{i,j:\lambda_i+\lambda_j>0}\frac{2\left|\langle i|\partial_{\phi}\rho|j\rangle\right|^2}{\lambda_i+\lambda_j}.$$

A centered finite difference is

$$\partial_{\phi}\rho\approx\frac{\rho(\phi+h)-\rho(\phi-h)}{2h},$$

while an automatic-differentiation backend may evaluate the derivative directly.

The quantum Cramér-Rao bound gives

$$\operatorname{Var}(\hat{\phi})\geq\frac{1}{N F_Q},$$

for $N$ independent probes under the usual regularity assumptions.

Therefore, low $F_Q$ means that the declared parameter becomes difficult toestimate. It does not automatically mean:

the object cannot be detected,

every quantum measurement fails,

every physical parameter is hidden,

every state, angle, wavelength, or detector is concealed.

This is why QFI is paired with classical capture, shadow, throughput, absorption,and applicable channel-distance diagnostics.

Control mathematics

Standard simultaneous perturbation stochastic approximation uses schedules

$$a_k=\frac{a}{(A+k)^{\alpha}},\qquadc_k=\frac{c}{k^{\gamma}},$$

and Bernoulli perturbations

$$\Delta_{k,i}\in{-1,+1}.$$

The two-evaluation gradient estimator is

J(\mathbf{x}_k-c_k\boldsymbol{\Delta}_k)}{2c_k}\boldsymbol{\Delta}_k.$$

A projected update has the generic form

\Pi_{\mathcal{X}}\left(\mathbf{x}_k-a_k\widehat{\mathbf{g}}_k\right).$$

The private MSGA policy adds guarded comparisons under a frozen disturbance so aproposal is not automatically accepted merely because a noisy gradient pointsthere. The exact objective composition, trust region, moments, rescue rules,headroom logic, and coefficients remain private.

Energy and anti-absorption logic

A concealment system should not receive credit for simply destroying the probe.The energy partition is conceptually audited as

$$R+A+\mathcal{S}+T=1,$$

where

$R$ is reflected fraction,

$A$ is absorbed fraction,

$\mathcal{S}$ is diffuse scattering fraction,

$T$ is forward transmitted fraction.

A valid control objective therefore needs separate penalties or constraints forabsorption and inadequate throughput. Low capture accompanied by high absorptionis a black absorber, not a successful restoration cloak.

Scientific claim matrix

Statement

Public status

The dashboard studies simultaneous classical and QFI suppression

Supported by project design

A reported private run crossed configured thresholds

Requires hashed raw private exports

The bundled synthetic showcase crossed thresholds

Educational only, not scientific evidence

The model proves omnidirectional visible-band invisibility

Not supported

The model is a full Maxwell or QED solver

False

The finite flag complex proves a topological material phase

False

Named material constants represent a fabricated specimen

Not without specimen-specific calibration

Low QFI equals universal quantum undetectability

False

Throughput and absorption must be audited with observability

Supported methodological requirement

Scientific limitations

Reduced-order physics: The private model is not FDTD, FEM, PIC, ab-initio,or full-vector Maxwell simulation.

Finite source sampling: Spectral and angular nodes do not establish acontinuum proof.

Finite quantum channel: QFI and channel distances refer to a declaredreduced state space and parameterization.

Model-coupled observables: Classical and quantum metrics arise from thesame modeled material state and are not independent laboratory instruments.

Illustrative material priors: Uncalibrated constants cannot certify agraphene, GO/rGO, hBN, ITO, or generic metamaterial specimen.

Display particles: Packet animation is explanatory rather thancarrier-resolved electrodynamics.

One-scale topology: Displayed Betti numbers are not persistence diagramsor material topological invariants.

Accelerated lifecycle: Damage and healing rates require sample-specificvalidation before predictive use.

Synthetic public data: The bundled showcase is intentionally incapable ofestablishing private-engine performance.

Publishing a real result safely

Do not copy the private notebook into this repository and delete cells. Instead:

Run the private engine in the private repository.

Export the complete result privately.

Apply a private allow-list sanitizer.

Review the sanitized CSV manually.

Validate the exact public schema.

Generate public plots only from the sanitized CSV.

Publish a manifest containing hashes, version, run date, and limitations.

Run the public-release audit before pushing.

The public renderer rejects extra telemetry columns:

python scripts/verify_public_telemetry.py data/public_telemetry.csv

The complete schema is documented indocs/PUBLIC_TELEMETRY_SCHEMA.md.

Collaboration

The private implementation is available only through a controlled collaboration.A serious request should identify:

the research question,

the proposed contribution,

the concrete deliverable,

relevant prior work,

the minimum access required,

attribution and publication expectations,

confidentiality and IP expectations.

Open aCollaboration requestor read COLLABORATION.md.

Private access may begin with a narrow dataset, frozen executable, hosted API, orspecific module rather than the complete source tree.

Copyright and permissions

Copyright © 2026 Christopher Salnave. All rights reserved.

This repository is publicly viewable but not open source. No broad license isgranted to copy, modify, redistribute, sublicense, sell, or create derivativeworks from the repository contents beyond platform terms, applicable law, or aseparate written agreement.

See LICENSE.md, NOTICE.md, and docs/IP_AND_GITHUB_RELEASE_NOTES.md.

[!CAUTION]A notice deters lawful reuse but cannot physically prevent copying. The coreprotection is architectural: do not place enabling private material in apublic repository or its Git history.

Citation

Suggested citation:

@software{salnave_obscura_2026,
  author  = {Christopher Salnave},
  title   = {OBSCURA: Programmable Metamaterial Dual-Observability Lab},
  year    = {2026},
  version = {Public Showcase 1.0},
  url     = {https://github.com/csalnav2/obscura-metamaterial-observability-lab},
  note    = {Reduced-order simulated dual-observability benchmark; public showcase does not include the private engine}
}

A machine-readable citation is available in CITATION.cff.

Background references

S. L. Braunstein and C. M. Caves, “Statistical distance and the geometry ofquantum states,” Physical Review Letters 72, 3439-3443 (1994).https://doi.org/10.1103/PhysRevLett.72.3439

J. C. Spall, “Multivariate stochastic approximation using a simultaneousperturbation gradient approximation,” IEEE Transactions on AutomaticControl 37, 332-341 (1992). https://doi.org/10.1109/9.119632

J. B. Pendry, D. Schurig, and D. R. Smith, “Controlling electromagneticfields,” Science 312, 1780-1782 (2006).https://doi.org/10.1126/science.1125907

U. Leonhardt, “Optical conformal mapping,” Science 312, 1777-1780 (2006).https://doi.org/10.1126/science.1126493

Repository status

Research prototype and collaboration showcase. The private implementation isunder active development. Public artifacts should be interpreted according totheir provenance labels: synthetic, sanitized private export, orindependently reproduced.
