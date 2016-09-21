# author: Hendrik Werner s4549775
# author Constantin Blach s4329872

from pylab import *
from scipy.stats.mstats import zscore
import scipy.io

# assignment 2.1.1
wine_data = scipy.io.loadmat("wine.mat")
attribute_names = wine_data["attributeNames"]

columns = [wine_data["X"][:, i] for i in range(12)]
f = figure()
for i, values in enumerate(columns):
    s = f.add_subplot(1, 12, i + 1)
    s.hist(values)
    s.set_title(attribute_names[0, i][0])
    s1 = f.add_subplot(2, 12, i + 1)
    s1.boxplot(zscore(values))
    s1.set_title(attribute_names[0, i][0])
    i += 1
show()

# assignment 2.1.2
