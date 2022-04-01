# Matplotlib is a Python library for publication-quality 2D and 3D graphics, with support for a variety 
# of different output formats.

'''
					1. Introduction Matplotlib
'''
# Matplotlib actually provides multiple entry points into the library, with different APIs:
#		- a stateful API 
#		- object-oriented API


# Importing object-oriented API
import matplotlib as mpl # imports the main Matplotlib module
import matplotlib.pyplot as plt # for convenient access to the submodule matplotlib.pyplot 
from mpl_toolkits.mplot3d.axes3d import Axes3D

GRAPH_AXIS = """
- A graph in Matplotlib is structured in terms of a Figure instance and one or more Axes instances within the figure. 
- The Figure instance provides a canvas area for drawing, and the 
- Axes instances provide coordinate systems that are assigned to fixed regions of the total figure canvas. 
- The Axes instance provides a coordinate system that can be used to plot data in a variety of plot styles, 
including line graphs, scatter plots, bar plots, and many other styles.
"""

EXAMPLE_1 = """
graph the function y(x) = x**3 + 5x**2 + 10, together with its first and second derivatives, over
the range x ∈ [−5, 2].
"""
# STEP 1: create NumPy arrays for the x range 
import numpy as np
x = np.linspace(-5, 2, 100)
# STEP 2: compute the three functions we want to graph.
y1 = x**3 + 5*x**2 + 10
y2 = 3*x**2 + 10*x
y3 = 6*x + 10
# STEP 3:  create Matplotlib Figure and Axes instances, 
fig, ax = plt.subplots()
# STEP 4: use the plot method of the Axes instance to plot the data,
ax.plot(x, y1, color="blue", label="y(x)")
ax.plot(x, y2, color="red", label="y'(x)")
ax.plot(x, y3, color="green", label="y”(x)")
# STEP 5: set basic graph properties such as x and y axis labels, using the set_xlabel and set_ylabel methods 
ax.set_xlabel("x")
ax.set_ylabel("y")
# STEP 6: generating a legend using the legend method.
ax.legend()

# To create the actual graphs, we use ax.plot, 
# which takes as first and second arguments NumPy arrays with numerical data for the x and y values of the graph, 
# We also used the optional color arguments to specify the color of each line 
# and label keyword to assign a text label to each line.


# matplotlib backend
# Matplotlib provides backends for generating graphics in different formats (e.g., PNG, PDF, Postscript, and SVG
# A variety of different widget toolkits (e.g., Qt, GTK, wxWidgets, and Cocoa for Mac

# use the function mpl.use, to select which backend to use:
import matplotlib as mpl
mpl.use('qt4agg') # select the Qt4Agg backend
import matplotlib.pyplot as plt


'''
					2. Figure
'''
""" 
Figure object is used to providing a canvas on which, Axes instances can be placed, 
It also provides methods for performing actions on figures, 
and it has several attributes that can be used to configure the properties of a figure.
"""
FIGURE_OBJECT = '''
Figure object is created using the function plt.figure. 

optional keyword arguments:
	- figsize - accepts a tuple (width, height), specifying the width and height of the figure canvas in inches. 
	- facecolor - specify the color of the figure canvas

Figure Object Methods:
	- add_axes - create a new Axes instance and assign it to a region on the figure canvas. 
		*mandatory argument: 
			- list containing the coordinates of the lower-left corner and the width and height of the Axes 
			  in the figure canvas coordinate system, on the format (left, bottom, width, height).
			  The coordinates and the width and height of the Axes object are expressed as fractions of 
			  total canvas width and height;

		* keyword arguments:
			- facecolor - background color for the Axes object

	- suptitle - set an overall figure title. Accepts String

	- savefig  - save a figure to a file
		* mandatory argument: takes a string with the output filename

		* other args:
			- format - output format, Options: (PNG, PDF, EPS, and SVG formats)
			- dpi - resolution of the generated image
			- transparent - boolean argument (True, False), make figure canvas transparent 

'''	
# EXAMPLE:
fig = plt.figure(figsize=(8, 2.5), facecolor="#f1f1f1")
# axes coordinates as fractions of the canvas width and height
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes((left, bottom, width, height), facecolor="#e1e1e1")

x = np.linspace(-2, 2, 1000)
y1 = np.cos(40 * x)
y2 = np.exp(-x**2)
ax.plot(x, y1 * y2)
ax.plot(x, y2, 'g')
ax.plot(x, -y2, 'g')
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.savefig("graph.png", dpi=100, facecolor="#f1f1f1")


'''
					3. Axes
'''

