from codefiles.utils.utils import read_data, add_users_map, func_default_categories, sort_on_date, modify_cols, send_to_csv
import os

path_of_data_folder = '/Users/roddystones/Documents/datafiles'
capital_one_file = os.path.join(path_of_data_folder, 'CapitalOneTrans.csv') # change name to match snake case

card_users = {9623: 'Reanne C.', 
              3176: 'Roderick S.'}

default_categories_cof = {'Other Services': 'Misc', 
                      'Merchandise': 'Misc', 
                      'Payment/Credit': 'Payment/FromCheckings', 
                      'Dining': 'Restaurants', 
                      'Gas/Automotive': 'Transportation', 
                      'Insurance': 'Insurance', 
                      'Internet': 'Misc', 
                      'Entertainment': 'Entertainment'}

def process_capital_one():
    """
    This takes the capital one transaction file and transforms it into my standard format then exports to csv as a new modified file.
    """
    df = read_data(capital_one_file)
    add_users_map(df, card_users)
    func_default_categories(df, default_categories_cof)
    df = modify_cols(df, tablename='Capital One', Date='Transaction Date')
    df = sort_on_date(df)
    send_to_csv(df, path_of_data_folder,'capital_one_data.csv')

if __name__ == '__main__':
    process_capital_one()