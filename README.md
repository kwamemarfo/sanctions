

  
# Sanctions

  
## Requirements


This project aims to develop a scalable back-end solution for managing data on individuals sanctioned by the EU and/or UN. The solution should consist of the following key components:

- **Database**: A robust and scalable database will be implemented to store all the relevant data securely.

- **API Endpoints**: The solution will provide API endpoint(s) to deliver the data in JSON format. These endpoints will enable users to access the necessary information efficiently.

- **Comprehensive Data**: The API must be capable of providing all the essential data required for the project, similar to the functionality offered by [https://www.sanctionsmap.eu](https://www.sanctionsmap.eu).

By fulfilling these requirements, the project will deliver a reliable and efficient back-end solution for managing and accessing data on sanctioned individuals.



  
## Proposed Solution

<div align="center">
  
![Proposed Solution](https://i.postimg.cc/VvjmhTsf/top-view-2-drawio.png)
    
</div>
    
### External Sources

This project requires two external sources:

- A CSV file ("peoples.csv") containing information about the sanctioned individuals. You can find this file at [https://webgate.ec.europa.eu/fsd/fsf/public/rss](https://webgate.ec.europa.eu/fsd/fsf/public/rss).
- A JSON file ("regime.json") containing information about the respective countries. You can access this file at [https://www.sanctionsmap.eu/api/v1/regime](https://www.sanctionsmap.eu/api/v1/regime).


### Staging

During the staging stage, an ETL (Extract, Transform, Load) method will be implemented. Ideally, this would be done using a tool like Apache Airflow, which provides proper logs. However, due to budget constraints and limited time on free-tier cloud accounts, we will develop our own ETL solution. A cron job will be applied daily to execute the ETL process.

For more details and the code used for the ETL process, please refer to the "ETL" folder.

### Database

The database for this project will be hosted on a free-tier account, most likely using PostgreSQL. However, other databases like MySQL can be considered if necessary. For detailed information about the database architecture and structure, please refer to the "Data Assets" folder.

### API

To accommodate the budget constraints of this project, a cost-effective approach will be taken to build the API on pythonanywhere.com. However, an additional API will be created in Java to maintain knowledge in that language, although it will not be utilized in this project. For more information about the API, please refer to the "api" folder.