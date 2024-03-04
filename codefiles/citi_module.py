from codefiles.utils.utils import read_data, filter_out_debit_charges, positive_values_amounts, payment_category, set_datetime, modify_cols, users_roderick, merge_dataframes, sort_on_date, func_default_categories, send_to_csv
import os

path_of_data_folder = '/Users/roddystones/Documents/datafiles'
debit_file = os.path.join(path_of_data_folder, 'CitiDebit.csv')
credit_file = os.path.join(path_of_data_folder, 'CitiCredit.csv')

default_categories_citi = {'Payment/FromCheckings': 'PaymentFromCheckings', 
                      'Restaurants': 'Restaurants', 
                      'Vehicle Services': 'Transportation', 
                      'Merchandise': 'Misc', 
                      'Services': 'Misc'}

def process_citi():
    """
    Takes both the debit and credit csv files and puts them into a standard format before merging. Then it is exported to csv.
    """
    debit_df = read_data(debit_file, skiprows=5)
    set_datetime(debit_df, 'Date')
    debit_df = modify_cols(debit_df, 'Citi', 'Roderick S.')

    # credit
    citi_credit_df = read_data(credit_file)
    citi_credit_df = filter_out_debit_charges(citi_credit_df)
    positive_values_amounts(citi_credit_df, 'Credit')
    payment_category(citi_credit_df)
    users_roderick(citi_credit_df)
    set_datetime(citi_credit_df, 'Date')
    citi_credit_df = modify_cols(citi_credit_df, 'Citi')

    # combined
    citi_merged_df = merge_dataframes(debit_df, citi_credit_df)
    citi_merged_df = sort_on_date(citi_merged_df)
    func_default_categories(citi_merged_df, default_categories_citi)
    send_to_csv(citi_merged_df, path_of_data_folder, 'citi_data.csv')
    

if __name__ == '__main__':
    process_citi()