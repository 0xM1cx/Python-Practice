import os
import numpy as np 
import matplotlib.pyplot as plt 
import cv2
import tensorflow as tf 

def training_NN():
	mnist = tf.keras.datasets.mnist
	(x_train, y_train), (x_test, y_test) = mnist.load_data()

	x_train = tf.keras.utils.normalize(x_train, axis=1)
	x_test = tf.keras.utils.normalize(x_test, axis=1)

	model = tf.keras.models.Sequential()
	model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
	model.add(tf.keras.layers.Dense(128, activation='relu'))
	model.add(tf.keras.layers.Dense(128, activation='relu'))
	model.add(tf.keras.layers.Dense(10, activation='softmax'))

	model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

	model.fit(x_train, y_train, epochs=3)
	model.save('handwritten.model')



def load_model():
	model = tr.keras.models.load_model('handwritten.model')

def main():
	# training_NN()
	load_model()
