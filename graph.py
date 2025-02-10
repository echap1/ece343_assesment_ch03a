import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

x_min = 0
x_max = 30
y_min = -1.1
y_max = 1.1

V = 0.19
beta = 1.1
omega = 6
alpha = 0.05

z = np.arange(x_min, x_max, (x_max - x_min) / 1000)

top = np.array(V * np.exp(alpha * z))
bottom = np.array(V * (-np.exp(alpha * z)))

fig, ax = plt.subplots()

periods = 4
frames_per_period = 30
frames = periods * frames_per_period


def animate(i):
    ax.clear()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    t = (i / frames_per_period) * (2 * np.pi / omega)
    v = np.array(V * np.exp(alpha * z) * np.cos(omega*t + beta*z))
    line, = ax.plot(z, v, color='blue', lw=1)
    line2, = ax.plot(z, top, color='black', lw=1, linestyle='--')
    line3, = ax.plot(z, bottom, color='black', lw=1, linestyle='--')
    return line, line2, line3


ani = FuncAnimation(fig, animate, frames=frames)
ani.save("wave.gif", dpi=150, writer=PillowWriter(fps=25))
