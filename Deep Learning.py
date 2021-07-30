import pandas as pd
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from sklearn.preprocessing import LabelEncoder

read = pd.read_csv('Churn_Modelling.csv')

# Label Encoding necessary for categorical values else a problem
le = LabelEncoder()
encoded = read.apply(le.fit_transform)
read = pd.DataFrame(encoded.values,columns = read.columns)

x = read.drop(['RowNumber','CustomerId','Surname','Exited'],axis=1)
y = read['Exited']

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size = 0.2,random_state=0)

model = Sequential()
model.add(Dense(1024,activation='relu',input_dim=10))
model.add(Dense(512,activation='relu',))
model.add(Dense(256,activation='relu',))
model.add(Dense(64,activation='relu',))
model.add(Dense(32,activation='relu',))
model.add(Dense(16,activation='relu',))
model.add(Dense(4,activation='relu',))
model.add(Dense(1,activation='relu',))
model.compile(optimizer='adam', loss = 'binary_crossentropy',metrics=['accuracy'])
model.fit(xtrain,ytrain,epochs=50,batch_size = 100)
print(model.summary())

ypred = model.predict(xtest)
from sklearn.metrics import accuracy_score
print('Deep Learning',accuracy_score(ypred,ytest)*100)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(xtrain,ytrain)
ypred = lr.predict(xtest)
print('Machine Learning',accuracy_score(ypred,ytest)*100)
