import gzip
from collections import defaultdict
from random import random

def readGz(f):
  for l in gzip.open(f):
    yield eval(l)


for l in readGz("train.json.gz"):
	if (l['reviewerID'] == 'U365857020'):
  		print(l['itemID'])