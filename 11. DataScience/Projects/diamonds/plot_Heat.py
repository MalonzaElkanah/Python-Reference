# Looking at the Shiny Diamonds
# import the pandas and numpy library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read the diamonds CSV file
# build a DataFrame from the data
df = pd.read_csv('diamonds.csv')
# drop the index column
df = df.drop('Unnamed: 0', axis=1)
f, ax = plt.subplots(figsize=(10, 8))
corr = df.corr()
print (corr)
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),
cmap=sns.diverging_palette(220, 10, as_cmap=True),
square=True, ax=ax)
plt.show()
