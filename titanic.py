import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
from patsy import dmatrices
import statsmodels.api as sm
from scipy import stats
from sklearn.linear_model import LogisticRegression #logistic regression
from sklearn import svm #support vector Machine
from sklearn.ensemble import RandomForestClassifier #Random Forest
from sklearn.neighbors import KNeighborsClassifier #KNN
from sklearn.naive_bayes import GaussianNB #Naive bayes
from sklearn.tree import DecisionTreeClassifier #Decision Tree
from sklearn.model_selection import train_test_split #training and testing data split
from sklearn import metrics #accuracy measure
from sklearn.metrics import confusion_matrix #for confusion matrix


#train = pd.read_csv('train.csv')
#print(train.head())
#print(train.describe())


# plt.figure(figsize=(10,8))
# #70 refers to the number of bins you want to create
# train['Age'].hist(bins=70)
# plt.title("Age Dist")
# plt.xlabel("Age")
# plt.ylabel("Number of passengers")
# plt.show()


# train['Sex']=train['Sex'].apply(lambda sex:1 if sex=='male' else 0)
# train['Age']=train['Age'].fillna(train['Age'].mean())
# train['Fare']=train['Fare'].fillna(train['Fare'].mean())
# 
# print(train.head())
# 
# 
# test=pd.read_csv('test.csv')
# test['Sex']=test['Sex'].apply(lambda sex:1 if sex=='male' else 0)
# test['Age']=test['Age'].fillna(test['Age'].mean())
# test['Fare']=test['Fare'].fillna(test['Fare'].mean())
# 
# cols=["Pclass","Sex","Age"]


#survived = train['Survived'].values
#data_train = train[cols].values
#data_test = test[cols].values
# model = LogisticRegression()
# model.fit(data_train,survived)
# predict = model.predict(data_test)


#https://www.kaggle.com/ash316/eda-to-prediction-dietanic

#random note: ML does not do well with continuous variables. should try to bin whereever necessary (age, income, asset!)
data = pd.read_csv('train.csv')

#replace categorical with numeric
data['Sex'].replace(['male','female'],[0,1],inplace=True)
data['Embarked'].replace(['S','C','Q'],[0,1,2],inplace=True)
#data['Initial'].replace(['Mr','Mrs','Miss','Master','Other'],[0,1,2,3,4],inplace=True)

#drop unneeded columns
data.drop(['Name','Age','Ticket','Fare','Cabin','PassengerId'],axis=1,inplace=True)

#drop rows that have na in it. ML can't handle na values
data = data.dropna()

#train data is the syllabus.
#test data is the exam.
#we see how much the machine has scored and if it scores well are model is successful.
#test_size=0.3 means 30% of the data is used for the test data
train,test=train_test_split(data,test_size=0.3,random_state=0,stratify=data['Survived'])
train_X=train[train.columns[1:]]
train_Y=train[train.columns[:1]]
test_X=test[test.columns[1:]]
test_Y=test[test.columns[:1]]
X=data[data.columns[1:]]
Y=data['Survived']


model = LogisticRegression()
model.fit(train_X,train_Y)
prediction3=model.predict(test_X)

#cannot do summary. have to use statsmodel for this (see below)
print('The accuracy of the Logistic Regression is',metrics.accuracy_score(prediction3,test_Y))



'''
#https://github.com/agconti/kaggle-titanic/blob/master/Titanic.ipynb

#take care of random error printing res.summary()
stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq, df)

df = pd.read_csv('train.csv')
print(df.head())

#drop ticket and cabin from the analysis
df = df.drop(['Ticket','Cabin'], axis=1) 

#drop rows that have na in it
df = df.dropna()


#C means its a categorical variable, vs continuous/numerical
formula = 'Survived ~ C(Pclass) + C(Sex) + Age + SibSp  + C(Embarked)' 
results = {}

y,x = dmatrices(formula, data=df, return_type='dataframe')
model = sm.Logit(y,x)
res = model.fit()
results['Logit'] = [res, formula]
print(res.summary())

'''



