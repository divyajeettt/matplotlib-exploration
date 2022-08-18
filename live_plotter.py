import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

################################################################################

def more_data(n: int) -> None:
    plt.cla()
    plt.grid(True)

    plt.plot(x_values, y_values, color="blue")
    plt.axhline(y=0, color="black", linewidth=2)
    plt.axvline(x=0, color="black", linewidth=2)

    x_values.append(n)
    y_values.append(random.randint(-n*10, n*10))

################################################################################

x_values: list[int] = []
y_values: list[int] = []

print("Enter the interval for refreshing the plot (in ms)")
print("Ideally, the interval should be between 50-70")
interval: float = float(input(">>> "))

if interval < 0:
    print("Invalid interval (negative)")
else:
    animate = FuncAnimation(plt.gcf(), more_data, interval=50)
    plt.show()