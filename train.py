import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv('./data/Student_performance_data _.csv')
# print(df.head())
data = df.drop(['StudentID', 'Ethnicity', 'GPA', 'GradeClass'], axis=1)
target = df.GPA

# print(data)
# print(target)

x_train, x_x, y_train, y_y = train_test_split(data, target, test_size=0.4)
x_val, x_test, y_val, y_test = train_test_split(x_x, y_y, test_size=0.2)

model = LinearRegression()
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
print(y_test)
print(y_predict)

print(model.score(x_test, y_test))  # 0.95
# print(accuracy_score(y_test, y_predict))