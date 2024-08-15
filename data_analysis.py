import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = './data/Student_performance_data _.csv'
df = pd.read_csv(file_path)
print(df.head())
print(df.shape)
print(df.describe())


print(df.info())
print(df.isnull().sum()) # check null
def heat_map():
    numerical_data = df.select_dtypes(include='number')
    plt.figure(figsize=(20, 10))
    sns.heatmap(numerical_data.corr(), annot=True, cmap='coolwarm')
    plt.show()


def ParentalSupport_gpa():
    plt.bar(df['ParentalSupport'], df['GPA'])
    plt.xlabel('ParentalSupport')
    plt.ylabel('GPA')
    plt.show()


def Absences_gpa():
    plt.bar(df['Absences'], df['GPA'])
    plt.xlabel('Absences')
    plt.ylabel('GPA')
    plt.show()


def ParentalEducation_gpa():
    plt.bar(df['ParentalEducation'], df['GPA'])
    plt.xlabel('ParentalEducation')
    plt.ylabel('GPA')
    plt.show()


def studyTimeWeekly_gpa():
    plt.bar(df['StudyTimeWeekly'], df['GPA'])
    plt.xlabel('StudyTimeWeekly')
    plt.ylabel('GPA')
    plt.show()


def Extracurricular_gpa():
    plt.bar(df['StudyTimeWeekly'], df['GPA'])
    plt.xlabel('StudyTimeWeekly')
    plt.ylabel('GPA')
    plt.show()


# heat_map()
# age_gpa()
# gender_gpa()
# Absences_gpa()
# studyTimeWeekly_gpa()
# ParentalSupport_gpa()
# Extracurricular_gpa()
print(df.head())

grade_count = df['GradeClass'].value_counts()
print(grade_count)
