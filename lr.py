#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-

# Logistic Regression classifier

import sys
import numpy
#from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as LR
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.datasets import load_svmlight_file
#from sklearn import preprocessing
#import pylab as pl

def main(train, test):

        # loads data
        #print ("Loading data...")
        X_train, y_train = load_svmlight_file(train)
        X_test, y_test = load_svmlight_file(test)
        # splits data
        # print ("Spliting data...")
        # X_train, X_test, y_train, y_test =  train_test_split(X_data, y_data, test_size=0.5, random_state = 5)

        X_train = X_train.toarray()
        X_test = X_test.toarray()

        # fazer a normalizacao dos dados #######
        # scaler = preprocessing.RobustScaler()
        # X_train = scaler.fit_transform(X_train)
        # X_test = scaler.fit_transform(X_test)
        
        #Create a Gaussian Classifier
        model = LR(solver='lbfgs', max_iter=140)

        #print ('Fitting knn')
        model.fit(X_train, y_train)

        # predicao do classificador
        #print ('Predicting...')
        y_pred = model.predict(X_test)

        # mostra o resultado do classificador na base de teste
        print ('Accuracy: ',  model.score(X_test, y_test))

        # cria a matriz de confusao
        cm = confusion_matrix(y_test, y_pred)
        print (cm)
        print(classification_report(y_test, y_pred, labels=[0,1,2,3,4,5,6,7,8,9]))


if __name__ == "__main__":
        if len(sys.argv) != 3:
                sys.exit("Use: lr.py <train> <test>")

        main(sys.argv[1], sys.argv[2])


