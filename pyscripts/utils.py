import numpy as np
from sklearn.preprocessing import OneHotEncoder

def features_preprocessor(datasetLocation):
	data = np.genfromtxt(datasetLocation,delimiter=",",usecols=range(41))
	encoder = OneHotEncoder(categorical_features=[1,2,3])
	encoder.fit(data)

	trainingData_features = encoder.transform(data).toarray()

	return trainingData_features
