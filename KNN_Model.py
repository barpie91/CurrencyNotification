import pandas as pd
from sklearn.neighbors import NearestNeighbors

#preprocessing data
data = pd.read_excel('waluty.xlsx', skiprows=2)
data = data[['Data', 'Kurs', 'Waluta']]
data['Data'] = pd.to_datetime(data['Data'])
cut_of_date = pd.Timestamp('2023-01-01')
training_data_set = data[data['Data'] < cut_of_date]
test_data_set = data[data['Data'] > cut_of_date]

def create_windows(data, windows_size=3):
    windows = [data[i:i+windows_size] for i in range(len(data) - windows_size + 1)]
    return windows

x_train = create_windows(training_data_set['Kurs'].values)
x_test = create_windows(test_data_set['Kurs'].values)

#1. Initiation
knn = NearestNeighbors(n_neighbors = 3)
#2. Fitting
knn.fit(x_train)

########################################################################################

from sklearn.neighbors import NearestNeighbors

class Model:

    """
    The class represents the k-nearest neighbors algorithm that takes a threshold
     as an initiator and methods that fit, train and return an anomaly score based on the given dataset.
    """

    def __init__(self, k, threshold):
      self.knn = NearestNeighbors(n_neighbors = k)
      self.threshold = threshold
      self.lista = []

    def fit(self, training_data_set):
      x_train = create_windows(training_data_set['Kurs'].values)
      self.knn.fit(x_train)

    def predict(self, test_data_set):
      x_test = create_windows(test_data_set['Kurs'].values)
      distance, indices = self.knn.kneighbors(x_test)
      return distance

    def anomaly_score(self, test_data_set):
    #został przekroczony threshold to 1
      for item in self.predict(test_data_set):
        if item[-1] > self.threshold:
          self.lista.append(1)
        else:
          self.lista.append(0)
      return self.lista