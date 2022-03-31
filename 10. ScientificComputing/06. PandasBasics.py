'''
- This library provides convenient data structures for representing series and tables of data and makes it easy 
	to transform, split, merge, and convert data. 
- These are important steps in the process of cleansing raw data into a tidy form that is suitable for analysis. 

- The Pandas library builds on top of NumPy and complements it with features that are particularly useful 
	when handling data, such as labeled indexing, hierarchical, indices, 
	alignment of data for comparison and merging of datasets, handling of missing data, and much more.
'''

'''
							1. Introduction to Panda
'''
# 1.1 Importing Modules

import pandas as pd

## 1.2 Panda Data Structures
# Series objects - Represents series data 
# DataFrame objects - Represents tabular data


'''
							2. Series
'''
# The merit of being able to index a data series with labels rather than integers is apparent even in the simplest. 
# Displaying the object in IPython reveals the data of the Series object together with the corresponding indices
In [1]: import pandas as pd
In [2]: s = pd.Series([909976, 8615246, 2872086, 2273305])
In [3]: s
Out[3]: 0     909976
        1     8615246
        2     2872086
        3     2273305
        dtype: int64

# Using the index and values attributes, we can extract the underlying data for the index and the values stored in 
# the series:
In [4]: list(s.index)
Out[4]: [0, 1, 2, 3]
In [5]: s.index
Out[5]: RangeIndex(start=0, stop=4, step=1)
In [6]: s.values
Out[6]: array([ 909976, 8615246, 2872086, 2273305], dtype=int64)


# With a Series object this is possible, and we can assign the index attribute of a Series object to a list 
# with new indices to accomplish this. 
# We can also set the name attribute of the Series object, to give it a descriptive name:
In [7]: s.index = ["Stockholm", "London", "Rome", "Paris"]
In [8]: s.name = "Population"
In [9]: s
Out[9]: Stockholm     909976
         London       8615246
         Rome         2872086
         Paris        2273305
         Name: Population, dtype: int64


# We can also set the index and name attributes through keyword arguments to the Series object when it is created:
In [10]: s = pd.Series([909976, 8615246, 2872086, 2273305], name="Population",
    ...:               index=["Stockholm", "London", "Rome", "Paris"])


# We can access elements in a Series by indexing with the corresponding index (label)
In [11]: s["London"]
Out[11]: 8615246

# or directly through an attribute with the same name as the index, if the index label is a valid Python symbol name
In [12]: s.Stockholm
Out[12]: 909976

# Indexing a Series object with a list of indices gives a new Series object with a subset of the original data 
In [13]: s[["Paris", "Rome"]]
Out[13]: Paris    2273305
         Rome     2872086
         Name: Population, dtype: int64


# we can easily compute descriptive statistics using the Series methods: 
statistics_series_method = '''
count 	- the number of data points

median 	- calculate the median 

mean 	- calculate the mean value 

std 	- calculate the standard deviation 

min and max - minimum and maximum values 

quantile 	- calculating quantiles
'''

In [14]: s.median(), s.mean(), s.std()
Out[14]: (2572695.5, 3667653.25, 3399048.5005155364)

In [15]: s.min(), s.max()
Out[15]: (909976, 8615246)

In [16]: s.quantile(q=0.25), s.quantile(q=0.5), s.quantile(q=0.75)
Out[16]: (1932472.75, 2572695.5, 4307876.0)

# All of the preceding data are combined in the output of the describe method, which provides a summary of 
# the data represented by a Series object
In [17]: s.describe()
Out[17]: count          4.000000
         mean     3667653.250000
         std      3399048.500516
         min       909976.000000
         25%      1932472.750000
         50%      2572695.500000
         75%      4307876.000000
         max      8615246.000000
         Name: Population, dtype: float64


'''
							3. DataFrame
'''
'''
For higher-dimensional arrays (mainly two-dimensional arrays, or tables), the corresponding data structure 
is the Pandas DataFrame object. 
It can be viewed as a collection of Series objects with a common index.
'''

# Initialize a DataFrame by passing a nested Python list to the constructor of the DataFrame object.
In [18]: df = pd.DataFrame([[909976, "Sweden"],
    ...:                    [8615246, "United Kingdom"],
    ...:                    [2872086, "Italy"],
    ...:                    [2273305, "France"]])
In [19]: df
Out[19]: 
         0               1
0   909976          Sweden
1  8615246  United Kingdom
2  2872086           Italy
3  2273305          France

