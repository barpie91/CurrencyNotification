# CurrencyNotification

Anomaly detection project

The purpose of this document is to present anomaly detection solution
that helps to identify anomalies in currency rates based on API data.

The document focuses mainly on code with best OPP and Data Science
practices. However, it can be used further in comprehensive implementations. 

Key assumptions "Work in progress":
Implementation of Currency exchange class on Google Cloud platform 
to collect daily currency rates and save them in the CSV file located
in the destination directory. 

Currency Exchange class

The class represents URL and currency code as attributes and methods
that query the API and transform it further to the destination format
in CSV file.

Currency Tracker class

The class represents a CSV file and list of thresholds as attributes and methods that load the data,
 compare rates with the given thresholds, set and check alerts, and send notification to the destination user.

 KNN Model class

 The class represents the k-nearest neighbors algorithm that takes a threshold
 as an initiator and methods that fit, train and return an anomaly score based on the given dataset.

 Treshold Model class

 The class represents a anomaly detection class that takes a thresholds as an init attributes, go through the list
 of currency rates and with the given tresholds return an anomaly score based on the given dataset.

 Neural Network model

"" Work in progress ""

