UDOT Wrangler is a Python library for UDOT-related paramters and utilities with Network Wrangler.

## System Requirements
UDOT Wrangler does require Python 3.7+. (_Note: Recommend Python version: 3.10_) If you have a different version of Python installed (e.g. from ArcGIS), conda or a similar virtual environment manager can care of installing it for you in the installation instructions below.

## Installation
UDOT Wrangler is available on PyPI.

### Latest Official Version
Users can install via standard pip command. _Note: Recommend Python version: 3.10_
```bash
pip install udot-wrangler
```

Users can also install via package managers such as uv.
```bash
uv add udot-wrangler
# if `network-wrangler` is a prerelease
# uv add udot-wrangler --prerelease=allow
```

### From GitHub
```bash
pip install git+https://github.com/wsp-sag/udot_wrangler.git@main#egg=udot_wrangler
```

If you wanted to install from a specific tag/version number or branch, replace `@main` with `@<branchname>`  or `@tag`

### From Clone

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
## Example Notebooks
Example prototype notebooks can be found in the .notebook folder. Examples include
1. Create a base Network Wrangler scenario with input roadway network.
2. Create Project Card skeletion with input CUBE LOG.
3. Create a build scenario and apply project card, write out CUBE roadway network.

The following cell in these notebooks requires users to define path to their local clones of `udot_wrangler` and `cube_wrangler`.
```python
udot_parameters = UDOT_Parameters(
    udot_wrangler_base_dir = "path/to/your/local/udot/wrangler/folder",
    cube_wrangler_base_dir = "path/to/your/local/cube/wrangler/folder",
)
```
To do that, users can run the follow commands in the command prompt to make sure they have `udot_wrangler` and `cube_wrangler` folders locally
```bash
cd path to where you want to put wrangler
git clone https://github.com/wsp-sag/udot_wrangler
git clone https://github.com/network-wrangler/cube_wrangler
```