# Contributing to UDOT Wrangler

## Setup

### Recommended Tools

- [GitHub desktop](https://desktop.github.com/) to manage access to the main repository.
- [Git](https://git-scm.com/downloads) to conduct required version control.
- [VSCode](https://code.visualstudio.com/download) to edit and test code.
- Some type of terminal application (note, this comes with Mac/Ubuntu).

### Setup Virtual Environment

Create and/or activate the virtual environment where you want to install UDOT Wrangler.

### Clone

To effectively work on UDOT Wrangler locally, install it from a clone by either:

1. Use the GitHub user interface by clicking on the green button "clone or download" in the [main UDOT wrangler repository page](https://github.com/wsp-sag/udot_wrangler).
2. Use the command prompt in a terminal to navigate to the directory that you would like to store your udot wrangler clone and then using a [git command](https://git-scm.com/downloads) to clone it.

!!! example "Clone udot wrangler"
    ```bash
    cd path to where you want to put wrangler
    git clone https://github.com/wsp-sag/udot_wrangler
    ```

### Install in Develop Mode

Install UDOT Wrangler in ["develop" mode](https://pip.pypa.io/en/stable/reference/pip_install/?highlight=editable#editable-installs) using the `-e` flag so that changes to your code will be reflected when you are using and testing udot wrangler:

!!! example "Install UDOT Wrangler from Clone"
    ```bash
    cd udot_wrangler
    pip install -e .
    ```

### IDE Settings

### VSCode

Select conda env as Python interpreter:

`cmd-shift-P`: Python: Select Interpreter


## Development Workflow

1. Create [an issue](https://github.com/wsp-sag/udot_wrangler/issues) for any features/bugs that you are working on.
2. [Create a branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository) to work on a new issue (or checkout an existing one where the issue is being worked on).  

## Code of Conduct

Contributors to the UDOT Wrangler Project are expected to read and follow the [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md) for the project.
