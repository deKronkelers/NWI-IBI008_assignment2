# author: Hendrik Werner s4549775
# author Constantin Blach s4329872

import scipy.io
from pylab import *
from scipy.stats.mstats import zscore

# assignment 2.1.1
wine_data = scipy.io.loadmat("./data/wine.mat")
attribute_names = wine_data["attributeNames"]
attribute_units = [
    "g/dm^3", "g/dm^3", "g/dm^3", "g/dm^3", "g/dm^3", "mg/dm^3", "mg/dm^3",
    "g/cm^3", "pH", "g/dm^3", "% vol.", "0-10"
]

columns = [wine_data["X"][:, i] for i in range(12)]
f, grid = plt.subplots(2, 12)
for i, values in enumerate(columns):
    attribute_name = attribute_names[0, i][0]
    x_label = attribute_units[i]
    y_label = "Number of data points"
    s = grid[0, i]
    s.set_title(attribute_name)
    s.hist(values)
    s.set_xlabel(x_label)
    if i == 0:
        s.set_ylabel(y_label)
    s = grid[1, i]
    s.boxplot(zscore(values))
    s.set_xlabel(x_label)
    if i == 0:
        s.set_ylabel(y_label)
show()


# remove outliers
def remove_outliers(values, expected_value, factor=10):
    return np.array(list(filter(lambda value: value < expected_value * factor, values)))


volatile_acidity_filtered = remove_outliers(columns[1], 2)
density_filtered = remove_outliers(columns[7], 1)
alcohol_filtered = remove_outliers(columns[10], 5)

filtered_attributes = [(1, volatile_acidity_filtered), (7, density_filtered),
                       (10, alcohol_filtered)]

f2, grid = plt.subplots(2, 3)
y_label = "Number of data points"
for x in range(3):
    attribute = filtered_attributes[x]
    attribute_name = attribute_names[0, attribute[0]][0]
    x_label = "{} in {}".format(attribute_name, attribute_units[attribute[0]])
    s = grid[0, x]
    s.set_title(attribute_name)
    s.hist(columns[attribute[0]])
    s.set_xlabel(x_label)
    s.set_ylabel(y_label)
    s = grid[1, x]
    s.hist(attribute[1])
    s.set_xlabel(x_label)
    s.set_ylabel(y_label)

plt.tight_layout()
show()

# assignment 2.1.2
