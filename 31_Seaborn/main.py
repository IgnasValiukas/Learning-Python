import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset('mpg')
print(mpg.head(10).to_string())
print(mpg.shape)

# 1
sns.histplot(mpg['acceleration'])
plt.show()

# 2
sns.histplot(mpg['displacement'])
plt.show()

# 3
sns.histplot(mpg, x='cylinders', hue='cylinders', palette='Set1', discrete=True, legend=False)
plt.show()

# 4
sns.histplot(mpg, x='model_year', hue='model_year', palette='Set1', discrete=True, legend=False)
plt.show()

# 5
sns.histplot(mpg, x='origin', hue='origin', legend=False)
plt.show()

# 6
sns.barplot(mpg, x='origin', y='displacement', hue='origin', legend=False)
plt.show()

# 7
sns.scatterplot(mpg, x='displacement', y='acceleration', hue='origin', size='cylinders')
plt.show()

# 8
sns.pairplot(mpg, hue='origin')
plt.show()

# 9
sns.boxplot(mpg, x='origin', y='mpg', hue='origin')
plt.show()

# 10
corr = mpg.corr(numeric_only=True)
print(corr)
sns.heatmap(corr, annot=True)
plt.show()

# 11
data = sns.FacetGrid(mpg, col='origin')
data.map(sns.scatterplot, 'acceleration', 'cylinders')
plt.show()