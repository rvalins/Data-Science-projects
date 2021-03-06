# Data Science Projects repository
Welcome to my Data Science Projects repository at GitHub. Here you find some interesting files to your projects in Data Science.


## Table of Contents

## Machine	Learning with Scikit-Learn and TensorFlow 

### [Emotion and identity detection from face images](https://github.com/rvalins/Data-Science-projects/tree/master/emotion-identity-detection)

**Convolutional neural network**

In deep learning, a convolutional neural network (CNN, or ConvNet) is a class of deep, feed-forward artificial neural networks, most commonly applied to analyzing visual imagery.

This project includes a code that allows users to create a dataset from a collection of images and to prepare Train and Test files to the model.

1. Train Test Spilt (Scikit-Learn)
2. Training the model
3. Evaluation of the model

**Source:**
- https://en.wikipedia.org/wiki/Convolutional_neural_network
- https://www.kaggle.com/c/facial-keypoints-detector
- https://www.datascienceacademy.com.br/


### [Machine Learning on the Iris dataset (classification model)](https://github.com/rvalins/Data-Science-projects/blob/master/classification-models)
Supervised learning is the machine learning task of learning a function that maps an input to an output based on example input-output pairs.

**Algorithms:**
- K-nearest Neighbours (KNN)
- Logistic regression

**Source:**
- https://www.dataschool.io/


### [Machine Learning on Weather Data (classification model)](https://github.com/rvalins/Data-Science-projects/blob/master/decision-tree)
Supervised learning is the machine learning task of learning a function that maps an input to an output based on example input-output pairs.

**Algorithms:**
- Decision Tree

**Source:**
- UCSanDiegoX: Python for Data Science


### [Regression Analysis using Machine Learning](https://github.com/rvalins/Data-Science-projects/blob/master/regression-model)
Regression analysis consists of a set of machine learning methods that allow us to predict a continuous outcome variable (y) based on the value of one or multiple predictor variables (x).

**Source:**
- http://www.sthda.com/english/wiki/regression-analysis-essentials-for-machine-learning
- https://www.dataschool.io/
- https://www.datascienceacademy.com.br/


### [Machine Learning on Kaggle Socccer Dataset (clustering model)](https://github.com/rvalins/Data-Science-projects/blob/master/clustering_model)
Cluster analysis or clustering is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense) to each other than to those in other groups (clusters). k-means clustering aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean.

**Algorithms:**
- k-means clustering

**Source:**
- UCSanDiegoX: Python for Data Science
- https://en.wikipedia.org/wiki/Cluster_analysis
- https://en.wikipedia.org/wiki/K-means_clustering


### [Anomaly Detection (KDD CUP 99 network intrusion data)](https://github.com/rvalins/Data-Science-projects/blob/master/anomaly-detection)
The detection of anomalies has signiﬁcant relevance and often provides critical actionable information in various application domains.
Isolation Forest is an outlier detection technique that identifies anomalies instead of normal observations. Similarly to Random Forest it is built on an ensemble of binary (isolation) trees. 

**Algorithms:**
- Isolation Forest

**Source:**
- https://www.depends-on-the-definition.com
- https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf


### [Time Series Analysis - ARIMA Forecasting](https://github.com/rvalins/Data-Science-projects/blob/master/time_series_analysis)
Time Series is a collection of data points at constant time intervals. These are analyzed to determine the long term trend so as to forecast the future or perform some other form of analysis.
ARIMA models are applied in some cases where data show evidence of non-stationarity, where an initial differencing step (corresponding to the "integrated" part of the model) can be applied one or more times to eliminate the non-stationarity.

**Source:**
- https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average
- https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/
- https://www.edureka.co/


### [Multivariate Time Series Forecasting - Long Short-Term Memory (LSTM)](https://github.com/rvalins/Data-Science-projects/blob/master/multivariate_time_series_lstm)
Multivariate time series analysis considers simultaneously more than one time-dependent variable. Each variable depends not only on its past values but also has some dependency on other variables.
Long Short-Term Memory (LSTM) recurrent neural networks are able to almost seamlessly model problems with multiple input variables.

**Source:**
- https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/
- https://www.analyticsvidhya.com/blog/2018/09/multivariate-time-series-guide-forecasting-modeling-python-codes/


## Using Python to performance Data Manipulation or to automate tasks

### [ElasticSearch](https://github.com/rvalins/Data-Science-projects/blob/master/elasticsearch)
This project allows users to connect to a ElasticSearch server, to extract and to write this data in a JSON file.

Elasticsearch is a full-text, distributed NoSQL database.

This code also record the previous indexes that were scanned to only get new inputs.

You can use the JSON to CSV file to convert to a structered table format.

### [Convert JSON to CSV file](https://github.com/rvalins/Data-Science-projects/blob/master/json_to_csv)
This project reads a JSON file, parse it and convert it to a CSV file.

### [Merge TXT files and Convert to CSV](https://github.com/rvalins/Data-Science-projects/blob/master/merge_txt_and_convert_to_csv)
This project automatically merge txt files based on column position and convert to CSV file.

### [Using Python to send Emails from Gmail](https://github.com/rvalins/Data-Science-projects/blob/master/send_email)
This project aggregate several features, such as:
1. To custom email sender address
As your email address is more likely to be to be recognized by your applicants and reviewers, your email is more likely to be received and not get caught in spam filters.

2. To custom subject field
You will be able to set up an interactive subject field

3. To define recipients according to a mailing list (CSV file)
This project extract information from a mailing list, grouping recipients according to their company (for example)

4. To define language content
Possibility to send different contents according to the language informed at mailing list

5. To use HTML format in your message
This project allows you to import a HTML content and send it, according to the language selected

6. To use attachments
This project allows you to send more than one attachment, no matter the filetype and addressed correctly to the recipients group

7. To keep register of the use
This project create a log register for further reference


### [Data Analytics with Python by Web scraping](https://github.com/rvalins/Data-Science-projects/blob/master/webscraping)
This project allows you to extract information from one website, using Python (BeautifulSoup).

BeautifulSoup is a Python library which helps you to navigate, search and modify the parse tree.

This information will be presented in a word cloud visualization.
