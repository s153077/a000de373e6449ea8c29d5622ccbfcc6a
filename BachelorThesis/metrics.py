from numpy import *

"""
WRITTEN BY:
Nicklas Hansen
"""

def compute_score(score, metric):
	result,dict,metrics = [],{},[]
	if (metric==TPR_FNR):
		metrics.append('tpr')
		metrics.append('fnr')
	for j in range(len(score[0])):
		x = []
		for i in range(len(score)):
			y = score[i]
			x.append(y[j])
		result.append(mean(array(x)))
	for k in range(len(result)):
		dict[metrics[k]] = result[k]
	return dict

def TPR_FNR(y, yhat):
		n = len(y[0])
		TP=FP=TN=FN=0
		TPR=FNR=0.0
		for i in range(n):
			a = bool(yhat[0,i])
			b = bool(y[0,i])
			TP += int(a & b)
			TN += int((not a) & ( not b))
			FP += int(a & (not b))
			FN += int(b & (not a))
		if (TP + FP) > 0:
			TPR = TP / (TP + FP)
		if (TP + FN) > 0:
			FNR = FN / (TP + FN)
		return TPR, FNR