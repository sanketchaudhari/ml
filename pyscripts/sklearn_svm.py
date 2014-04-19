print " Importing the required modules. Please wait. \n"
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import utils

print "#####################################"
print "This is SVM using the Gaussian Kernel"
print "#####################################"

#Load the data

print "\n Now loading the data. \n"
training_features = utils.features_preprocessor('../network-intrusion-dataset/modified dataset/id_training.txt')
training_classes = np.genfromtxt('../network-intrusion-dataset/modified dataset/id_classes_training.txt')

test_features = utils.features_preprocessor('../network-intrusion-dataset/test-dataset/id_testing.txt')
test_classes = np.genfromtxt('../network-intrusion-dataset/test-dataset/id_classes_testing.txt')

print "\n The data has been loaded.\n"

svm_clf = SVC()

print "\n Fitting the data. \n" 
svm_clf.fit(training_features, training_classes)

print "\n Now predicting over the test data set \n"
predictions = svm_clf.predict(test_features)

print "\n The accuracy of the algorithm is : ", accuracy_score(predictions, test_classes)



