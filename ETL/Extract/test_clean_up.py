import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock
import os

from ETL.Extract.clean_up import Clean_up


class TestCleanUp(unittest.TestCase):
    
    def setUp(self):
        self.clean_up = Clean_up()
    
    def test_remove_oldest_file(self):
        files = [
            'ETL/Extract/Downloaded_Files/person_one_2022_01_01.csv',
            'ETL/Extract/Downloaded_Files/person_one_2022_01_02.csv',
            'ETL/Extract/Downloaded_Files/person_one_2022_01_03.csv',
            'ETL/Extract/Downloaded_Files/person_two_2022_01_01.csv',
            'ETL/Extract/Downloaded_Files/person_two_2022_01_02.csv',
            'ETL/Extract/Downloaded_Files/person_two_2022_01_03.csv',
            'ETL/Extract/Downloaded_Files/regime_2022_01_01.csv',
            'ETL/Extract/Downloaded_Files/regime_2022_01_02.csv',
            'ETL/Extract/Downloaded_Files/regime_2022_01_03.csv'
        ]
        
        expected_removed_files = [
            'ETL/Extract/Downloaded_Files/person_one_2022_01_01.csv',
            'ETL/Extract/Downloaded_Files/person_two_2022_01_01.csv',
            'ETL/Extract/Downloaded_Files/regime_2022_01_01.csv'
        ]
        
        with patch('os.remove') as mock_remove:
            removed_files = self.clean_up.remove_oldest_file(files)
        
        print(removed_files)
        print(expected_removed_files)
        self.assertEqual(removed_files, expected_removed_files)
        self.assertEqual(mock_remove.call_count, 2)
        mock_remove.assert_any_call('ETL/Extract/Downloaded_Files/person_one_2022_01_01.csv')
        mock_remove.assert_any_call('ETL/Extract/Downloaded_Files/person_two_2022_01_01.csv')
        mock_remove.assert_any_call('ETL/Extract/Downloaded_Files/regime_2022_01_01.csv')
        
    def side_effect(self, x):
        if len(x.split('/')) >= 4:
            file_type = x.split('/')[3]
            if '*' in file_type:
                return [file for file in self.file_types.keys() if file_type.replace('*', '') in file]
            else:
                return file_types.get(file_type, [])
        else:
            raise ValueError(f"Invalid value of x: {x}")
        
    
    def test_files(self):
        self.file_types = {
            'person_one': [
                'ETL/Extract/Downloaded_Files/person_one_2022_01_01.csv',
                'ETL/Extract/Downloaded_Files/person_one_2022_01_02.csv',
                'ETL/Extract/Downloaded_Files/person_one_2022_01_03.csv'
            ],
            'person_two': [
                'ETL/Extract/Downloaded_Files/person_two_2022_01_01.csv',
                'ETL/Extract/Downloaded_Files/person_two_2022_01_02.csv',
                'ETL/Extract/Downloaded_Files/person_two_2022_01_03.csv'
            ],
            'regime': [
                'ETL/Extract/Downloaded_Files/regime_2022_01_01.csv',
                'ETL/Extract/Downloaded_Files/regime_2022_01_02.csv',
                'ETL/Extract/Downloaded_Files/regime_2022_01_03.csv'
            ],
        }
        
        expected_removed_files = {
            'person_one': [
                'ETL/Extract/Downloaded_Files/person_one_2022_01_01.csv'
            ],
            'person_two': [
                'ETL/Extract/Downloaded_Files/person_two_2022_01_01.csv'
            ],
            'regime': [
                'ETL/Extract/Downloaded_Files/regime_2022_01_01.csv'
            ]
        }
        
        with patch('glob.glob') as mock_glob, \
             patch('os.remove') as mock_remove:
            
            mock_glob.side_effect = self.side_effect
            removed_files = self.clean_up.files()
        
        self.assertEqual(removed_files, expected_removed_files)
        self.assertEqual(mock_remove.call_count, 2)
        mock_remove.assert_any_call('ETL/Extract/Downloaded_Files/person_one_2022_01_01.csv')
        mock_remove.assert_any_call('ETL/Extract/Downloaded_Files/person_two_2022_01_01.csv')


if __name__ == '__main__':
    unittest.main()