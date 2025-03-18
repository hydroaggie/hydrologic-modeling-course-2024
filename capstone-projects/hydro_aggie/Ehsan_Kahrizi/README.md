# Integrating Hydrological Modeling with Automated Anomaly Detection to Distinguish Sensor Errors from Hydrological Events in the Logan River Observatory
This repository contains data and scripts necessary for reproducing the xx model.

## Summary
Hydrological models typically contain multiple inputs, and their power relies on accessing reliable input datasets. One of the inputs is field data collected by the in-situ sensors (Reitan, T. 2022; Horsburgh et al., 2015; Gibert et al., 2018).
The field data collected by in-situ sensors contains different hydrological patterns, e.g., natural flow variations, flood events, gaining or losing state, or drought, that could complicate the analysis of model outputs. Further, field infrastructure, which is used for measuring the in-situ data, has issues that sometimes create errors in the dataset, e.g., calibration errors and, maintenance artifacts, sensor failure. This interaction adds many complexities to the models' input and makes the models' prediction unreliable. There is a demand to determine whether observed patterns in model outputs are due to genuine hydrological processes or are created by field measurement infrastructure. Currently, there is no study to distinguish patterns resulting from hydrological processes and anomalies caused by sensor issues (Shen, 2018; Jones et al., 2022).
My project is about integrating hydrological modeling with automated anomaly detection to know how hydrological models can assist in differentiating between sensor-related anomalies/errors and actual hydrological patterns/processes. By answering this question, I plan to develop a workflow that uses hydrological model predictions to validate sensor data anomalies and accurately classify them as either sensor errors or genuine hydrological events. My expected result is presenting an analysis/workflow that helps better understand the hydrological process. 

## Methods
Modeling: I will use the ATS Model to simulate the streamflow dynamics of surface water. 
Data Collection and Preparation: I will use the LRO datasets at the Tony Grove site, which are available every 15 minutes. 
For ATS simulation, I will retrieve the required inputs, like soil texture, precipitation, evapotranspiration, meshes, etc., from free access platforms like USGS. Modeling Approach: I will try to simulate hydrological conditions during known periods of sensor anomalies (e.g., ice burial and out-of-water events) to check patterns from the model response with sensor data. I will identify patterns using a predefined threshold where sensor anomalies align with model predictions (indicating natural events) and where they do not (indicating sensor errors). 

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
Provide any citation for the model or data (if it is stored somewhere else).


## References
Reitan, T. (2022). Review of methods for automation of quality control on hydrologic time series and considerations for a research approach at NVE.
Horsburgh, J. S., Reeder, S. L., Jones, A. S., & Meline, J. (2015). Open source software for visualization and quality control of continuous hydrologic and water quality sensor data. Environmental Modelling & Software, 70, 32-44.
Gibert, K., Horsburgh, J. S., Athanasiadis, I. N., & Holmes, G. (2018). Environmental data science. Environmental Modelling & Software, 106, 4-12.
Shen, C. (2018). A transdisciplinary review of deep learning research and its relevance for water resources scientists. Water Resources Research, 54(11), 8558-8593.
Jones, A. S., Jones, T. L., & Horsburgh, J. S. (2022). Toward automating post processing of aquatic sensor data. Environmental Modelling & Software, 151, 105364.
![image](https://github.com/user-attachments/assets/1f02b9be-eb32-45f3-858a-fad20d64702d)

