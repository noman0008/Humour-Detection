
import json
import pickle

d = []

def getData(funnyFile, notFunnyFile, dataFile):
	funnyCount = 0
	notFunnyCount = 0

	for line in funnyFile:
		#print line
		try:
			t = ('1', line.encode('utf-8'))
		except UnicodeDecodeError:
			pass
		d.append(t)

	for line in notFunnyFile:
		try:
			t = ('0', line.encode('utf-8'))
		except UnicodeDecodeError:
			pass
		d.append(t)

	print len(d)
	pickle.dump(d, dataFile)
	
	return d

if __name__ == "__main__":

	outputFileName = raw_input("output file name:")
	

	funnyFile = open('dataset/Jokes16000.txt','r')
	notFunnyFile = open('dataset/quotes.txt','r')
	dataFile = open(outputFileName,'w')

	getData(funnyFile, notFunnyFile, dataFile)

	funnyFile.close()
	notFunnyFile.close()
	dataFile.close()



