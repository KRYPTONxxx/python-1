import requests
import json
import sqlite3

city='Tbilisi'
key='b0382a9da8d31051dd5eecdc220673dc'
url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'
r = requests.get(url)
# print(r.status_code)
# print(r.headers)
# print(r)
result=json.loads(r.text)
# print(result)

temp=result['main']['temp']
weather=result['weather'][0]['main']
# print(json.dumps(result,indent=4))

with open('data.jason', 'w') as file:
    json.dump(result,file, indent=4)

conn=sqlite3.connect("wheather.sqlite3")
cur=conn.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS dataweather 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                city_name VARCHAR(50),
                temperature FLOAT,
                weather VARCHAR(50)) ''')

cur.execute('INSERT INTO dataweather (city_name, temperature,weather) VALUES (?,?,?)', (city,temp,weather))
conn.commit()