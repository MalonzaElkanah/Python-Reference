'''
Problem Statement — A car company has released a new SUV in the market. Using the previous data about the sales of their SUV’s, they want to predict the category of people who might be interested in buying this.
'''

import pandas as pd

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score 

# we will import the dataset and separate dependent variable(purchased) and independent variable(age, salary)
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values
print(X)
print(y)

# training and test the data.
# split data in a ratio of 70–80% for training subset and 20–30% for the testing subset. 
# we have created create Training and Testing sets using cross_validation.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# scale the input values for better performance using StandarScaler 
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# create our Logistic Regression model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# predict the results of our test set.
y_pred = classifier.predict(X_test)


cm = confusion_matrix(y_test, y_pred)
print(cm)

# based on our confusion matrix, we can calculate the accuracy. So in our above example, the accuracy would be:
# TP + TN / FN + FP   
print(accuracy_score(y_test, y_pred)*100) 

