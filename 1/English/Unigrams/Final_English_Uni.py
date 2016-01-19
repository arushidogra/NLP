
# -*- coding: utf-8 -*-
import re
import os
import matplotlib.pyplot as plt
f = open("test.txt","r")
corpus = f.read()
" ".join(corpus.split())
f.close()
output=[]
data = re.findall("(?:(?:(?:|\n| |\?|\.|!|,|&|~|\(|\)|\*|_|;|\"|/|:|#| @|< | >|\^|{|}|$|%|\[|\]) ?([A-Za-z]+)|(<\w+>)|(\w+-\w+)|(\w+@?\.?\w+.\w+)|((?:\w*\W*\d+\w*\W*/)+\d+)|(/d+/w*/W*\?\w*\W*)|(\w+'\w+)|(\w* ?°? ?\w*)|((?:\d+,)*\d+)) ?((?:\n| |\?|\.|!|,|&|~|\(|\)|\*|_|;|\"|/|%|$|:|#| @|< | >|\^|{|}|\[|\]|\^)))",corpus)
                                    
list_final = []
for i in data:
    for j in i:
        if len(j)>0 and j!=' ' and j!='\n' and j!='\t' :
            list_final.append(j)




dir_store= {}

for i in list_final:
    dir_store[i]=0

for i in list_final :
    dir_store[i]+=1

dir_store.pop(" ",None)
dir_store.pop("\n",None)

final=[]
for i in dir_store.viewitems():
    p = list(i)
    p.reverse()
    final.append(p)

final.sort()
final.reverse()
os.system("touch ../unigram_english_output_1.txt")
r = open("../unigram_english_output_1.txt","r+")

for i in final:
    string = "('" + i[1] + "')    " + str(i[0]) + "\n"
    r.write(string)

r.close()


