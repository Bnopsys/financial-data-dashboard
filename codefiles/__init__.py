"""
A library of dependencies related to the financial-data-dashboard.

By using `from codefiles import *` it will provide: `citi_to_csv`, `cof_to_csv`, `navy_fed_to_csv` * subject to change!!!!!

Below are all the institutions I choose to use to include in my financial ecosystem.
    * Citi
        - Requires two files: Transaction file, and Credit file.
        - Transaction file contains categories but doesn't have include payments so they need to be in their own file.
        - For testing purposes: Run the file as __main__ to see it print out dataframe.
    * Capital One
        - Requires one file: Transaction file
        - File contains information for both Reanne and I
        - Uses two dictionaries for changing information: Adding ['Users'], and standardizing ['Category'] column
        - For testing purposes: Run the file as __main__ to see it print out dataframe.
    * Navy Federal
        - Requires two files: Checkings file, and Credit file.
        - Checkings file is for all income to account as well as money going out to credit cards/venmo cash exchanges.
        - Credit file is for all credit card charges and their respective payments from my checkings.
        - For testing purposes: Run the file as __main__ to see it print out dataframe.
    * Graphs
    * Tables


"""



# The __all__ variable allows us to specify what to import with the `import *` method
__all__ = ['citi_to_csv', 'cof_to_csv', 'navy_fed_to_csv']

from .data_cleaning.citicleaning import citi_to_csv
from .data_cleaning.capitalonecleaning import cof_to_csv
from .data_cleaning.navyfedcleaning import navy_fed_to_csv


# from graphs 
# from tables