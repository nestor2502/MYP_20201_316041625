import sys
import os

dir = os.path.dirname(__file__)

classifier_path =os.path.join(dir,"../../main/penguin")
test1_path =os.path.join(dir,"./penguin")
test2_path =os.path.join(dir,"./penguin_like")
test3_path =os.path.join(dir,"./no_penguin")

sys.path.insert(0,classifier_path)
sys.path.insert(0,test1_path)
sys.path.insert(0,test2_path)
sys.path.insert(0,test3_path)


from PenguinClassifier import PenguinClassifier
import unittest
import os
import cv2


class PenguinClassifierTest(unittest.TestCase):

	def test_penguin_images(self):
		"""
		The class PenguinClassifier clasify penguin images.
		"""
		penguin = PenguinClassifier()
		successes = 0
		sample = 0
		for img in os.listdir(test1_path):
			try:
				if penguin.classify(os.path.join(test1_path,img)):
					successes +=1
				sample +=1
			except:
				pass
		self.assertTrue(successes/sample >= 0.3)

	def test_non_penguin_images(self):
		"""
		The class PenguinClassifier clasify non-penguin images.
		"""
		penguin = PenguinClassifier()
		successes = 0
		sample = 0
		path = os.path.abspath("test/penguin/no_penguin")
		for img in os.listdir(test2_path):
			try:
				if penguin.classify(os.path.join(test2_path,img)):
					successes +=1
				sample +=1
			except:
				pass
		self.assertTrue(successes/sample < 0.5)

	def test_penguin_like(self):
		"""
		The class PenguinClassifier clasify penguin like images.
		"""
		penguin = PenguinClassifier()
		successes = 0
		sample = 0
		path = os.path.abspath("test/penguin/penguin_like/")
		for img in os.listdir(test3_path):
			try:
				if penguin.classify(os.path.join(test3_path,img)):
					successes +=1
				sample +=1
			except:
				pass
		self.assertTrue(successes/sample < 0.2)

if __name__ == '__main__':
	unittest.main()
