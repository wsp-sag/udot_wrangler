---
hide:
 - navigation
---

UDOT Wrangler is a Python library for UDOT-related paramters and utilities with Network Wrangler.

## System Requirements

We recommend using Python 3.10 for UDOT Wrangler. If you have a different version of Python installed (e.g. from ArcGIS), PIP or a Python environment manager such as uv can take care of installing it for you in the installation instructions below.

!!! tip "installing Python"

    UDOT Wrangler has been fully tested with 3.10. Using the latest version of Python 3.13 may have compatibility issues with any updated APIs or dependencies. If you would like to install Python 3.10. You can do so from the official Python release: https://www.python.org/downloads/. It should take care of installing pip for you.

!!! tip "installing conda?"

    For conda users, apologies that UDOT Wrangler has not yet been published to conda distribution channels. You will not be able to install via your common `conda install ...` command. But you could use `pip install ...`.

## Installation

### Step 1. Create and Activate Virtual Environment

Create and/or activate the virtual environment where you want to install UDOT Wrangler.

!!! example "Option 1 (RECOMMENDED). Use a modern Python manager such as UV"

    If you care about speed and dependency lock, UV is a better option than others. But first, you need to install UV, see detailed instructions here: https://docs.astral.sh/uv/getting-started/installation/.

    ```bash
    # Run the installer. Please review the printed message after installation.
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

    # Add uv to PATH
    $env:PATH = "$env:USERPROFILE\.local\bin;$env:Path"
    ```

    To verify that UV is installed correctly, open a new Command Prompt (not Anaconda Prompt) and run the following command.
    ```bash
    uv --version
    ```

    Then you can create and activate a new Python environment with UV. In the Command Prompt, the following commands will create a new Python environment with Python 3.10.

    ```bash
    # make a directory for your uv environment
    mkdir udot_wrangler_env
    cd udot_wrangler_env
    uv init --python 3.10
    ```

!!! example "Option 2 (Most Familiar to Python Users). Create a new Python virtual environment using Conda"

    ```bash
    conda create -n udot_wrangler_env python=3.10
    conda activate udot_wrangler_env
    ```

!!! example "Option 3 (For Users Who Prefer PIP). Create a new Python virtual environment using PIP"

    ```bash
    python -m venv udot_wrangler_env
    udot_wrangler_env\Scripts\activate
    ```

### Step 2. Install UDOT Wrangler and its Dependencies
UDOT Wrangler is available on PyPI.

#### From Latest Official Release on PyPI
If users use uv in Step 1, they will install UDOT Wrangler via uv. In a Command Prompt:
```bash
# make sure you are in the directory that you created for your uv environment in Step 1
cd path\to\udot_wrangler_env
uv add udot-wrangler --prerelease=allow
# if `network-wrangler` is a prerelease
# uv add udot-wrangler --prerelease=allow
```

If users use Conda or PIP in Step 1, they can install UDOT Wrangler via the standard pip command. In the activated Python environment created in Step 1, type:
```bash
pip install udot-wrangler
```

#### From GitHub
```bash
pip install git+https://github.com/wsp-sag/udot_wrangler.git@main#egg=udot_wrangler
```

If you wanted to install from a specific tag/version number or branch, replace `@main` with `@<branchname>`  or `@tag`

#### From Local Clone

If you are going to be working on UDOT Wrangler locally, you might want to clone it to your local machine and install it from the clone.  The -e will install it in [editable mode](https://pip.pypa.io/en/stable/reference/pip_install/?highlight=editable#editable-installs).

If you have [GitHub desktop](https://desktop.github.com/) installed, you can either do this by using the GitHub user interface by clicking on the green button "clone or download" in the [main UDOT wrangler repository page](https://github.com/wsp-sag/udot_wrangler).

Otherwise, you can use the command prompt to navigate to the directory that you would like to store your UDOT wrangler clone and then using a [git command](https://git-scm.com/downloads) to clone it.

```bash
cd path to where you want to put wrangler
git clone https://github.com/wsp-sag/udot_wrangler
```

Then you should be able to install UDOT Wrangler in "develop" mode.

```bash
cd udot_wrangler
pip install -e .
```

### Step 3. Getting Ready to Run Example Notebooks
The 02 and 03 example notebooks requires the user to define paths to their local clones of udot_wrangler and cube_wrangler. To do that, users can run the following commands in Command Prompt to make sure they have udot_wrangler and cube_wrangler folders locally. If you have already cloned them in Step 2, you can skip this step.

```bash
cd path to where you want to put wrangler
git clone https://github.com/wsp-sag/udot_wrangler
git clone https://github.com/network-wrangler/cube_wrangler
```

### Common Installation Issues
TBD (please give us feedback on any installation issues you encounter so that we can document them here!)

## Quickstart

To get a feel for the API and using project cards, please refer to the prototype jupyter notebooks in `.notebook`.

To start the notebook, open a command line in the udot_wrangler top-level directory and type:

`jupyter notebook`

When launching jupyter notebook from conda, you may want to set the following:

```bash
conda install ipykernel
python -m ipykernel install --user --name=udot_wrangler_env --display-name "Python (udot_wrangler_env)"
```

## Contributing

Contributions are welcome. Please review [contributing guidelines and instructions](development.md).

## Companion Software
The following software are key dependencies of UDOT Wrangler. They are installed as part of UDOT Wrangler installation so that you do not need to install them individually.

[NetworkWrangler](https://network-wrangler.github.io/network_wrangler): Network Wrangler is a Python library for managing travel model network scenarios.

[CubeWrangler](https://network-wrangler.github.io/cube_wrangler): A Python package that contains utilities for working with Network Wrangler and CUBE. CUBE is a commercial travel modeling software package. CUBE Wrangler contains methods for carrying out the I/O to and from CUBE.

[ProjectCard](https://network-wrnagler.github.io/projectcard): Initially part of NetworkWrangler, the functionality for reading, writing and validating ProjectCard objects was pulled out into a separate project so that it could be used by other entities without necessitating NetworkWrangler.

## Having an issue?

🪲 UDOT Wrangler may contain bugs.

🤔 Also, since it has primarily been used by its developers, the documentation may contain some omissions or not be entirely clear.

But we'd love to make it better! Please report bugs or incorrect/unclear/missing documentation with a [GitHub Issue](https://github.com/wsp-sag/udot_wrangler/issues) -  or [fix them yourself with a pull request](development.md)!

## License

[Apache-2.0](https://choosealicense.com/licenses/apache-2.0/)

## Release History

{!
    include-markdown "../CHANGELOG.md"
    heading-offset=1
!}
