import sys
import os
from main.guinea_pig.GuineaPigClassifer import GuineaPig
from main.giraffe.GiraffeClassifier import Giraffe
from main.penguin.PenguinClassifier import PenguinClassifier
from main.hippo.HippoClassifier import HippoClassifier
from main.ostrich.OstrichClassifier import Ostrich

def main():
    if (len(sys.argv) <= 1):
        print("Don't have any argument! Execute: python3 <main_path> <image_path> ")
        sys.exit(0)

    img_path = os.path.join(sys.argv[1])

    if not(os.path.exists(sys.argv[1])):
        print("That file doesn't exist or wrong path!")
        sys.exit(0)

    if not(os.path.isfile(sys.argv[1])):
        print("That doesn't a valid file!")
        sys.exit(0)

    print(sys.argv[1])

    classiferGuineaPig = GuineaPig()
    classiferPenguin = PenguinClassifier()
    classiferHippo = HippoClassifier()
    classiferOstrich = Ostrich()
    classifierGiraffe = Giraffe()

    if classiferGuineaPig.classify(img_path):
        print("The image is : guinea pig")
    elif classiferPenguin.classify(img_path):
        print("The image is : penguin")
    elif classiferHippo.classify(img_path):
        print("The image is : hippo")
    elif classiferOstrich.classify(img_path):
        print("The image is : ostrich")
    elif classifierGiraffe.classify(img_path):
    	print("The image is : giraffe")	
    else:
        print("The image is not an animal known to the classifier")

if __name__ == "__main__":
    main()