# we can use labeled indexing for rows by assigning a sequence of labels to the index attribute, and, in addition, 
# we can set the columns attribute to a sequence of labels for the columns:
In [20]: df.index = ["Stockholm", "London", "Rome", "Paris"]
In [21]: df.columns = ["Population", "State"]
In [22]: df
Out[22]: 
           Population           State
Stockholm      909976          Sweden
London        8615246  United Kingdom
Rome          2872086           Italy
Paris         2273305          France


# The index and columns attributes can also be set using the corresponding keyword arguments to the DataFrame 
# object when it is created:
In [23]: df = pd.DataFrame([[909976, "Sweden"],
    ...:                    [8615246, "United Kingdom"],
    ...:                    [2872086, "Italy"],
    ...:                    [2273305, "France"]],
    ...:                   index=["Stockholm", "London", "Rome", "Paris"],
    ...:                   columns=["Population", "State"])

# An alternative way to create the same data frame, which sometimes can be more convenient, 
# is to pass a dictionary with column titles as keys and column data as values:
In [24]: df = pd.DataFrame({"Population": [909976, 8615246, 2872086, 2273305],
    ...:                    "State": ["Sweden", "United Kingdom", "Italy", "France"]},
    ...:                   index=["Stockholm", "London", "Rome", "Paris"])

# Each column in a data frame can be accessed using the column name as attribute or 
# by indexing with the column label
In [25]: df.Population
Out[25]: Stockholm     909976
         London       8615246
         Rome         2872086
         Paris        2273305
         Name: Population, dtype: int64

# Rows of a DataFrame instance can be accessed using the loc indexer attribute.
In [26]: df.loc["Stockholm"]
Out[26]: Population    909976
         State         Sweden
         Name: Stockholm, dtype: object

# Passing a list of row labels to the loc indexer results in a new DataFrame that is a subset of the original 
# DataFrame, containing only the selected rows
In [27]: df.loc[["Paris", "Rome"]]
Out[27]: 
       Population   State
Paris     2273305  France
Rome      2872086   Italy

# The loc indexer can also be used to select both rows and columns simultaneously, by first passing a row label 
# (or a list thereof ) and second a column label (or a list thereof ).
In [28]: df.loc[["Paris", "Rome"], "Population"]
Out[28]: 
Paris    2273305
Rome     2872086
Name: Population, dtype: int64

# We can compute descriptive statistics using the methods (mean, std, median, min, max, etc.) for a DataFrame, 
# the calculation is performed for each column with numerical data types:
In [29]: df.mean()
Out[29]: Population    3667653.25
         dtype: float64


