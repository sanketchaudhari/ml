import utils

data = utils.features_preprocessor('../network-intrusion-dataset/training-dataset/kdd-training-final-encoded')

opFile = open('../network-intrusion-dataset/training-dataset/28April_training-dataset-full-oneHotEncoded','w')
for item in data:
	print >> opFile, ','.join(item)

opFile.close()
