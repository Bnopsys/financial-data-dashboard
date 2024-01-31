# (WIP) Financial Dashboard Project

The Financial Dashboard Project is a tool that takes my current bank/credit card transactions and analyzes the data so I can make meaningful conclusions from it. For privacy reasons, I didn't include my data with the project. <br/> 
> Project Goals: 
> 1. Learn more about Pandas and become more comfortable with it, 
> 2. Create a budget for both myself and Reanne
> 3. Work more with Data Visualization



## Python
**Importing functions from Modules**



## Pandas
**Converting to Datetime** <br/>
By using the following code you can convert your date column to datetime and also convert to days. For what I need dates for, having the time isn't very relavant.

```python
df['Date'] = pd.to_datetime(df['Date']) 
df['Date'] = df['Date'].dt.date
```


## Budget



## Data Visualization

### Tables


### Graphs/Charts


# TODO:
* get reerees data(navy fed data)

[x] pull/clean data
    [x] Citi
    [x] NavyFed
    [x] Capital One
[x] Make sure all of the dates are set to datetime and also use .dt.date !!!
[x] Combine all data into one dataframe
[ ] Visualize/Interpret Data
    [ ] Charts/Graphs
    [ ] Show total income vs expenses
    [ ] Categorize data
    [ ] High Charges (200+)
[ ] Move the file documentation area in a convienient spot so others can swap it with their paths

---Data Drop Folder-------------------
* make a datadrop folder and when I run the final code it takes the current month with the first 
date of data to the last date for the folder name where all the output is saved
