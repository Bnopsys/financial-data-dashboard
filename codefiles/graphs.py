import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def boxplot(deviation_data):
    plot = sns.boxplot(data=deviation_data)
    # plt.show()
    return plot

# sankey chart
# barchart
# scatterplot with regression line
# stacked bar chart