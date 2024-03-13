import pandas as pd
import numpy as np # look more into numpy for extra data
from codefiles.data_assist import boba_shops, grocery_list

class Maindf:
    """
    The purpose of this class is to take the product of main_df_creation(name subject to change) and make base changes to it.
    
    Think of this class as restructuring the bones of the data. It handles bigger operations (moving lines to different categories)

    After execution of this class the next class that takes the data will analyze it/prepare it for the visualization phase.
    
    """
    def __init__(self, df: pd.DataFrame):
        self.data = df

    def correcting_categories(self, shop_list: list, newloc: str):
        for item in shop_list:
            mask = self.data['Description'].str.contains(item, case=False)
            self.data.loc[mask, 'Category'] = newloc # TODO  what does this mean with the .loc/ learn all the different uses for .loc

    def run(self):
        """
        Public method to run everything. Its job is to combine the differnt methods together and run everything 
        in the correct order rather than chaining different events. 

        TODO change this so make it more scalable.
        """
        # correct categories
        dict_of_cats_to_correct = {'Boba':boba_shops, 'Groceries': grocery_list}
        for category, shoplist in dict_of_cats_to_correct.items():
            self.correcting_categories(shop_list=shoplist, newloc=category)

if __name__ == "__main__":
    mainfile = '/Users/roddystones/Documents/datafiles/main_datafile.csv'
    exportpath = '/Users/roddystones/Documents/datafiles/main_df_test.xlsx'

    df = pd.read_csv(mainfile)
    
    # using class
    main_df_tsting = Maindf(df)
    main_df_tsting.run()
