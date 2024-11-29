import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np
#old
# from sklearn.neighbors import NearestNeighbors
# import numpy as np

# class Model:
#   def __init__(self, k, threshold):
#     self.knn = NearestNeighbors(n_neighbors = k)
#     self.threshold = threshold
#     self.lista = []

#   def fit(self, training_data_set):
#     x_train = create_windows(training_data_set['Kurs'].values)
#     self.knn.fit(x_train)

#   def predict(self, test_data_set):
#     x_test = create_windows(test_data_set['Kurs'].values)
#     distance, indices = self.knn.kneighbors(x_test)
#     return distance

#   def anomaly_score(self):
#     for item in self.predict(test_data_set):
#       if item[-1] > self.threshold:
#         self.lista.append(1)
#       else:
#         self.lista.append(0)
#     return self.lista

#new

class KNNModel:
  def __init__(self, k, threshold):
    self.knn = NearestNeighbors(n_neighbors = k)
    self.threshold = threshold
    self.DataFrame = pd.DataFrame(training_data_set)

  def fit(self, training_data_set):
    x_train = create_windows(self.DataFrame['Kurs'].values)
    self.knn.fit(x_train)

  def predict(self, test_data_set):
    x_test = create_windows(test_data_set['Kurs'].values)
    distance, indices = self.knn.kneighbors(x_test)
    return distance

  def anomaly_score(self):
    """
    Chciałbym dodać dodatkową kolumnę do DataFrame'u aby móc później wizualizować
    przez 0 albo 1. Podpowiesz jak to można zrobić?
    
    Czy metoda do wizualizacji ma tutaj sens? Czy zrobić to poza klasą?

    """
    for item in self.predict(test_data_set):
      if item[-1] > self.threshold:
        self.DataFrame['check_value'] = 1
      else:
        self.DataFrame['check_value'] = 0
    return self.DataFrame

    def visualize(self):
      pass