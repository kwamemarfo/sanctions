import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock
import os

from ETL.Extract.clean_up import Clean_up


class TestCleanUp(unittest.TestCase):
    
    def setUp(self):
        self.clean_up = Clean_up()
        
        
if __name__ == '__main__':
    unittest.main()