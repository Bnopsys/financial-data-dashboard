import pandas as pd

class DataStats:

    def __init__(self, df: pd.DataFrame, user: str = None|str) -> None:
        
        self.data = df
        self.user = user
        self.todays_date = pd.to_datetime('now')
        self.month_prior_date = self.todays_date - pd.DateOffset(month=1)

    def modify_user(self):
        self.data = self.data.loc[self.data['User'] == self.user]

    def month_to_date(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        start_date, end_date = self.month_prior_date, self.todays_date
        mask = (self.data['Date'] <= end_date) & (self.data['Date'] >= start_date)
        self.data = self.data.loc[mask]

    def past_month(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        end_date = self.todays_date + pd.offsets.MonthEnd(0) - pd.offsets.MonthBegin(1)
        start_date = end_date - pd.DateOffset(month=1)
        mask = (self.data['Date'] >= start_date) & (self.data['Date'] <= end_date)
        self.data = self.data.loc[mask]

    def data_cols(self):
        # TODO fix this so it doesnt look as bad. maybe group them differently.
        self.avg_spending = self.data.groupby('Category').agg(avg_spending = 
                                                              pd.NamedAgg(column='Debit', aggfunc='mean'))
        
        self.total_spending = self.data.groupby('Category').agg(total_spend = 
                                                                pd.NamedAgg(column='Debit', aggfunc='sum'))
        
        self.debit_max = self.data.groupby('Category').agg(debit_max = 
                                                           pd.NamedAgg(column='Debit', aggfunc='max'))
        
        self.debit_min = self.data.groupby('Category').agg(debit_min = 
                                                           pd.NamedAgg(column='Debit', aggfunc='min'))
        
        self.credit_max = self.data.groupby('Category').agg(credit_max = 
                                                            pd.NamedAgg(column='Credit', aggfunc='max'))
        
        self.credit_min = self.data.groupby('Category').agg(credit_min = 
                                                            pd.NamedAgg(column='Credit', aggfunc='min'))
        
        self.std_per_cat = self.data.groupby('Category').agg(std_cats = 
                                                             pd.NamedAgg(column='Debit', aggfunc='std'))
        
        self.n_unique = self.data.groupby('Category').agg(n_unique = 
                                                          pd.NamedAgg(column='Description', aggfunc='nunique'))
        
        self.user_purchases = self.data.groupby('Category').agg(user_purchases = 
                                                                pd.NamedAgg(column='User', aggfunc='count'))