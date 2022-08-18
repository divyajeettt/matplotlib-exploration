import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np

################################################################################

# generate a large list of inputs
X: np.ndarray = np.arange(-200, 200.5, 0.5)
Y: np.ndarray = X

X_AXIS: np.ndarray
Y_AXIS: np.ndarray
X_AXIS, Y_AXIS = np.meshgrid(X, Y)

################################################################################

GRAPHS_TO_PLOT: dict[str, np.ndarray] = {
    # "x + y": X_AXIS + Y_AXIS,
    # "x - y": X_AXIS - Y_AXIS,
    # "xy": X_AXIS * Y_AXIS,
    # "x / y": X_AXIS / Y_AXIS,

    ############################################################################

    # "|x| + |y|": np.fabs(X_AXIS) + np.fabs(Y_AXIS),
    # "|x| - |y|": np.fabs(X_AXIS) - np.fabs(Y_AXIS),
    # "|x||y|": np.fabs(X_AXIS) * np.fabs(Y_AXIS),
    # "|x| / |y|": np.fabs(X_AXIS) / np.fabs(Y_AXIS),

    ############################################################################

    # "x² + y²": X_AXIS**2 + Y_AXIS**2,
    # "x² - y²": X_AXIS**2 - Y_AXIS**2,
    # "√(x² + y²)": np.sqrt(X_AXIS**2 + Y_AXIS**2),
    # "√(x² - y²)": np.sqrt(X_AXIS**2 - Y_AXIS**2),

    ############################################################################

    # "x³ + y³": X_AXIS**3 + Y_AXIS**3,
    # "x³ - y³": X_AXIS**3 - Y_AXIS**3,
    # "∛(x³ + y³)": np.cbrt(X_AXIS**3 + Y_AXIS**3),
    # "∛(x³ - y³)": np.cbrt(X_AXIS**3 - Y_AXIS**3),

    ############################################################################

    # "log(x) + log(y)": np.log(X_AXIS) + np.log(Y_AXIS),
    # "log(x) - log(y)": np.log(X_AXIS) - np.log(Y_AXIS),

    ############################################################################

    # "1 - |x+y| - |y-x|": 1 - np.fabs(X_AXIS+Y_AXIS) - np.fabs(Y_AXIS-X_AXIS),
    # "1 - |y|": 1 - np.fabs(Y_AXIS),
    # "1 - |x|": 1 - np.fabs(X_AXIS),
}

ax: plt.axes = plt.axes(projection="3d")

patches: list[mp.Patch] = []
colors: list[str] = len(GRAPHS_TO_PLOT) * [
    "red", "orange", "green", "blue", "purple", "cyan", "magenta", "yellow"
]

for func, z_axis in GRAPHS_TO_PLOT.items():
    ax.plot_surface(X_AXIS, Y_AXIS, z_axis, color=colors[0])
    patches.append(mp.Patch(color=colors[0], label=f"z = {func}"))
    colors.pop(0)

if not GRAPHS_TO_PLOT:
    print("No graphs to plot")
else:
    ax.legend(handles=patches)
    plt.show()