from typing import Callable
import matplotlib.pyplot as plt
import numpy as np
import math

################################################################################

# CONSTANTS
R: float = 10.0
A: float = 10.0
B: float = 5.0

################################################################################

# generate a large list of inputs
dx: float = 0.015
ANGLES: np.ndarray = np.arange(0, 8*np.pi + dx, dx)

################################################################################

GRAPHS_TO_PLOT: set[Callable[[float], float]] = {
    # (lambda x: R),         # Circle

    ############################################################################

    # (lambda x: A*B / math.hypot(A*math.sin(x), B*math.cos(x))),  # Ellipse - 1
    # (lambda x: A*B / math.hypot(B*math.sin(x), A*math.cos(x))),  # Ellipse - 2

    ############################################################################

    # (lambda x: A * x),                             # Archimedean Spiral
    # (lambda x: A * math.exp(x/10)),                # Logarithmic Spiral
    # (lambda x: (math.nan if not x else A / x)),    # Hyperbolic/Inverse Spiral
    # (lambda x: A * math.sqrt(x)),                  # Parabolic Spiral

    ############################################################################

    # (lambda x: R + A*math.sin(x)),                 # Cardiod - 1
    # (lambda x: R + A*math.cos(x)),                 # Cardiod - 2
    # (lambda x: R - A*math.sin(x)),                 # Cardiod - 3
    # (lambda x: R - A*math.cos(x)),                 # Cardiod - 4

    ############################################################################

    # (lambda x: A * math.cos(3*x)),                 # Rose Curve - 3 petals
    # (lambda x: A * math.cos(4*x)),                 # Rose Curve - 4 petals
    # (lambda x: A * math.cos(5*x)),                 # Rose Curve - 5 petals
    # (lambda x: A * math.cos(6*x)),                 # Rose Curve - 6 petals
}

plt.axes(projection="polar")

for function in GRAPHS_TO_PLOT:
    for theta in ANGLES:
        plt.polar(theta, function(theta), marker=".", color="black")

if not GRAPHS_TO_PLOT:
    print("No graphs to plot")
else:
    plt.show()