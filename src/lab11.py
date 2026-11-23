"""Lab 11 starter code: simple neural networks from scratch (perceptron, MLP for XOR)."""
import numpy as np

def train_perceptron(X, y, lr=0.1, epochs=50):
    """y in {0,1}. Return weights w (bias first)."""
    raise NotImplementedError('TODO: implement this')

def perceptron_predict(w, X):
    raise NotImplementedError('TODO: implement this')

def sigmoid(z):
    raise NotImplementedError('TODO: implement this')

def train_mlp(X, y, hidden=4, lr=1.0, epochs=5000, seed=0):
    """One hidden layer, sigmoid units, backprop on MSE. Return params dict."""
    raise NotImplementedError('TODO: implement this')

def mlp_predict(params, X):
    raise NotImplementedError('TODO: implement this')
