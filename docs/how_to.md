# How To

## Build a Base Network Scenario from UDOT CUBE Network

You can find the example jupyter notebook `01-make-network-wrangler-files-from-cube.ipynb`.

!!! tip "create a base scenario"

    This step should only be run once to create the base scenario. Once created, all work should be performed on top of the base scenario.

## Create A Project Card from A CUBE LOG File

You can find the example jupyter notebook `02-make-project-cards-from-cube-logs.ipynb`.

!!! tip "add project metadata to project card skeleton"

    The Project Cards created by this notebook are "skeleton" in that they do not contain enough project meta information. User can open the skeletons and enter the information on `project`, `tags`, `dependencies`, and `notes`. See documentation from [ProjectCard](https://network-wrangler.github.io/projectcard/main/)

## Push Project Cards to A Registry

When two people coding network changes in parallel in CUBE, it is possible that they create new links and nodes without overlapping IDs. However, overlapping IDs are not allow in Network Wrangler by design. To avoid overlapping IDs, users should push the project cards they generated into a Project Card Registry. A project card registry does the following:

- Identifies Project Cards that add roadway or transit links to the network.
- Hosts a registry of new nodes and/or new links, identifying the project that adds them
- Automatically recodes overlapping new nodes and/or new link IDs in the project cards
- Fail if the Project Card adds a node or link with an ID that is already in the base network, as this suggest there may be a disconnect between the configuration file and the details of the base network.

!!! tip "add project cards to registry"

    We have set up a registry for the Cache county: [cache_project_card_registry](https://github.com/wsp-sag/cache_project_card_registry), and have staged some real project cards in the `stage` branch. Users can continue to add project cards to the `stage` branch or create another branch.

## Create a Build Network Scenario

You can find the example jupyter notebook `03-apply-project-cards-and-create-buid-network.ipynb`.

!!! tip "mix and match project cards"

    You can create a scenario with a group of project cards by specifying the corresponding project `tag`

!!! tip "write out CUBE network"

    UDOT Wrangler does not require CUBE license. Therefore it does not directly output a .net CUBE file. Instead, it write out links and nodes in fixed width format and a CUBE .s script that users can execute in CUBE to create the .net file.