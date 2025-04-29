# Assessing the Potential of Integrating Hydrological Modelling Outputs with Logan River Observatory Gauge Datasets to Improve Anomaly Detection of Streamflow Data in the Franklin Sub-watershed

This repository contains data and scripts necessary for reproducing the ATS model.

## Summary
Hydrological models typically contain multiple inputs, and their power relies on accessing reliable input datasets. One of the inputs is field data collected by the in-situ sensors (Reitan, T. 2022; Horsburgh et al., 2015; Gibert et al., 2018).
The field data collected by in-situ sensors contains different hydrological patterns, e.g., natural flow variations, flood events, gaining or losing state, or drought, that could complicate the analysis of model outputs. Further, field infrastructure, which is used for measuring the in-situ data, has issues that sometimes create errors in the dataset, e.g., calibration errors and maintenance artifacts, sensor failure. This interaction adds many complexities to the models' input and makes the models' predictions unreliable. There is a demand to determine whether observed patterns in model outputs are due to genuine hydrological processes or are created by field measurement infrastructure. Currently, no study distinguishes patterns resulting from hydrological processes and anomalies caused by sensor issues (Shen, 2018; Jones et al., 2022).
My project is about integrating hydrological modeling with automated anomaly detection to know how hydrological models can assist in differentiating between sensor-related anomalies/errors and actual hydrological patterns/processes. By answering this question, I plan to develop a workflow that uses hydrological model predictions to validate sensor data anomalies and accurately classify them as either sensor errors or genuine hydrological events. My expected result is to present an analysis/workflow that helps better understand the hydrological process. 

## Methods
Modeling: I will use the ATS Model to simulate the streamflow dynamics of surface water. 
Data Collection and Preparation: I will use the LRO datasets at the Franklin site, which are available every 15 minutes. 
For the ATS simulation, I will retrieve the required inputs, like soil texture, precipitation, evapotranspiration, meshes, etc., from free-access platforms like USGS. Modeling Approach: I will try to simulate hydrological conditions during known periods of sensor anomalies (e.g., ice burial and out-of-water events) to check patterns from the model response with sensor data. I will identify patterns using a predefined threshold where sensor anomalies align with model predictions (indicating natural events) and where they do not (indicating sensor errors). 

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
- `data`: provides data needed to run the model (e.g., meshes, meteorological forcing, observation, etc.)
- `model`: provides input files and essential model outputs (e.g., observation points, mass balance)
- `scripts`: provides the scripts or jupyter notebooks for pre- and post-processing model files
- `results`: provides any results generated from the model analysis (e.g., figures associated with rthe eport)


## References
Adu-Manu, K. S., Katsriku, F. A., Abdulai, J. D., & Engmann, F. (2020). Smart River Monitoring Using Wireless Sensor Networks. Wireless Communications and Mobile Computing, 2020. https://doi.org/10.1155/2020/8897126
Gibert, K., Horsburgh, J. S., Athanasiadis, I. N., & Holmes, G. (2018). Environmental Data Science. Environmental Modelling and Software, 106, 4–12. https://doi.org/10.1016/j.envsoft.2018.04.005
Horsburgh, J. S., Reeder, S. L., Jones, A. S., & Meline, J. (2015). Open source software for visualization and quality control of continuous hydrologic and water quality sensor data. Environmental Modelling and Software, 70, 32–44. https://doi.org/10.1016/j.envsoft.2015.04.002
Jones, A. S. (2024). Water Data Science: Data Driven Techniques, Training, and Tools Water Data Science: Data Driven Techniques, Training, and Tools for Improved Management of High Frequency Water Resources for Improved Management of High Frequency Water Resources Data Data Recommended Citation Recommended Citation. Utah State University. https://digitalcommons.usu.edu/etd2023/134
Jones, A. S., Aanderud, Z. T., Horsburgh, J. S., Eiriksson, D. P., Dastrup, D., Cox, C., Jones, S. B., Bowling, D. R., Carlisle, J., Carling, G. T., & Baker, M. A. (2017). Designing and Implementing a Network for Sensing Water Quality and Hydrology across Mountain to Urban Transitions. Journal of the American Water Resources Association, 53(5), 1095–1120. https://doi.org/10.1111/1752-1688.12557
Jones, A. S., Jones, T. L., & Horsburgh, J. S. (2022). Toward automating post processing of aquatic sensor data. Environmental Modelling and Software, 151. https://doi.org/10.1016/j.envsoft.2022.105364
Neilson, B. T., Tennant, H., Strong, P. A., & Horsburgh, J. S. (2021). Detailed streamflow data for understanding hydrologic responses in the Logan River Observatory. Hydrological Processes, 35(8). https://doi.org/10.1002/hyp.14268
Oleksy, I. A., Jones, S. E., & Solomon, C. T. (2022). Hydrologic Setting Dictates the Sensitivity of Ecosystem Metabolism to Climate Variability in Lakes. Ecosystems, 25, 1328–1345. https://doi.org/10.1007/s10021-021-0071
Pellerin, B. A., Stauffer, B. A., Young, D. A., Sullivan, D. J., Bricker, S. B., Walbridge, M. R., Clyde, G. A., & Shaw, D. M. (2016). Emerging Tools for Continuous Nutrient Monitoring Networks: Sensors Advancing Science and Water Resources Protection. Journal of the American Water Resources Association, 52(4), 993–1008. https://doi.org/10.1111/1752-1688.12386
Reitan, T. (2022). Review of methods for automation of quality control on hydrologic time series and considerations for a research approach at NVE. Norwegian Water Resources and Energy Directorate. https://publikasjoner.nve.no/rapport/2022/rapport2022_15.pdf
Rode, M., Wade, A. J., Cohen, M. J., Hensley, R. T., Bowes, M. J., Kirchner, J. W., Arhonditsis, G. B., Jordan, P., Kronvang, B., Halliday, S. J., Skeffington, R. A., Rozemeijer, J. C., Aubert, A. H., Rinke, K., & Jomaa, S. (2016). Sensors in the Stream: The High-Frequency Wave of the Present. Environmental Science and Technology, 50(19), 10297–10307. https://doi.org/10.1021/acs.est.6b02155
Shen, C. (2018). A Transdisciplinary Review of Deep Learning Research and Its Relevance for Water Resources Scientists. In Water Resources Research (Vol. 54, Issue 11, pp. 8558–8593). Blackwell Publishing Ltd. https://doi.org/10.1029/2018WR022643
Turnipseed, D. P., Sauer, V. B., & Survey, U. S. G. (2010). Discharge measurements at gaging stations. In Techniques and Methods. https://doi.org/10.3133/tm3A8
![image](https://github.com/user-attachments/assets/b57d4f3a-85bb-44d1-8944-baec3a14a17e)

