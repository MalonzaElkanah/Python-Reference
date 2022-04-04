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

'''
The Axes object is central to most plotting activities with the Matplotlib library.
1. Provides the coordinate system in which we can plot data and mathematical functions,
2. Contains the axis objects that determine where the axis labels and the axis ticks are placed. 
3. Methods of this Axes class used for drawing different types of plots. 
'''
# Matplotlib provides several different Axes layout managers, which create and place Axes instances within
# a figure canvas following different strategies. Example:


# the plt.subplots function
# This can fill a figure with a grid of Axes instances,  specified by using the first and the second arguments,
# alternatively with the nrows and ncols arguments.
subplots_ARGS = '''
nrows and ncols 	- fill a figure with a grid of Axes instances 

sharex and sharey	- specify that columns/rows should share x and y axes, which can be set to True or False.

fig_kw and subplot_kw - Accepts dictionaries with keyword arguments that are used when creating the 
						Figure and Axes instances, respectively. This allows us to set the properties of 
						the Figure/Axes object.
'''

EXAMPLE_2 = """
To generate a grid of Axes instances in a newly created Figure object, 
with three rows and two columns 
"""
fig, axes = plt.subplots(nrows=3, ncols=2)
# Function plt.subplots returns a tuple (fig, axes), where fig is a Figure instance and axes
# is a NumPy array of size (nrows, ncols)


'''
			3.2 Plot Types
'''
# Matplotlib implements many types of plotting techniques as methods of the Axes object.
PLOT_TYPES = '''
Axes.plot 		- draws curves in the coordinate system provided

Axes.step 
Axes.bar 
Axes.hist
Axes.errorbar 
Axes.scatter 
Axes.fill_between 
Axes.quiver

'''
# All plotting functions in Matplotlib expect data as NumPy arrays as input, 
# typically as arrays with x and y coordinates as the first and second arguments.



'''
		3.3 Line Properties
'''
# In line plots, we frequently need to configure properties of the lines in the graph, I.E the line width, 
# color, and style(solid, dashed, dotted,..). This is achieved by with keyword arguments to the plot methods

Basic_Line_Properties_ARGUMENTS = """
color  	-	A color specification can be a string with a color name, such as“red,” “blue,” etc., or 
			a RGB color code on the form “#aabbcc.” A color specification. 

alpha 	-	The amount of transparency. Float number between 0.0(completely transparent) and 1.0(completely opaque). 

linewidth, lw	- The width of a line. Float number. 

linestyle, ls	- The style of the line, i.e., whether the line is to be drawn as a solid/dotted/dashed.	
					“-” – solid
					“--” – dashed
					“:” – dotted
					“.-” – dash-dotted 

marker 		- 	Each data point, whether or not it is connected with adjacent data points, can be represented with a
				marker symbol as specified with this argument.
 				+, o, * = cross, circle, star
				s = square
				. = small dot
				1, 2, 3, 4, ... = triangle-shaped symbols with different angles. 

markersize 	-	The marker size. Float number. 

markerfacecolor 	-	The fill color for the marker. Color specification (see in the preceding text). 

markeredgewidth 	-	The line width of the marker edge. Float number. 

markeredgecolor 	- 	The marker edge color. Color specification (see above). 

"""

x = np.linspace(-5, 5, 5)
y = np.ones_like(x)

def axes_settings(fig, ax, title, ymax):
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(0, ymax+1)
    ax.set_title(title)
    
fig, axes = plt.subplots(1, 4, figsize=(16,3))

# Line width
linewidths = [0.5, 1.0, 2.0, 4.0]
for n, linewidth in enumerate(linewidths):
    axes[0].plot(x, y + n, color="blue", linewidth=linewidth)
axes_settings(fig, axes[0], "linewidth", len(linewidths))

# Line style
linestyles = ['-', '-.', ':']
for n, linestyle in enumerate(linestyles):
	axes[1].plot(x, y + n, color="blue", lw=2, linestyle=linestyle)
# custom dash style
line, = axes[1].plot(x, y + 3, color="blue", lw=2)
length1, gap1, length2, gap2 = 10, 7, 20, 7
line.set_dashes([length1, gap1, length2, gap2])
axes_settings(fig, axes[1], "linetypes", len(linestyles) + 1)

# marker types
markers = ['+', 'o', '*', 's', '.', '1', '2', '3', '4']
for n, marker in enumerate(markers):
	# lw = shorthand for linewidth, ls = shorthand for linestyle
	axes[2].plot(x, y + n, color="blue", lw=2, ls='*', marker=marker)
