__author__ = 'Jake'
import tensorflow as tf

import tensorflow.contrib.learn as skflow
from sklearn import metrics
import pandas as pd
import os
import AI_Functions


path = r'C:\Users\Jake\Desktop\Sir_Heaton_AI_Class\data\iris.csv'

# Read iris dataset
filename_read = path
df = pd.read_csv(filename_read,na_values=['NA','?'])

# Extract just the columns we shall predict on
AI_Functions.encode_numeric_zscore(df,'sepal_l')
AI_Functions.encode_numeric_zscore(df,'sepal_w')
AI_Functions.encode_numeric_zscore(df,'petal_l')
AI_Functions.encode_numeric_zscore(df,'petal_w')
species = AI_Functions.encode_text_index(df,'species')

# Create x(predictors) and y (expected outcome)
x,y = AI_Functions.to_xy(df,'species')

# Create a deep neural network with 3 hidden layers of 10, 20, 10
classifier = skflow.TensorFlowDNNClassifier(hidden_units=[10, 20, 10], n_classes=3,steps=200)

# Fit/train neural network
classifier.fit(x, y)

# Measure accuracy
score = metrics.accuracy_score(y, classifier.predict(x))
print("Final score: {}".format(score))

# How to make many predictions
pred = classifier.predict(x)
predDF = pd.DataFrame(pred)
pred_nameDF = pd.DataFrame(species[pred])
actual_nameDF = pd.DataFrame(species[df['species']])
df2 = pd.concat([df,predDF,pred_nameDF,actual_nameDF],axis=1)
df2.columns = ['sepal_l','sepal_w','petal_l','petal_w','expected','predicted','expected_str','predicted_str']
