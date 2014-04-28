import numpy as np
from sklearn.preprocessing import OneHotEncoder

def formator(value):
	return "%.2f" % value

def features_preprocessor(datasetLocation):
	data = np.genfromtxt(datasetLocation,delimiter=",",usecols=range(41)) ##!!! usecols = range(41)
	encoder = OneHotEncoder(categorical_features=[1,2,3])
	encoder.fit(data)
	trainingData_features = encoder.transform(data).toarray().tolist()
	formatted_trainingData = [[formator(v) for v in r] for r in trainingData_features]	# Convert float valued list to string.
	print len(formatted_trainingData[0])
	return formatted_trainingData
