"""

This file's purpose is to handle standard deviation/outlier data
File is to take some of the data burden off analytical file. 

"""

import pandas as pd

class StandardDeviationData:
    def __init__(self) -> None:
        pass



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
    ...
    # test class here
    