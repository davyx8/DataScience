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
	return (float(C)/(len(ratingsA)+len(ratingsB)-C))


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

sizes={}
inter={}
objects=[]
objects2=[]
scores={}
longRating={}
cosinescores={}
helpful=[]
maxJac=0
idx=0
for l in readGz("/cs/stud/davyx8/.++/train.json.gz"):
  inter[l['reviewerID']]=0
  sizes[l['reviewerID']]=0
  longRating[l['reviewerID']]={}
  ratings.append((l['reviewerID'], l['itemID'], l['rating']))
  helpful.append(l['helpful'])
  nUser[l['reviewerID']] += 1
  nItem[l['itemID']] += 1
  if (l['reviewerID'] == 'U229891973'):
  	ratingsA.append((l['reviewerID'], l['itemID'], l['rating']))

  	A+= 1
  if (l['reviewerID'] == 'U622491081'):
  	ratingsB.append((l['reviewerID'], l['itemID'], l['rating']))
  	objects2.append((l['itemID'],l['rating']))
  	objects.append(l['itemID'])




print("The jaccard of U229891973 and U622491081:")
print(jacCalc(ratingsA,ratingsB))

for tmp in ratings:
	sizes[tmp[0]]=sizes[tmp[0]]+1
	if (tmp[1] in objects):
		inter[tmp[0]]=inter[tmp[0]]+1
		longRating[tmp[0]].update({tmp[1]:tmp[2]})
		
	# jacc score calc, (inters/unifi)
	#i didnt use the function cause it was easier this way
	scores[tmp[0]]=float(inter[tmp[0]])/(sizes[tmp[0]]+len(objects)-inter[tmp[0]])


for i in scores:
	if scores[i]>maxJac:
		maxJac=scores[i]
print("Users with highest score")
for i in scores:
	if scores[i]==maxJac:
		print i

#Cosine similarity part
vec=[0]*len(objects)
scoresvec=[0]*len(objects)
i=0

for x in (objects2):
	vec[i]=x[0]
	scoresvec[i]=objects2[i][1]
	i=i+1

tmpvec=[0]*len(objects2)
for tmp in longRating:

	for i in longRating[tmp]:
		idx=vec.index(i)
		tmpvec[idx]=longRating[tmp][i]
	try:
		cosinescores[tmp]=cosine_similarity(tmpvec,scoresvec)
		#print(cosine_similarity(tmpvec,scoresvec))
	except ZeroDivisionError:
		cosinescores[tmp]=0
	if(tmp=='U229891973'):
		print("The cosine similarity of U229891973 and U622491081:")
		print(cosine_similarity(tmpvec,scoresvec))

maxcos=0
for i in cosinescores:
	if cosinescores[i]>maxcos:
		maxcos=cosinescores[i]
print("Users with highest  cosine score")
for i in cosinescores:
	if cosinescores[i]==maxcos:
		print i


