import matplotlib.pyplot as plt

covid_data = [
    {"state": "California", "cases": 12129699},
    {"state": "Texas", "cases": 8466220},
    {"state": "Florida", "cases": 7574590},
    {"state": "Newyork", "cases": 6794738},
    {"state": "Illinois", "cases": 4083292},
    {"state": "Pennsylvania", "cases": 3527754},
    {"state": "North Carolina", "cases": 3472644},
    {"state": "Ohio", "cases": 3400652},
    {"state": "Georgia", "cases": 3068208},
    {"state": "Michigan", "cases": 3064125}
]

states = [entry["state"] for entry in covid_data]
cases = [entry["cases"] for entry in covid_data]

state_colors = {
    'California': 'blue',
    'Texas': 'red',
    'Florida': 'green',
    'Newyork': 'yellow',
    'Illinois': 'purple',
    'Pennsylvania': 'orange',
    'North Carolina': 'cyan',
    'Ohio': 'magenta',
    'Georgia': 'lime',
    'Michigan': 'pink'
}

plt.style.use('dark_background')

fig, ax = plt.subplots()

ax.bar(states, cases, color=[state_colors[state] for state in states])

ax.set_title("Corona Patients in the 10 Biggest States")
ax.set_xlabel("States")
ax.set_ylabel("Number of Cases (in millions)")

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()
