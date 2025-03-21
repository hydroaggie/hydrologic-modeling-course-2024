## My amazing project title 
Simulating Surface Runoff in the Red Butte Creek in Utah Using Amanzi-ATS

## Summary
1. Background and Motivation
The Red Butte Creek is a tributary of the Jordan River which has an area of 19 km2 and is situated in an elevation range between 1,646–2,530 m, the creek is crucial for the surrounding ecosystems and communities (Brooks et al., 2021). Understanding the surface runoff dynamics, particularly in response to varying precipitation patterns during dry and wet periods, is essential for sustainable water resource management (NRCS, 2024). This project aims to simulate surface runoff using Amanzi-ATS (Coon et al., 2019), focusing on the period from 2021 to 2024 to evaluate the potential impacts on the watershed. The Red Butte Creek is an ideal case study due to its unique combination of mountainous and varied land uses.

## Research questions
2. Research Questions, Goals and/or Objectives
a) How does surface runoff behave under different precipitation conditions (dry and wet periods) in the Red Butte Creek during 2021 to 2024?
b) What are the key factors influencing surface runoff in this region?
c) How can the results inform water resource management and planning?

## Methods 
3. Methods
I will develop this project in the Red Butte Creek as my primary focus considering existing current conditions and land uses. If for any reason this site proves unsuitable, I will consider alternative areas with similar characteristics. To develop this project, I will use Amanzi-ATS, an integrated surface and subsurface flow model, to simulate surface runoff. I choose this model for its capability to handle complex watershed simulations and analyze different precipitation conditions. 
Based on (Bhanja et al., 2023), I will collect data on topography (USGS, 2025, Tarboton, 2024) to create DEM, soil properties (Utah UGRC, 2025), land use (DWRe et al., 2022; Jon Dewitz, 2023), and climate data (temperature and precipitation) (Daly & Bryant, 2013) for the years 2021 to 2024. The year 2021 will be used to calibrate the model, while the period from 2022 to 2024 will be used to validate the model and compare the results with observed data. This includes differentiating between dry and wet periods to simulate different conditions.

4. Expected Results and Significance of the Proposed Work
Expected Results: This project will provide detailed simulations of surface runoff dynamics under various precipitation conditions from 2021 to 2024, including hydrographs, ponded depth distributions, and discharge flow rates to compare precision with observed data that later can be used to identify possible impacts considering future climate projections.
Significance: The results will provide insights into the potential impacts of varying precipitation patterns on surface runoff in the Red Butte Creek. This information is valuable for stakeholders involved in water resource management, flood risk assessment, and ecological conservation. The findings could also contribute to developing strategies for climate adaptation and resilience.


## Citations
5. References
Bhanja, S. N., Coon, E. T., Lu, D., & Painter, S. L. (2023). Evaluation of distributed process-based hydrologic model performance using only a priori information to define model inputs. Journal of Hydrology, 618, 129176. https://doi.org/10.1016/j.jhydrol.2023.129176
Brooks, P. D., Gelderloos, A., Wolf, M. A., Jamison, L. R., Strong, C., Solomon, D. K., Bowen, G. J., Burian, S., Tai, X., Arens, S., Briefer, L., Kirkham, T., & Stewart, J. (2021). Groundwater-Mediated Memory of Past Climate Controls Water Yield in Snowmelt-Dominated Catchments. Water Resources Research, 57(10), e2021WR030605. https://doi.org/10.1029/2021WR030605
Coon, E., Svyatsky, D., Jan, A., Kikinzon, E., Berndt, M., Atchley, A., Harp, D., Manzini, G., Shelef, E., Lipnikov, K., Garimella, R., Xu, C., Moulton, D., Karra, S., Painter, S., Jafarov, E., & Molins, S. (2019). Advanced Terrestrial Simulator [Computer software]. Los Alamos National Laboratory (LANL), Los Alamos, NM (United States). https://doi.org/10.11578/DC.20190911.1
Daly, C., & Bryant, K. (2013). The PRISM Climate and Weather System – An Introduction. https://prism.oregonstate.edu/
DWRe, USDA, NASS, & CDL. (2022). Water Related Land Use 2021. https://services1.arcgis.com/99lidPhWCzftIe9K/arcgis/rest/services/WaterRelatedLandUse/FeatureServer/0/metadata?format=default&f=html
Jon Dewitz. (2023). National Land Cover Database (NLCD) 2021 Products [Dataset]. U.S. Geological Survey. https://doi.org/10.5066/P9JZ7AO3
NRCS. (2024). Logan River Watershed Project | Natural Resources Conservation Service. https://www.nrcs.usda.gov/conservation-basics/conservation-by-state/utah/logan-river-watershed-project
Tarboton, D. (2024). Collection of Great Salt Lake Data | CUAHSI HydroShare. https://www.hydroshare.org/resource/b6c4fcad40c64c4cb4dd7d4a25d0db6e/
Utah UGRC. (2025). UGRC - Utah Soils. https://gis.utah.gov/products/sgid/geoscience/soils/
















# My amazing project title
This repository contains data and scripts necessary for reproducing the xx model.

## Summary
Provide a summary of the proposed project with the following format: 1-2 sentences about the background, one sentence on knowledge gap or motivation, one sentence on the overall goal of this project, 2-3 sentences on the objectives, 1-2 sentences on the expected outcome.

## Methods
- Modeling tool
State what modeling code you will be using

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
Provide any citation for the model or data (if it is stored somewhere else).
