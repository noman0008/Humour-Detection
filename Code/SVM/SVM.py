
import pickle
import sklearn
from sklearn.feature_extraction.text  import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn import cross_validation
from sklearn.cross_validation import KFold
import os

d = []

def create_tfidf_training_data(docs):
        y = [d[0] for d in docs]
        corpus = [d[1] for d in docs]
        vectorizer = TfidfVectorizer(min_df = 1)
        X = vectorizer.fit_transform(corpus)
        return X, y

def train_svm(X, y, k):
        if k == 'linear':
                svm = SVC(C=1.0, kernel='linear')
        elif k =='rbf':
                svm = SVC(C=1.0, kernel='rbf')
        svm.fit(X, y)
        return svm


if __name__ == "__main__":

        k = raw_input("Enter kernel type (linear/rbf):")
        
        
        print "creating tfidf features..."
        os.chdir('..')
        dataFile = open('dataset/data.txt','rb')
        d = pickle.load(dataFile)
        X, y = create_tfidf_training_data(d)

        
        kf = KFold(len(y), n_folds = 5, shuffle= True)
        
        iteration = 1
        accuracies = []
        for train, test in kf:
                print ("iteration " + str(iteration) + ":")
                

                print "Creating training testing data..."
                y_train = []
                y_test = []
                X_train, X_test = X[train], X[test]
                for i in train:
                        y_train.append(y[i])
                for j in test:
                        y_test.append(y[j])

                print "training classifier..."
                svm = train_svm(X_train, y_train, k)

                print "getting predictions..."
                predictions = svm.predict(X_test)

                print "calculating accuracies..."
                s = accuracy_score(y_test, predictions)
                print s
                accuracies.append(s)
                iteration = iteration + 1

        print "Accuracy: ",
        print reduce(lambda x, y: x + y, accuracies) / float(len(accuracies))
        dataFile.close()
