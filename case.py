import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance .csv')

print(df)
#Гипотеза №1: присутствие подготовительного курса у студентов положительно влияет на результы
#Гипотеза №2: Студенты, получающие льготное питание, имеют более низкие результаты
#Гипотеза №3: Студенты с высоким уровнем образования у родителей имеют более высокие результаты

prep = df.groupby('test preparation course').mean()
prep[['math score', 'reading score', 'writing score']].plot(kind = 'barh', subplots = True, grid = True, figsize=(10, 6))
plt.title('Влияние подготовительного курса на результаты')
plt.ylabel('Средний балл')
plt.xlabel('Присутствие подготовительного курса')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['math score'], df['reading score'], df['writing score'])
plt.title('Средний балл')
plt.xlabel('math score')
plt.ylabel('reading score')
plt.colorbar()
plt.show()



lunch = df.groupby("lunch").mean()
lunch[['math score', 'reading score', 'writing score']].plot(kind='pie', figsize=(10, 6), subplots=True, autopct='%1.1f%%')
plt.title('Влияние льготного питания на результаты')
plt.xlabel('Средний балл')
plt.show()

parental = df.groupby('parental level of education').mean()
parental[['math score', 'reading score', 'writing score']].plot(kind='barh', figsize=(10, 6), grid = True)
plt.title('Влияние уровня образования родителей на результаты')
plt.ylabel('Средний балл')
plt.xlabel('Уровень образования родителей')
plt.show()

parental = df.groupby('parental level of education').mean()
parental[['math score', 'reading score', 'writing score']].plot(kind='box', figsize=(10, 6))
plt.title('Влияние уровня образования родителей на результаты')
plt.ylabel('Средний балл')
plt.xlabel('Уровень образования родителей')
plt.show()

parental = df.groupby('parental level of education').mean()
parental[['math score', 'reading score', 'writing score']].plot(kind='pie', figsize=(10, 16), subplots=True, autopct='%1.1f%%')
plt.title('Влияние уровня образования родителей на результаты')
plt.ylabel('Средний балл')
plt.xlabel('Уровень образования родителей')
plt.show()