"""
A library of dependencies related to the financial-data-dashboard.

Below are all the institutions I choose to use to include in my financial ecosystem.
Contains: 
    * Citi
        - Requires two files: Transaction file, and Credit file.
        - Transaction file contains categories but doesn't have include payments so they need to be in their own file.
    * Capital One
    * Navy Federal


"""



__all__ = ['capitalonecleaning', 'citicleaning', 'graphs', 'navyfedcleaning', 'tables']

from citicleaning import citi_to_csv
from capitalonecleaning import cof_to_csv
from navyfedcleaning import navy_fed_to_csv
# from graphs 
# from tables