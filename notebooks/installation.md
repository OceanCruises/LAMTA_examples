# Installation steps

## 1. Clone the examples repository

```{warning}
If you plan to contribute to the code or documentation, we recommend forking the repository first and cloning your fork instead.
```

```bash
# Users
git clone https://github.com/OceanCruises/LAMTA_examples

# Contributors
# git clone https://github.com/<your-username>/LAMTA_examples

cd LAMTA_examples
```

---

## 2. Create and activate the examples environment

We recommend using the dedicated Conda environment to ensure that the notebook, plotting, and native dependencies are available.

```bash
conda env create -f conda/environment.yml
conda activate lamta_examples
```

This creates the `lamta_examples` environment with Python 3.12 and the tools required to run the notebooks, including `ipykernel`, `matplotlib`, `cartopy`, and `cmocean`.

---

## 3. Install LAMTA Examples

From the root of the cloned `LAMTA_examples` repository:

```bash
python -m pip install -e .
```

This installs `LAMTA_examples` in editable mode together with its Python dependencies.

LAMTA is automatically installed from the [OceanCruises/LAMTA](https://github.com/OceanCruises/LAMTA) repository, so a separate LAMTA installation is not required for users who only want to run the example notebooks.

---

## 4. Verify the installation

Check that LAMTA is available in the environment:

```bash
python -c "import lamta; print('LAMTA import OK')"
```

You can also check which LAMTA installation is being used:

```bash
python -c "import lamta; print(lamta.__file__)"
```

---

## 5. Run the notebooks

You can use any Jupyter-compatible interface such as **VS Code**, JupyterLab, or classic Jupyter Notebook.

We recommend **Visual Studio Code**.

- Make sure the `lamta_examples` environment is available
- Open a notebook from the `notebooks/` directory
- Select the **`lamta_examples`** Python kernel

In VS Code, open the notebook and use **Select Kernel** in the top-right corner to select `lamta_examples`.

---

## Developing LAMTA locally

The installation above is recommended for users who want to run the example notebooks.

If you are also developing LAMTA itself, we recommend cloning both repositories side-by-side:

```text
lamta_dev/
├── LAMTA/
└── LAMTA_examples/
```

After creating and activating the `lamta_examples` environment and installing `LAMTA_examples`, install the local LAMTA checkout in editable mode:

```bash
conda activate lamta_examples
python -m pip install -e ../LAMTA
```

This replaces the LAMTA version installed from GitHub with your local editable checkout. Any changes made to the local LAMTA source code will then be immediately available when running the example notebooks.