import pandas as pd
import os
from codefiles.utils.utils import set_datetime, sort_on_date



def merge_dataframes(dataframes_list: list[pd.DataFrame], folder_path):
    """
    This function concats a list of dataframes then runs the util functions set_datetime and sort_on date. 
    Lastly it converts the dataframe to csv based on the location we specify in the main function.
    """
    mainframe:pd.DataFrame = pd.concat(dataframes_list, ignore_index=0)
    set_datetime(mainframe, 'Date')
    sort_on_date(mainframe)
    mainframe.to_csv(os.path.join(folder_path, 'main_datafile.csv'), index=0)


    



