import sys
import os
dir = os.path.dirname(__file__)

classifier_path =os.path.join(dir,"../")
preprocess_path = os.path.join(dir,"../../tools")
h5_path = os.path.join(dir, '../../training')

sys.path.insert(0,classifier_path)
sys.path.insert(0,preprocess_path)
sys.path.insert(0,h5_path)

import tensorflow as tf
from tensorflow import keras
from Preprocess import * 
from Classifier import *
import numpy as np

class PenguinClassifier(Classifier):
	"""
	This class models a penguin classifier.
	"""
	def __init__(self):
		super(PenguinClassifier, self).__init__()
		self.__model = keras.Sequential()
		if os.path.exists(os.path.join(h5_path,"penguin.h5")):
			self.__model = keras.models.load_model(os.path.join(h5_path,"penguin.h5"))
		else:
			self.__model = self.__penguin_model()

	def __penguin_model(self):
		"""
		Return a model to classify penguins

		Return:
			tf.keras.Model: A model to classify penguins.
		"""
		model = keras.Sequential([
	    keras.layers.Flatten(input_shape=(60, 60,1)),
	    keras.layers.Dense(128, activation=tf.nn.relu),
	    keras.layers.Dense(3, activation=tf.nn.softmax)])

		# Compiling the model using some basic parameters
		model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
              		  metrics=['accuracy'])
		return model
 

	def classify(self,img_test):
	    """ 
	    Abstract method that implement each animal class. Contains the process to know
	    if img_test is or not animal (guinea pig, penguin, emu, giraff, hippo)

	 	Return:
	        bool:True If img_test is penguin False in other case.
	               
	    """

	    preprocess = Preprocess()
	    img = preprocess.prepare_image(img_test,60)
	    predictions = self.__model.predict(img)
	    max = np.argmax(predictions)
	    labels = ["penguin","non_penguin","penguin_like"]
	    result = labels[max]

	    if result == "penguin":
	    	return True
	    return False

	def training(self, images_path, labels_path, repetitions):
		""" 
            train the neuronal network with their model. This method only executes when
            no exist a file .h5 of the animal in directory 'training'.

            Args:
                images_path(str): path of the file that contains the processed images.
                labels_path(str): path of the file that contains the labels of the images.
                repetitions(int): number of times you train with the set of data set.

        """
		model = self.__penguin_model()
		train_images = pickle.load(open(images_path, "rb"))
		train_labels = pickle.load(open(labels_path, "rb"))
		model.fit(np.array(train_images), np.array(train_labels), epochs = repetitions)
		model.save("../training/penguin.h5")
		self.__model = keras.models.load_model("../../training/penguin.h5")