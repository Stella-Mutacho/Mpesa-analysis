import pandas as pd

class Cleaner():
    '''
    This class contains helper functions to explore data and functions to clean data in a pandas dataframe.
    '''
    def __init__(self) -> None:
        pass
    
    def removerowsByValue(self, df,column,val) :
        '''
        Function to remove rows with unwanted column values
        params: 
            df: Pandas.Dataframe
                Dataframe with the row to be dropped
            column: string
                column label to be read
            val: string
                value of the row to be dropped
        '''
        df = df.drop(df.loc[df[column]==val].index)
        return df
     
    def drop_columns(self, df, columns):
        '''
        Function that drops columns 
        Args:
        pandas dataframe columns
        '''
        df= df.drop(columns, axis=1)

        return df 
    def convert_to(self, df,columns, data_type):
        '''
        Convert Columns to desired data types.
        '''

        for column in columns:
            df[column] = df[column].astype(data_type)
        
        return df

    

