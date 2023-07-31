# Note: Transformations here is kept to a minimum to ensure we have records that accurately reflect source files
# Most of the transformations will be done in the data assets (MDA, CDA)

import json
import glob
import pandas as pd
from pandas import json_normalize


class Transform():
    def __init__(self, downloaded_files):
        self.downloaded_files = downloaded_files
        
    
    def get_downloaded_files(self):
        downloaded_files = [glob.glob(f'ETL/Extract/Downloaded_Files/{file[0]}*') 
                            for file in self.downloaded_files if len(file) > 1]
        return downloaded_files
    
    
    def transform_csv(self, files_list):
        if files_list:
            file_to_transform = max(files_list)
            file_transformed = pd.read_csv(file_to_transform, sep=';')
            return file_transformed
        
        
    def transform_json(self, files_list):
        # Transform downloaded json file into dataframe
        if files_list:
            file_to_transform = max(files_list)
            # For any issues that might occur such as empty json or incorrect structure
            try:
                with open(file_to_transform, encoding='utf-8') as reg:
                    data = json.load(reg)
                file_transformed = pd.json_normalize(data, "data")
                return file_transformed
            except Exception as e:
                return e
            
            
    def regime_rename(self, data):
        if isinstance(data, pd.DataFrame):
            data = data.rename(columns=
                               {
                                   'id': 'regimes_id', 
                                   'type': 'regimes_type', 
                                   'adopted_by.data.id' : 'adopted_by_data_id', 
                                   'adopted_by.data.title' : 'adopted_by_data_title', 
                                   'country.data.code' : 'country_data_code', 
                                   'country.data.title' : 'country_data_title', 
                                   'category.data' : 'category_data', 
                                   'court_rulings.data' : 'court_rulings_data', 
                                   'legal_acts.data' : 'legal_acts_data', 
                                   'measures.data' : 'measures_data', 
                                   'guidances.data' : 'guidances_data', 
                                   'general_guidances.data' : 'general_guidances_data', 
                                   'country.data' : 'country_data', 
                                   'category.data.id' : 'category_data_id', 
                                   'category.data.title' : 'category_data_title'
                               })
            
            # Put the json columns into strings, the table dtype will be defined in data assets
            for col in data.columns[:]:
                data[f'{col}'] = data[f'{col}'].astype(str)
            return data
    

    def main(self):
        file_locations = self.get_downloaded_files()
        dataframes = {}
        
        for file_location in file_locations:
            file_name = file_location[0].split("\\")[-1]
            
            # Transform into dataframes
            if file_name.startswith("regime"):
                trans_file = self.transform_json(file_location)
                trans_file = self.regime_rename(trans_file)
                dataframes[file_name] = trans_file
                
            elif file_name.startswith("person"):
                trans_file = self.transform_csv(file_location)
                dataframes[file_name] = trans_file
            else:
                dataframes[file_name] = f"ERROR, Failed to transform file at location {file_location}"
                
        # returns dict {file_name : dataframe, ...}
        return dataframes