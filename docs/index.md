---
hide:
 - navigation
---

UDOT Wrangler is a Python library for UDOT-related paramters and utilities with Network Wrangler.

## System Requirements

UDOT Wrangler does require Python 3.7+. (Note: Recommend Python version: 3.10) If you have a different version of Python installed (e.g. from ArcGIS), PIP or a similar virtual environment manager can care of installing it for you in the installation instructions below.

!!! tip "installing Python"

    UDOT Wrangler has been fully tested with 3.10. Using the latest version of Python 3.13 may have issues with any updated APIs or dependencies. If you would like to install Python 3.10. You can do so from the official Python release: https://www.python.org/downloads/. It should take care of installing pip for you.

??? warning "installing conda?"

    For conda users, apologies that UDOT Wrangler has not yet been published to conda distribution channels. You will not be able to install via your common `conda install ...` command. But you could use the From Clone option describes in the Installation section below.

## Installation

### Step 1. Create and Activate Virtual Environment

Create and/or activate the virtual environment where you want to install UDOT Wrangler.

!!! example "Option 1. Create a new Python virtual environment for using pip"

    ```bash
    python -m venv udot_wrangler_env
    udot_wrangler_env\Script\activate
    pip install udot-wrangler
    ```

!!! example "Option 2. Use Python package and project manager such as UV"

    If you care about speed and dependency lock, UV is a better option than pip.

    ```bash
    uv init
    ```

### Step 2. Install UDOT Wrangler and its Dependencies
UDOT Wrangler is available on PyPI.

#### Latest Official Version
Users can install via standard pip command. In the activated Python environment created in Step 1, type:
```bash
pip install udot-wrangler
```

Users can also install via UV.
```bash
uv add udot-wrangler
# if `network-wrangler` is a prerelease
# uv add udot-wrangler --prerelease=allow
```

#### From GitHub
```bash
pip install git+https://github.com/wsp-sag/udot_wrangler.git@main#egg=udot_wrangler
```

If you wanted to install from a specific tag/version number or branch, replace `@main` with `@<branchname>`  or `@tag`

#### From Clone

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

### Common Installation Issues
TBD

## Quickstart

To get a feel for the API and using project cards, please refer to the prototype jupyter notebooks in `.notebook`.

To start the notebook, open a command line in the udot_wrangler top-level directory and type:

`jupyter notebook`

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
