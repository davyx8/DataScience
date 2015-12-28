__author__ = 'davyx8'
import nltk
nltk.download()
f = open('SpeakEZ.txt', 'r')

text=f.read()
print(text)
text= nltk.word_tokenize(text)
w=nltk.pos_tag(text)
print(w)