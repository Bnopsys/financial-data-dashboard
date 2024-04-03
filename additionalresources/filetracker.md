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
| codefiles   | mergefiles.py      | In work(move to existing file)| merges a list of dataframes and saves as filename: main_datafile.csv|
| codefiles   | navy_fed_module.py | Complete        | transforms navy fed data into std format|
