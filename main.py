import pandas
from sklearn.linear_model import  LinearRegression


data=pandas.read_csv('Book1.csv')
print(data.head())

sem=LinearRegression()

sem.fit(data[['Semester']], data[['CGPA']])

print(sem.predict([[9]]))