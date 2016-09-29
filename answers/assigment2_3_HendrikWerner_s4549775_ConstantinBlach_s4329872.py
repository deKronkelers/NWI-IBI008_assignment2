# author: Hendrik Werner s4549775
# author Constantin Blach s4329872

import itertools

from pylab import *

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
print("Combinations of four aliens:\n{}".format(combinations_of_4))
combinations_of_4_with_mean = [(array(c).mean(), c) for c in combinations_of_4]
print("Combinations of four aliens with their mean:\n{}".format(combinations_of_4_with_mean))

# assignment 2.3.1 iii
print("\n(iii)")
combinations_of_2_means = array([mc[0] for mc in combinations_of_2_with_mean])
mx_2 = combinations_of_2_means.mean()
print("mx for combinations of 2:\n{}".format(mx_2))
sigmax_2 = combinations_of_2_means.std()
print("sigmax for combinations of 2:\n{}".format(sigmax_2))
combinations_of_4_means = array([mc[0] for mc in combinations_of_4_with_mean])
mx_4 = combinations_of_4_means.mean()
print("mx for combinations of 4:\n{}".format(mx_4))
sigmax_4 = combinations_of_4_means.std()
print("sigmax for combinations of 4:\n{}".format(sigmax_4))


# assignment 2.3.1 iv
def approximate_sigmax_crude(n):
    return standard_deviation / n ** .5


def approximate_sigmax_good(m, n):
    return (standard_deviation / n ** .5) * ((m - n) / (m - 1)) ** .5


print("\n(iv)")
print("Crude approximation of sigmax for n=2: {}".format(approximate_sigmax_crude(2)))
print("Good approximation of sigmax for n=2: {}".format(approximate_sigmax_good(len(data), 2)))
print("Crude approximation of sigmax for n=4: {}".format(approximate_sigmax_crude(4)))
print("Good approximation of sigmax for n=4: {}".format(approximate_sigmax_good(len(data), 4)))

# assignment 2.3.1 v
f, grid = plt.subplots(1, 3)
for i, data_set in enumerate([
    ("Population", data),
    ("Sample means n=2", combinations_of_2_means),
    ("Sample means n=4", combinations_of_4_means)
]):
    s = grid[i]
    s.hist(data_set[1], bins=range(2, 19))
    s.set_xlabel(data_set[0])
    s.set_ylabel("Number of data points")
plt.tight_layout()
show()
