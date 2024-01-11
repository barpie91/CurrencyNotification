# CurrencyNotification

Anomaly detection project

The purpose of this document is to present anomaly detection solution
that helps to identify anomalies in currency rates based on API data.

The document focuses mainly on code with best OPP and Data Science
practices. However, it can be used further in comprehensive implementations. 

Key assumptions:
1. Implementation of Currency exchange class on Google Cloud platform 
to collect daily currency rates and save them in the CSV file located
in the destination directory. 

Currency Exchange class

The class represents URL and currency code as attributes and methods
that query the API and transform it further to the destination format
in CSV file.

Currency Tracker class

The class represents CSV file as an init
