class TresholdModel:

    def __init__(self, treshold_low, treshold_high):
      self.treshold_low = treshold_low
      self.treshold_high = treshold_high
      self.lista = []

    def fit(self):
        pass

    def predict(self, test_data_set_values):
      for item in test_data_set_values:
        if item > self.treshold_high:
          self.lista.append(1)
        elif item < self.treshold_low:
          self.lista.append(1)
        else:
          self.lista.append(0)
      return self.lista