# Using the DataFrame method info and the attribute dtypes, we can obtain a summary of the content 
# in a DataFrame and the data types of each column:
In [30]: df.info()                                                              
<class 'pandas.core.frame.DataFrame'>
Index: 4 entries, Stockholm to Paris
Data columns (total 2 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   Population  4 non-null      int64 
 1   State       4 non-null      object
dtypes: int64(1), object(1)
memory usage: 256.0+ bytes



'''
							4. Read csv file into DataFrame."
'''
# The pandas library supports numerous methods for reading data from files of different formats. 
# we use the read_csv function to read in data and create a DataFrame object from a CSV file.
read_csv_useful_args = """
header 		- specifies which row, if any, contains a header with column names 

skiprows 	- number of rows to skip before starting to read data, or a list of line numbers of lines to skip 

delimiter 	- the character that is used as a delimiter between column values 

encoding 	- the name of the encoding used in the file, e.g., utf-8 

nrows 		- number of rows to read
"""
# The first and only mandatory argument to the pd.read_csv function is a filename or a URL to the data source.
In [31]: df_diamond = pd.read_csv('files/diamonds.csv')

# the header is by default taken from the first line. However, we could also write out all these options explicitly:
In [32]: df_diamond = pd.read_csv("files/diamonds.csv", delimiter=",", encoding="utf-8", header=0)

In [33]: df_diamond.info()                                                       
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 53940 entries, 0 to 53939
Data columns (total 11 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   Unnamed: 0  53940 non-null  int64  
 1   carat       53940 non-null  float64
 2   cut         53940 non-null  object 
 3   color       53940 non-null  object 
 4   clarity     53940 non-null  object 
 5   depth       53940 non-null  float64
 6   table       53940 non-null  float64
 7   price       53940 non-null  int64  
 8   x           53940 non-null  float64
 9   y           53940 non-null  float64
 10  z           53940 non-null  float64
dtypes: float64(6), int64(2), object(3)
memory usage: 4.5+ MB


'''It is informative to display a tabular view of the data. However, this dataset is too large to display in full,
the head and tail methods are handy for creating a truncated dataset containing the first few and last few rows, 
respectively. 
Both of these functions take an optional argument that specifies how many rows to include in the truncated
DataFrame. Note also that df.head(n) is equivalent to df[:n], where n is an integer.
'''
In [34]: df_diamond.head()
Out[34]: 
   Unnamed: 0  carat      cut color clarity  ...  table  price     x     y     z
0           1   0.23    Ideal     E     SI2  ...   55.0    326  3.95  3.98  2.43
1           2   0.21  Premium     E     SI1  ...   61.0    326  3.89  3.84  2.31
2           3   0.23     Good     E     VS1  ...   65.0    327  4.05  4.07  2.31
3           4   0.29  Premium     I     VS2  ...   58.0    334  4.20  4.23  2.63
4           5   0.31     Good     J     SI2  ...   58.0    335  4.34  4.35  2.75

[5 rows x 11 columns]


# we can create new columns and update columns in a DataFrame simply by assigning a Series object to the DataFrame 
# indexed by the column name, 
# we can delete columns using the Python del keyword.
# The apply method creates and returns a new Series object for which a function passed to apply has been applied 
# to each element in the original column.

# Example: Using the same method, we also tidy up the State values by removing extra white spaces in 
# its elements using the string method strip.
In [41]: df_pop["State"].values[:3]  # contains extra white spaces
Out[41]: array([' United Kingdom', ' Germany', ' Spain'], dtype=object)
In [42]: df_pop["State"] = df_pop["State"].apply(lambda x: x.strip())
In [43]: df_pop.head()
Out[43]:


# Inspecting the data types of the columns
In [35]: df_diamond.dtypes                                                                                        
Out[35]: 
Unnamed: 0      int64
carat         float64
cut            object
color          object
clarity        object
depth         float64
table         float64
price           int64
x             float64
y             float64
z             float64
dtype: object

# We can change the index to one of the columns of the DataFrame using the set_index method, 
# which takes as argument the name of the column to use as index. 
# The result is a new DataFrame object, and the original DataFrame is unchanged.
In [36]:  df_diamond2 = df_diamond.set_index('carat')

# using the sort_index method, we can sort the data frame with respect to the index:
In [37]: df_diamond2 = df_diamond2.sort_index()                                                                  

In [38]: df_diamond2.head()                                                                                      
Out[38]: 
       Unnamed: 0      cut color clarity  depth  table  price     x     y     z
carat                                                                          
0.2         31594  Premium     E     VS2   61.1   59.0    367  3.81  3.78  2.32
0.2         31598    Ideal     D     VS2   61.5   57.0    367  3.81  3.77  2.33
0.2         31597  Premium     F     VS2   62.6   59.0    367  3.73  3.71  2.33
0.2         31596    Ideal     E     VS2   59.7   55.0    367  3.86  3.84  2.30
0.2         31595  Premium     E     VS2   59.7   62.0    367  3.84  3.80  2.28


# The sort_index method also accepts a list of column names, in which case a hierarchical index is created. 
# A hierarchical index uses tuples of index labels to address rows in the data frame. 
# We can use the sort_index method with the integer-valued argument level,
In [39]: df_diamond3 = df_diamond.set_index(["carat", "cut"]).sort_index(level=0)
In [40]: df_diamond3.head(7)
Out[41]: 
               Unnamed: 0 color clarity  depth  table  price     x     y     z
carat cut                                                                     
0.2   Ideal         31596     E     VS2   59.7   55.0    367  3.86  3.84  2.30
      Ideal         31598     D     VS2   61.5   57.0    367  3.81  3.77  2.33
      Ideal         31600     E     VS2   62.2   57.0    367  3.76  3.73  2.33
      Premium          15     E     SI2   60.2   62.0    345  3.79  3.75  2.27
      Premium       31592     E     VS2   59.8   62.0    367  3.79  3.77  2.26
      Premium       31593     E     VS2   59.0   60.0    367  3.81  3.78  2.24
      Premium       31594     E     VS2   61.1   59.0    367  3.81  3.78  2.32



# A DataFrame with a hierarchical index can be partially indexed using only its 
# zeroth level index (df_diamond3.loc[0.31]) or 
# completely indexed using a tuple of all hierarchical indices (df_diamond3.loc[(0.31, "Ideal")]):
In [42]: df_diamond3.loc[(0.31, "Ideal")]                                                                                       
Out[42]: 
             Unnamed: 0 color clarity  depth  table  price     x     y     z
carat cut                                                                   
0.31  Ideal          14     J     SI2   62.2   54.0    344  4.35  4.37  2.71
      Ideal         731     I    VVS1   61.6   55.0    557  4.36  4.41  2.70
      Ideal         732     I    VVS1   61.3   56.0    557  4.36  4.38  2.68
      Ideal         733     I    VVS1   62.3   54.0    557  4.37  4.40  2.73
      Ideal         734     I    VVS1   62.0   54.0    557  4.37  4.40  2.72
...                 ...   ...     ...    ...    ...    ...   ...   ...   ...
      Ideal       51641     G     VS2   62.2   56.0    544  4.31  4.34  2.69
      Ideal       51646     I    VVS2   61.6   57.0    544  4.35  4.39  2.69
      Ideal       51980     E     SI1   61.5   55.0    547  4.39  4.42  2.71
      Ideal       52309     D     SI1   61.9   57.0    548  4.36  4.39  2.71
      Ideal       52310     D     SI1   62.3   56.0    548  4.32  4.35  2.70

[1209 rows x 9 columns]


'''If we want to sort by a column rather than the index, we can use the sort_values method. 
It takes a column name, or a list of column names, with respect to which the DataFrame is to be sorted. 
It also accepts the keyword argument ascending, which is a Boolean or a list of Boolean values that specifies 
whether the corresponding column is to be sorted in ascending or descending order:
'''
In [43]: df_diamond.set_index("carat").sort_values(["cut", "price"], ascending=[False, True]).head()
Out[43]:
       Unnamed: 0        cut color clarity  depth  table  price     x     y     z
carat                                                                            
0.24            6  Very Good     J    VVS2   62.8   57.0    336  3.94  3.96  2.48
0.24            7  Very Good     I    VVS1   62.3   57.0    336  3.95  3.98  2.47
0.26            8  Very Good     H     SI1   61.9   55.0    337  4.07  4.11  2.53
0.23           10  Very Good     H     VS1   59.4   61.0    338  4.00  4.05  2.39
0.30           20  Very Good     J     SI1   62.7   59.0    351  4.21  4.27  2.66


# With categorical data such as the State column, it is frequently of interest to summarize how many values of 
# each category a column contains. Such counts can be computed using the value_counts method
# (of the Series object).
In [44]: colorcount = df_diamond['color'].value_counts()
In [45]: colorcount.head()
Out[45]: 
G    11292
E     9797
F     9542
H     8304
D     6775
Name: color, dtype: int64


# Sum of Price of Each Carat
In [46]: df_diamond3 = df_diamond[["carat", "price"]].set_index(["carat"])
In [47]: df_diamond4 = df_diamond3.sum(level="carat").sort_values("price", ascending=False)
In [48]: df_diamond4.head(10)
Out[48]:
          price
carat          
1.01   12346191
1.51    8509528
1.00    8166397
1.50    7975437
2.01    6483459

'''we can obtain the same results using the groupby method, which allows us to group rows of a DataFrame 
by the values of a given column, and apply a reduction function on the resulting object (e.g., sum, mean, min, 
max, etc.). The result is a new DataFrame with the grouped-by column as index. '''
In [31]: df_diamond5 = (df_diamond.drop(['depth', 'table', 'x', 'y', 'z'], axis=1).groupby("carat")
    ...: .sum().sort_values("price", ascending=False))                                           

In [32]: df_diamond5.head(10)                                                                                                            
Out[32]: 
       Unnamed: 0     price
carat                      
1.01     27871030  12346191
1.51     17615735   8509528
1.00     18402415   8166397
1.50     16702037   7975437
2.01     11211999   6483459
0.90     11383715   5849684
0.70     73206754   4984338
1.02     10939284   4943443
1.20     10167637   4310670
1.52      8301897   4042500

# Note that here we also used the drop method to remove the depth, table, price, x, y, z column, 
# hence the axis=1, use axis=0 to drop rows) from the DataFrame (since it is not meaningful
# to aggregate the colums by summation)


'''
							5. Time Series
'''
# Time series are a common form of data in which a quantity is given, for example, at
# regularly or irregularly spaced timestamps or for fixed or variable time spans (periods).

# Using pandas time-series indexers, DatetimeIndex and PeriodIndex, we can carry out many common date, 
# time, period, and calendar operations, such as selecting time ranges and shifting and resampling of
# the data points in a time series.

# 


