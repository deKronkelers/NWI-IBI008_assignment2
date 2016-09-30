# author: Hendrik Werner s4549775
# author: Constantin Blach s4329872
# some code is taken from ex2_1_1.py

import itertools

from mpl_toolkits.mplot3d import Axes3D
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
W = np.dot(X, np.transpose(V[:, :4])) + means
show_first_10(W)

# make a matrix of scatter plots of each combination of two principal
# components for PC1-PC4 against each other
principal_components = [(i, X[:, i]) for i in range(4)]
pc_combinations = list(itertools.combinations(principal_components, 2))
f, grid = plt.subplots(2, 3)
for i, combination in enumerate(pc_combinations):
    pc1 = combination[0][1]
    pc1_nr = combination[0][0]
    pc2 = combination[1][1]
    pc2_nr = combination[1][0]
    s = grid[i // 3, i % 3]
    s.set_title("PC{} against PC{}". format(pc1_nr, pc2_nr))
    s.set_xlabel("PC{}".format(pc1_nr))
    s.set_ylabel("PC{}".format(pc2_nr))
    s.scatter(pc1, pc2)
plt.tight_layout()
show()

# make a 3-dimensional scatter plot of three principal components PC1-PC3
# plot elements belonging to different class in different colors
fig = plt.figure()
ax3D = fig.add_subplot(111, projection="3d")
for i in range(y_filtered.shape[1]):
    if y_filtered[0, i] == 0:
        ax3D.scatter(
            np.array(principal_components[0][1][i]),
            np.array(principal_components[1][1][i]),
            np.array(principal_components[2][1][i]),
            c="r"
        )
    else:
        ax3D.scatter(
            np.array(principal_components[0][1][i]),
            np.array(principal_components[1][1][i]),
            np.array(principal_components[2][1][i]),
            c="b"
        )
show()
