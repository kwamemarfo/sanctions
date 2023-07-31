# Extract

There are 3 files needed for this project:
- regime.json
- person_one.csv
- person_two.csv

The files can be downloaded by executing the code `extract.py`. In additon, the code will return either httpmessage (this could be httperror) or string object to denote if download was succesfull.


### For the extracation the following will be implemented:
- Check if the files needed are present:
  - If not present, download the file and append the file's date to the file (we can retrieve the date downloaded by querying the modified time as the file will only be modified once)
- If it is present, check if the files are older than 7 days. If they are older, check and download new files if they're available

## Naming convention
The following are the naming structure that will be adopted for the downloaded files:
regime.json -- will be called --> regimes_{date}.json
20230607-FULL-1_1.csv -- will be called --> person_two_{date}.csv
20230607-FULL-1_0.csv -- will be called --> person_one_{date}.csv