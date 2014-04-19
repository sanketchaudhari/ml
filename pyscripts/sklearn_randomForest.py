
print " Importing the required modules. Please wait. \n"
import numpy as np
from sklearn.ensemble import RandomForestClassifier	##
from sklearn.metrics import accuracy_score

print " ####################################"
print " This is the Random Forest Classifier"
print " ####################################"

#Load the data

print "\n Now loading the data."
training_features = np.genfromtxt('dataset_training_features.txt')
training_classes = np.genfromtxt('dataset_training_class.txt')

test_features = np.genfromtxt('dataset_testing_features.txt')
test_classes = np.genfromtxt('dataset_testing_class.txt')
print "\n The data has been loaded."

rndf_clf = RandomForestClassifier()	##
print " ", rndf_clf			##

print "\n Fitting the data..." 
rndf_clf.fit(training_features, training_classes)	##

print "\n Now predicting over the test data set..."
predictions = rndf_clf.predict(test_features)		##

print "\n The accuracy of the algorithm is : ", accuracy_score(predictions, test_classes)



