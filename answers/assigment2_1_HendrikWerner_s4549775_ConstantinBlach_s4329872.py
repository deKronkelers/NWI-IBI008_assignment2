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

filtered_attributes = [(1, volatile_acidity_filtered, "g/dm^3"), (7, density_filtered, "g/cm^3"),
                       (10, alcohol_filtered, "%vol")]

f2, grid = plt.subplots(2, 3)
y_label = "Number of data points"
for x in range(3):
    attribute = filtered_attributes[x]
    attribute_name = attribute_names[0, attribute[0]][0]
    s = grid[0, x]
    s.set_title(attribute_name)
    s.hist(columns[attribute[0]])
    s.set_xlabel("{} in {}".format(attribute_name, attribute[2]))
    s.set_ylabel(y_label)
    s = grid[1, x]
    s.hist(attribute[1])
    s.set_xlabel("{} in {}".format(attribute_name, attribute[2]))
    s.set_ylabel(y_label)

plt.tight_layout()
show()

# assignment 2.1.2
