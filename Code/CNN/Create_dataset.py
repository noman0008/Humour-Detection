import pickle

preview = open("data.pickle", "rb");
reviewsLst =  pickle.load(preview);
funny = open("funny.txt","a");
nfunny = open("notfunny.txt","a");

counter = 0

ls = []
fc = 0;
nfc = 0
for review in reviewsLst:
	if review[0] == '1': 
		stri  = review[1].replace('\n', '')
		funny.write(stri+"\n")
	else:	
		stri  = review[1].replace('\n', '')
		nfunny.write(stri+"\n")


		
