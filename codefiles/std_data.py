"""

This file's purpose is to handle standard deviation/outlier data
"""

import pandas as pd

"""
 - Take into consideration that since this gets rid of outliers it should be able to work with both debit and credit hence the typeAlias and literals above being important.
 - make sure that defining variables inside of a function with self. allows them to be 'class-global'
 - keep on pushing according to the steps layed out below.
 - TODO make a dictionary to identify when the user adds a category which column it uses(debit or credit)

"""



class StandardDeviationData:
    def __init__(self, df: pd.DataFrame) -> None:
        self.data = df
        self.lookback_data = df
        self.outlier_counter = 0

    def categorical_describe(self, category, amount_type):

        """
        Category: Please provide one of the following categories: Groceries, Transfers, Misc, 
        Savings, PaymentFromCheckings, Salary, Deposits, Restaurants, Transportation, or Insurance

        Amount Type: Either 'Debit' or 'Credit'. This specifies whether to fill NaNs to 0 for the column.
        """

        self.data = self.data.loc[self.data['Category'] == category][amount_type].fillna(0)
        # TODO figure out if it would just be better to fill both debit and credit with 0's and calculate based on both columns.
        self.data_vars()
        data_list = []
        

        for row_index, row in self.data.items():
            debit_val = row

            if self.confirm_not_outlier(debit_val): # refactor this into a separate function.
                outlier_df = self.row_outlier_df(row_index=row_index)
                data_list.append(outlier_df)
                self.remove_outlier_from_df(row_index)

        data_df = pd.DataFrame(data_list) 
        data_df.rename(columns={'Unnamed: 0': 'Index'}, inplace=True)
        data_df.set_index('Index', inplace=True)

    def data_vars(self):
        """
        for column specify either 'Debit' or 'Credit' to choose the data you want to look at.
        """
        self.mean = self.data.describe().at['mean']
        self.std = self.data.describe().at['std']
        self.twenty_five_percent = self.data.describe().at['25%']
        self.seventy_five_percent = self.data.describe().at['75%']
        self.outliers =  (self.twenty_five_percent - (1.5 * (self.seventy_five_percent - self.twenty_five_percent)), 
                 self.seventy_five_percent + (1.5 * (self.seventy_five_percent - self.twenty_five_percent)))

    def confirm_not_outlier(self, amount):
        if not self.outliers[0] <= amount <= self.outliers[1]:
            return True
        return False
    
    def row_outlier_df(self, row_index):
        outlier_row = self.lookback_data.loc[row_index]
        return outlier_row
    
    def remove_outlier_from_df(self, row_index):
        self.data.drop(index=row_index, inplace=True)

    def run(self, categories_list: list):

        categs_dict = {'Groceries': 'Debit', 
                       'Transfers': '', 
                       'Misc': '', 
                       'Savings': '', 
                       'PaymentFromCheckings': 'Credit', 
                       'Salary': 'Credit', 
                       'Deposits': '', 
                       'Transportation': 'Debit', 
                       'Insurance': 'Debit', 
                       'Restaurants': 'Debit', 
                       'Boba': 'Debit'}
        for category in categories_list:
            self.categorical_describe(category)


if __name__ == '__main__':
    file = '/Users/roddystones/Documents/datafiles/main_datafile.csv'
    df1 = pd.read_csv(file)

    print(df1['Category'].drop_duplicates())
    cols = df1.loc[df1['Category'] == 'Restaurants']
    
    testcls = StandardDeviationData(df1)
    testcls.categorical_describe('Groceries', 'Debit')
    # testing describe function first
    # test class here
    

"""
# This is a facade design pattern approach which hides the complexity of the class inside of the function.
# can be used after creating the class.

def run_standard_deviation(data: pd.DataFrame, categories):
    sdd = StandardDeviationData(data)
    return sdd.run(categories)
"""