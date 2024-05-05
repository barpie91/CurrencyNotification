from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

data = pd.read_excel('waluty.xlsx', skiprows=2)
data = data[['Data', 'Kurs', 'Waluta']]
data['Data'] = pd.to_datetime(data['Data'])
cut_of_date = pd.Timestamp('2023-01-01')
training_data_set = data[data['Data'] < cut_of_date]
test_data_set = data[data['Data'] > cut_of_date]

training_data_set_values = training_data_set['Kurs'].values
test_data_set_values = test_data_set['Kurs'].values

def create_windows(data, windows_size=10):
    windows = [data[i:i+windows_size] for i in range(len(data) - windows_size + 1)]
    return windows

#Splitting the data into training and test
x_train = create_windows(training_data_set['Kurs'].values)
x_test = create_windows(test_data_set['Kurs'].values)

#Normalize the data
scaler = MinMaxScaler()
train_targets = scaler.fit_transform(x_train)
test_targets = scaler.transform(x_test)

#print(train_targets)