import os
import pandas as pd
import logging
import syslog
import tabula
import sys
import pandas as pd
from unicodedata import category


from clean_statements import Cleaner 
cleaner= Cleaner()


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
    def transform_raw_data(self, raw_data_df):
        """
            This function transforms the raw dataset extracted from the web into a dataframe that can be easily loaded the database    
            Returns: pd.DataFrame 
        """
        Mpesa_data= raw_data_df.drop('Unnamed: 7', axis=1)
        Clean_data= cleaner.removerowsByValue(Mpesa_data, column='Transaction Status', val='Transaction Status')
        details=Clean_data['Details']
        detsA=[]
        
        for row in details:
            if 'Pay Bill Online ' in row:
                category= 'Pay Bill Online'
            elif 'Customer Transfer' in row:
                category = 'Customer Transfer'
            elif 'Merchant Payment 'in row :
                category= 'Merchant Payment'
            elif 'Business Payment' in row:
                category = 'Business Payment' 
            elif 'Funds received' in row:
                category = 'Funds received'
            elif 'Customer Withdrawal' in row:
                category = 'Customer Withdrawal'
            elif 'Deposit of Funds' in row:
                category = 'Deposit of Funds'
            elif 'Buy Bundles' in row:
                category='Buy Bundles'
            elif 'M-Shwari Withdraw' in row:
                category= 'M-Shwari Withdraw'
            elif 'M-Shwari Deposit' in row:
                category= 'M-Shwari Deposit'
            elif 'Pay Bill Charge' in row:
                category= 'Pay Bill Charge'
            elif 'Airtime Purchase' in row:
                category= 'Airtime Purchase'
            elif 'Pay Bill to' in row:
                category= 'Pay Bill to'
            else:
                category= row
            detsA.append(category)
        Clean_data['Transaction Type']=detsA
        Data= cleaner.drop_columns(Clean_data,['Transaction Status','Details'])
        return Data
    def convert_correctDtypes(self,Data):
        Data['Paid in']= Data['Paid in'].str.replace(',', '').astype(float)
        Data['Withdraw\rn']= Data['Withdraw\rn'].str.replace(',', '').astype(float)
        Data['Balance']= Data['Balance'].str.replace(',', '').astype(float)
        Data['Completion Time']=pd.to_datetime(Data['Completion Time'])
        cleaner.convert_to(Data, ['Receipt No','Transaction Type'], str)
        return Data

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
        filename = "mpesa_records{}.csv".format(fetch_date)
        return os.path.join("~/data/", filename)

    def save_df(self, df, filename):
        df.to_csv(filename)
        print('Successfully saved')