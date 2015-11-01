import gzip
from collections import defaultdict
from random import random

nUser = defaultdict(int)
nItem = defaultdict(int)
def readGz(f):
  for l in gzip.open(f):
    yield eval(l)

def jacCalc(ratingsA,ratingsB):
	C=0

	for k in ratingsA:
		for z in ratingsB:
			if (k[1] == z[1]):

				C+=1
	return (float(C)/(len(ratingsA)+len(ratingsB)))

ratings=[]
ratingsA=[]
ratingsB=[]
A=0
B=0
sizes={}
inter={}
objects=[]
scores={}
for l in readGz("/tmp/train.json.gz"):
  inter[l['reviewerID']]=0
  ratings.append((l['reviewerID'], l['itemID'], l['rating']))
  nUser[l['reviewerID']] += 1
  nItem[l['itemID']] += 1
  if (l['reviewerID'] == 'U229891973'):
  	ratingsA.append((l['reviewerID'], l['itemID'], l['rating']))

  	A+= 1
  if (l['reviewerID'] == 'U622491081'):
  	ratingsB.append((l['reviewerID'], l['itemID'], l['rating']))
  	objects.append(l['itemID'])
  	B+= 1





print("The jaccard similarity is:")
print(jacCalc(ratingsA,ratingsB))
maxJac=0

for tmp in ratings:
	sizes[tmp[0]]=+1
	if (tmp[1] in objects):
		inter[tmp[1]]=+1
	scores[tmp[0]]=float(inter[tmp[0]])/sizes[tmp[0]]


print(scores)



