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

