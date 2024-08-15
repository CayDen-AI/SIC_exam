import pandas as pd


file_path = './data/Student_performance_data _.csv'
df = pd.read_csv(file_path)
print(df.head())
print(df.shape)