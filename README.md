# (WIP) Financial Dashboard Project

The Financial Dashboard Project is a tool that takes my current bank/credit card transactions and analyzes the data so I can make meaningful conclusions from it. For privacy reasons, the data isnt included with the project. <br/> 

> Project Goals: 
> 1. Learn more about Pandas and become more comfortable with it, 
> 2. Create a budget for both myself and Reanne
> 3. Work more with Data Visualization

## Vision
The vision i see with this project is that after building the code i can have it make API calls daily to my banks so that I can monitor bank and credit card transactions. There are apps around that let you manually input expenses like buying a coffee or something but these require dicipline to track all expenes. If i could just pull the data from my bank accounts directly I could open see all of my transactions for multiple accounts and have the code sort charges so that I keep to my budget. 

Also there would be different visuals to help me track my progress. So pie charts, bar graphs and a mix of short and long range charts showing both day by day as well as monthly data to give me information to go off of.

# Pull
In order to get the data for the project we need to go to the websites of the required finincial institutions. In this case I have been using Navy Fed, Capital One, and Citi Bank.

# Transform 
To convert the miriad of different formats, this step of the process takes the data and changes it into a standardized format.

# Merge
Merging the data can only be done once the data has already been cleaned and changed into a format that is standard across the board. This step is pretty simple, adding the lines on top of eachother since they all occured from different banks. 

# Modify

# Visualize

# Classes Used

## MainfileCreation
The MainfileCreation class handles the pull, transform, and merging operations of the code.

## Maindf
The Maindf class handles operations inside of the dataframe like major changes or anything that was necessary to change once the data was merged. In this case it handles changing certain categories of charges based on Description. 