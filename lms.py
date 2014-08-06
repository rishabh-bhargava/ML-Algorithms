import numpy as np


##########################################################################
# X is list of numpy arrays where each array is feature variable (input)
# Y is a list of numbers where each number is a target variable (output)
# alpha is the step size
##########################################################################
def least_mean_squares(x, y, alpha):

	x = np.concatenate((np.ones((len(x), 1)), x), axis = 1)

	size_x = x[0].shape[0]
	theta = np.zeros(size_x)

	#error = 0.0001
	iterate = 0 

	while iterate < 10000:
		for j in xrange(size_x):
			thetaj_sum = 0
			for i, point in enumerate(x):
				thetaj_sum += (np.dot(point, theta) - y[i]) * point[j]
			theta[j] -= alpha*thetaj_sum
		iterate+=1

	return theta

x_test = []
x_test.append(np.array([1]))
x_test.append(np.array([2]))
x_test.append(np.array([3]))
x_test.append(np.array([4]))

y_test = [1, 3, 3, 7]

alpha = 0.01

print x_test

print least_mean_squares(x_test, y_test, alpha)