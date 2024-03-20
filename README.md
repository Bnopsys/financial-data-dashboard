# (WIP) Financial Dashboard Project

The Financial Dashboard Project is a tool that takes my current bank/credit card transactions and analyzes the data so I can make meaningful conclusions from it. For privacy reasons, the data isnt included with the project. <br/> 

> Project Goals: 
> 1. Learn more about Pandas and become more comfortable with it, 
> 2. Create a budget for both myself and Reanne
> 3. Work more with Data Visualization

The next few sections will focus on what I've learned during this project.

## Python

**Modules** <br/>
Working with hundreds if not thousands lines of code was getting quite overwelming so I decided to break up the code into different modules.

**Using Init Files to Manage Modules** <br/>
The trouble with modules is that since everything's split it needs to be connected together afterwards to work correctly. Thats why I had to start using `__init__.py` files. These magic files allow you to handle all of your importing rather than having 10+ different module imports in the main file. Also you can use the `__all__` variable to specify which functions you want to import with `from {module} import *` method.

## Pandas

**Converting to Datetime** <br/>
By using the following code you can convert your date column to datetime and also convert to days. For what I need dates for, having the time isn't very relavant.

```python
df['Date'] = pd.to_datetime(df['Date']) 
df['Date'] = df['Date'].dt.date
```

##### Talk about ProcessData Class
In this class we pass it three different companies as *args.
The companies are then put into a list.
Had to change all of the functions to handle variables differently. 
    Before: self.company = company # this is the company string passed when making the class

    After: self.company = list(company) # this is a list of all of the companies passed into the class

Then the information is sent to the refresh_csv() function. It has to iterate over each string in the list(i.e 'Cit', 'Captial One', 'Navy Fed') and uses each as the variable.
It works through the validation functions with the individual company and after passing those it can use the company ex. 'Citi' to lookup from the company_dict the appropriate {company}_to_csv() functions and pass as the input the two files also referenced in the dictionary.

Next I called the merge_financial_csvs() function which has one parameter: dataframes_list. so to fill that parameter i call the create_df() as an argument.

This function creates an empty list and iterates over each company similarly to the refresh_csv(). It sets the current company in our self.company list as the company and uses that for the same validation. Then it appends a new csv file into the dataframes list and saves the location of the csv as specified in our company_dict[Modified File].

Since we now have our list of dataframes, we can run the merge_financial_csvs() with the list of dataframes. 

This function does a simple concat, changes the date to datetime, does some sorting and resets the index before exporting to csv. Now the class has completed its utility and we have our processed data ready to be used for the next steps.

** rewritten:
I added list comprehension to the merge_financial_csvs() so that instead of creating an empty list and appending dataframes to it in the create_df() function now it acts like normal with a company variable. *Note I changed the append feature back to a return dataframe so that it could work properly with the list comprehension. But in my handle_multiple_dataframes() function I added the line `dataframes_list = [self.create_df(x) for x in self.company]`. This creates a list of dataframes and manipulates each company in the list turning them into dataframes which then gets used as an argument for the merge_financial_csvs() function.
## Budget



## Data Visualization

### Tables


### Graphs/Charts

## Vision
The vision i see with this project is that after building the code i can have it make API calls daily to my banks so that I can monitor bank and credit card transactions. There are apps around that let you manually input expenses like buying a coffee or something but these require dicipline to track all expenes. If i could just pull the data from my bank accounts directly I could open see all of my transactions for multiple accounts and have the code sort charges so that I keep to my budget. 

Also there would be different visuals to help me track my progress. So pie charts, bar graphs and a mix of short and long range charts showing both day by day as well as monthly data to give me information to go off of.