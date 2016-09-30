# author: Hendrik Werner s4549775
# author: Constantin Blach s4329872
# some code is taken from ex2_1_1.py

from pylab import *
from scipy.io import loadmat

# assignment 2.2.1

# Load Matlab data file to python dict structure
mat_data = loadmat('./data/zipdata.mat')

# create the data matrix X and the class index vector y from the data
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

# remove the digits with the class index 2-9 from the data
X_filtered, y_filtered = filter_data(X, y, keep=[0, 1])


def show_first_10(D):
    f, grid = plt.subplots(2, 5)
    for i, x in enumerate(D[:10, :]):
        x = reshape(x, (16, 16))
        s = grid[i // 5, i % 5]
        s.set_title("Image #{}".format(i))
        s.imshow(x, extent=(0, 16, 0, 16), cmap=cm.gray_r)
    show()

show_first_10(X_filtered)

means = [X_filtered[:, col].mean() for col in range(256)]
Y = X_filtered - np.ones((X_filtered.shape[1])) * means
U, s, Vt = linalg.svd(Y)
V = np.transpose(Vt)

# create a new data matrix X overwriting the old data matrix
X = np.dot(Y, V[:, :4])
W = np.dot(X, np.transpose(V[:, 0:4])) + means
show_first_10(W)
