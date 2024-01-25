import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

from_email = "barpietrzyk@gmail.com"
to_email = "barpietrzyk@gmail.com"
password = "judw ijwp dnvx bohs"

def send_email(subject, message, to_email, from_email, password):
  msg = MIMEMultipart()
  msg['Subject'] = subject
  msg['From'] = from_email
  msg['To'] = to_email
  msg.attach(MIMEText(message, 'plain'))

  with smtplib.SMTP('smtp.gmail.com', 587) as server:
      server.starttls()
      server.login(from_email, password)
      server.send_message(msg)

class CurrencyTracker:

  """
The class represents a CSV file and list of thresholds as attributes and methods that load the data,
 compare rates with the given thresholds, set and check alerts, and send notification to the destination user.
  """
  def __init__(self, CSV_Path):
    self.CSV_Path = CSV_Path
    self.df = self.load_currency_data()
    self.thr_dict = []
    self.currency_value_column = 'Kurs'
    self.data_column = 'Data'
    self.currency_code = 'Waluta'
    self.model_params = {'treshold_low': 3,
                         'treshold_high': 5,
                         'knn_treshold' : 0.01,
                         'k' : 5}

  def load_currency_data(self):
    """It reads data from the file created and filled in
   	    the previous step (scrapping data)
   	    read_excel instead of read_csv.
	  Returns:
    	It returns dataframe.
	  """
  def load_currency_data(self):
    df = pd.read_excel(self.CSV_Path, skiprows = 2)
    #df['ID'] = df.index
    df = df[['Data', 'Kurs', 'Waluta']]
    return df

  def comparison(self, currency_code, model_type):
      """It checks if there are any items above/below given threshold.
	      Args:
    	  currency_code (string): selected currency code
    	  treshold_low (float): selected threshold
    	  treshold_high (float): selected threshold

	      Returns:  if exists, it returns the list of items below and/or above threshold.
	    """
      df_currency_code = self.df[self.df[self.currency_code] == currency_code]

      if model_type == 'KNN':
        model = KNNModel(self.model_params['k'], self.model_params['treshold_knn'])
      elif model_type == 'Treshold':
        model = TresholdModel(self.model_params['treshold_high'], self.model_params['treshold_low'])
      
      anomaly_score_list = model.predict(df_currency_code[self.currency_value_column])

      lista_date = []

      for i, element in enumerate(anomaly_score_list):
        if element == 1:
          lista_date.append(df_currency_code[self.data_column].values[i])
      return lista_date


  def set_alert(self, currency_code, treshold_low, treshold_high):
    """The method enables to set destined thresholds and currency
  	    code in the form of a dictionary.
	  Args:
    	  currency_code (string): selected currency code
    	  treshold_low (float): selected threshold
    	  treshold_high (float): selected threshold
	  """
    self.thr_dict.append({
        'currency': currency_code,
        'low': treshold_low,
        'high': treshold_high})

  def check_alerts(self):
    """It checks given threshold values with the data and if any appears to met them
        sends notification with the listed values.
    """
    for item in self.thr_dict:
      above_treshold_list, below_treshold_list = self.comparison(item['currency'], item['low'], item['high'])#popraw
      if len(above_treshold_list) > 0 | len(below_treshold_list):
        below_treshold_string = ", ".join(below_treshold_list)
        above_treshold_string = ", ".join(above_treshold_list)
        self.send_notification(item['currency'], below_treshold_string, above_treshold_string)#popraw

  def send_notification(self, currency_code, below_treshold_string, above_treshold_string):
    message = f"""
          Dzień: {datetime.now().date()}
          Kurs: {currency_code}
          Dla podanej waluty i podanych tresholdow lista z ostatniego miesiaca.
          Poniżej threshold: {below_threshold_string}
          Powyżej thresholdu: {above_threshold_string}
          """

    subject = f"Alert anomalii w kursie {currency_code}"
    send_email(subject, message, to_email, from_email, password)