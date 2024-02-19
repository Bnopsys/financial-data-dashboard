import pandas as pd
import numpy as np

def filter_out_credit_cats(df: pd.DataFrame):
    """
    This function filters out the below categories since they focus on credit charges.
    
    **Currently omitting Payment/FromCheckings, Savings, Paychecks/Salary, and Deposits categories** 
    """
    modified_df = df.loc[(df['Category'] != 'Payment/FromCheckings') & 
                         (df['Category'] != 'Savings') & 
                         (df['Category'] != 'Paychecks/Salary') & 
                         (df['Category'] != 'Deposits')]
    return modified_df

# debit stats
def data_stats(df: pd.DataFrame, user: str = None):
    """
    This function returns the following categories in table format so it can be used to make visualizations off of:
    * average spending(mean)
    * total spending(sum)
    * highest purchase price in debit column(max)
    * lowest purchase price in debit column(min)
    * highest purchase price in credit column(max)
    * lowest purchase price in credit column(min)
    * standard deviation of column(std)
        * helps you see how spread out the data is and can be analyzed more to try and keep purchases within a certain range
        * indicates somethings wrong if the number is not similar to previous months.
    * unique places shopped at(nunique)
        * if this number is less than user_purchases it means the same places have been shopped at multiple times
    * amount of times the user has swiped card
    """
    
    if user != None:
        df = df.loc[df['User'] == user]

    return df.groupby('Category').agg(
    avg_spending = pd.NamedAgg(column='Debit', aggfunc='mean'), 
    total_spend = pd.NamedAgg(column='Debit', aggfunc='sum'), 
    debit_max = pd.NamedAgg(column='Debit', aggfunc='max'), 
    debit_min = pd.NamedAgg(column='Debit', aggfunc='min'), 
    credit_max = pd.NamedAgg(column='Credit', aggfunc='max'), 
    credit_min = pd.NamedAgg(column='Credit', aggfunc='min'), 
    std_cats = pd.NamedAgg(column='Debit', aggfunc='std'), 
    n_unique = pd.NamedAgg(column='Description', aggfunc='nunique'), 
    user_purchases = pd.NamedAgg(column='User', aggfunc='count'))

# top N categories for spending (possibly top three?)
def top_n_spending_cats(df: pd.DataFrame, category, n): # TODO havent worked on yet.
    return df.groupby(['Category'] == category)['Debit'].sum().nlargest(n)

# top five purchases
def find_top_five_purchases(df: pd.DataFrame):
    """
    This function takes the entire dataframe and removes the payment lines then returns the top five purchases.
    """
    df1 = filter_out_credit_cats(df)
    df1 = df1.sort_values(by=['Debit'], ascending=False)
    return df1.head(5)

# total expenses vs income
def total_expenses(df:pd.DataFrame):
    modified_df = df.loc[(df['Category'] != 'Deposits') & 
                         (df['Category'] != 'Payment/FromCheckings') & 
                         (df['Category'] != 'Paychecks/Salary') & 
                         (df['Category'] != 'Savings')]
    return modified_df['Debit'].sum()
    

def total_income(df: pd.DataFrame):
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
    

# function dealing with savings


def identifying_payments(df: pd.DataFrame): # TODO REFACTOR without for loop.
    """
    This function identifys all debit charges from the account in the category Payment/FromCheckings 
    and gets the total to see how much was paid off this month.
    """
    credit_df = df.loc[df['Category'] == 'Payment/FromCheckings']
    payment_total = 0
    for _, row in credit_df.iterrows():
        payment: float = row['Debit']
        if pd.isna(payment) or payment == '':
            continue
        payment_total += payment
    return payment_total