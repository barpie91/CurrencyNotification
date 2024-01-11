import pandas as pd

class CurrencyTracker:
  def __init__(self, CSV_Path):
    self.CSV_Path = CSV_Path
    self.df = self.load_currency_data()
    self.thr_dict = []

  def load_currency_data(self):
    """it reads data from the file created and filled in 
       the previous step (currency exchange data crawler)
       read_excel instead of read_csv
    Returns:
        it returns dataframe
    """
    df = pd.read_excel(self.CSV_Path)
    return df

  def comparison(self, currency_code, treshold_low, treshold_high):
    """it checks if there are any items above/below given threshold       
    Args:
        currency_code (string): selected currency code
        treshold_low (float): selected threshold
        treshold_high (float): selected threshold

    Returns:
        if exists, it returns the list of items below and/or above threshold.
    """
    is_greater_than_treshold = self.df[currency_code].gt(treshold_high).any()
    
    if is_greater_than_treshold:
      above_treshold = self.df[self.df[currency_code] > treshold_high]
      above_treshold_list = above_treshold['Data'].list()
    else:
      above_treshold_list = []
      
    is_lower_than_treshold = self.df[currency_code].lt(treshold_low).any()

    if is_lower_than_treshold:
      below_treshold = self.df[self.df[currency_code] < treshold_low]
      below_treshold_list = below_treshold['Data'].list()
    else:
      below_treshold_list = []
    return below_treshold_list, above_treshold_list

  def set_alert(self, currency_code, treshold_low, treshold_high):
    """The method enables to set destined thresholds and currency 
      code in the form of dictionary.

    Args:
        currency_code (string): selected currency code
        treshold_low (float): selected threshold
        treshold_high (float): selected threshold
    """
    self.thr_dict.append({
        'currency': currency_code,
        'low': treshold_low,
        'high': treshold_high
    })

  def check_alerts(self):
    """It checks whether determined thresholds are 
    """
    for item in self.thr_dict:
      above_treshold_list, below_treshold_list = self.comparison(item['currency'], item['low'], item['high'])
      if len(above_treshold_list) > 0 | len(below_treshold_list):
        self.notification(item['currency'], below_treshold_list, above_treshold_list)


  def send_notification(self, currency_code, below_treshold_list, above_treshold_list):
    """It sends notification to the destined email with the list of elements 
    which exceeds given threshold.
     """
    pass