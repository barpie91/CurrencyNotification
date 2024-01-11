import requests
import csv

class CurrencyExchange:
  def __init__(self, URL, currency_code):
    self.URL = URL
    self.currency_code = currency_code

  def fetch_currency_data(self):
    """The function gets the data from the API 
    Returns:
        It responses with the data in the json format 
    """
    API_URL = f"{self.URL}/exchangerates/rates/a/{self.currency_code}/"
    response = requests.get(API_URL)
    return response.json()


  def extract_data_from_response(self, data):
    """It transforms the json format file into a list
    Args:
        it takes json file as an argument
    Returns:
        _it returns the list as a row of data with the currency rate
    """
    lists = [data['rates'][0]["effectiveDate"], data['currency'], data['code'], data['rates'][0]["mid"]]
    return lists


  def save_to_csv(self, data, file_name = 'currency_exchange.csv'):
    """it saves API imported data into a csv file

    Args:
        data: json file
        file_name: destination file name
    """
    with open(file_name, "a", newline='') as csv_file:
      writer = csv.writer(csv_file)
      if csv_file.tell() == 0:
        headers = ["Date", "Currency", "Code", "Rate"]
        writer.writerow(headers)
      writer.writerow(self.extract_data_from_response(data))
      