axes_settings(fig, axes[2], "markers", len(markers))

# marker size and color
markersizecolors = [(4, "white"), (8, "red"), (12, "yellow"), (16, "lightgreen")]
for n, (markersize, markerfacecolor) in enumerate(markersizecolors):
	axes[3].plot(x, y + n, color="blue", lw=1, ls='-', marker='o', markersize=markersize, 
		markerfacecolor=markerfacecolor, markeredgewidth=2)
axes_settings(fig, axes[3], "marker size/color", len(markersizecolors))


'''
		3.4 Legends
'''
# legend may be added to an Axes instance in a Matplotlib figure using the legend method.
# Only lines with assigned labels are included in the legend (the label argument of Axes.plot to assign a label) 
# The legend method accepts a large number of optional arguments.

LEGEND_ARGS = '''
loc 	 - specify where in the Axes area the legend is to be added: 
			loc=1 for upper-right corner, loc=2 for upper-left corner, 
			loc=3 for the lower-left corner, and loc=4 for lower-right corner,

bbox_to_anchor	- makes the legend can be placed at an arbitrary location within the figure canvas. 
					Accepts tuple in the form (x, y), where x and y are the canvas coordinates within the Axes object. 
					(0, 0) corresponds to the lower-left corner, and (1, 1) corresponds to the upper-right corner. 
					If x and y can be smaller than 0 and larger than 1 the legend is to be placed outside the Axes area


ncols 	- splits the legend labels into multiple columns,

'''

ax.legend(ncol=4, loc=3, bbox_to_anchor=(0, 1))

'''
		3.5 Text Formatting and Annotations
'''

'''Matplotlib provides several ways of configuring font properties. 
- The default values can be set in the Matplotlib resource file, and 
- Session-wide configuration can be set in the mpl.rcParams dictionary
- On a case-to-case basis, by passing a set of standard keyword arguments to functions that create text labels in a graph.
'''
Example_3 = '''
The following example demonstrates how to add text labels and annotations to a
Matplotlib figure using ax.text and ax.annotate, as well as how to render a text label
that includes an equation that is typeset in LaTeX.
'''

