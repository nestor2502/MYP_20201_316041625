import sys
import os

dir = os.path.dirname(__file__)

classifier_path =os.path.join(dir,"../")
preprocess_path = os.path.join(dir, '../../tools/')
h5_path = os.path.join(dir, '../../training/')

sys.path.insert(0,classifier_path)
sys.path.insert(0,preprocess_path)
sys.path.insert(0, h5_path)

from Classifier import Classifier
import Preprocess


import tensorflow as tf
from tensorflow import keras
import pickle
import os
import numpy as np

class HippoClassifier(Classifier):

	def __init__(self):
		pass

	def __createModel(self):
		"""
		Modelo to diferenciate an hippo yo another object or animal
		Return: model
		"""
		model = keras.Sequential()
		#first cap
		model.add (keras.layers.Conv2D (32, (3,3),activation = 'relu', input_shape = (50, 50, 1)))
		model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))
		#second cap
		model.add (keras.layers.Conv2D (64, (3,3),activation = 'relu'))
		model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))
		#third cap
		model.add (keras.layers.Conv2D (128, (3,3),activation = 'relu'))
		model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))
		#fourth cap
		model.add (keras.layers.Conv2D (256, (3,3),activation = 'relu'))
		model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))

		model.add(keras.layers.Flatten())
		model.add(keras.layers.Dense(128,activation='relu'))
		model.add(keras.layers.Dense(2, activation='softmax'))
		model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
		return model

	def training(self, images_path,labels_path,repetitions):
		"""
		Train the model doing 300 epochs
		params: images_path
				labels_path 
		"""
		train_images = pickle.load(open(str(images_path), "rb"))
		train_labels = pickle.load(open(str(labels_path), "rb"))
		model = self.__createModel()
		#We are training the model with 300 iterations 
		model.fit(train_images, train_labels, epochs=300)
		model.save(os.path.join(h5_path,'hippo.h5'))


	def classify(self, path_image):
		"""
		Method that classify an image that hippo or not hippo
		"""
		model = keras.models.load_model(os.path.join(h5_path,'hippo.h5'))
		pre = Preprocess.Preprocess()
		img_test =pre.prepare_image(path_image,50)
		predictions = model.predict(img_test)
		max = np.argmax(predictions)
		cat = ["hippo","no_hippo"]
		result = str(cat[max])
		if result == 'hippo':
			return True
		if result == 'no_hippo':
			return False
