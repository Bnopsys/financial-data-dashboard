"""
Goal with this file is to provide options on how to export the data. I had this inside of the main_df_module 
file and it didnt make sense to export before analysis had happened.

By giving this class the main data and any extra data you can export all of it.

For right now: 
1. Focus on exporting just main data and add the additional data later.
"""

import pandas as pd
import os


class ExportData:
    def __init__(self, df) -> None:
        self.data = df

    def current_categories_dict(self):
        """
        This function drops duplicates from the 'Category' Column and then uses this as a list in a dictionary composition to return 
        {Key='Category': Value='Dataframe of Category'}
        """
        unique_categories = list(self.data['Category'].drop_duplicates())
        return {category: self.data[(self.data['Category'] == category)] for category in unique_categories}


    def sort_dfs(self, categs_dict: dict):
        """
        TODO rather than returning a dict, this should just modify self.data so its only function is to sort the data.
        """
        return {category: df.sort_values(by=['Date']) for category, df in categs_dict.items()} # takes more than two values


    def create_excel(self, categs_dict, exportpath) -> None:
        """
        This takes the categories_dict and turns it into an excel sheet to see all data.
        TODO look up if its good practice to use except Exception as e.
        """
        try:
            with pd.ExcelWriter(exportpath) as writer:
                for sheetname, df in categs_dict.items():
                    df = pd.DataFrame(df)
                    df.to_excel(writer, sheet_name=sheetname, index=False)
        
        except Exception as e:
            print(e)

    def create_csv(self, categs_dict, exportpath, exportname) -> None:
        """
        This takes the categories_dict and turns it into a csv file. 
        TODO look into error handling like with create_excel.
        """
        for category, df in categs_dict.items():
            df = pd.DataFrame(df)
            filename = os.path.join(exportpath, category, exportname)
            df.to_csv(path_or_buf=filename)
