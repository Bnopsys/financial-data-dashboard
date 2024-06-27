import pandas as pd
import numpy as np
from collections import Counter

def filter_out_credit_cats(df: pd.DataFrame):
    """
    This function filters out the below categories since they focus on credit charges.
    """
    modified_df = df.loc[(df['Category'] != 'PaymentFromCheckings') & 
                         (df['Category'] != 'Savings') & 
                         (df['Category'] != 'Salary') & 
                         (df['Category'] != 'Deposits')]
    return modified_df

def find_top_five_purchases(df: pd.DataFrame):
    """
    This function takes the entire dataframe and removes the payment lines then returns the top five purchases.
    """
    df1 = filter_out_credit_cats(df)
    df1 = df1.sort_values(by=['Debit'], ascending=False)
    return df1.head(5)

def total_income(df: pd.DataFrame) -> float:
    """
    This function performs some operations so the data can be narrowed down to only income charges.
    """
    gained_income = df.loc[df['Table'] == 'Navy Fed']
    gained_income = gained_income.fillna(0)
    gained_income['Credit'] = pd.to_numeric(gained_income['Credit'], errors='coerce')
    income_df = gained_income.loc[gained_income['Credit'] > 0]
    masked_df = remove_transfer_from_savings_mask(income_df)
    total_income = masked_df['Credit'].sum()
    return total_income

def remove_transfer_from_savings_mask(df: pd.DataFrame):
    """
    This function uses a mask(boolean array) and checks to see which rows contain the conditional of 
    having 'Transfer From Savings' in it. Then it preforms a `.loc` based on an inverted mask 
    and returns that dataframe.

    # TODO add to interesting stuff learned: Boolean Arrays(masks) along with inverting them to have the equivalent of 
    does not contain.
    """
    mask = df['Description'].str.contains('Transfer From Savings', case=False)
    inverted_mask = df.loc[~mask]
    return inverted_mask
    
def identifying_payments(df: pd.DataFrame): # TODO REFACTOR without for loop.
    """
    This function identifys all debit charges from the account in the category PaymentFromCheckings 
    and gets the total to see how much was paid off this month.
    """
    credit_df = df.loc[df['Category'] == 'PaymentFromCheckings']
    payment_total = 0
    for _, row in credit_df.iterrows():
        payment: float = row['Debit']
        if pd.isna(payment) or payment == '':
            continue
        payment_total += payment
    return payment_total

def tracking_payments(df: pd.DataFrame):# refactor to decouple
    df = df.loc[df['Category'] == 'PaymentFromCheckings'].fillna(0)
    df = df.sort_values(by='Date')
    debit_list = df['Debit']
    credit_list = df['Credit']
    masked_debit = debit_list[df['Debit'] > 0]
    masked_credit = credit_list[df['Credit'] > 0]

    counter_credit = Counter(masked_credit)
    counter_debit = Counter(masked_debit)

    trans_dict = {'Roderick S.': 0, 'Reanne C.': 0}
    for transaction in counter_credit.elements():
        if transaction in counter_debit and counter_debit[transaction] > 0:
            trans_dict['Roderick S.'] += transaction
            counter_debit[transaction] -= 1
        else:
            trans_dict['Reanne C.'] += transaction
    return trans_dict

def budget_deviation(series: pd.Series, budget_dict: dict, date=None):#Use this function to compare total spend series to budget dict to find where theres deviation.
    """
    To access this function for the input you need to take the data_stats function and 
    use the 'total_spend' column as the series input.
    """
    deviation = {}
    for category, value in series.items():
        deviation[category] = budget_dict.get(category, 0) - value
    return deviation

if __name__ == '__main__':
    ...