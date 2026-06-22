UDOT Wrangler is a Python library for UDOT-related paramters and utilities with Network Wrangler.

## User Guide
The latest user guide can be found on the GitHub IO page: [https://wsp-sag.github.io/udot_wrangler/](https://wsp-sag.github.io/udot_wrangler/).

## Workflow
The typical workflow for using UDOT Wrangler is demonstrated with the Cache County model network. The documentation for the workflow can be found on the [Workflow](https://wsp-sag.github.io/udot_wrangler/workflow.html) tab of the GitHub IO page.

## Example Notebooks
Example prototype notebooks can be found in the .notebook folder. Examples include
1. Create a base Network Wrangler scenario with input roadway network.
2. Create Project Card skeleton with input CUBE LOG.
3. Create a build scenario and apply project card, write out the build Network Wrangler scenario as well as the build CUBE roadway network.

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