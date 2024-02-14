import pandas as pd
import numpy as np


# total spending
def total_spending(df: pd.DataFrame):
    """
    This function gets the sum of the entire debit column. 
    
    **Currently omitting Payment/FromCheckings, Savings, Paychecks/Salary, and Deposits categories** 
    """
    modified_df = df.loc[(df['Category'] != 'Payment/FromCheckings') & (df['Category'] != 'Savings') & (df['Category'] != 'Paychecks/Salary') & (df['Category'] != 'Deposits')]
    return modified_df['Debit'].sum()

# avg spending per category
def avg_spending_per_cat(df: pd.DataFrame):
    return df.groupby('Category')['Debit'].mean()

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
def top_n_spending_cats(df: pd.DataFrame, category, n):
    return df.groupby(['Category'] == category)['Debit'].sum().nlargest(n)

# category expenses over time

# expense distribution pie chart

# monthly budget vs actuals

# expense correlation between different spending categories (category and amount) using correlation matrices

# saving trends over time

# top five purchases
def find_top_five_purchases(df: pd.DataFrame):
    """
    This function takes the entire dataframe and removes the payment lines then returns the top five purchases.
    """
    df = df.loc[df['Category'] != 'Payment/ToCredit']
    df = df.sort_values(by=['Debit'], ascending=False)
    return df.head(5)