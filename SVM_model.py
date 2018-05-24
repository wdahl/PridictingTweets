#William Dahl
#ICSI 431 Data Mining
#April 11th, 2018

import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

x = [[0 for i in range(10)] for j in range(500)] #2d array holding frecuncy of words in tweets
y = [0 for i in range(500)] #total frecuncy of each tweet
#opens the file for reading
with open("labled_tweets.txt", "r") as f:
	#loops through the 500 tweets
	for i in range(500):
		line = f.readline().lower()#line read 
		y[i] = line[1]
		#checks if one of the 10 words apears in the tweet
		if "car" in line:
			x[i][0] = 1
		if "girls" in line:
			x[i][1] = 1
		if "shelter" in line:
			x[i][2] = 1
		if "puppy" in line:
			x[i][3] = 1
		if "mom" in line:
			x[i][4] = 1
		if "dad" in line:
			x[i][5] = 1
		if "street" in line:
			x[i][6] = 1
		if "bus" in line:
			x[i][7] = 1
		if "road" in line:
			x[i][8] = 1
		if "driver" in line:
			x[i][9] = 1 

print x
print y

clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, x, y, cv=10)

print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2 ))

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],'C': [1, 10, 100, 1000]},{'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]
scores = ['precision', 'recall']
svr = svm.SVC(C=1)
for score in scores:
    print("# Tuning hyper-parameters for %s"% score)
    clf = GridSearchCV(svr, tuned_parameters, cv=10,scoring='%s_macro'% score)
    clf.fit(x, y)
    print("best parameters %s" % clf.best_params_)
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"% (mean, std *2, params))

x_test = [[0 for i in range(10)] for j in range(100)] #2d array holding frecuncy of words in tweets
y_test = [0 for i in range(100)] #total frecuncy of each tweet
#opens the file for reading
with open("unlabled_tweets.txt", "r") as f:
	#loops through the 500 tweets
	for i in range(100):
		vector_sum = 0 #frecuency total
		line = f.readline().lower()#line read 
		#checks if one of the 10 words apears in the tweet
		if "car" in line:
			x[i][0] = 1
		if "girls" in line:
			x[i][1] = 1
		if "shelter" in line:
			x[i][2] = 1
		if "puppy" in line:
			x[i][3] = 1
		if "mom" in line:
			x[i][4] = 1
		if "dad" in line:
			x[i][5] = 1
		if "street" in line:
			x[i][6] = 1
		if "bus" in line:
			x[i][7] = 1
		if "road" in line:
			x[i][8] = 1
		if "driver" in line:
			x[i][9] = 1

		#sums the frecuncy of each word in each tweet together
		for j in range(10):
			vector_sum += x[i][j]

		y[i] = vector_sum#sets the total frecunct of a tweet to the index in y at i

for score in scores:
	y_true, y_pred = y_test, clf.predict(x_test)

p = open("predicted_tweets.txt", "w")
with open("unlabled_tweets.txt", "r") as f:
	for i in range(100):
		line = f.readline()
		if y_pred[i] < 0:
			line = "0" + line
		else:
			line = "1" + line

		p.write(line)
