import glob
import os
from datetime import datetime

class Clean_up:
    
    def __init__(self):
        self.regime = 'regime'
        self.person_one = 'person_one'
        self.person_two = 'person_two'
        self.folder_path = 'ETL/Extract/Downloaded_Files/'
    
    def remove_oldest_file(self, files):
        removed_files = []
        while len(files) > 2:
            oldest_file = min(files, key=lambda x: datetime.strptime(
                "_".join(os.path.basename(x).split('_')[-3:]).split('.')[0], '%Y_%m_%d'))
            os.remove(oldest_file)
            removed_files.append(oldest_file)
            files.remove(oldest_file)
        return removed_files
            
    
    def files(self):
        file_types = {
            self.person_one: [],
            self.person_two: [],
            self.regime: []
        }
        
        for file_type in file_types:
            file_pattern = os.path.join(self.folder_path, f'{file_type}*')
            file_types[file_type] = glob.glob(file_pattern)
        
        removed_files = {}
        for file_type, files in file_types.items():
            removed_files[file_type] = self.remove_oldest_file(files)
        
        return removed_files