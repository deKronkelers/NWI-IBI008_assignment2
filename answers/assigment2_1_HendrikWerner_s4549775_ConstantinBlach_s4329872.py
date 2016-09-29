# author: Hendrik Werner s4549775
# author Constantin Blach s4329872

import scipy.io
from pylab import *
from scipy.stats import pearsonr
from scipy.stats.mstats import zscore

# assignment 2.1.1
wine_data = scipy.io.loadmat("./data/wine.mat")
attribute_names = [nl[0] for nl in wine_data["attributeNames"][0]]

attribute_units = [
    "g/dm^3", "g/dm^3", "g/dm^3", "g/dm^3", "g/dm^3", "mg/dm^3", "mg/dm^3",
    "g/cm^3", "pH", "g/dm^3", "% vol.", "0-10"
]

columns = [wine_data["X"][:, i] for i in range(12)]
f, grid = plt.subplots(2, 12)
for i, values in enumerate(columns):
    attribute_name = attribute_names[i]
    s = grid[0, i]
    s.set_title(attribute_name)
    s.hist(values)
    s.set_xlabel(attribute_units[i])
    if i == 0:
        s.set_ylabel("Number of data points")
    s = grid[1, i]
    s.boxplot(zscore(values))
    s.set_xlabel(attribute_name)
    if i == 0:
        s.set_ylabel("zscores")
show()


# remove outliers
def remove_outliers(values, scores, expected_value, factor=10):
    i = 0
    while i < values.shape[0]:
        if values[i] >= expected_value * factor:
            values = np.delete(values, i)
            scores = np.delete(scores, i)
        else:
            i += 1
    return values, scores


volatile_acidity_filtered, volatile_acidity_scores = remove_outliers(columns[1], list(columns[11]), 2)
density_filtered, density_scores = remove_outliers(columns[7], list(columns[11]), 1)
alcohol_filtered, alcohol_scores = remove_outliers(columns[10], list(columns[11]), 5)

filtered_attributes = [
    (1, volatile_acidity_filtered, volatile_acidity_scores),
    (7, density_filtered, density_scores),
    (10, alcohol_filtered, alcohol_scores)
]

f2, grid = plt.subplots(2, 3)
y_label = "Number of data points"
for x in range(3):
    attribute = filtered_attributes[x]
    attribute_name = attribute_names[attribute[0]]
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
f3, grid = plt.subplots(1, 3)
for i, attribute in enumerate(filtered_attributes):
    attribute_name = attribute_names[attribute[0]]
    s = grid[i]
    s.set_title(attribute_name)
    s.scatter(attribute[1], attribute[2])
    s.set_xlabel("{} in {}".format(attribute_name, attribute_units[attribute[0]]))
    s.set_ylabel(attribute_names[11])
    print(pearsonr(attribute[1], attribute[2]))
plt.tight_layout()
show()
