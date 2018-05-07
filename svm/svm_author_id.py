#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

clf = svm.SVC(C=10000, kernel='rbf')

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print("Training time is: ", round(time()-t0, 3), "s")

t0 = time()
preds = clf.predict(features_test)
print("Prediction time is: ", round(time()-t0, 3), "s")

print("Prediction: 10th: ", preds[10], ", 26th: ", preds[26], ", 50th: ", preds[50])
print("Sara (0) preds: ", len([p for p in preds if p == 0]))
print("Chris (1) preds: ", len([p for p in preds if p == 1]))

print("Test prediction accuracy: " + str(clf.score(features_test, labels_test)))
