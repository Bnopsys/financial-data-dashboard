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

    return df.groupby('Category').agg(avg_spending = pd.NamedAgg(column='Debit', aggfunc='mean'), 
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
def exp_vs_income(df:pd.DataFrame):
    """
    # TODO this could be an issue if the dataframe doesnt have these specific columns on a given month.
    """
    # expenses
    expenes_df = filter_out_credit_cats(df)

    # income # TODO needs to filter out transfers fro savings. this is skewing the data.
    """gained_income = df.loc[(df['Category'] == 'Deposits') | 
                           (df['Category'] == 'Paychecks/Salary') | 
                           (df['Category'] == 'Transfers')]"""
    gained_income = df.loc[df['Table'] == 'Navy Fed']
    gained_income = gained_income.fillna(0)
    gained_income['Credit'] = pd.to_numeric(gained_income['Credit'], errors='coerce')
    income_df = gained_income.loc[gained_income['Credit'] > 0]
    total_income = income_df['Credit'].sum()

def remove_transfer_from_savings_mask():
    ...
    # need to 
# function dealing with savings
