import requests
import pandas as pd
import matplotlib.pyplot as plt


response = requests.get('https://www.example.com')
print(response.text)


params = {'key': 'value'}
response = requests.get('https://www.example.com', params=params)
print(response.text)


data = {'key': 'value'}
response = requests.post('https://www.example.com', data=data)
print(response.text)



try:
    data = pd.read_csv('data.csv')
    print(data.head())

    print(data.describe())

    print(data.groupby('column_name').sum())
except FileNotFoundError as e:
    print(f"File not found: {e}")
except KeyError as e:
    print(f"Invalid column name: {e}")
except Exception as e:
    print(f"An error occurred: {e}")


x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.show()

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [2, 5, 8, 11, 14]
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')
plt.legend()
plt.show()

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels)
plt.show()