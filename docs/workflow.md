# Workflow for UDOT Team

Prototype workflow notebooks can be found in the [UDOT Wrangler GitHub repository's notebook folder](https://github.com/wsp-sag/udot_wrangler/tree/main/.notebook).

## Step 1. Build a Base Network Scenario from UDOT CUBE Network

A step-by-step guide is available in the example jupyter notebook `01-make-network-wrangler-files-from-cube.ipynb`.

!!! tip "create a base scenario"

    This step should only be run once to create the base scenario. Once created, all work should be performed on top of the base scenario.

## Step 2. Create A Project Card from A CUBE LOG File

A step-by-step guide is available in the example jupyter notebook `02-make-project-cards-from-cube-logs.ipynb`.

The following cell in this notebook requires users to define paths to their local clones of `udot_wrangler` and `cube_wrangler`.
```python
udot_parameters = UDOT_Parameters(
    udot_wrangler_base_dir = "path/to/your/local/udot/wrangler/folder",
    cube_wrangler_base_dir = "path/to/your/local/cube/wrangler/folder",
)
```
To do that, users can run the following commands in Command Prompt to make sure they have `udot_wrangler` and `cube_wrangler` folders locally
```bash
cd path to where you want to put wrangler
git clone https://github.com/wsp-sag/udot_wrangler
git clone https://github.com/network-wrangler/cube_wrangler
```

!!! tip "add project metadata to project card skeleton"

    The Project Cards created by this notebook are "skeletons" because they do not contain project meta information. User can open the skeletons and add information such as `project`, `tags`, `dependencies`, and `notes`. For more guidance, refer to the documentation for [ProjectCard](https://network-wrangler.github.io/projectcard/main/).

## Step 3. Push Project Cards to Project Card Registry

When two people code network changes in parallel in CUBE, it is common that they create new links and nodes with overlapping IDs. However, overlapping IDs are not allowed in Network Wrangler by design. To avoid overlapping IDs, users can submit their generated project cards into a Project Card Registry. A Project Card Registry does the following:

- Identifies Project Cards that add roadway or transit links to the network.
- Hosts a registry of new nodes and/or new links, identifying the project that adds them
- Automatically recodes overlapping new nodes and/or new link IDs in the project cards
- Fails if the Project Card adds a node or link with an ID that is already in the base network, as this suggests there may be a disconnect between the configuration file and the details of the base network.

!!! tip "add project cards to registry"

    We have set up a registry for the Cache county: [cache_project_card_registry](https://github.com/wsp-sag/cache_project_card_registry), and have staged some real project cards in the `stage` branch. Users can continue to add project cards to the `stage` branch or create another branch.

!!! tip "final project cards"

    Use project cards from the project card registry as the final cards for production.

## Step 4. Create a Build Network Scenario

A step-by-step guide is available in the example jupyter notebook `03-apply-project-cards-and-create-buid-network.ipynb`.

!!! tip "mix and match project cards"

    You can create a scenario with a group of project cards by specifying the corresponding project `tag`.

!!! tip "write out CUBE network"

    UDOT Wrangler does not require CUBE license. Therefore it does not directly output a .net CUBE file. Instead, it write out links and nodes in fixed width format and a CUBE .s script that users can execute in CUBE to create the .net file.