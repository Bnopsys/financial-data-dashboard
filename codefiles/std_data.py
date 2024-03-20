"""

This file's purpose is to handle standard deviation/outlier data
"""

import pandas as pd

class StandardDeviationData:
    def __init__(self, df: pd.DataFrame) -> None:

        self.data = df
        self.lookback_data = df


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

        outliers_df = pd.DataFrame(data_list) 
        outliers_df.rename(columns={'Unnamed: 0': 'Index'}, inplace=True)
        outliers_df.set_index('Index', inplace=True)

        return outliers_df


    def data_vars(self):

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
                       'Transfers': 'Debit', 
                       'Misc': 'Debit', 
                       'Savings': 'Debit', 
                       'PaymentFromCheckings': 'Credit', 
                       'Salary': 'Credit', 
                       'Deposits': 'Credit', 
                       'Transportation': 'Debit', 
                       'Insurance': 'Debit', 
                       'Restaurants': 'Debit', 
                       'Boba': 'Debit'}
        
        outlier_data = {}
        for category in categories_list:
            outlier_data[category] = self.categorical_describe(category, amount_type=categs_dict[category])

        return outlier_data
    