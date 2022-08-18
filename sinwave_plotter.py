import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

################################################################################

def plot_sinwave(n: int) -> None:
    global angle

    plt.cla()
    plt.grid(True)

    plt.plot([0, angle+5], zeroes, color="black", linewidth=2.5)
    plt.plot(zeroes, values, color="black", linewidth=2.5)

    x_axis.append(angle)

    sinwave.append(math.sin(angle))
    plt.plot(x_axis, sinwave, color="red", linewidth=1.5)
    plt.plot([x_axis[-1]], [sinwave[-1]], color="black", marker="o")

    coswave.append(math.cos(angle))
    plt.plot(x_axis, coswave, color="blue", linewidth=1.5)
    plt.plot([x_axis[-1]], [coswave[-1]], color="black", marker="o")

    angle += 0.05

################################################################################

angle: float = 0.0
zeroes: list[int, int] = [0, 0]
values: list[int, int] = [-1, 1]

x_axis: list[float] = []
sinwave: list[float] = []
coswave: list[float] = []

print("Enter the interval for refreshing the plot (in ms)")
print("Ideally, the interval should be between 10-50")
interval: float = float(input(">>> "))

if interval < 0:
    print("Invalid interval (negative)")
else:
    animate_components = FuncAnimation(plt.gcf(), plot_sinwave, interval=interval)
    plt.grid(True)
    plt.show()
