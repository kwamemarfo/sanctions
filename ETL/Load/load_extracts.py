import glob
import sqlite3
import os

# should inherit from transform so Load(Transform)
class Load_data:
    
    def into_database(self, file_name, dataframe):
        print(file_name)
        try:
            database_folder = "Database/"
            database_file = f"{database_folder}sanctions.db"
            os.makedirs(database_folder, exist_ok=True)
            conn = sqlite3.connect(database_file)
            df_count = dataframe.to_sql(name=file_name, con=conn, if_exists="replace", index=False)
            completed = True, df_count           
        except sqlite3.Error as e:
            completed = False, f"An error occurred: {e}"
        finally:
            conn.close()
            return completed