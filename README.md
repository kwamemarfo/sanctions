

  
# Sanctions

  
## Requirements


This project aims to develop a scalable back-end solution for managing data on individuals sanctioned by the EU and/or UN. The solution should consist of the following key components:

- **Database**: A robust and scalable database will be implemented to store all the relevant data.

- **API Endpoints**: The solution will provide API endpoint(s) to deliver the data in JSON format. These endpoints will enable users to access the necessary information efficiently.

- **Comprehensive Data**: The API must be capable of providing all the essential data required for the project, similar to the functionality offered by [https://www.sanctionsmap.eu](https://www.sanctionsmap.eu).

By fulfilling these requirements, the project will deliver a reliable and efficient back-end solution for managing and accessing data on sanctioned individuals.

Note: This project needs to be completed within a budget of £0, hence, it will be necessary to explore cost-effective solutions and implement innovative methods.



  
## Proposed Solution

<div align="center">
  
![Proposed Solution](https://i.postimg.cc/9fyQ5GRc/database-architect-drawio.png)
    
</div>

In order to facilitate this project, above data pipeline solution has been devised. The solution comprises of the following sections:
    
### Sources
The data sources for this project include an API and a CSV file. The API data will be fetched from [https://www.sanctionsmap.eu/api/v1/regime](https://www.sanctionsmap.eu/api/v1/regime), while the CSV file will be scraped from [https://webgate.ec.europa.eu/fsd/fsf/public/rss](https://webgate.ec.europa.eu/fsd/fsf/public/rss).

### Extract & Load
The data will be extracted from the sources and saved as a backup file on [pythonanywhere.com](https://www.pythonanywhere.com) in the directory named `ETL/Extract/Downloaded_Files`. Afterward, minor transformations will be applied to the extracted files to ensure they can be loaded into the data lake effectively. Please refer to the "ETL" folder for more information on the Extract & Load process.

### Data Lake
The Data Lake serves as a storage location for the extracted data files. The files will be stored in a SQL-type database within the Data Lake.

### Transform
Once the files are in the Data Lake, various transformations will be applied, including normalizations, data quality checks, and removal of unnecessary fields. These transformations will prepare the data for further processing.

### Data Warehouse
Transformed data will be loaded into the Data Warehouse. A data model will be created based on the transformed data. 

### Data Models
Data models are derived from the transformed data in the Data Warehouse. These models will be used to generate the necessary data required for the API endpoints.

For more details about the Data Warehouse, transformations, data models, and the overall process, please refer to the `Data Assets` folders.

## API
The API will utilise the data models to provide the required data for endpoints. The API endpoints will be designed to serve the project's specific needs.

Please refer to the corresponding folders and sections mentioned above for detailed information on each step of the data pipeline.