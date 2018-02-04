import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns																							#Basic information looking
%matplotlib inline																								#Create some simple plots from seaborn
																												#Training a Linear Regression Model
#Basic information looking                                         												#Split data into Training set and a testing test
USAhousing = pd.read_csv('USA_Housing.csv')																		#Creating and Training the Model
USAhousing.head()																								#fit the data
USAhousing.info()																								#Model Evaluation, look at the coeffeicent
USAhousing.describe()																							#Get Predictions From our Model
USAhousing.columns																								#Regression Evaluation Metrics
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

#Fill in missing data
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


#Decision Trees and Random Forests in Pythons
#More Information Gain
#Entropy is a measure of uncertainty associated with our data

#Use for both classification and regression problem
#Hunt's algorithm, greedy model. Take in the current most optimal decision instead of account for the global optimuizaiton
Check simple pairplot of this small dataset
sns.pairplot(df,hue='Kyphosis',palette='Set1')

#Train Test Split
from sklearn.model_selection import train_test_split
X = df.drop('Kyphosis', axis=1)
Y = df['Kyphosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

#Train
from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)

#Prediction and evaluation
from sklearn.metrics import classification_report,confusion_matrix

#Tree Visualization
from IPython.display import Image  
from sklearn.externals.six import StringIO  
from sklearn.tree import export_graphviz
import pydot 
#Get the features wanted, in this case it is age, number, start
features = list(df.columns[1:])

dot_data = StringIO()  
export_graphviz(dtree, out_file=dot_data,feature_names=features,filled=True,rounded=True)
graph = pydot.graph_from_dot_data(dot_data.getvalue())  
Image(graph[0].create_png())

#Random Tree
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(X_train, y_train)
rfc_pred = rfc.predict(X_test)
print(classification_report(y_test,rfc_pred))



#K Nearest Neightbors
#Use to find connection between the data and target classes and predicts a class for a new data point based off of the features
#con: High Prediction Cost, not good with multi dimensional data
#Categorical features don't work well

1. Get the file and basic information

2. Get the standard version of the data
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis=1))
scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))
df_feat = [d.DataFrame(scaled_features, columns=df.columns[:-1])]

3. Train the data
from sklearn.model_selection import train_test_split
X = scaled_features
Y = df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

4. Find the ideal k constant
from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors =1)
knn.fit(X_train,y_train)
pred = knn.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,prep))

#plotting the error rate to see which one has the lowest k value
error_rate = []

for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_Train,y_train)
    pred_i = knn.predict(X_Train)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,40), error_rate,color='color',linestyle='dashed',marker='o', marketfacecolor='red', markersize = 10)
plt.title("")
plt.xlabel('')
plt.ylabel('')