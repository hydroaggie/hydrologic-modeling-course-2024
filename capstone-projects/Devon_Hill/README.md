# 1D Column Model for Hydrothermal Processes in the Tundra Active Layer
This repository contains data and scripts necessary for reproducing a 1D Column Model for Hydrothermal Processes in the Tundra Active Layer using ATS.

## Summary
Hydrologic processes influence carbon transport in the layer which seasonally freezes and thaws above permafrost (active layer) by controlling redox state and thus the transformation and mobilization of carbon (Cardenas et al., 2023). Building a model to accurately represent the hydrothermal processes in the active layer and provide a good foundation for future, more complex modeling is the
motivation for this project.

one sentence on the overall goal of this project, 2-3 sentences on the objectives, 1-2 sentences on the expected outcome.

## Methods
- Modeling tool: ATS

- Study Area
State what real or hypothetical study area you will be working on 

## Repository Structure
```
|-- data
|-- model
|   |-- inputs
|   `-- outputs
|-- scripts
`-- results
|   |-- figures
```
- `data`: provides data needed to run the model (e.g., meshes, meterological forcing, observation, etc.)
- `model`: provides input files and essential model outputs (e.g., observation points, mass balance)
- `scripts`: provides the scripts or jupyter notebooks for pre- and post- processing model files
- `results`: provides any results generated from the model analysis (e.g., figures associated with report)

## Citation
Cardenas, M. B., Neilson, B. T., Shuai, P., Kling, G., Cory, R., Coon, E. (2023). DOE Proposal Narrative: Dynamics of interconnected surface-subsurface flow and reactive transport
processes across the hillslope-riparian zone river corridor continuum of cold, high-latitude watersheds. 1-20.

E.T. Coon, M. Berndt, A. Jan, D. Svyatsky, A.L. Atchley, E. Kikinzon, D.R. Harp, G. Manzini, E. Shelef, K. Lipnikov, R. Garimella, C. Xu, J.D. Moulton, S. Karra, S.L. Painter, E. Jafarov, and S. Molins. 2020. Advanced Terrestrial Simulator. U.S. Department of Energy, USA. Version 1.0. [Github Repo](https://github.com/amanzi/ats).

Provide any citation for the model or data (if it is stored somewhere else).
