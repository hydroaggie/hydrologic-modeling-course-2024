# Hydrological Modeling for Streamflow Using ATS: Performance Comparison with USGS NHM and Observed Data
This repository contains data and scripts necessary for reproducing the ATS model.

## Summary
Hydrological models are essential tools for simulating streamflow and understanding water balance dynamics. The USGS National Hydrologic Model (NHM) is widely used for hydrological simulations across the United States, leveraging various physical and statistical approaches to model streamflow. NHM is a semi-distributed model, meaning it divides a watershed into sub-basins or hydrologic response units (HRUs) and applies hydrological processes to each unit in a simplified manner (Hay et al., 2023). Physics-based hydrological models, such as the Advanced Terrestrial Simulator (ATS), offer a fully distributed approach by incorporating integrated surface and subsurface hydrological processes at a high spatial resolution (Bhanja et al., 2023). Comparing the performance of ATS with NHM in simulating streamflow for different catchments can help evaluate the strengths and weaknesses of each model. 

## Methods
- Modeling tool
ATS will be used due to its capability to integrate surface and subsurface hydrological processes in a physically based manner. ATS is particularly useful for catchments with complex hydrological interactions, allowing for a more detailed representation of soil moisture and groundwater-surface water interactions (Molins et al., 2022; Xu et al., 2022). The USGS NHM, which provides large-scale streamflow simulations, will be used as a benchmark for comparison. Two catchments in Northern Utah will be selected for this study due to data availability and the importance of streamflow modeling in this region for integrated water management. Climatic, topography and soil data will be used for the ATS model. NHM output data and observed values from USGS gages will be retrieved for comparison and benchmarking. 

- Study Area
The study area is the catchment upstream of USGS gage 10172200 located RED BUTTE CREEK AT FORT DOUGLAS near Salt Lake city, Utah.

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
Bhanja, S. N., Coon, E. T., Lu, D., & Painter, S. L. (2023). Evaluation of distributed process-based hydrologic model performance using only a priori information to define model inputs. Journal of Hydrology, 618, 129176. https://doi.org/10.1016/j.jhydrol.2023.129176
Hay, L. E., LaFontaine, J. H., Beusekom, A. E. V., Norton, P. A., Farmer, W. H., Regan, R. S., Markstrom, S. L., & Dickinson, J. E. (2023). Parameter estimation at the conterminous United States scale and streamflow routing enhancements for the National Hydrologic Model infrastructure application of the Precipitation-Runoff Modeling System (NHM-PRMS). In Techniques and Methods (Nos. 6-B10). U.S. Geological Survey. https://doi.org/10.3133/tm6B10
Molins, S., Svyatsky, D., Xu, Z., Coon, E. T., & Moulton, J. D. (2022). A Multicomponent Reactive Transport Model for Integrated Surface-Subsurface Hydrology Problems. Water Resources Research, 58(8), e2022WR032074. https://doi.org/10.1029/2022WR032074
Xu, Z., Molins, S., Özgen-Xian, I., Dwivedi, D., Svyatsky, D., Moulton, J. D., & Steefel, C. (2022). Understanding the Hydrogeochemical Response of a Mountainous Watershed Using Integrated Surface-Subsurface Flow and Reactive Transport Modeling. Water Resources Research, 58(8), e2022WR032075. https://doi.org/10.1029/2022WR032075


