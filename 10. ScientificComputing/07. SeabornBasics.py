# The Seaborn graphics library is built on top of Matplotlib, and it provides functions for generating graphs
# that are useful when working with statistics and data analysis

# The Seaborn library distinguishes itself from the underlying Matplotlib library in that it provides polished 
# higher-level graph functions for a specific application domain, namely, statistical analysis and data visualization.


'''
							1. INTRODUCTION to Seaborn
'''
# Installing Seabon 
pip3 install seaborn

# Importing Seaborn
In [1]: import seaborn as sns

# To get started using the Seaborn library, we first set a style for the graphs it produces using the sns.set function.
In [2]: sns.set(style="darkgrid") # produces graphs with a gray background



'''
							2. kdeplot and distplot
'''


# kdeplot and distplot, which plot a kernel-density estimate plot and a histogram plot with a 
# kernel-density estimate overlaid on top of the histogram, respectively.
In [2]: sns.distplot(df_temp.to_period("M")["outdoor"]["2014-04"].dropna().values, bins=50);
   ...: sns.distplot(df_temp.to_period("M")["indoor"]["2014-04"].dropna().values, bins=50);

# The kdeplot function can also operate on two-dimensional data, showing a contour graph of the joint 
# kernel-density estimate. Relatedly, we can use the jointplot function to plot the joint distribution 
# for two separate datasets.

In [3]: sns.kdeplot(df_temp.resample("H").mean()["outdoor"].dropna().values,
   ...:             df_temp.resample("H").mean()["indoor"].dropna().values, shade=False)
In [4]: with sns.axes_style("white"):
   ...:     sns.jointplot(df_temp.resample("H").mean()["outdoor"].values,
   ...:                   df_temp.resample("H").mean()["indoor"].values, kind="hex")


'''
							3. boxplot and violin plot
'''

# The seaborn library also provides functions for working with categorical data. A simple example of a graph 
# type that is often useful for datasets with categorical variables is the standard boxplot for visualizing 
# the descriptive statistics (min, max, median, and quartiles) of a dataset.

# An interesting twist on the standard boxplot is violin plot, in which the kernel-density estimate is shown
# in the width of boxplot. The boxplot and violinplot functions can be used to produce such graphs
In [5]: fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
   ...: sns.boxplot(df_temp.dropna(), ax=ax1, palette="pastel")
   ...: sns.violinplot(df_temp.dropna(), ax=ax2, palette="pastel")

In [6]: sns.violinplot(x=df_temp.dropna().index.month,
   ...:                y=df_temp.dropna().outdoor, color="skyblue");



'''
								4. Heat Map
'''

# The Seaborn library provides the function heatmap for generating this type of graphs.
In [7]: df_temp["month"] = df_temp.index.month
   ...: df_temp["hour"] = df_temp.index.hour
In [8]: table = pd.pivot_table(df_temp, values='outdoor', index=['month'], columns=['hour'],
   ...:                        aggfunc=np.mean)

In [9]: fig, ax = plt.subplots(1, 1, figsize=(8, 4))
   ...: sns.heatmap(table, ax=ax)


