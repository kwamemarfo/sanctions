

  
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
  
![Proposed Pipeline Solution](https://i.postimg.cc/sX4Rf465/database-architect-2-drawio.png)
    
</div>

To address the requirements of this project, a data pipeline will be implemented using Terraform and AWS services. The pipeline will consist of the following components:

### Sources
Two data sources will be extracted for processing: a CSV file from [https://webgate.ec.europa.eu/fsd/fsf/public/rss](https://webgate.ec.europa.eu/fsd/fsf/public/rss) and a JSON file from [https://www.sanctionsmap.eu/api/v1/regime](https://www.sanctionsmap.eu/api/v1/regime).

### Extract & Load
The extracted files will be loaded into an S3 bucket, serving as the data lake, where the original files will be preserved. AWS Glue will be used for the extraction and loading process.

### Data Lake 
The data lake, implemented using S3, will provide a centralized storage location for the extracted data, ensuring efficient storage and retrieval of large volumes of data.

### Transform 
AWS Glue will be used to transform the extracted data. Glue provides a serverless ETL service capable of performing various transformations. If necessary, alternative transformation options such as dbt may be considered and explored..

### Data Warehouse 
The transformed data will be stored in another S3 bucket, serving as the data warehouse. This will facilitate easy access and analysis of the transformed data.

### Models 
Models will be created within the Data Warehouse. AWS Glue will be employed to perform these transformations, resulting in the creation of the desired models. 

For more details about the Data Warehouse, transformations, data models, and the overall process, please refer to the `Data Assets` folders.

### API 
The API endpoints will be created based on the models defined in the data warehouse. These endpoints will expose the transformed data, allowing for consumption by applications and/or for analytics purposes.

The proposed solution will utilize Terraform for Infrastructure as Code (IaC) to build the pipeline. Additionally, AWS Elastic Beanstalk will be used for continuous integration and deployment (CI/CD). Lambda functions will be leveraged to execute specific tasks within the pipeline, while Amazon API Gateway will be used to expose the API endpoints.
 
 

## Challenges

The initial design for this project aimed to create a fully Python-based solution using pythonanywhere.com. However, it was discovered that this approach was not scalable and/or feasible due to limitations imposed by pythonanywhere.com.

One of the challenges encountered was the need to whitelist the data sources' websites in order to enable data extraction. Unfortunately, the time and resources required to pursue this whitelisting process were not deemed efficient for the project.

As a result, an alternative solution using AWS services was devised to overcome these limitations. The proposed data pipeline, as described in the "Proposed Solution" section, utilizes AWS Glue, S3, Lambda functions, and Amazon API Gateway to achieve the project's objectives.

By transitioning to this AWS-based solution, we can bypass the whitelisting limitations and ensure the efficient extraction, transformation, and storage of the required data in a scalable manner.

Please refer to the "Proposed Solution" section for a detailed explanation of the alternative solution.

### Update
Due to other commitments, this project will resume again after September 2024
