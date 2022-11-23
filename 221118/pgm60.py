from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("D:/BCSE101E/221118/Student_Marks.csv")
print(data.head(10))
print("\n\n")
sns.boxplot(x=data['Marks'])
plt.show()
print(data['number_courses'].value_counts())
print("\n\n")
le = LabelEncoder()
data['number_courses'] = le.fit_transform(data['number_courses'])
data['time_study'] = le.fit_transform(data['time_study'])
print('transformed data\n\n', data.head(10))
data['number_courses'] = le.inverse_transform(data['number_courses'])
data['time_study'] = le.inverse_transform(data['time_study'])
print('inversed data\n\n', data.head(10))
fig, ax = plt.subplots(1, 2)
sns.barplot(x=data['number_courses'], y=data['time_study'], ax=ax[0])
sns.barplot(x=data['number_courses'], y=data['Marks'], ax=ax[1])
fig.show()
