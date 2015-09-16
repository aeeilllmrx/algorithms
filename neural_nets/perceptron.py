from random import choice
from numpy import array, dot, random


class Perceptron():

    def __init__(self, eta=0.2, n_weights=3):
        
	self.eta = eta
        self.n_weights = n_weights
        self.w = random.rand(n_weights)

    
    def evaluate(self, result):

        return 1 if result > 0 else 0

    def update_weight(self, x, y):

        result = dot(self.w, x)
        error = y - self.evaluate(result)
        self.w += self.eta * error * x

    def train(self, training_data):
        for i in range(10):
            for x, y in training_data:
                self.update_weight(x, y)

    def predict(self, test_data):    

	for (x, y) in test_data:
    	    r = self.evaluate(dot(self.w, x))
    	    if r == y:
        	tell = "correct!"
    	    else:
        	tell = "wrong!"
            print "{} -- {}: {}".format(x, y, tell)

training_data = [
    (array([10,0,-5]), 0),
    (array([5,1,-3]), 0),
    (array([-6,0,8]), 1),
    (array([-12,7,5]), 1),
]

test_data = [
    (array([99,1,-2]), 0),
    (array([3,0,-1]), 0),
    (array([-5,6,4]), 1),
    (array([-1,0,10]), 1),
]

p = Perceptron()
p.train(training_data)
p.predict(test_data)



