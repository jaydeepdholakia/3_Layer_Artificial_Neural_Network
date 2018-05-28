import numpy as np

#sigmoid function
def sigmoid(x,deriv=False):
	if (deriv==True):
		return x*(1-x)

	return 1/(1+np.exp(-x))

#input data
X = np.array([[0,0,1],
			  [0,1,1],
			  [1,0,1],
			  [1,1,1]])

#output data
Y = np.array([[0],
			  [1],
			  [1],
			  [0]])



#synapses (weights)
sy0 = 2*np.random.random((3,4))-1
sy1 = 2*np.random.random((4,1))-1

#training step
for j in range(60000):
	
	#layers
	l0 = X
	l1 = sigmoid(np.dot(l0,sy0))
	l2 = sigmoid(np.dot(l1,sy1))

	l2_error = Y - l2

	#printing errors
	if(j % 10000) == 0:
		print("Error: "+str(np.mean(np.abs(l2_error))))

	l2_delta = l2_error*sigmoid(l2,deriv=True)

	l1_error = l2_delta.dot(sy1.T)

	l1_delta = l1_error*sigmoid(l1,deriv=True)

	#update weights
	sy1 += l1.T.dot(l2_delta)
	sy0 += l0.T.dot(l1_delta)

print("Output after training is: ")
print(np.round(l2))