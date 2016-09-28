# author: Hendrik Werner s4549775
# author Constantin Blach s4329872

import itertools

from numpy import array

# assignment 2.3.1
data = array([2, 3, 6, 8, 11, 18])

# assignment 2.3.1 i
print("(i)")
m = data.mean()
print("mean = {}".format(m))
standard_deviation = data.std()
print("standard deviation = {}".format(standard_deviation))

# assignment 2.3.1 ii
print("\n(ii)")
combinations_of_2 = list(itertools.combinations(data, 2))
print("Combinations of two aliens:\n{}".format(combinations_of_2))
combinations_of_2_with_mean = [(array(c).mean(), c) for c in combinations_of_2]
print("Combinations of two aliens with their mean:\n{}".format(combinations_of_2_with_mean))
combinations_of_4 = list(itertools.combinations(data, 4))
print("Combinations of two aliens:\n{}".format(combinations_of_4))
combinations_of_4_with_mean = [(array(c).mean(), c) for c in combinations_of_4]
print("Combinations of two aliens with their mean:\n{}".format(combinations_of_4_with_mean))