fig, ax = plt.subplots(figsize=(12, 3))
ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(-0.5, 3.5)
ax.set_ylim(-0.05, 0.25)
ax.axhline(0)
# text label
ax.text(0, 0.1, "Text label", fontsize=14, family="serif")
# annotation
ax.plot(1, 0, "o")
ax.annotate("Annotation", fontsize=14, family="serif", xy=(1, 0), xycoords="data", xytext=(+20, +50), 
	textcoords="offset points", arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.5"))

# equation
ax.text(2, 0.1, r"Equation: $i\hbar\partial_t \Psi = \hat{H}\Psi$", fontsize=14, family="serif")


Font_Properties_Arguments = '''
fontsize 			- The size of the font, in points.

family or fontname 	- The font type.

backgroundcolor 	- Color specification for the background color of the text label.

color 		- Color specification for the font color.

alpha 		- Transparency of the font color.

rotation 	- Rotation angle of the text label.
'''


'''
			3.6 Axis Properties
'''
'''
A two-dimensional graph has two axis objects: for the horizontal x axis and the vertical y axis. 
Each axis can be individually configured with respect to attributes such as 
the axis labels, the placement of ticks and the tick labels, and the location and appearance of the axis itself.
'''


'''
		# Axis Labels and Titles
'''
# We can set the axis labels using the set_xlabel and set_ylabel methods:
	# they both take a string with the label as first arguments. In addition, 
	# the optional labelpad argument specifies the spacing, in units of points, from the axis to the label.
	# additional arguments for setting text properties, such as color, fontsize, and fontname

# we can also set a title of an Axes object, using the set_title method.

x = np.linspace(0, 50, 500)
y = np.sin(x) * np.exp(-x/10)
fig, ax = plt.subplots(figsize=(8, 2), subplot_kw={'facecolor':"#ebf5ff"})

ax.plot(x, y, lw=2)
ax.set_xlabel("x", labelpad=5, fontsize=18, fontname='serif', color="blue")
ax.set_ylabel("f(x)", labelpad=15, fontsize=18, fontname='serif', color="blue")
ax.set_title("axis labels and title example", fontsize=16, fontname='serif', color="blue")


'''
	# Axis Range
'''
# the set_xlim and set_ylim sets the range of the x and y axes of a Matplotlib.
	# take two arguments that specify the lower and upper limit that is to be displayed on the axis, respectively.

# the axis method, accepts the string argument 
	# 'tight', for a coordinate range that tightly fit the lines it contains, and 
	# 'equal', for a coordinate range where one unit length along each axis corresponds to the same number of pixels (i.e., a ratio preserving coordinate system).

# the autoscale method to selectively turn on and off autoscaling, 
	# by passing True and False as first argument, 
	# for the x and/or y axis by setting its axis argument to 'x', 'y', or 'both'.	

x = np.linspace(0, 30, 500)
y = np.sin(x) * np.exp(-x/10)

fig, axes = plt.subplots(1, 3, figsize=(9, 3), subplot_kw={'facecolor': "#ebf5ff"})

axes[0].plot(x, y, lw=2)
axes[0].set_xlim(-5, 35)
axes[0].set_ylim(-1, 1)
axes[0].set_title("set_xlim / set_y_lim")

axes[1].plot(x, y, lw=2)
axes[1].axis('tight')
axes[1].set_title("axis('tight')")

axes[2].plot(x, y, lw=2)
axes[2].axis('equal')
axes[2].set_title("axis('equal')")


'''
	# Axis Ticks, Tick Labels, and Grids
'''

# Matplotlib module mpl.ticker provides a general and extensible tick management system 
# Matplotlib distinguishes between major ticks and minor ticks. 
	# major tick - By default, has a corresponding label, while
	# minor ticks that do not have labels and they marh distances between major ticks
x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
y = np.sin(x) * np.exp(-x**2/20)

fig, axes = plt.subplots(1, 4, figsize=(12, 3))

axes[0].plot(x, y, lw=2)
axes[0].set_title("default ticks")

axes[1].plot(x, y, lw=2)
axes[1].set_title("set_xticks")
axes[1].set_yticks([-1, 0, 1])
axes[1].set_xticks([-5, 0, 5])

axes[2].plot(x, y, lw=2)
axes[2].set_title("set_major_locator")
axes[2].xaxis.set_major_locator(mpl.ticker.MaxNLocator(4))
axes[2].yaxis.set_major_locator(mpl.ticker.FixedLocator([-1, 0, 1]))
axes[2].xaxis.set_minor_locator(mpl.ticker.MaxNLocator(8))

axes[2].yaxis.set_minor_locator(mpl.ticker.MaxNLocator(8))
axes[3].plot(x, y, lw=2)
axes[3].set_title("set_xticklabels")
axes[3].set_yticks([-1, 0, 1])
axes[3].set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
axes[3].set_xticklabels([r'$-2\pi$', r'$-\pi$', 0, r'$\pi$', r'$2\pi$'])

x_minor_ticker = mpl.ticker.FixedLocator([-3 * np.pi / 2, -np.pi / 2, 0,

np.pi / 2, 3 * np.pi / 2])
axes[3].xaxis.set_minor_locator(x_minor_ticker)
axes[3].yaxis.set_minor_locator(mpl.ticker.MaxNLocator(4))



# Grid
# We can turn on axis grids using the grid method of an axes object which takes optional keyword arguments: 
	# color, linestyle, and linewidth, for specifying the properties of the grid lines. 
	# axis that can be assigned values 'major', 'minor', or 'both', and 'x', 'y', or 'both', respectively.

ig, axes = plt.subplots(1, 3, figsize=(12, 4))
x_major_ticker = mpl.ticker.MultipleLocator(4)
x_minor_ticker = mpl.ticker.MultipleLocator(1)
y_major_ticker = mpl.ticker.MultipleLocator(0.5)
y_minor_ticker = mpl.ticker.MultipleLocator(0.25)

for ax in axes:
    ax.plot(x, y, lw=2)
    ax.xaxis.set_major_locator(x_major_ticker)
	ax.yaxis.set_major_locator(y_major_ticker)
	ax.xaxis.set_minor_locator(x_minor_ticker)
	ax.yaxis.set_minor_locator(y_minor_ticker)

axes[0].set_title("default grid")
axes[0].grid()
axes[1].set_title("major/minor grid")
axes[1].grid(color="blue", which="both", linestyle=':', linewidth=0.5)

axes[2].set_title("individual x/y major/minor grid")
axes[2].grid(color="grey", which="major", axis='x', linestyle='-', linewidth=0.5)
axes[2].grid(color="grey", which="minor", axis='x', linestyle=':', linewidth=0.25)
axes[2].grid(color="grey", which="major", axis='y', linestyle='-', linewidth=0.5)




