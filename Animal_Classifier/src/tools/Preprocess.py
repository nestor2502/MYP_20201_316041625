 # imports that this class
import cv2
import numpy as np
import random
import pickle
import os
# end import
class Preprocess(object):

	"""
	This class preprocesses the images to feed a neural network.
	"""
	def __init__(self):
		"""
		Builder for Preprocessor.
		"""
		self.__IMG_SIZE = 1
		self.__training_date = []
		self.__labels = []
		self.__features = []
		
	def load_training_data(self, data_dir, categories, img_size):
		"""
		Load images in the data_dir directory and all subdirectories whose names are the same as tags in categories
		
		Args:
			data_dir(str): directory that content the images for a neural network.
			categories(tuple): data classifications.
			img_size(int): image size for a neural network.
		Raises:
			TypeError: if any argument isn't a valid type
			ValueError: if img_size is less than 1 or data_dir isn't a valid directory
		"""
		if type(data_dir) is not str:
			raise TypeError("data_dir isn't a string")
		if type(categories) is not list:
			raise TypeError("categories isn't a tuple")
		if type(img_size) is not int:
			raise TypeError("img_size isn't a integer number")
		if not os.path.isdir(data_dir):
			raise ValueError("data_dir isn't a valid directory")
		if img_size < 1:
			raise ValueError("img_size is less than 1")

		self.__IMG_SIZE = img_size
		for category in categories:
			path = os.path.join(data_dir,category)
			class_num = categories.index(category)
			for img in os.listdir(path):
				try:
					img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
					new_array = cv2.resize(img_array,(self.__IMG_SIZE,self.__IMG_SIZE))
					self.__training_date.append((new_array,class_num))
				except Exception as e :
					pass

	def split_and_prepare(self):
		"""
		Preprocces the images.
		"""
		random.shuffle(self.__training_date)
		for features, label in self.__training_date:
			self.__features.append(features)
			self.__labels.append(label)
		self.__features = np.array(self.__features).reshape(-1,self.__IMG_SIZE,self.__IMG_SIZE,1)
		self.__features = self.__features/255.0

	def write_out(self, directory_out):
		"""
		Create or rewrite two files that contain the preprocessed images and the labels of the image categories.
		The file that will have the processed images will be images.pickle and
		the file that will have the labels of the image categories will be labels.pickle.
		
		Args:
			directory_out(str): directory that will content the preprocessed data.

		Raises:
			TypeError: if directory_out isn't a string
			ValueError: if directory_out isn't a valid directory
		"""
		if type(directory_out) is not str:
			raise TypeError("directory_out isn't a string")
		if not os.path.isdir(directory_out):
			raise ValueError("directory_out isn't a valid directory")

		self.split_and_prepare()
		pickle_out = open(os.path.join(directory_out,"images.pickle"),"wb")
		pickle.dump(self.__features,pickle_out)
		pickle_out.close()

		pickle_out = open(os.path.join(directory_out,"labels.pickle"),"wb")
		pickle.dump(self.__labels,pickle_out)
		pickle_out.close()

	def prepare_image(self,img_path,img_size):
		"""
		Return processed image that it can be read by a neural network, 
		the image is resized to be an image that has the same size on all sides.

		Args:
			img_path(str): path of the file that contents the image.
			img_size(int): length of the new resized imagen.

		Returns:
			numpy.array: processed image.

		Raises:
			TypeError: if the img_path don't exist or is'nt a image.
			ValueError: if img_size is less than 1.
		"""
		if type(img_path) is not str:
			raise TypeError("img_path isn't a string")
		if not os.path.isfile(img_path):
			raise ValueError("img_path isn't a file")
		if type(img_size) is not int:
			raise TypeError("img_size isn't a integer number")
		if img_size < 1:
			raise ValueError("img_size is less than 1")
		array = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
		if len(array) == 0:
			raise TypeError("img_path isn't a image")
		array = cv2.resize(array,(img_size,img_size))
		array = np.array(array).reshape(-1,img_size,img_size,1)
		array = array/255.0
		return array