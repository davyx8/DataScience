import gzip


def readGz(f):
  for l in gzip.open(f):
    yield eval(l)


helpful=[]
ratings=[]
for l in readGz("/cs/stud/davyx8/.++/train.json.gz"):
  ratings.append((l['reviewerID'], l['itemID'], l['rating']))
  helpful.append(l['helpful'])


#suggestion for helpful-calculation
# number of (helpful ratio*min(1, #number of rate/average number of rates)
hlpVec=[0]*len(ratings)
hlpScore=[0]*len(ratings)
i=0
for hlp in helpful :
	hlpVec[i]=hlp['outOf']
	hlpScore[i]=hlp['nHelpful']/float(hlp['outOf'])
	i+=1


average=sum(hlpVec)/float(len(hlpVec))
print(average)

for x in range(len(hlpScore)):
	hlpScore[x]=hlpScore[x]*min(1,hlpVec[x]/float(average)) 
	print('review number {0:d}  is {1:.2f} -helpful '.format(x,hlpScore[x]))
