# -*- coding: utf-8 -*-
"""SVM_Linear.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FFqeRVAVVz1W1qAnwRpN622ilE_LaVKl
"""

#loading libraries and preparing the data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.io import loadmat
from sklearn.svm import SVC

data = loadmat('/content/drive/MyDrive/Depo/PatternHW/hw5/Dataset1.mat')

input = data['X']
label = data['y']

np.shape(input)

#svm model
def Model(input, label, C_value):
    model = SVC(kernel="linear", C = C_value)
    model.fit(input, label)
    prediction = model.predict(input)
    return model, prediction

#plotting the decision boundary of the model
def Plot_Boundary(input, model):
    pos_input = []
    neg_input = []
    for i in range(len(input)):
        if label[i] == 0:
            neg_input.append(input[i, :])
        else:
            pos_input.append(input[i, :])
    
    pos_input = np.asarray(pos_input)
    neg_input = np.asarray(neg_input)

    xmin = input.min()
    xmax = input.max()

    slope = model.coef_[0]
    bias = model.intercept_[0]

    x0 = np.linspace(xmin, xmax, 200)
    boundary = -slope[0]/slope[1] * x0 - bias/slope[1]

    plt.scatter(pos_input[:, 0], pos_input[:, 1], c = 'blue')
    plt.scatter(neg_input[:, 0], neg_input[:, 1], c = 'red')
    plt.plot(x0, boundary, c = "black")

def Accuracy(prediction, label):
    count = 0
    for i in range(len(label)):
        if prediction[i] == label[i]:
            count += 1

    print(f"Accuracy of the model is: {(count / len(label) * 100)}%")

#running the algorithm
model, prediction = Model(input, label, 1)

Plot_Boundary(input, model)

Accuracy(prediction, label)

model, prediction = Model(input, label, 100)

Plot_Boundary(input, model)

Accuracy(prediction, label)