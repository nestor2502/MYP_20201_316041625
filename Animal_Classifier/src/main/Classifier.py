from abc import ABC,abstractmethod

class Classifier(ABC):

    @abstractmethod
    def classify(self,img_test):
        """ 
            Abstract method that implement each animal class. Contains the process to know
            if img_test is or not animal (guinea pig, penguin, emu, giraff, hippo)

            Args:

            Returns:
                bool: True, if img_test is guinea pig, penguin, emu, giraff or hippo, 
                      False in other case.
                
        """
        pass

    @abstractmethod
    def training(self,images_path,labels_path,repetitions):
        """ 
            Abstract method that implement each animal class. In this method each class
            train the neuronal network with their model. This method only executes when
            no exist a file .h5 of the animal in directory 'training'.

            Args:
                images_path(str): path of the file that contains the processed images.
                labels_path(str): path of the file that contains the labels of the images.
                repetitions(int): number of times you train with the set of data set.

        """
        pass