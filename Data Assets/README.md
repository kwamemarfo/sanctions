# Data Assets

This README provides an overview of the data assets in the project and explains the data pipeline, data lake, data warehouse, and data modeling methods used.

The following files are included in this folder:

- `Entities File Analysis.ipynb`: This file contains the analysis performed on the extracted entities file. The analysis serves as the basis for the data transformation and modeling processes.

- `Regimes File Analysis.ipynb`: This file contains the analysis performed on the extracted regimes file. The analysis is used to inform the data transformation and modeling steps.

- `country_code.csv`: This file contains data created to enable effective join between the extracted files.

- `README.md`: This file contains the instructions outlined here for the repository.

These analysis files play a crucial role in understanding the structure and content of the extracted data, guiding the subsequent transformation and modeling processes.

Please refer to these files for detailed insights into the data and the steps taken to prepare it for further processing.

## Data Pipeline

The data pipeline in this project follows the illustrated diagram below:

![Data Pipeline](https://i.postimg.cc/tJcVSmzC/data-arc-physical-2-drawio.png)

## Data Lake and Data Warehouse

In the modeling of the data lake and data warehouse, a combination of methods was employed. The data lake utilises a vault-like approach to preserve the raw format of the data. This raw data is then further processed in the data warehouse to create a normalized representation that aligns with the project's business use case.

## Data Modeling

The data was modeled using a hybrid approach that incorporates elements of both star and normalized schemas. In this project, where the objective is to provide data to an API and considering the requirement for all the data, a minimalist hybrid approach was adopted. While not strictly adhering to the traditional star schema with separate dimension and fact tables, the data was structured in a way that allows for the creation of such tables if necessary. This design facilitates easy analytics and reporting by business intelligence tools.


### Conceptual Model

The conceptual model, depicted in the diagram below, showcases the hybrid approach mentioned earlier:

![Conceptual Model](https://i.postimg.cc/4dZFYCJH/conceptual-model-drawio.png)

The hybrid approach combines elements of both star and normalized schemas. This approach is advantageous because it allows for flexibility in data analysis and reporting. While the star schema is not fully adopted in this project, the data is structured in a way that enables easy creation of dimension and fact tables, facilitating analytics if needed.

### Logical Model

The logical model, illustrated in the diagram below, represents the structure of the data:

![Logical Model](https://i.postimg.cc/XYb2HSCH/physical-model-3-drawio.png)

The logical model provides a detailed view of the data organization and relationships. It serves as a blueprint for organizing and querying the data effectively.