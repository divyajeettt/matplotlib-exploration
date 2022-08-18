import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

################################################################################

def plot_components(n: int) -> None:
    global line_X, line_Y, comp_X, comp_Y, angle

    plt.cla()
    plt.grid(True)

    plt.plot(values, zeroes, color="black", linewidth=3)
    plt.plot(zeroes, values, color="black", linewidth=3)

    plt.plot(circle_X, circle_Y, color="blue", linewidth=2.5)
    plt.plot(comp_X, comp_Y, color="red", linewidth=2, linestyle="--")
    plt.plot(line_X, line_Y, color="black", marker="o")

    curr_X: float = math.cos(angle)
    curr_Y: float = math.sin(angle)

    line_X = [0, curr_X]
    line_Y = [0, curr_Y]

    circle_X.append(curr_X)
    circle_Y.append(curr_Y)

    comp_X = [curr_X, curr_X, curr_X, 0]
    comp_Y = [0, curr_Y, curr_Y, curr_Y]

    angle += 0.025

################################################################################

angle: float = 0.0
zeroes: list[int, int] = [0, 0]
values: list[int, int] = [-1, 1]

line_X: list[float] = []
line_Y: list[float] = []

circle_X: list[float] = []
circle_Y: list[float] = []

comp_X: list[float] = []
comp_Y: list[float] = []

print("Enter the interval for refreshing the plot (in ms)")
print("Ideally, the interval should be between 10-30")
interval: float = float(input(">>> "))

if interval < 0:
    print("Invalid interval (negative)")
else:
    animate_components = FuncAnimation(plt.gcf(), plot_components, interval=interval)
    plt.grid(True)
    plt.show()