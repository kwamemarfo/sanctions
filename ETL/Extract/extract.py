# This code will extract 3 files named regimes.json, person_one.csv, person_two.csv
# Note: Currrent date will be added to the files, ex: regime_2023_07_06.json

import glob
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
import requests
import urllib.request
from bs4 import BeautifulSoup


class Extract:
    
    def __init__(self):
        self.regimes_url = 'https://www.sanctionsmap.eu/api/v1/regime'
        self.persons_url = 'https://webgate.ec.europa.eu/fsd/fsf/public/rss'
        self.regime = 'regime'
        self.person_one = 'person_one'
        self.person_two = 'person_two'
        self.folder_path = 'ETL/Extract/Downloaded_Files/'
          
    
    def latest_file(self, files_list):
        # Get the latest modified file from the list
        latest_file = max(files_list, key=os.path.getmtime)
        return latest_file

    
    def get_file_date(self, file):
        file_date = "_".join(file.split("_")[3:]).split(".")[0]
        file_datetime = datetime.strptime(file_date, '%Y_%m_%d')
        return file_datetime
        
    
    def is_file_current(self, file):
        # Check if the file is current (modified within 1 day)
        file_date = self.get_file_date(file)
        check_date = datetime.today() + relativedelta(days=-1)
        return file_date  > check_date
            
        
    def check_files(self, files_list):
        # Check if any of the files in the list are out of date
        latest_file = files_list
        if len(files_list) >= 1:
            latest_file = self.latest_file(files_list)
            if self.is_file_current(latest_file):
                return False, latest_file      
        # No files available/No current files (prompts download)
        return True, latest_file
 

    def create_file_names_with_dates(self):
        # Create file names with today's date appended
        file_names = {
            self.regime : "json", 
            self.person_one : "csv", 
            self.person_two : "csv"
        } 
        todays_date_str = datetime.today().strftime('%Y_%m_%d')
        files_todays_date = [
            f"{file}_{todays_date_str}.{file_names[file]}" 
            for file in file_names
        ]
        return files_todays_date
    
     
    def enable_download(self, person_file, pub_date):
        # Check if the file needs to be downloaded based on its modification date and the publication date
        if person_file:
            latest_file = self.latest_file(person_file)
            latest_file_date = self.get_file_date(latest_file)
            if pub_date > latest_file_date:
                return True
            else:
                return False
        else:
            return True
        
        
    def download_file(self, url, file_name):
        # Download a file from the given URL and save it with the specified file name
        # return httpmessage or httperror
        try:
            download_folder = self.folder_path
            os.makedirs(download_folder, exist_ok=True)
            file_path = os.path.join(download_folder, file_name)
            
            with requests.get(url, stream=True) as response:
                response.raise_for_status()
                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                    
            return file_name, response   
        except Exception as e:
            return file_name, e
            
    
    def get_person_urls(self):
        # Get the URLs of the person files and the publication date from the RSS feed
        resp = requests.get(self.persons_url)
        person_urls = []
        pub_date = ""
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'xml')
            tags = soup.find_all('enclosure', attrs = {'type': 'text/plain'})

            # take only the first 2 urls (make adjustments if structure changes in future)
            urls = [tag['url'] for tag in tags][:2]
            urls.sort()
            persons = [self.person_one, self.person_two]
            person_urls = list(zip(persons, urls))
            pub_date = str(soup.find('pubDate')).strip('</pubDate>')
            pub_date = datetime.strptime(pub_date, '%a, %d %b %Y %H:%M:%S %Z')
        return pub_date, person_urls
    
    
    def persons_file(self):
        # Get the existing person files
        files_needed = [
            glob.glob(f'{self.folder_path}{self.person_one}*'),
            glob.glob(f'{self.folder_path}{self.person_two}*')
        ]
        return files_needed
    
    
        
    def main(self):
        person_files = self.persons_file()
        person_one = person_files[0]
        person_two = person_files[1]

        # check if files are latest
        p_one_check, p_one_latest_file = self.check_files(person_one)
        p_two_check, p_two_latest_file = self.check_files(person_two)
        
        
        person_one_download = person_two_download = regimes_download = ''
        
        if p_one_check or p_two_check:
            current_file_names = self.create_file_names_with_dates()
            pub_date, person_urls = self.get_person_urls()
            
            enable_download_person_one = self.enable_download(person_one, pub_date)
            enable_download_person_two = self.enable_download(person_two, pub_date)
            
            if enable_download_person_one:
                person_one_download = self.download_file(person_urls[0][1], current_file_names[1])
            
            if enable_download_person_two:
                person_two_download = self.download_file(person_urls[1][1], current_file_names[2])
                
            if enable_download_person_one or enable_download_person_two:
                regimes_download = self.download_file(self.regimes_url, current_file_names[0])
                       
        
        # Use return later to identify downloaded items
        return regimes_download, person_one_download, person_two_download   
    

