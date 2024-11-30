import pandas as pd
#old
# class TresholdModel:

#     """
#     The class represents the k-nearest neighbors algorithm that takes a threshold
#      as an initiator and methods that fit, train and return an anomaly score based on the given dataset.
#     """

#     def __init__(self, treshold_low, treshold_high):
#       self.treshold_low = treshold_low
#       self.treshold_high = treshold_high
#       self.lista = []

#     def fit(self):
#         pass

#     def predict(self, test_data_set_values):
#       for item in test_data_set_values:
#         if item > self.treshold_high:
#           self.lista.append(1)
#         elif item < self.treshold_low:
#           self.lista.append(1)
#         else:
#           self.lista.append(0)
#       return self.lista

#new

class TresholdModel:

    def __init__(self, treshold_low, treshold_high):
      self.data_column = 'Kurs'
      self.treshold_low = treshold_low
      self.treshold_high = treshold_high
      self.DataFrame = pd.DataFrame(training_data_set)

    def fit(self):
        pass

    def predict(self, test_data_set_values):
      for item in self.DataFrame[self.data_column]:
        if item > self.treshold_high:
          self.DataFrame['check_value'] = self.DataFrame[self.data_column] > self.treshold_high
        elif item < self.treshold_low:
          self.DataFrame['check_value'] = self.DataFrame[self.data_column] < self.treshold_low
        else:
          False
      return self.DataFrame

    def vizualize(self):
      pass

      # colors = {True: 'red', False: 'blue'}
      # bar_colors = viz['check_value'].map(colors)

      # return

      # plt.bar(viz['Data'], viz[self.data_column], color=bar_colors)