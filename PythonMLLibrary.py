NumPy Exercise - two D array
import numpy as np
np.zeros(10)
#Create an array of 10 ones
np.ones(1)
#Create an array of 10 fives
np.ones(10) * 5
#Create an array of the integers from 10 to 50
np.arange(10,51)
#Create an array of all the even integers from 10 to 50
np.arange(10,51,2)
#Create a 3x3 matrix with values ranging from 0 to 8
np.arange(9).reshape(3,3)
#create a 3x3 identity matrix
np.eye(3)
#random number 0 and 1
np.random.rand(1)
#generate random numbers predicable with seed()
np.random.seed(10), np.random.rand(4)
#Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
np.random.rand(25)
#Create an array of 20 linearly spaced points between 0 and 1
np.linspace(0,1,20)
#Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:
mat = np.arange(1,26).reshape(5,5)

mat[2:,1:] get row 3 to 5 and column 2 to 5
mat[3,4] including = 20
mat[:3,1:2] = array([[ 2], [ 7], [12]])
mat[3:5,:]
.sum() #Get the sum of all the values in mat
.std() #get the standard deviation of the values in mat
.sum(axis=0) #Get the sum of all the columns in mat
.sqrt(arr) .mean() .min() .max() .count()
.exp(arr) .describe() .transpose() .info()
.sin(arr)
.log(arr)

NP can do regular operation * / + - < > <= >= != 

Pandas use to convert different type data to table and use advance function to filter and remap the data

import panda as pd 
#read and write to csv file
df = pd.read_csv('file_name')
df = df.to_csv('example', index=False)
#Excel Input and output, beware of image in the excel file, it may cause it to crash
pd.read_excel('Excel_Sample.xlsx',sheetname='Sheet1')
pd.to_excel('excelname.xlsm', sheetname)
#Html Input
df = pd.read_html('http://.....html')
#Read Database in sql
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:momory:')
df.to_sql('data', engine)
sql_df = pd.read_sql('data', con=engine)

#Convert to DataFrames
df= pd.DataFrame(np.random(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
df['W'] or df['W', 'Z'] #to call one or more column
#creating new columns
df['new'] = #whatever
#Removing columns
df.drop('nameofthecolumn',axis=1) #need to use "inplace=True" to make it inplace change
#selecting Rows
df.loc['A'] #using the name to location row
df.iloc[2] #using index to location the row
df.loc['B','Y'] #locate a item in table
df.loc[['A', 'B', ['W', 'Y']]] #selecting a box of element
#can also use condition to filter data
df[df>0]
df[df['W']>0]

#reset to index base row
df.reset_index()
#set a new index
df.set_index("colNAME") #another use of "inplace=True" to make it inplace change
#use multi-index and multiple level index hierarchy
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
MultiIndex(levels=[['G1', 'G2'], [1, 2, 3]],
           labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])
#set index names 
df.index.names #check how many name you need
df.index.names = ['Group','Num']
#select the first index
df.xs('G1')
df.xs(['G1',1])
df.xs(1,level='Num')

#GROUP BY function
df.groupby('Company') #supportive function .mean(), std()

#Create a series in Pando - A Series is very similar to a NumPy array. A Series can have axis labels, meaning it can be indexed by a label, instead of just a number location. 
#It also doesn't need to hold numeric data, it can hold any arbitrary Python Object.
pd.Series(data=my_list) #set label "index=labels"
#Can do normal operation just like matrices

#Operations To Find Unique
df['ColName'].unique #return all unique number
df['ColName'].nunique #return the number of unique number
df['col2'].value_counts() #return the count of each unique number

#applying function
def times2(x):
    return x*2
df['col1'].apply(times2)
df['col3'].apply(len) #length

#Get Column and index names:
df.columns '''return the column''' df.head() #return the top 5
df.index

#Important function
df.sort_values(by='col2') # sort
df.isnull() '#Return null value in true or false' df.dropna() '#drop all drop with NAN', "thresh=2" allow for row with less than 2 nan to keep their row
df.fillna("STRING OR NUMBER of your choice")
df.pivot_table(values='D',index=['A', 'B'],columns=['C']) #pivot table 

#Concatenation, Merging, Joining
#Concatenation basically glues together DataFrames. Keep in mind that dimensions should match along the axis you are concatenating on.
pd.concat([df1,df2,df3]) "axis=1"
#Merging allow you to merge DataFrames together using similar logic as merging sql
pd.merge(left,right,how='inner',on='key')
#join two potentially differently-indexed Dataframe into a single result
left.join(right) # 'how='outer''
		EXAMPLE:
			left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
			                     'B': ['B0', 'B1', 'B2']},
			                      index=['K0', 'K1', 'K2']) 

			right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
			                    'D': ['D0', 'D2', 'D3']},
			                      index=['K0', 'K2', 'K3'])


SciPy
#MAthematical algorithms and convenience functions built on NumPy
#Linear Algebra
from scipy import linalg
#Get Determinant of a matrix
linalg.det(Matrix)
#Find the decomposition of a matrix Solving for A = P L U
P, L, U = linalg.lu(Matrix)
#dot product
np.dot(L,U)
#finding eigenvalues and eignevectors of matrix, measure of distoriton indeced by the transformation and eigenvectos tell you about how the distortion is oriented. It tells the person how linear transformation works
EW, EV = linalg.eig(A)\
#Solving Lienar Equaiton
s = linalg.solve(A,v)

#Sparse Linear Algebra  computing with sparse and potentially very large matrice
from scipy import sparse
A = sparse.lil_matrix((1000, 1000))
A[0,:100] = np.random.rand(100)
A.setdiag(np.random.rand(1000))

from scipy.sparse import linalg
A.tocsr()
b = np.random.rand(1000)
linalg.spsolve(A, b)
#There is a lot more that SciPy is capable of, such as Fourier Transforms, Bessel Functions, etc...

"Snsborn"
import seaborn as sns
df['col'].hist(bins="number of bins")
df['A'].plot(kind="hist", bins=30)
df['A'].plot.hist()
#Area plot
plot.area(alpha="0 to 1") 
#bar plot
df2.plot.bar()
#boxplot
sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')
#distribution graph
sns.distplot(titanic['fare'],bins=30,kde=False,color='red')
#joint Graph
sns.jointplot(x='fare',y='age',data=titanic)
#swarmplot
sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')
#count plot
sns.countplot(x='sex',data=titanic)
#heat map
sns.heatmap(titanic.corr(),cmap='coolwarm')