import requests
import csv

class CurrencyExchange:
  def __init__(self, URL, currency_code):
    self.URL = URL
    self.currency_code = currency_code

  def fetch_currency_data(self):
    """"    Brief description of what the function does.

    More detailed description if necessary. This may include explanations about
    the function's purpose, its behavior, and any side effects.

    Parameters:
    param1 (type): Description of param1.
    param2 (type): Description of param2.

    Returns:
    type: Description of the return value."""
    API_URL = f"{self.URL}/exchangerates/rates/a/{self.currency_code}/"
    response = requests.get(API_URL)
    return response.json()


  def extract_data_from_response(self, data):
     lists = [data['rates'][0]["effectiveDate"], data['currency'], data['code'], data['rates'][0]["mid"]]
     return lists


  def save_to_csv(self, data, file_name = 'currency_exchange.csv'):
    with open(file_name, "a", newline='') as csv_file:  #a = append
      writer = csv.writer(csv_file)
    # Check if the file is empty; if it is, write headers
      if csv_file.tell() == 0:#csv_file class
        headers = ["Date", "Currency", "Code", "Rate"]
        writer.writerow(headers)
      writer.writerow(self.extract_data_from_response(data))
      
