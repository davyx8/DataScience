import gzip
import math
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


def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

ratings=[]
ratingsA=[]
ratingsB=[]
A=0
B=0
sizes={}
inter={}
objects=[]
objects2=[]
scores={}
longRating={}
for l in readGz("/cs/stud/davyx8/.++/train2.json.gz"):
  inter[l['reviewerID']]=0
  sizes[l['reviewerID']]=0
  longRating[l['reviewerID']]={}
  ratings.append((l['reviewerID'], l['itemID'], l['rating']))
  
  nUser[l['reviewerID']] += 1
  nItem[l['itemID']] += 1
  if (l['reviewerID'] == 'U229891973'):
  	ratingsA.append((l['reviewerID'], l['itemID'], l['rating']))

  	A+= 1
  if (l['reviewerID'] == 'U622491081'):
  	ratingsB.append((l['reviewerID'], l['itemID'], l['rating']))
  	objects2.append((l['itemID'],l['rating']))
  	objects.append(l['itemID'])
  	B+= 1




print("The jaccard of U229891973 and U622491081:")
print(jacCalc(ratingsA,ratingsB))
maxJac=0
idx=0
for tmp in ratings:
	sizes[tmp[0]]=sizes[tmp[0]]+1
	if (tmp[1] in objects):
		inter[tmp[0]]=inter[tmp[0]]+1
		#tmp2=longRating[tmp[0]
		#tmp2['aa']=l[tmp[2]]
		longRating[tmp[0]].update({tmp[1]:tmp[2]})
		
		print(longRating[tmp[0]])
	scores[tmp[0]]=float(inter[tmp[0]])/sizes[tmp[0]]


#for i in scores:
#	if scores[i]>maxJac:
#		maxJac=scores[i]
#print("Users with highest score")
#for i in scores:
#	if scores[i]==maxJac:
#		print i

#Cosine similarity part
cosinescores=[]
vec=[0]*len(objects2)
i=0
scoresvec=[0]*len(objects2)
for x in (objects2):
	print(x)
	print(x[0])
	print(objects2[i][1])
	vec[i]=x[0]
	i=i+1
	scoresvec[i]=objects2[i][1]

print(vec)
tmpvec=[0]*len(objects2)
for tmp in longRating:

	for i in longRating[tmp]:
		idx=vec.index(i)
		tmpvec[idx]=longRating[tmp][i]
		print(tmpvec)
		print(cosine_similarity(tmpvec,scoresvec))




