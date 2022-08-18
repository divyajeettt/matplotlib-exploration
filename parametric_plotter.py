import matplotlib.pyplot as plt
import numpy as np

################################################################################

# CONSTANTS
r = 10
a, b = 10, 5
k1, k2 = 3, 2
def sec(x):
    return 1 / np.cos(x)

################################################################################

# generate a large list of inputs (floats)
t = theta = np.arange(-450, 450.015625, 0.015625)

################################################################################

graphs_to_plot = {
    # # Heart Shape
    # "(16sin³t, 13cost - 5cos2t - 2cos3t - cos4t)": (
    #     16 * np.sin(t)**3,
    #     13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
    # ),

    ############################################################################

    # # Kite Shape
    # "(rcos³t, rsin³t)": (r * np.cos(t)**3, r * np.sin(t)**3),

    ############################################################################

    # # Lissajous Curve
    # "(acosk₁t, bsink₂t)": (a * np.cos(k1*t), b * np.sin(k2*t)),

    ############################################################################

    # # Cycloid
    # "(r(t - sint), r(1 - cost))": (r * (t - np.sin(t)), r * (1 - np.cos(t))),

    ############################################################################

    # # Parabola - 1
    # "(at², 2at)": (a * t**2, 2*a*t),

    # # Parabola - 2
    # "(-at², 2at)": (-a * t**2, 2*a*t),

    # # Parabola - 3
    # "(2at, at²)": (2*a*t, a * t**2),

    # # Parabola - 4
    # "(2at, -at²)": (2*a*t, -a * t**2),

    ############################################################################

    # # Circle
    # "(rcosθ, rsinθ)": (r * np.cos(theta), r * np.sin(theta)),

    ############################################################################

    # # Infinity Symbol - 1
    # "(rsinθ, rsin2θ)": (r * np.sin(theta), r * np.sin(2*theta)),

    # # Infinity Symbol - 2
    # "(rsin2θ, rsinθ)": (r * np.sin(2*theta), r * np.sin(theta)),

    ############################################################################

    # # Ellipse - 1
    # "(acosθ, bsinθ)": (a * np.cos(theta), b * np.sin(theta)),

    # # Ellipse - 2
    # "(bcosθ, asinθ)": (b * np.cos(theta), a * np.sin(theta)),

    ############################################################################

    # # Hyperbola - 1
    # "(asecθ, btanθ)": (a * sec(theta), b * np.tan(theta)),

    # # Hyperbola - 2
    # "(btanθ, asecθ)": (b * np.tan(theta), a * sec(theta)),
}

plt.figure(figsize=(10, 5))
plt.axhline(y=0, color="black", linewidth=2)
plt.axvline(x=0, color="black", linewidth=2)

for name, (x, y) in graphs_to_plot.items():
    plt.plot(x, y, marker=".", label=name)

if not graphs_to_plot:
    print("No graphs to plot")
else:
    plt.grid(True)
    plt.legend()
    plt.show()