import pandas as pd

class DataStats:

    def __init__(self, df: pd.DataFrame, user: str = None) -> None:
        """
        After modifying the data one way, you must create a new class instance when filtering the data a different way.
        """
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

    def format_cols(self):
        self.data = self.data.copy()
        self.data.fillna(0, inplace=True)

    def type_data(self, financial_type: str):
        options = ['Debit', 'Credit']
        if financial_type not in options:
            raise ValueError('Please enter either: Debit or Credit for financial_type')
        
        self.format_cols()
        return self.data.groupby('Category').agg(avg_spending = pd.NamedAgg(column=financial_type, aggfunc='mean'), 
                                                 total_spend = pd.NamedAgg(column=financial_type, aggfunc='mean'), 
                                                 max = pd.NamedAgg(column=financial_type, aggfunc='max'), 
                                                 min = pd.NamedAgg(column=financial_type, aggfunc='min'), 
                                                 std = pd.NamedAgg(column=financial_type, aggfunc='std'), 
                                                 n_unique = pd.NamedAgg(column='Description', aggfunc='nunique'), 
                                                 user_purchases = pd.NamedAgg(column='User', aggfunc='count'))