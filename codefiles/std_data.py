"""
This file's purpose is to handle standard deviation/outlier data

It shouldnt remove all outliers but only true outliers that would just make the data ugly to look at. 
By going 2 standard deviations beyond the outlier limits, I can identify the difference between normal outliers from buying cars.
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

        self.current_data = self.data.loc[self.data['Category'] == category][amount_type].fillna(0)
        self.data_vars()
        data_list = []
        
        for row_index, row in self.current_data.items():
            debit_val = row

            if self.confirm_not_outlier(debit_val): # refactor this into a separate function.
                outlier_df = self.row_outlier_df(row_index=row_index)
                data_list.append(outlier_df)
                self.remove_outlier_from_df(row_index)

        outliers_df = pd.DataFrame(data_list) 
        outliers_df.rename(columns={'Unnamed: 0': 'Index'}, inplace=True)
        

        return outliers_df


    def data_vars(self):

        self.mean = self.current_data.describe().at['mean']
        self.std = self.current_data.describe().at['std']
        self.twenty_five_percent = self.current_data.describe().at['25%']
        self.seventy_five_percent = self.current_data.describe().at['75%']
        self.outliers =  (self.twenty_five_percent - (1.5 * (self.seventy_five_percent - self.twenty_five_percent)), 
                 self.seventy_five_percent + (1.5 * (self.seventy_five_percent - self.twenty_five_percent)))
        
        # TODO recalculate the std before identifying since i want to see what the std would look like without these
        self.true_outliers = (self.outliers[0] - (2 * self.std), self.outliers[1] + (2 * self.std))


    def confirm_not_outlier(self, amount):
        if not self.true_outliers[0] <= amount <= self.true_outliers[1]:
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
        
        outlier_data = []
        for category in categories_list:
            outlier_data.append(self.categorical_describe(category, amount_type=categs_dict[category]))
        
        # outlier_data = pd.DataFrame(outlier_data)
        return outlier_data
    