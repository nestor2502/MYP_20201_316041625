import sys
import os
import unittest

dir = os.path.dirname(__file__)

classifier_path =os.path.join(dir,"../../main/guinea_pig")
test1_path =os.path.join(dir,"./img_test/yes_guinea_pig")
test2_path =os.path.join(dir,"./img_test/no_guinea_pig")
test3_path =os.path.join(dir,"./img_test/similar_guinea_pig")

sys.path.insert(0,classifier_path)
sys.path.insert(0,test1_path)
sys.path.insert(0,test2_path)
sys.path.insert(0,test3_path)

from GuineaPigClassifer import GuineaPig

class GuineaPigClassifierTest(unittest.TestCase):
    """ Test class of GuineaPigClassifier"""

    def test_img_GuineaPig(self):
        """ Test if CNN almost detect correctly guinea's pig images
        """
        classifierGuineaPig = GuineaPig()

        contAsserts = 0

        for img in os.listdir(test1_path):

            if classifierGuineaPig.classify(os.path.join(test1_path,img)): 

                contAsserts+=1

        self.assertTrue(contAsserts >= len(os.listdir(test1_path))-5)

    def test_img_notGuineaPig(self):

        contAsserts = 0

        classifierGuineaPig = GuineaPig()

        for img in os.listdir(test2_path):

            if not classifierGuineaPig.classify(os.path.join(test2_path,img)): 

                contAsserts+=1

        self.assertTrue(contAsserts >= len(os.listdir(test2_path))-2)

    def test_img_similarGuineaPig(self):
        
        contAsserts = 0

        classifierGuineaPig = GuineaPig()

        for img in os.listdir(test3_path):

            if not classifierGuineaPig.classify(os.path.join(test3_path,img)): 

                contAsserts+=1

        self.assertTrue(contAsserts >= len(os.listdir(test1_path))-3)

if __name__ == "__main__":
    unittest.main()