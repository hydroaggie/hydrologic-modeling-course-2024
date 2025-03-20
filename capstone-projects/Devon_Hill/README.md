# 1D Column Model for Hydrothermal Processes in the Tundra Active Layer
This repository contains data and scripts necessary for reproducing a 1D Column Model for Hydrothermal Processes in the Tundra Active Layer using ATS.

## Summary
Hydrologic processes influence carbon transport in the layer which seasonally freezes and thaws above permafrost (active layer) by controlling redox state and thus the transformation and mobilization of carbon (Cardenas et al., 2023). The motivation for this project is to utlimately add understanding to cold region carboon budget by building a model to accurately represent the hydrothermal and chemical processes in this active layer. Given the complexity and difficulty of such a model, the overall goal for this class project is to build a working 1D model which can represent the hydrothermal processes in a column including an active layer and permafrost. This overall goal may be achieved by completing two objectives. The first objective is establishing an effective spinup which prepares the model for the second objective which is to run a transient simulation. Finally, if time allows, a third objective would be to compare the effect of variability in climate forcing. The expected outcome of this project is a working 1D model which captures hydrothermal process in the soil column (which includes both active layer and permafrost). Understanding the impact of variability in climate forcing would be a bonus if there is time to work on the third objective.

## Methods
- Modeling tool: ATS

- Study Area: Imnavait Creek, Alaska

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

Liston, G.E., A.K. Reinking, and N.T. Boleman. 2023. Daily SnowModel Outputs Covering the ABoVE Core Domain, 3-km Resolution, 1980-2020. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2105

https://daymet.ornl.gov/single-pixel/api/data?lat=35.9621&lon=-84.2916&vars=dayl,prcp,srad,swe,tmax,tmin,vp&start=1990-01-01&end=2006-12-31
