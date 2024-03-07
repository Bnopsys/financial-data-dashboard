from codefiles.utils.utils import read_data, modify_cols, converting_amount_indicator, merge_dataframes, sort_on_date, func_default_categories, send_to_csv
import os

path_of_data_folder = '/Users/roddystones/Documents/datafiles'
checkings_file = os.path.join(path_of_data_folder, 'NavyFedCheckings.csv')
visa_credit_file = os.path.join(path_of_data_folder, 'NavyFedCredit.csv')

default_categories_navyfed = {'Restaurants/Dining': 'Restaurants', 
                      'Groceries': 'Groceries', 
                      'Credit Card Payments': 'PaymentFromCheckings', 
                      'General Merchandise': 'Misc', 
                      'Transfers': 'Transfers', 
                      'Automotive Expenses': 'Misc', 
                      'Savings': 'Savings', 
                      'Paychecks/Salary': 'Salary', 
                      'Deposits': 'Deposits', 
                      'Interest': 'Misc'}

def handle_files(filename):
    df = read_data(filename)
    converting_amount_indicator(df)
    df = modify_cols(df=df, tablename='Navy Fed', user='Roderick S.', date='Booking Date')
    return df

def process_navy_fed():
    """
    This function takes both the checkings/credit csv files from Navy Fed and puts them into a standard format before merging. 
    Lastly it is exported to csv.
    """

    credit_df = handle_files(visa_credit_file)
    checking_df = handle_files(checkings_file)
    
    
    # merged 
    nf_merged_df = merge_dataframes(checking_df, credit_df)
    nf_merged_df = sort_on_date(nf_merged_df)
    func_default_categories(nf_merged_df, default_categories_navyfed)
    send_to_csv(nf_merged_df, path_of_data_folder, 'navyfed_data.csv')

    """category_list = list(nf_merged_df['Category'].drop_duplicates())
    print(category_list)
    for category in category_list:
        print(nf_merged_df.loc[nf_merged_df['Category'] == category])
        print("")"""
    
    

if __name__ == '__main__':
    process_navy_fed()
    

