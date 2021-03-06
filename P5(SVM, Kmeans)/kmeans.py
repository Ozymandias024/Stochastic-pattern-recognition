# -*- coding: utf-8 -*-
"""Kmeans.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-eB6Xx3RoooZ_lyyY2bGhtTtQh96ARPH
"""

#importing essential libraries and converting the image into a flat matrix
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import copy

image = io.imread('/content/drive/MyDrive/Depo/PatternHW/hw5/bird.tiff')
initialimage = image.copy()

np.shape(image)
rows = image.shape[0]
cols = image.shape[1]
image = np.reshape(image, (rows * cols, 3))
np.shape(image)
image

#plotting the distribution of colors in the 256*256*256 space
from matplotlib import projections
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection="3d")
ax.scatter3D(image[:, 0], image[:, 1], image[:, 2], s = 0.003, c = 'black')

#randomly selecting some colors from our pixels to be the initial centroids
def Initialize_Centroids(image, k):
    Centroids = []
    for i in range(k):
        RandomIndex = np.random.randint(0, len(image))
        Centroids.append(image[RandomIndex, :])
    return np.asarray(Centroids)

#normal distance of two vectors
def Distance(vector1, vector2):
    length = len(vector1)
    norm = 0
    for i in range(length):
        norm += np.power(vector1[i] - vector2[i], 2)
    dist = np.sqrt(norm)
    return dist

#finding the closest centroid to each point
def FindClosestCentroids(image, Centroids):
    distances = np.zeros((len(image), len(Centroids)))
    for i in range(len(image)):
        for j in range(len(Centroids)):
            distances[i, j] = Distance(Centroids[j], image[i])
    
    ClosestCentroid = np.argmin(distances, axis = 1)
    return ClosestCentroid

#reassessing the location of centroid by averaging every point in each cluster
def CalibrateCentroids(image, closestcentroids, k):
    count = np.zeros((k, 1))
    NewCentroids = np.zeros((k, 3))
    for i in range(len(image)):
        NewCentroids[ClosestCentroids[i]] += image[i]
        count[ClosestCentroids[i]] += 1
    NewCentroids = (NewCentroids / count).astype(np.uint8)
    return NewCentroids

#assigning the color of the closest centroid to every pixel
def Color(image, closestcentroids, centroids):

    
    coloredImage = np.zeros((np.shape(image)))

    for i in range(len(image)):
        color = closestcentroids[i]
        coloredImage[i, :] = centroids[color, :]    
    

    return coloredImage

#running the k means algorithm
k = 32
Centroids = Initialize_Centroids(image, k)

for i in range(10):

    ClosestCentroids = FindClosestCentroids(image, Centroids)

    Centroids = CalibrateCentroids(image, ClosestCentroids, k)

    image = Color(image, ClosestCentroids, Centroids)

#reconstructing our image

ReconstructedImage = np.reshape(image, (rows , cols, 3)).astype(np.uint8)

io.imshow(ReconstructedImage)