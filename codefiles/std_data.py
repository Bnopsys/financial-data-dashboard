"""

This file's purpose is to handle standard deviation/outlier data
"""

import pandas as pd
from typing import TypeAlias, Literal

typeLiteral: TypeAlias = Literal['Debit', 'Credit']
"""
look into this typeAlias so that I can have either debit or credit as options
if not I could just make a list and see if the provided response is in the list to work off of. 

But I want to learn more about TypeAlias and Literals.
-------
After that I need to continue filling in the StandardDeviationData class. 
 - Take into consideration that since this gets rid of outliers it should be able to work with both debit and credit hence the typeAlias and literals above being important.
 - make sure that defining variables inside of a function with self. allows them to be 'class-global'
 - keep on pushing according to the steps layed out below.

"""
categories = {'Groceries': 'Debit', 'Transfers': 'Debit'}

class StandardDeviationData:
    def __init__(self, df: pd.DataFrame) -> None:
        self.data = df

    def categorical_describe(self, category):
        self.data = self.data.loc[self.data['Category'] == category]['Debit'].fillna(0)
        self.data_vars('Debit')

    def data_vars(self, column: str):
        """
        for column specify either 'Debit' or 'Credit' to choose the data you want to look at.
        """
        self.mean = self.data.describe().loc['mean'][column]
        self.std = self.data.describe().loc['std'][column]
        self.twenty_five_percent = self.data.describe().loc['25%'][column]
        self.seventy_five_percent = self.data.describe().loc['75%'][column]
        self.outliers =  (self.twenty_five_percent - (1.5 * (self.seventy_five_percent - self.twenty_five_percent)), 
                 self.seventy_five_percent + (1.5 * (self.seventy_five_percent - self.twenty_five_percent)))
        
    def confirm_not_outlier(self, amount):
        if not self.outliers[0] <= amount <= self.outliers[1]:
            return True
        return False

    # first step: get described data and dataframe filtered based on category
        # replace described data for function based on getting 25% and 75% data
    # second step: use described data to return outliers 

    # third step: Make an empty list(or dict: if its a dict it could have row_no: row_data) which can hold the outlier rows

    # fourth step: loop over rows in dataframe(im using items which may not be the best approach maybe i should use iterrows or something else)

    # fith step: for each row in dataframe check if it is an outlier

    # sixth step: if not, skip. If so, take the row and add it to the list/dict.

    # seventh step: remove the outlier line from the main dataframe

    # eighth step: create a dataframe from the list/dict values.
        
    # TODO use the standard deviation and mean metrics to give the user an idea on where the data falls and how to better understand the data.




def categorical_describe(df: pd.DataFrame, category):
    """
    Uses the built in pandas describe function to get more information on the standard deviation of a column.
    """
    df_method, describe_method = get_df_describe(df, category)
    outliers = identifying_outlier_range(describe_method)
    outliers_df = pd.DataFrame(columns = df.columns) # placeholder df until counter goes above 0
    outlier_counter = 0

    for row_index, row in df_method.items():
        debit_val = row
        
        if confirm_not_outlier(debit_val, outliers):
            outlier_df = row_outlier_df(df, row_index=row_index)
            outliers_df = identifying_outliers_df_before_concat(outlier_df, outliers_df, outlier_counter)
            outlier_counter += 1
    return df, outliers_df

def get_df_describe(df: pd.DataFrame, category):
    df_method = df.loc[df['Category'] == category]['Debit'].fillna(0)
    return df_method, df_method.describe()

def identifying_outlier_range(describe_method):
    q1 = describe_method.at['25%']
    q3 = describe_method.at['75%'] 
    outliers =  (q1 - (1.5 * (q3 - q1)), 
                 q3 + (1.5 * (q3 - q1)))
    return outliers

def confirm_not_outlier(debit_val, outliers):
    if not outliers[0] <= debit_val <= outliers[1]:
        return True
    return False

def row_outlier_df(df: pd.DataFrame, row_index):
    outlier_row = df.loc[row_index]
    return pd.DataFrame([outlier_row])

def remove_outlier_from_df(df: pd.DataFrame, row_index):
    return df.drop(index=row_index, inplace=True)

def identifying_outliers_df_before_concat(df:pd.DataFrame, outliers_df: pd.DataFrame, counter):
    if counter == 0:
        return df
    
    elif counter > 0:
        return pd.concat([outliers_df, df])
    
    else:
        raise Exception('Out of bounds Counter')
    

if __name__ == '__main__':
    file = '/Users/roddystones/Documents/datafiles/main_datafile.csv'
    df1 = pd.read_csv(file)

    print(df1['Category'].drop_duplicates())
    cols = df1.loc[df1['Category'] == 'Misc'].drop_duplicates()
    print(cols)
    testcls = StandardDeviationData(df1)
    # testing describe function first
    # test class here
    

"""
# This is a facade design pattern approach which hides the complexity of the class inside of the function.
# can be used after creating the class.

def run_standard_deviation(data: pd.DataFrame, categories):
    sdd = StandardDeviationData(data)
    return sdd.run(categories)
"""