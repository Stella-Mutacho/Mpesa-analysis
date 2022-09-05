import os
import pandas as pd
import logging
import syslog
import tabula
import sys
import pandas as pd


logger = logging.getLogger()
formatter= logging.Formatter('%(asctime)s -%(lineno)s -%(levelname)s-%(message)s')
logger.setLevel(logging.DEBUG)
fhandler= logging.FileHandler(filename='../airflow/logs/extract.log', mode='w')
fhandler.setFormatter(formatter)
fhandler.setLevel(logging.INFO)
logger.addHandler(fhandler)

class Extractor:

    def __init__(self):
        pass
    def pdf_to_csv(self,pdfstatement,filename):
        # convert PDF into CSV
        tabula.convert_into(pdfstatement, filename, output_format="csv", pages='all')
    
    
    def load_csv(self, path):
        """
        Function to Load csv file.
        Args:
            path: location of csv file and its name.        
        Returns:
            df: dataframe.
        """
        df = pd.read_csv(path)
        return df
    def read_summary(self,path):
        summary= pd.read_csv('../data/mpesaData.csv', index_col = False,  nrows=11)
        summary.drop('Unnamed: 3', axis=1, inplace=True)
        
    def get_file_path(self, fetch_date):
        """
        This function constructs a filename to be used 
        Params:
            fetch_date: str
                The date the mpesa statement was downloaded from mpesa app
        Returns:
            filepath: os.Path
                The path to the file
                """        
        filename = "mpesa_summary{}.csv".format(fetch_date)
        return os.path.join("~/data/", filename)

    def save_df(self, df, filename):
        df.to_csv(filename)
        print('Successfully saved')