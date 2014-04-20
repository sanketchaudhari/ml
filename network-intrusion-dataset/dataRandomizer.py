#!/usr/bin/python
from __future__ import division
import math
import random

#List that will store the training dataset
trainingData = []
trainingClassData = []


#Read the data from the training dataset into the trainingData list
with open('./training-dataset/training_dataset_full.txt','r') as bigFile:
	for line in bigFile:
		trainingData.append(line.strip().split(","))

with open('./training-dataset/training_dataset_classes_full.txt','r') as bigClassFile:
	for line in bigClassFile:
		trainingClassData.append(line.strip())
		
print "Total number of entries in the original dataset : ", len(trainingData)

#Number of random data points we need from the full dataset
total_data_points_needed = 10000

#List containing the indices of only the entries classified "normal" in the training data
normalIndexList = []
for item in trainingData:
	if item[41] == 'normal.':
		normalIndexList.append(trainingData.index(item))
print "Number of normal entries in the original dataset : ",len(normalIndexList)

#Self explanatory
number_of_normal_entries_in_original_dataset = len(normalIndexList)
print number_of_normal_entries_in_original_dataset
number_of_entries_in_original_dataset = len(trainingData)
print number_of_entries_in_original_dataset
number_of_normal_entries_in_final_dataset = int(math.floor((number_of_normal_entries_in_original_dataset / number_of_entries_in_original_dataset)*(total_data_points_needed)))
print number_of_normal_entries_in_final_dataset

#Now, from the total number of normal entries in the original dataset, we randomly choose
#the indices for our required number of normal data points.
my_random_indices_normal_entries = random.sample(xrange(number_of_normal_entries_in_original_dataset), number_of_normal_entries_in_final_dataset)

#List containing our final training dataset after randomizing and cutting it small.
finalTrainingData = []
finalTrainingClassData = []

#Populate the final training data list with the entries. 
for index in my_random_indices_normal_entries:
	finalTrainingData.append(trainingData[normalIndexList[index]])

for index in my_random_indices_normal_entries:
	finalTrainingClassData.append(trainingClassData[normalIndexList[index]])
	
#Self explanatory.
number_of_remaining_data_points = total_data_points_needed - number_of_normal_entries_in_final_dataset
print number_of_remaining_data_points
#Creating a list of indices which correspond to "not normal" entries in the original dataset.
indexList = range(number_of_entries_in_original_dataset)
tempList = set(normalIndexList)
notNormalIndexList = [x for x in indexList if x not in tempList]
print len(notNormalIndexList)
my_random_indices_notNormal_entries = random.sample(xrange(len(notNormalIndexList)), number_of_remaining_data_points)

#Finally append these entries to our randomized final dataset.
for index in my_random_indices_notNormal_entries:
	finalTrainingData.append(trainingData[notNormalIndexList[index]])
	
for index in my_random_indices_notNormal_entries:
	finalTrainingClassData.append(trainingClassData[notNormalIndexList[index]])
print "Total number of entries in the final training dataset : ", len(finalTrainingData)

opFile = open('./training-dataset/training_dataset_mini.txt','w')
for item in finalTrainingData:
	print >> opFile, ','.join(item)

opClassFile = open('./training-dataset/training_dataset_classes_mini.txt','w')
for item in finalTrainingClassData:
	print >> opClassFile, ''.join(item)

print "Data has been randomized successfully."
opFile.close()
