# 3_Layer_Artificial_Neural_Network

A ANN (Artificial Neural Network) for predicting the output based on our input data and training data.

## Overview
Here I have coded a 3 layer Neural Network in Python (to be specific version 3.6).

# Pre-requisites to be installed
Python 3.6 and Anaconda

## Working
I take a 3 by 4 array as an input X and take Y as a 4 by 1 array that is the output that we want our program to predict.

Then we assign synapses which are nothing but weights (Learn how a neuron works [here](https://www.youtube.com/watch?v=XJ7HLz9VYz0&list=PLRqwX-V7Uu6aCibgK1PTWWu9by6XFdCfh)). We take random values for it.

Then inside a for loop which repeats for 60000 times, we take 1st layer as our input X.

In second layer we calculate the sigmoid of multiplication (dot product) of 1st layer and 1st weight. Learn more about finding sigmoid and how it work [here](https://excel.ucf.edu/classes/2007/Spring/appsII/Chapter1.pdf) It really helped me in learning it much clearer.

Then in the third and the last layer we do same as above but take sigmoid of the dot product of layer 2 and weight 2.

Now as the last layer is the final output we need to see how much is our final output differs from what we want. By subtracting it from Y. That is our error of layer 3.

We then get the delta of layer 3 (Check the code for how it's done). Here we calculate how much does it differ from that instance called Gradient.

Now we get the error of layer 2nd and same get the delta of it.

After that, we update our weights called as Backpropagation.

After it repeats 60000 times you get the prediction which you print it out and if you want to get more accurate the just roundoff it.
