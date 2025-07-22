These notebooks are prototypes for demonstrating the Network Wrangler workflow with the Cache County network.

## Data
The data to run these notebooks can be found on [WSP OneDrive](https://wsponlinenam.sharepoint.com/:f:/r/sites/US-UDOT-Network-Wran/Shared%20Documents/Phase_1/prototype_cache?csf=1&web=1&e=cIVGk6).

## Notebooks

- `01-make-network-wrangler-files-from-cube.ipynb` creates a base Network Wrangler scenario with input roadway network. This notebook only needs to be run once.
- `02-make-project-cards-from-cube-logs.ipynb` creates Project Card skeleton from input CUBE LOG. Users can then edit the output Project Card skeleton with project information including project description, dependencies, tags, etc.
- `03-apply-project-cards-and-create-build-network.ipynb` creates a build scenario and applies project card, writes out the build scenario in Network Wrangler format. It also writes out build links and nodes in fixed width format for generating CUBE roadway network (.net). Along with the fixed width format files, there is a `make_cube_roadway_network_from_fixed_width_file.s` CUBE script that users can run to generate the build CUBE .net.

## Parameters
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