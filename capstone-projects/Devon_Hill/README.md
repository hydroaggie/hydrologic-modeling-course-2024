# 1D Column Model for Hydrothermal Processes in the Tundra Active Layer
This repository contains data and scripts necessary for reproducing a 1D Column Model for Hydrothermal Processes in the Tundra Active Layer using ATS.

## Summary
Hydrothermal processes in the arctic permafrost active layer are critical for understanding the carbon export from arctic regions. Weather variability is projected to increase in the future and may have an unknown impact on the hydrothermal processes in arctic regions. This project utilizes an Advanced Terrestrial Simulator (ATS) physically based column (1D) model to assess the impact of weather (precipitation and air temperature) variability on the active layer of arctic permafrost. Here the thaw depth, water table depth, and ground surface temperature resulting from five different 9-year transient runs (2011-2020) are compared. Air temperature variability had a much greater variability than precipitation variability. Greater air temperature variability resulted in deeper water tables and thaw depths with warmer summer ground surface temperatures and colder winter ground surface temperatures. Less air temperature variability resulted in very shallow thaw depths and near saturation for the entire summer period. Precipitation variability runs had an important impact on wintertime ground surface temperatures presumably due to the difference in snow depth and density. These findings demonstrate the response of the active layer to shifts in weather variability which help shape the perspective of future conditions in the arctic.  

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

## Citations
Liston, G. E., Reinking, A. K., & Boleman, N. T. (2023). Daily SnowModel Outputs Covering the ABoVE Core Domain, 3-km Resolution, 1980-2020 [Data set]. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2105

Mukherjee, N. (n.d.). 2D Transect Imnavait Creek. Github. Retrieved April 25, 2025, from https://github.com/neelarunmukherjee/imnavait_2D

Schädel, C., Rogers, B. M., Lawrence, D. M., Koven, C. D., Brovkin, V., Burke, E. J., Genet, H., Huntzinger, D. N., Jafarov, E., McGuire, A. D., Riley, W. J., & Natali, S. M. (2024). Earth system models must include permafrost carbon processes. Nature Climate Change, 14(2), 114–116. https://doi.org/10.1038/s41558-023-01909-9

Shuai, P. (n.d.). pinshuai/imnavait. GitHub. Retrieved April 25, 2025, from https://github.com/pinshuai/imnavait

Stocker, T. F., Qin, D., Plattner, G.-K., Tignor, M., Allen, S. K., Boschung, J., Nauels, A., Xia, Y., Bex, V., & Midgley, P. M. (Eds.). (2013). Climate Change 2013: The Physical Science Basis. Nature, 499, 413. https://www.nature.com/articles/nature12310

Thornton, M. M., Shrestha, R., Wei, Y., Thornton, P. E., & Kao, S.-C. (2022). Daymet: Daily Surface Weather Data on a 1-km Grid for North America, Version 4 R1 (Version 4.1). ORNL Distributed Active Archive Center. https://doi.org/10.3334/ORNLDAAC/2129 

