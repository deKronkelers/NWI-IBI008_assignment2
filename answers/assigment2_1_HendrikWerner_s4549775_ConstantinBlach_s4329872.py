# author: Hendrik Werner s4549775
# author Constantin Blach s4329872

import scipy.io
from pylab import *
from scipy.stats.mstats import zscore

# assignment 2.1.1
wine_data = scipy.io.loadmat("./data/wine.mat")
attribute_names = wine_data["attributeNames"]

columns = [wine_data["X"][:, i] for i in range(12)]
f = figure()
for i, values in enumerate(columns):
    s = f.add_subplot(1, 12, i + 1)
    s.hist(values)
    s = f.add_subplot(2, 12, i + 1)
    s.boxplot(zscore(values))
    s.set_title(attribute_names[0, i][0])
show()


# remove outliers
def remove_outliers(values, expected_value, factor=10):
    return np.array(list(filter(lambda value: value < expected_value * factor, values)))


volatile_acidity_filtered = remove_outliers(columns[1], 2)
density_filtered = remove_outliers(columns[7], 1)
alcohol_filtered = remove_outliers(columns[10], 5)

f2 = figure()
j = 1
for i, values in [(1, volatile_acidity_filtered), (7, density_filtered), (10, alcohol_filtered)]:
    s = f2.add_subplot(1, 3, j)
    s.hist(columns[i])
    s = f2.add_subplot(2, 3, j)
    s.hist(values)
    s.set_title(attribute_names[0, i][0])
    j += 1
show()

# assignment 2.1.2
