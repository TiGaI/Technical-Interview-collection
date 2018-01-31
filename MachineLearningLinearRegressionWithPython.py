import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#Basic information looking
USAhousing = pd.read_csv('USA_Housing.csv')
USAhousing.head()
USAhousing.info()
USAhousing.describe()
USAhousing.columns
USAhousing.index

#Create some simple plots from seaborn
sns.pairplot(USAhousing)
#Get Distribution Graph from USAhousing
sns.distplot(USAhousing['Price'])
#Get Heatmap correlation Graph
sns.heatmap(USAhousing.corr())

#Training a Linear Regression Model
X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']

#Split data into Training set and a testing test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

#Creating and Training the Model
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
#fit the data
lm.fit(X_train,y_train)

#Model Evaluation, look at the coeffeicent
print(lm.intercept_)
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
coeff_df

#Get Predictions From our Model
predictions = lm.predict(X_test)
plt.scatter(y_test,predictions)
sns.distplot((y_test-predictions),bins=50);

#Regression Evaluation Metrics
Looking into 3 common Evaluation metrics for regression problems
MAE (Mean Absolute Error) absolute value of the errors ->>>> the easiest to understand, because its the average error.
MSE (Mean Squared Error) mean of the squared errors ->>>> is more popular than MAE, because MSE "punishes" larger errors, which tends to be useful in the real world.
RMSE (Root Mean Squared Error) square root of the mean of the squared errors ->>>>> even more popular than MSE, because RMSE is interpretable in the "y" units.


#Logistic Regression with Python
train = pd.read_csv('titanic_train.csv')
#Let's begin some exploratory data analysis! Check missing data!
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
sns.set_style('whitegrid')
sns.countplot(x='Survived',data=train,palette='RdBu_r')

sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Sex',data=train,palette='RdBu_r')

sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Pclass',data=train,palette='rainbow')

sns.distplot(train['Age'].dropna(),kde=False,color='darkred',bins=30)
train['Age'].hist(bins=30,color='darkred',alpha=0.7)

train['Fare'].hist(color='green',bins=40,figsize=(8,4))

plt.figure(figsize=(12, 7))
sns.boxplot(x='Pclass',y='Age',data=train,palette='winter')

Fill in missing data
sns.heatmap(train.isull(),yticklabels=False,cbar=False,cmap='viridis')
def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):

        if Pclass == 1:
            return 37

        elif Pclass == 2:
            return 29

        else:
            return 24

    else:
        return Age

#Drop all unnessessary columns
train.drop('Cabin',axis=1,inplace=True) 

sex = pd.get_dummies(train['Sex'],drop_first=True)
embark = pd.get_dummies(train['Embarked'],drop_first=True)
train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
train = pd.concat([train,sex,embark],axis=1)

#Building logistic regression Model
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(train.drop('Survived',axis=1), 
                                                    train['Survived'], test_size=0.30, 
                                                    random_state=101)

#Training and Predicing
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))

