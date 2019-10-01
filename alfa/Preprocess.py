import cv2
import numpy as np
#from matplotlib import pyplot as plt
import random
import pickle
import os
class Preprocess(object):
	"""docstring for ClassName"""
	def __init__(self, *arg,**kwargs):
		self.DATADIR = "data"
		self.CATEGORIES = ["men","women"]
		self.IMG_SIZE = 50
		self.training_date = []
		self.labels = []
		self.features = []

	def load_training_data(self):
		for category in self.CATEGORIES:
			path = os.path.join(self.DATADIR,category)
			class_num = self.CATEGORIES.index(category)
			for img in os.listdir(path):
				try:
					img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
					new_array = cv2.resize(img_array,(self.IMG_SIZE,self.IMG_SIZE))
					self.training_date.append(new_array,class_num)
				except Exception as e :
					pass

	def split_and_prepare(self):
		random.shuffle(self.training_date)
		for features, label in self.training_date:
			self.features.append(features)
			self.labels.append(label)
		self.features = np.array(self.features).reshape(-1,self.IMG_SIZE,self.IMG_SIZE,1)
		self.features = self.features/255.0

	def write_out(self):
		pickle_out = open("X.pickle","wb")
		pickle.dump(self.features,pickle_out)
		pickle_out.close()

		pickle_out = open("Y.pickle","wb")
		pickle.dump(self.features,pickle_out)
		pickle_out.close()

processor = Preprocess();
processor.load_training_data();
processor.split_and_prepare();
processor.write_out();
