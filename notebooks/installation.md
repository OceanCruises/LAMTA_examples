# Installation steps

## 1. Create and activate the examples environment

We recommend using a dedicated Conda environment to ensure all native
dependencies (HDF5, PROJ, GEOS, etc.) are available.

```bash
git clone https://github.com/OceanCruises/LAMTA_examples
cd LAMTA_examples
conda env create -f environment.yml
conda activate lamta_examples
```

This installs the scientific stack required by the notebooks
(`numpy`, `scipy`, `xarray`, `netCDF4`, `cartopy`, `matplotlib`, etc.).

---

## 2. Link your existing LAMTA installation to this environment

If you are **developing LAMTA** and already have a local clone, install it
in editable mode into the **activated** `lamta_examples` environment:

```bash
pip install -e /absolute/path/to/your/LAMTA
```

This reuses your existing working tree and ensures that any local changes
to LAMTA are immediately visible to the notebooks.

If LAMTA is already installed in editable mode in another environment,
you must still repeat this step for `lamta_examples` environment
(editable installs are environment-specific).

---

## 3. Verify that LAMTA is correctly available

```bash
python -c "import lamta; print('LAMTA import OK')"
```

If this fails, ensure that:
- the correct environment is activated,
- LAMTA was installed into this environment.

---

## 4. Open the notebooks

You can use **any Jupyter-compatible interface** (JupyterLab, classic Jupyter, VS Code, etc.).

- Make sure the `lamta_examples` environment is activated
- Open a notebook from the `notebooks/` directory
- When prompted, select the **`lamta_examples` Python kernel**

For example:
- **VS Code**: open a notebook → select kernel in the top-right corner
- **JupyterLab / Jupyter Notebook**: choose the kernel when opening the notebook