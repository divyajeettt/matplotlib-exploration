import matplotlib.pyplot as plt
import numpy as np

################################################################################

# CONSTANTS
R: float = 10.0
A: float = 10.0
B: float = 5
K1: float = 3
K2: float = 2

################################################################################

# generate a large list of inputs
dx: float = 0.015
t: np.ndarray = np.arange(-450, 450+dx, dx)
theta: np.ndarray = t

################################################################################

GRAPHS_TO_PLOT: dict[str, tuple[np.ndarray, np.ndarray]] = {
    # # Heart Shape
    # "(16sin³t, 13cost - 5cos2t - 2cos3t - cos4t)": (
    #     16 * np.sin(t)**3,
    #     13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
    # ),

    ############################################################################

    # # Kite Shape
    # "(rcos³t, rsin³t)": (R * np.cos(t)**3, R * np.sin(t)**3),

    ############################################################################

    # # Lissajous Curve
    # "(acosk₁t, bsink₂t)": (A * np.cos(K1*t), B * np.sin(K2*t)),

    ############################################################################

    # # Circle
    # "(rcosθ, rsinθ)": (R*np.cos(theta), R*np.sin(theta)),

    ############################################################################

    # # Cycloid
    # "(r(t - sint), r(1 - cost))": (R*(t-np.sin(t)), R*(1-np.cos(t))),

    ############################################################################

    # "(at², 2at)": (A * t**2, 2*A*t),                            # Parabola - 1
    # "(-at², 2at)": (-A * t**2, 2*A*t),                          # Parabola - 2
    # "(2at, at²)": (2*A*t, A * t**2),                            # Parabola - 3
    # "(2at, -at²)": (2*A*t, -A * t**2),                          # Parabola - 4

    ############################################################################

    # "(rsinθ, rsin2θ)": (R*np.sin(theta), R*np.sin(2*theta)),  # INF Symbol - 1
    # "(rsin2θ, rsinθ)": (R*np.sin(2*theta), R*np.sin(theta)),  # INF Symbol - 2

    ############################################################################

    # "(acosθ, bsinθ)": (A*np.cos(theta), B*np.sin(theta)),        # Ellipse - 1
    # "(bcosθ, asinθ)": (B*np.cos(theta), A*np.sin(theta)),        # Ellipse - 2

    ############################################################################

    # "(asecθ, btanθ)": (A/np.cos(theta), B*np.tan(theta)),      # Hyperbola - 1
    # "(btanθ, asecθ)": (B*np.tan(theta), A/np.cos(theta)),      # Hyperbola - 2
}

plt.figure(figsize=(10, 5))
plt.axhline(y=0, color="black", linewidth=2)
plt.axvline(x=0, color="black", linewidth=2)

for name, (x, y) in GRAPHS_TO_PLOT.items():
    plt.plot(x, y, marker=".", label=name)

if not GRAPHS_TO_PLOT:
    print("No graphs to plot")
else:
    plt.grid(True)
    plt.legend()
    plt.show()