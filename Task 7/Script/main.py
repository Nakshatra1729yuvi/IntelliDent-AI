import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix
from sklearn.preprocessing import LabelEncoder


data=pd.read_csv('D:\\IntelliDent AI\\Task 7\\data\\data.csv')  #Reading CSV file

X=data.drop(['label'],axis=1)  #Features
y=data['label']              #Target variable

le=LabelEncoder()
y=le.fit_transform(y)        #Encoding target variable



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  #Splitting data

model=LogisticRegression()   #Creating model

model.fit(X_train,y_train)   #Training model

y_pred=model.predict(X_test)  #Making predictions

accuracy=accuracy_score(y_test,y_pred)  #Calculating accuracy

conf_matrix=confusion_matrix(y_test,y_pred)  #Calculating confusion matrix

print(f'Accuracy: {accuracy}')

print(f'Confusion Matrix:\n{conf_matrix}')

# Writing results to a text file
with open('D:\\IntelliDent AI\\Task 7\\results\\results.txt', 'w') as f:
    f.write(f'Accuracy: {accuracy}\n')
    f.write(f'Confusion Matrix:\n{conf_matrix}\n')

