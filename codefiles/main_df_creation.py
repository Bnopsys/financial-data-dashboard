from .navy_fed_module import process_navy_fed
from .citi_module import process_citi
from .capital_one_module import process_capital_one
from .create_dfs import df_list_func, get_company_list
from .mergefiles import merge_dataframes
from .utils.utils import read_data, set_datetime, sort_on_date, validate_in_dict
from os import path
import pandas as pd

folder_path = '/Users/roddystones/Documents/datafiles'
modified_files_dict = {'capital one': 
                            {'file_path': path.join(folder_path, 'func_data_files', 'capital_one_data.csv'),
                            'file_func': process_capital_one}, 

                       'citi': 
                            {'file_path': path.join(folder_path, 'func_data_files', 'citi_data.csv'), 
                            'file_func': process_citi}, 

                       'navy fed': 
                            {'file_path': path.join(folder_path, 'func_data_files', 'navyfed_data.csv'), 
                            'file_func': process_navy_fed}}


class MainfileCreation:
    def __init__(self, companylist: list[str]): # if passed ['navy fed', 'citi', 'capital one']
        self.companylist = [company.lower() for company in companylist]


    def refresh_csvs(self):
        for company in self.companylist:
            if validate_in_dict(company, modified_files_dict):
                modified_files_dict[company]['file_func']


    def create_dfs(self):
        company_list = get_company_list(companies=self.companylist, company_dict=modified_files_dict)
        return df_list_func(company_list)


    def merge_dfs(self, df_list: list, folder_path: str):
        merge_dataframes(df_list, folder_path)


    def merge_dataframes(self, dataframes_list: list[pd.DataFrame], folder_path):
        """
        This function concats a list of dataframes then runs the util functions set_datetime and sort_on date. 
        Lastly it converts the dataframe to csv based on the location we specify in the main function.
        """
        mainframe:pd.DataFrame = pd.concat(dataframes_list, ignore_index=0)
        set_datetime(mainframe, 'Date')
        sort_on_date(mainframe)
        mainframe.to_csv(path.join(folder_path, 'main_datafile.csv'), index=0)

    def retrieving_main_df(self):
        return read_data(path.join(folder_path, 'main_datafile.csv'))
