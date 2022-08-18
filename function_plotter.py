import matplotlib.pyplot as plt
import numpy as np
import math

################################################################################

# generate a large list of inputs
dx: float = 0.025
X_AXIS: np.ndarray = np.arange(-200, 200+dx, dx)

# INF is the tolerance for infinity
# numbers not -INF <= x <= INF will be considered INFINITY
INF: float = 100

################################################################################

GRAPHS_TO_PLOT: dict[str, np.ndarray|list[float]] = {
    # "sin(x)": np.sin(X_AXIS),
    # "sin(2x)": np.sin(2 * X_AXIS),
    # "2sin(x)": np.sin(X_AXIS) * 2,
    # "½sin(x)": np.sin(X_AXIS) / 2,
    # "sin²(x)": np.sin(X_AXIS) ** 2,
    # "sin³(x)": np.sin(X_AXIS) ** 3,

    ############################################################################

    # "cos(x)": np.cos(X_AXIS),
    # "cos(2x)": np.cos(2 * X_AXIS),
    # "2cos(x)": np.cos(X_AXIS) * 2,
    # "½cos(x)": np.cos(X_AXIS) / 2,
    # "cos²(x)": np.cos(X_AXIS) ** 2,
    # "cos³(x)": np.cos(X_AXIS) ** 3,

    ############################################################################

    # "tan(x)": np.tan(X_AXIS),
    # "tan(2x)": np.tan(2 * X_AXIS),
    # "2tan(x)": np.tan(X_AXIS) * 2,
    # "½tan(x)": np.tan(X_AXIS) / 2,
    # "tan²(x)": np.tan(X_AXIS) ** 2,
    # "tan³(x)": np.tan(X_AXIS) ** 3,

    ############################################################################

    # "csc(x)": 1 / np.sin(X_AXIS),
    # "sec(x)": 1 / np.cos(X_AXIS),
    # "cot(x)": 1 / np.tan(X_AXIS),

    ############################################################################

    # "sin⁻¹(x)": [math.asin(x) if -1 <= x <= 1 else math.nan for x in X_AXIS],
    # "cos⁻¹(x)": [math.acos(x) if -1 <= x <= 1 else math.nan for x in X_AXIS],
    # "tan⁻¹(x)": [math.atan(x) for x in X_AXIS],
    # "csc⁻¹(x)": [
    #     math.asin(1 / x) if -1 <= 1/x <= 1 else math.nan for x in X_AXIS
    # ],
    # "sec⁻¹(x)": [
    #     math.acos(1 / x) if -1 <= 1/x <= 1 else math.nan for x in X_AXIS
    # ],
    # "cot⁻¹(x)": [math.pi/2 - math.atan(x) for x in X_AXIS],

    ############################################################################

    # "sinh(x)": np.sinh(X_AXIS),
    # "cosh(x)": np.cosh(X_AXIS),
    # "tanh(x)": np.tanh(X_AXIS),

    ############################################################################

    # "x⁻²": 1 / np.square(X_AXIS),
    # "x⁻¹": 1 / X_AXIS,
    # "x⁰": X_AXIS ** 0,
    # "x": X_AXIS,
    # "x²": np.square(X_AXIS),
    # "x³": X_AXIS ** 3,
    # "√x": np.sqrt(X_AXIS),
    # "∛x": np.cbrt(X_AXIS),

    ############################################################################

    # "eˣ": np.exp(X_AXIS),
    # "logₑx": np.log(X_AXIS),
    # "e⁻ˣ²": np.exp(-np.square(X_AXIS)),
    # "x¹′ˣ": np.fabs(X_AXIS) ** (1 / np.fabs(X_AXIS)),

    ############################################################################

    # "|x|": np.fabs(X_AXIS),
    # "[x]": np.sign(X_AXIS),
    # "{x}": X_AXIS - np.floor(X_AXIS),
    # "⌈x⌉": np.ceil(X_AXIS),
    # "⌊x⌋": np.floor(X_AXIS),

    ############################################################################

    # "erf(x)": [math.erf(x) for x in X_AXIS],
    # "erfc(x)": [math.erfc(x) for x in X_AXIS],

    ############################################################################

    # "50": 50 * X_AXIS**0,
    # "2x + 3": 2*X_AXIS + 3,
    # "x² + x - 2": X_AXIS**2 + X_AXIS - 2,
    # "x³ - x² - 4x + 4": X_AXIS**3 - X_AXIS**2 - 4*X_AXIS + 4,

    ############################################################################

    # "|sin(x)|": np.fabs(np.sin(X_AXIS)),
    # "|cos(x)|": np.fabs(np.cos(X_AXIS)),
    # "|tan(x)|": np.fabs(np.tan(X_AXIS)),

    # "sin⁻¹(sin(x))": [math.asin(math.sin(x)) for x in X_AXIS],
    # "cos⁻¹(cos(x))": [math.acos(math.cos(x)) for x in X_AXIS],
    # "tan⁻¹(tan(x))": [
    #     math.atan(math.tan(x)) if math.tan(x) <= 100 else math.nan
    #     for x in X_AXIS
    # ],

    # "xsin(x)": X_AXIS * np.sin(X_AXIS),
    # "xcos(x)": X_AXIS * np.cos(X_AXIS),
    # "xtan(x)": X_AXIS * np.tan(X_AXIS),

    # "sin(x) + cos(x)": np.sin(X_AXIS) + np.cos(X_AXIS),
    # "sin(x) - cos(x)": np.sin(X_AXIS) - np.cos(X_AXIS),
    # "-sin(x) + cos(x)": -np.sin(X_AXIS) + np.cos(X_AXIS),
    # "-sin(x) - cos(x)": -np.sin(X_AXIS) - np.cos(X_AXIS),

    # "x⁻¹sin(x)": np.sin(X_AXIS) / X_AXIS,
    # "x⁻¹cos(x)": np.cos(X_AXIS) / X_AXIS,
    # "x⁻¹tan(x)": np.tan(X_AXIS) / X_AXIS,

    # "x|x|": X_AXIS * np.fabs(X_AXIS),
    # "x²|x|": np.fabs(X_AXIS) * X_AXIS**2,
}

plt.figure(figsize=(10, 5))
plt.axhline(y=0, color="black", linewidth=3)
plt.axvline(x=0, color="black", linewidth=3)

limited: set[str] = {
    "tan(x)", "tan(2x)", "2tan(x)", "½tan(x)", "tan²(x)", "tan³(x)", "cot(x)",
    "csc(x)", "sec(x)", "|tan(x)|", "xtan(x)", "x⁻¹tan(x)"
}

for func, y_axis in GRAPHS_TO_PLOT.items():
    if func in limited:
        y_axis[y_axis > INF], y_axis[y_axis < -INF] = np.inf, -np.inf

    plt.plot(X_AXIS, y_axis, label=f"y = {func}", linewidth=2)

# plt.plot(
#     np.arange(-64*np.pi, 65*np.pi, np.pi), np.zeros(129),
#     marker="o", color="black"
# )

if not GRAPHS_TO_PLOT:
    print("No graphs to plot")
else:
    plt.grid(True)
    plt.legend()
    plt.show()
