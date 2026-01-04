# LAMTA Examples

This documentation site hosts example notebooks for the **LAMTA** package.
The notebooks are designed to run both locally and on Read the Docs.
Large raw datasets are not committed to this repository.

## Notebooks
- **Ocean_examples**: loading SST / altimetry / bathymetry fields and basic plots.
- **Lagrangian**: particle advection and diagnostics (FTLE, etc.).

## Data
Notebooks download small reference datasets automatically from GitHub Releases (tag `data-v0.1`) using `pooch`.
Downloaded files are verified via SHA256 and cached locally.

## Installation (local)
1. Create and activate the conda environment:
   ```bash
   conda env create -f conda/environment.yml
   conda activate lamta_examples
   ```

2. Install this repository (to access lamta_examples.data_fetch):
   ```bash
    pip install -e .
   ```

3. Install LAMTA (core package):
   ```bash
    pip install git+https://github.com/OceanCruises/LAMTA.git
    ```