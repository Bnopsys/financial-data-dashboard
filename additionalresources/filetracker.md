File Tracker

| Folder Name | File Name          | Status          | Remarks|
| :----------:| :-----------------:| :-----:         | :-----:|
| ~           | .gitignore         | Not used        | used for github|
| ~           | Debitsankey.png    | Not used        |used as a visualization demo|
| ~           | mainfile.py        | MAINFILE        | Main file for project. |
| ~           | README.md          | Needs attention | Informative Doc for project|
| codefiles   | __init__.py        | As required     | takes all files inside of the codefiles folder and allows them to cleanly import into mainfile for use.|
| codefiles   | analytical_data.py | Needs attention | deals with different metrics from the data.|
| codefiles   | capital_one_module.py| Complete      | transforms capital one data into std format.|
| codefiles   | citi_module.py     | Complete        | transforms citi data into std format|
| codefiles   | create_csvs.py     | Complete        | when given a list of files, this changes the data to dataframes.|
| codefiles   | data_assist.py     | As required     | extra dicts used for other files. treated as a holding spot for future dicts.|
| codefiles   | data_stats_cls.py  | Needs attention | standard deviation class that handles extreme outliers.|
| codefiles   | exporting_data.py  | Needs attention | not currently used but has capabilities to export data to excel with categorical sheetnames.|
| codefiles   | graphs.py          | Needs attention | not used currently but should be used in the creation of visualizations.|
| codefiles   | main_df_creation.py| Complete        | handles the refreshing, creating dfs, merging dfs(from mergefiles), exports file to csv and reads csv for mainfile.|
| codefiles   | main_df_module.py  | Needs attention | handles the category swapping of boba and grocery stores.|
| codefiles   | navy_fed_module.py | Complete        | transforms navy fed data into std format|
| codefiles/utils | __init__.py    | Complete        | handles all inner files to assist in importing them in other files.|
| codefiles/utils | utils.py       | Complete        | has small operations shared between the three refresh csv files cof, nf, and citi.|
| additionalresources | filetracker.md | CURRENT FILE | CURRENT FILE | 
| additionalresources | OLDmain.py | Not used        | Old file for main project before I rewrote it in late January |
| additionalresources | pysankey.py| Complete        | I got this code from github since it helps make sankey diagrams better than the Seaborn implementation.|
| additionalresources/planningpdfs| CapitalOneOutline.pdf| Complete| Used to help map out info on capital one during early development.| 
| additionalresources/planningpdfs| FinancesFreeform.pdf| Complete| Just used to help map out ideas for project.|
| additionalresources/planningpdfs| ProjectFlow.pdf| Complete| Another visual I made to help map out what I wanted out of this project.|