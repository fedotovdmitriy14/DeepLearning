import numpy as np


weights = np.array([0.1, 0.2, 0])
toes = np.array([8.5, 9.5, 9.9, 9.0])  # number of games
wlrec = np.array([0.65, 0.8, 0.8, 0.9])  # win/lose ration
nfans = np.array([1.2, 1.3, 0.5, 1.0])  # number of fans
input = np.array([toes[0], wlrec[0], nfans[0]])


def neural_network(input: np.array, weights: np.array):
    pred = input.dot(weights)  # dot product = скалярное произведение
    return pred


pred = neural_network(input, weights)
print(pred)
