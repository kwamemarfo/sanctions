

  
# Sanctions

  
## Requirements


The requirements for this project are to create a scalable back-end solution for individuals sanctioned by the EU and/or UN. The solution should include the following components:

- Database for storing the data
- API endpoint(s) to deliver the data in JSON format
- The API must be able to provide all the necessary data, similar to https://www.sanctionsmap.eu



  
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