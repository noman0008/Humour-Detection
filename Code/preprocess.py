import json
import pickle

d_lst = []

def prepare_data(input_file, data_file,n):
	funnyCount = 0
	notFunnyCount = 0

	for line in input_file:
		
		data = json.loads(line)
		if data["votes"]["funny"] > 2 and funnyCount < n:
			funnyCount += 1
			t = ('1',data["text"].encode('utf-8'))
			d_lst.append(t)

		elif notFunnyCount < n:
			notFunnyCount += 1
			t = ('0',data["text"].encode('utf-8'))
			d_lst.append(t)

		else:
			if funnyCount >= n and notFunnyCount >= n:
				break

	
	pickle.dump(d_lst, data_file)
	
	return d_lst

if __name__ == "__main__":
    
    
	

	out_file_name = input("output file name:")
	
	n = int(input("number of datapoints per class:"))

	input_file = open('dataset/yelp_academic_dataset_review.json','r')
    
    
    
	out_file_name = 'dataset/'+out_file_name
	data_file = open(out_file_name,'wb')
    

	prepare_data(input_file, data_file, n)

	input_file.close()
	data_file.close()



