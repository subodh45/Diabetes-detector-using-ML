#model creation

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pickle

#load data
data= pd.read_csv("diabetes_m2023.csv")
print(data)

#null data
print(data.isnull().sum())


#features and target

features = data[["FS", "FU"]]
target = data["Diabetes"]

#handle categorical data

nfeatures = pd.get_dummies(features)
print(nfeatures)

#train and test

x_train, x_test, y_train,y_test = train_test_split(nfeatures, target, random_state=99)
print("")

print(x_train)
print("")
print(x_test)

#model creation 
model = LogisticRegression()
model.fit(x_train, y_train)


#performance 

cr = classification_report(y_test, model.predict(x_test))
print(cr)



#make prediction

fs = float(input("enter fasting sugar" ))
fu =input("freq urination y/n")

if fu =="y":
   d = [[fs, 0, 1]]
else:
   d = [[fs, 1, 0]]

result = model.predict(d)
print(result[0])



#model save

"""f = open("db2.model", "wb")
pickle.dump(model, f)
f.close"""














