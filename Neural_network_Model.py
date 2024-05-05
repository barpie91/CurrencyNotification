import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam

class NeuralNetworkModel:
  def __init__(self, input_shape):
    self.build_autoencoder(input_shape)

  def build_autoencoder(self, input_shape):
    inputs = Input(shape=(input_shape,))#drugi wymiar sieci to rozmiar datasetu
    #Building encoder
    encoded = Dense(6, activation = 'relu')(inputs)
    encoded = Dense(2, activation = 'relu')(encoded)

    #Building decoder
    decoded = Dense(6, activation = 'relu')(encoded)
    decoded = Dense(input_shape, activation = 'sigmoid')(decoded) #wszystko co wpuszczamy do sieci musimy znormalizować (0,1)

    autoencoder = Model(inputs,decoded)

    # Compile the model with Adam optimizer and mean squared error loss
    autoencoder.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
    self.autoencoder = autoencoder

  def fit(self):

    self.autoencoder.fit(train_targets, train_targets, epochs = 100, validation_split = 0.2)


  def predict(self):

    return self.autoencoder.predict(test_targets)