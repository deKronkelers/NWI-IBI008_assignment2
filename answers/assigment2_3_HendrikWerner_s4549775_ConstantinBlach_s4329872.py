# author: Hendrik Werner s4549775
# author Constantin Blach s4329872

from numpy import array

# assignment 2.3.1
data = array([2, 3, 6, 8, 11, 18])

# assignment 2.3.1 i
print("(i)")
m = data.mean()
print("mean = {}".format(m))
standard_deviation = data.std()
print("standard deviation = {}".format(standard_deviation))
