import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cities=[
    {"name":"Tehran" , "x":-35 , "y":51 , "population":8693706 },
    {"name":"Mashhad" , "x":-36 , "y":59 , "population":3001184},
    {"name":"Isfahan" , "x":-32 , "y":51 , "population":1961260 },
    {"name":"Karaj" , "x":-35 , "y":50 , "population":1592492 },
    {"name":"Shiraz" , "x":-29 , "y":52 , "population":1565572 },
    {"name":"Tabriz", "x":-38 , "y":46 , "population":1558693 },
    {"name":"Qom" , "x":-34 , "y":50 , "population":1201158 },
    {"name":"Ahvaz" , "x":-31 , "y":48 , "population":1184788 },
    {"name":"Kermanshah" , "x":-34 , "y":47 , "population":946651 },
    {"name":"Urmia" , "x": -37, "y":45 , "population":736224}
]

x = [d['x'] for d in cities]
y = [d['y'] for d in cities]
names = [d['name'] for d in cities]
populations = [d['population'] for d in cities]

circle_sizes = [pop / 1000 for pop in populations]

plt.figure(figsize=(8, 6))

plt.grid(True, linestyle='--', alpha=0.7)
plt.scatter(x, y, s=circle_sizes, color='pink', edgecolors='black')
plt.title("10 biggest cities of Iran", color="purple")

for i in range(len(x)):
    plt.text(x[i], y[i], names[i], fontsize=9, ha='center', va='bottom')

plt.xlabel('North Coordinate')
plt.ylabel('East Coordinate')

title_text = "10 biggest cities of Iran"
plt.title(title_text, color="purple", bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0'))

plt.show()
