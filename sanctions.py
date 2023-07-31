from ETL.Extract import extract
from ETL.Extract import clean_up
from ETL.Transform import transform_files
from ETL.Load import load_extracts
import pandas as pd

class Sanctions:
    
    def extract(self):
        extraction = extract.Extract()
        extracted_files = extraction.main()
        return extracted_files
    
    
    def transform(self, extract_files):
        # Transform (Consider transforming sequentially if memory might be an issue)
        transformed_files = None
        if any(extract_files):
            transformation = transform_files.Transform(extract_files)
            transformed_files = transformation.main()
        return transformed_files
    
    
    def load(self, transformed_files):
        loaded_databases = {}
        if transformed_files:
            for file_name, dataframe in transformed_files.items():
                file_name = file_name.split(".")[0]
                load_into_db = load_extracts.Load_data()
                load_into_db = load_into_db.into_database(file_name, dataframe)
                loaded_databases[file_name] = load_into_db
        return loaded_databases
    
    def clean_files(self):
        cleaned = clean_up.Clean_up()
        cleaned = cleaned.files()
        return cleaned
        
        
    def main(self):
        extract = self.extract()
        
        transform = self.transform(extract)
        load = self.load(transform)
        
        clean_files = self.clean_files()
        
        print(load.keys())
        print(clean_files)
        print("Done with ETL, now trigger Data Asset creation if load is True (i.e contains data)")