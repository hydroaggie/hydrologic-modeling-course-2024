# Groundwater Model of Moab Using UGS data in PFLOTRAN
This repository contains data and scripts necessary for reproducing the xx model.

## Summary
This project provides a preliminary analysis of groundwater conditions at the study site and projects potential flow changes based on three wells from the UGS (see Figure 1). By establishing a foundation for future groundwater modeling efforts in the region, this project will contribute to a better understanding of local groundwater dynamics. The model will be run as a forecasting tool to predict how groundwater conditions may evolve under current pumping rates. The insights gained will help identify data gaps and guide further research.

## Methods
- Modeling tool
PFLOTRAN

- Study Area
Moab

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
Masbruch, M. D., Gardner, P. M., Nelson, N. C., Heilweil, V. M., Solder, J. E., Hess, M. D., McKinney, T. S., Briggs, M. A., & Solomon, D. K. (2019). Evaluation of groundwater resources in the Spanish Valley watershed, Grand and San Juan counties, Utah. U.S. Geological Survey.
