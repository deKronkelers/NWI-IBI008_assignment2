# author: Hendrik Werner s4549775
# author: Constantin Blach s4329872
# some code is taken from ex2_1_1.py

from pylab import *
from scipy.io import loadmat

# assignment 2.2.1

# Load Matlab data file to python dict structure
mat_data = loadmat('./data/zipdata.mat')

# Extract variables of interest
testdata = mat_data['testdata']
traindata = mat_data['traindata']
X = matrix(traindata[:, 1:])
y = matrix(traindata[:, 0])


def filter_data(data_set, class_index, keep=None):
    if keep is None:
        return
    i = 0
    while i < class_index.shape[1]:
        if class_index[0, i] in keep:
            i += 1
        else:
            data_set = np.delete(data_set, i, 0)
            class_index = np.delete(class_index, i)
    return data_set, class_index


X_filtered, y_filtered = filter_data(X, y, keep=[0, 1])

f, grid = plt.subplots(2, 5)
for i, x in enumerate(X_filtered[:10, :]):
    x = reshape(x, (16, 16))
    s = grid[i // 5, i % 5]
    s.set_title("Image #{}".format(i))
    s.imshow(x, extent=(0, 16, 0, 16), cmap=cm.gray_r)
show()
