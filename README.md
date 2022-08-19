# matplotlib-exploration

## About matplotlib-exploration

This repository contains simple projects/scripts that explore the simplest features of Python's [`matplotlib`](https://matplotlib.org/). These include:
- 2-dimensional plotting
- 3-dimensional plotting
- 2-dimensional parametrized plotting
- Plotting in polar coordinates
- Live-data plotting

## Instructions & Run

To use, Clone the repository on your device and navigate to the folder.

### 2-dimensional plotter

[`function_plotter.py`](https://github.com/divyajeettt/matplotlib-exploration/blob/main/function_plotter.py) is a 2-dimensional plotter. \
*Date of creation:* `October 25, 2020`
- Open the file in edit mode
- Un-comment the mathematical functions you want to plot from the dictionary `GRAPHS_TO_PLOT` defined on [Line 17](https://github.com/divyajeettt/matplotlib-exploration/blob/49c40730897c7d4ac72522f17db4d112c2012410/function_plotter.py#L17)
- You may also plot any other mathematical function by adding the following line in the dictionary:
```python
"LABEL": f(X_AXIS),
```
where `"LABEL"` will be displayed on the plot as `y = LABEL`
- Save the file, and execute:
```
python3 function_plotter.py
```

### Plotting in polar coordinates

[`polar_plotter.py`](https://github.com/divyajeettt/matplotlib-exploration/blob/main/polar_plotter.py) is a plotter that plots in polar coordinates. \
*Date of creation:* `October 30, 2020`
- Open the file in edit mode
- Un-comment the mathematical functions you want to plot from the set `GRAPHS_TO_PLOT` defined on [Line 21](https://github.com/divyajeettt/matplotlib-exploration/blob/49c40730897c7d4ac72522f17db4d112c2012410/polar_plotter.py#L21)
- You may also plot any other mathematical function by adding the following line in the set:
```python
(lambda x: f(x)),
```
- Save the file, and execute:
```
python3 polar_plotter.py
```

### 2-dimensional parametrized plotting

[`parametric_plotter.py`](https://github.com/divyajeettt/matplotlib-exploration/blob/main/parametric_plotter.py) is a 2-dimensional parametric plotter. \
*Date of creation:* `November 11, 2020`
- Open the file in edit mode
- Un-comment the mathematical functions you want to plot from the dictionary `GRAPHS_TO_PLOT` defined on [Line 22](https://github.com/divyajeettt/matplotlib-exploration/blob/49c40730897c7d4ac72522f17db4d112c2012410/parametric_plotter.py#L22)
- You may also plot any other mathematical function by adding the following line in the dictionary:
```python
"LABEL": (f(t), g(t)),
```
where `"LABEL"` will be displayed on the plot as `LABEL`
- Save the file, and execute:
```
python3 parametric_plotter.py
```

### 3-dimensional plotter

[`3D_plotter.py`](https://github.com/divyajeettt/matplotlib-exploration/blob/main/3D_plotter.py) is a 3-dimensional plotter. \
*Date of creation:* `November 26, 2020`
- Open the file in edit mode
- Un-comment the mathematical functions you want to plot from the dictionary `GRAPHS_TO_PLOT` defined on [Line 17](https://github.com/divyajeettt/matplotlib-exploration/blob/49c40730897c7d4ac72522f17db4d112c2012410/3D_plotter.py#L17)
- You may also plot any other mathematical function by adding the following line in the dictionary:
```python
"LABEL": f(X_AXIS, Y_AXIS),
```
where `"LABEL"` will be displayed on the plot as `z = LABEL`
- Save the file, and execute:
```
python3 3D_plotter.py
```

### Live-data plotter

[`live_plotter.py`](https://github.com/divyajeettt/matplotlib-exploration/blob/main/live_plotter.py) is a Live-data plotter. The data is randomly generated and refreshed on the screen after each interval (interval is selected by the user). \
*Date of creation:* `December 02, 2020`

Execute:
```
python3 live_plotter.py
```

#### Sine-wave plotter

[`sinewave_plotter.py`](https://github.com/divyajeettt/matplotlib-exploration/blob/main/sinwave_plotter.py) simply plots a sine-wave and a cosine-wave, refreshed on the screen after each interval (interval is selected by the user). \
*Date of creation:* `December 07, 2020`

Execute:
```
python3 sinewave_plotter.py
```

#### Circle plotter

[`circle_plotter.py`](https://github.com/divyajeettt/matplotlib-exploration/blob/main/circle_plotter.py) simply plots a circle, along with the component of the current point on the circle on the axes, refreshed on the screen after each interval (interval is selected by the user). \
*Date of creation:* `December 08, 2020`

Execute:
```
python3 circle_plotter.py
```

## Future Plans

Although some of my other projects do use these features, it would be nice to add the following to this repository:
- Add [subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)
- Add 3-dimensional parametrized plotting
