import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

bitcoin_data = pd.read_csv("BTC-USD.csv")
bitcoin_open_prices = bitcoin_data["Open"]

fig, ax = plt.subplots()
x_values, y_values = [], []
line, = ax.plot([], [], 'b-')

ax.set_xlim(0, len(bitcoin_open_prices))
ax.set_ylim(np.min(bitcoin_open_prices), np.max(bitcoin_open_prices))

def init():
    return line,

def update(frame):
    if frame < len(bitcoin_open_prices) - 1:
        x_values.append(frame)
        y_values.append(bitcoin_open_prices[frame])
        line.set_data(x_values, y_values)
    return line,

animation = FuncAnimation(fig, update, frames=np.arange(len(bitcoin_open_prices)),
                          init_func=init, blit=True, interval=5)

plt.show()
