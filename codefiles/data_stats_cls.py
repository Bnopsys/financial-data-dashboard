import pandas as pd

class DataStats:

    def __init__(self, df: pd.DataFrame, user: str = None) -> None:

        self.data = df
        self.user = user
        self.todays_date = pd.to_datetime('now')
        self.month_prior_date = self.todays_date - pd.DateOffset(month=1)

        if self.user != None:
            self.data = self.data.loc[self.data['User'] == self.user]


    def month_to_date(self):
        
        self.data = self.data.copy()
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        start_date, end_date = self.month_prior_date, self.todays_date
        mask = (self.data['Date'] <= end_date) & (self.data['Date'] >= start_date)
        self.data = self.data.loc[mask]

 
    def past_month(self):
        
        self.data = self.data.copy()
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        end_date = self.todays_date + pd.offsets.MonthEnd(0) - pd.offsets.MonthBegin(1)
        start_date = end_date - pd.DateOffset(month=1)
        mask = (self.data['Date'] >= start_date) & (self.data['Date'] <= end_date)
        self.data = self.data.loc[mask]


    def data_cols(self):
        # TODO to ensure the accuracy of this code, make the proper adjustments before we pull the groupby data
        # that means remove lines that dont matter for categorizing the data. (I.e. the duplicate charges from navy fed -> credit cards)
        self.data = self.data.copy()
        self.data.fillna(0, inplace=True)
        return self.data.groupby('Category').agg(
            debit_avg_spending = pd.NamedAgg(column='Debit', aggfunc='mean'), 
            credit_avg_spending = pd.NamedAgg(column='Credit', aggfunc='mean'),
            debit_total_spend = pd.NamedAgg(column='Debit', aggfunc='sum'), 
            credit_total_spend = pd.NamedAgg(column='Credit', aggfunc='sum'),
            debit_max = pd.NamedAgg(column='Debit', aggfunc='max'), 
            debit_min = pd.NamedAgg(column='Debit', aggfunc='min'), 
            credit_max = pd.NamedAgg(column='Credit', aggfunc='max'), 
            credit_min = pd.NamedAgg(column='Credit', aggfunc='min'), 
            std_cats = pd.NamedAgg(column='Debit', aggfunc='std'), 
            n_unique = pd.NamedAgg(column='Description', aggfunc='nunique'), 
            user_purchases = pd.NamedAgg(column='User', aggfunc='count'))
        
    
