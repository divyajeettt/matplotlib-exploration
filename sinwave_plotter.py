import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

################################################################################

def plot_sinwave(n):
    global angle

    plt.cla()
    plt.grid(True)

    plt.plot([0, angle+10], zeroes, color="black", linewidth=3)
    plt.plot(zeroes, [-1, 1], color="black", linewidth=3)

    x_axis.append(angle)

    sinwave.append(math.sin(angle))
    plt.plot(x_axis, sinwave, color="red", linewidth=1.5)
    plt.plot([x_axis[-1]], [sinwave[-1]], color="black", marker="o")

    # coswave.append(math.cos(angle))
    # plt.plot(x_axis, coswave, color="blue", linewidth=1.5)
    # plt.plot([x_axis[-1]], [coswave[-1]], color="black", marker="o")

    angle += 0.05

################################################################################

angle, zeroes = 0, [0, 0]
x_axis, sinwave, coswave = [], [], []

animate_components = FuncAnimation(plt.gcf(), plot_sinwave, interval=50)

plt.grid(True)
plt.show()