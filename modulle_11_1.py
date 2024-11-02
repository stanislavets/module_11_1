import requests

url = 'https://api.github.com/repos/python/cpython/commits?per_page=1'
response = requests.get(url)

if response.status_code == 200:
    commit_data = response.json()[0]
    sha = commit_data['sha']
    message = commit_data['commit']['message']
    author = commit_data['commit']['author']['name']
    date = commit_data['commit']['author']['date']

    print(f"SHA: {sha}")
    print(f"Message: {message}")
    print(f"Author: {author}")
    print(f"Date: {date}")
else:
    print("Error:", response.status_code)


import pandas as pd

# Чтение данных из CSV-файла
df = pd.read_csv('data.csv')

# Просмотр первых пяти строк
print(df.head())

# Вычисление среднего возраста
mean_age = df['age'].mean()
print(f"Средний возраст: {mean_age}")

# Фильтрация данных по условию
young_people = df.query("age < 25")
print(young_people)


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o', linestyle='--', color='b')
plt.title('Простая линия')
plt.xlabel('X ось')
plt.ylabel('Y ось')
plt.grid(True)
plt.show()