import glob
import os
from datetime import datetime

class clean_up:
    
    def __init__(self):
        self.regime = 'regime'
        self.person_one = 'person_one'
        self.person_two = 'person_two'
        self.folder_path = 'ETL/Extract/Downloaded_Files/'
    
    def files(self):
        # Ensure there are a maximum of 6 files with 2 for each type
        file_counts = {self.regime: 0, self.person_one: 0, self.person_two: 0}
        files = glob.glob(f'{self.folder_path}*')
        removed_files = []

        for file in files:
            file_name = os.path.basename(file).split('_')
            file_name = "_".join(file_name[:-3])
            if file_name in file_counts:
                file_counts[file_name] += 1
                if file_counts[file_name] > 2:
                    oldest_file = min(files, key=lambda x: datetime.strptime
                                      ("_".join(os.path.basename(x).split('_')[-3:]).split('.')[0], '%Y_%m_%d'))
                    os.remove(oldest_file)
                    removed_files.append(oldest_file)

        if removed_files:
            removed_file_names = [os.path.basename(file) for file in removed_files]
            return f"Removed files: {', '.join(removed_file_names)}"
        else:
            return "No files were removed"