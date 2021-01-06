import pickle
import nltk.data        
import nltk
import logging
import codecs
from gensim.models import word2vec
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)   
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os

lst_reviews = []
tokenizer = []
sentences = []

num_features = 100    # Word vector dimensionality                      
min_word_count = 40   # Minimum word count                        
num_workers = 4       # Number of threads to run in parallel
context = 10          # Context window size                                                                                    
downsampling = 1e-3   # Downsample setting for frequent words





def review_to_sentences( review): 
    sentence=[]
    global raw_sentence
    try:
        raw_sentences = nltk.word_tokenize(review.strip())
        for raw_sentence in raw_sentences:
            if len(raw_sentence) > 0:
                sentence.append(raw_sentence.lower().split())
                
        return sentence
    except UnicodeDecodeError as e:
        pass

def reviews_to_sentences(lst_reviews,sentences):
        count  = 1
        for review in lst_reviews:
                
                try:
                        sentences += review_to_sentences(str(review[1]))
                except TypeError as e:
                        pass
                count += 1
        print "Reviews read ",count
        return sentences

def Word2Vector(sentences):
        model = word2vec.Word2Vec(sentences, workers=num_workers,size=num_features, min_count = min_word_count, window = context, sample = downsampling)
        model_name = "Humor_Yelp"
        model.save(model_name)


    
global lst_reviews
os.chdir('..')
preview = open("dataset/data.txt", "rb")
lst_reviews =  pickle.load(preview)    

sentences = reviews_to_sentences(lst_reviews,sentences)
Word2Vector(sentences)
