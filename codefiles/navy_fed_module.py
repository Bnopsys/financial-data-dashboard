from codefiles.utils.utils import read_data, determining_category, set_datetime, modify_cols, converting_amount_indicator, merge_dataframes, sort_on_date, func_default_categories, send_to_csv
import os

path_of_data_folder = '/Users/roddystones/Documents/datafiles'
checkings_file = os.path.join(path_of_data_folder, 'NavyFedCheckings.csv')
visa_credit_file = os.path.join(path_of_data_folder, 'NavyFedCredit.csv')

default_categories_navyfed = {'Restaurants/Dining': 'Food', 
                      'Groceries': 'Food', 
                      'Credit Card Payments': 'Payment/FromCheckings', 
                      'Income': 'Income',
                      'General Merchandise': 'Merchandise', 
                      'Payment/ToCredit': 'Payment/ToCredit'}

def process_navy_fed():
    """
    This function takes both the checkings/credit csv files from Navy Fed and puts them into a standard format before merging. 
    Lastly it is exported to csv.
    """
    checking_df = read_data(checkings_file)
    determining_category(checking_df)
    set_datetime(checking_df, 'Date')
    checking_df = modify_cols(checking_df,'Navy Fed', 'Roderick S.')

    # credit
    nf_credit_df = read_data(visa_credit_file)
    converting_amount_indicator(nf_credit_df)
    nf_credit_df = modify_cols(nf_credit_df, 'Navy Fed', User='Roderick S.', Date='Booking Date')
    set_datetime(nf_credit_df,'Date')

    # merged 
    nf_merged_df = merge_dataframes(checking_df, nf_credit_df)
    nf_merged_df = sort_on_date(nf_merged_df)
    func_default_categories(nf_merged_df, default_categories_navyfed)
    send_to_csv(nf_merged_df, path_of_data_folder, 'navyfed_data.csv')
    

