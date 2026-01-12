# LAMTA example datasets and notebooks

This repository (`LAMTA_examples`) contains a collection of **tutorial notebooks**
illustrating Lagrangian trajectory analysis and diagnostics using the **LAMTA**
framework.

The full documentation, including rendered notebooks and workflow explanations,
is available on Read the Docs:

[Read the LAMTA examples documentation](https://lamta-examples.readthedocs.io/en/latest/)


## Notes on Read the Docs

The notebooks displayed on Read the Docs are rendered using **precomputed outputs**.
They are **not executed online**.

To reproduce, modify, or extend the analyses, the notebooks must be run locally
in a suitable Python environment with LAMTA installed.

## Data access model

The example notebooks rely on a set of **reference datasets** distributed via a
dedicated GitHub release:

**LAMTA examples data (v0.1)**  
Release tag: [`data-v0.1`](https://github.com/OceanCruises/LAMTA_examples/releases/tag/data-v0.1)

The data archives are **not committed to the repository**. Instead, they are:

- Hosted as compressed `.tar.gz` assets in the GitHub release
- Downloaded automatically at runtime using `pooch`
- Verified using SHA256 checksums
- Extracted locally into a `data/` directory

No manual download is required when running the notebooks locally
or when building the documentation.

Data access is handled programmatically via the helper function
`ensure_dataset()`.

## Contents of the data release

The data release provides reference datasets defining the expected file names,
variable conventions, and directory structure used in the notebooks:

- **Bathymetry**
  - ETOPO 2022 (Mediterranean Sea)

- **Sea Surface Temperature (SST)**
  - GHRSST OSTIA L4 (global, sample)
  - Sentinel-3 SLSTR L2P (Mediterranean Sea, June 2023)

- **Altimetry**
  - CMEMS DUACS merged all-sat L4 (Europe, June 2023)
  - Near-real-time (NRT) all-sat L4 (Europe, May 2023)
  - Near-real-time (NRT) all-sat L4 (Global, September 2022)

- **SWOT**
  - SWOT L3 LR SSH Expert (June 2023)

## Intended use

These datasets and notebooks are intended for:
- demonstration
- testing
- documentation
- development support

They are **not intended for scientific production use**.

Users applying LAMTA to their own datasets should use these examples
as a **reference for workflow and data structure**, and adapt the
loading routines accordingly.
