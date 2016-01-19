
# -*- coding: utf-8 -*-
import re
import os
import matplotlib.pyplot as plt
f = open("English1.txt","r")
corpus = f.read()
" ".join(corpus.split())
f.close()
output=[]
data = re.findall("(?:(?:(?:|\n| |\?|\.|!|,|&|~|\(|\)|\*|_|;|\"|/|:|#| @|< | >|\^|{|}|\[|\]) ?([A-Za-z]+)|(<\w+>)|(\w+-\w+)|(\w+@?\.?\w+.\w+)|((?:\w*\W*\d+\w*\W*/)+\d+)|(/d+/w*/W*\?\w*\W*)|(\w+'\w+)|(\w* ?°? ?\w*)|((?:\d+,)*\d+)) ?((?:\n| |\?|\.|!|,|&|~|\(|\)|\*|_|;|\"|/|:|#| @|< | >|\^|{|}|\[|\]|\^)))",corpus)
                                    
#print data
list_final = []
for i in data:
    for j in i:
        if len(j)>0 and j!=' ' and j!='\n' and j!='\t' :
            list_final.append(j)


list2_final=[]
j=1
p=len(list_final)
for i in range(1,p):
    list2_final.append(list_final[i-1]+ " "+ list_final[i])
   

list_final = list2_final

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
list_p=[]
j =0
for i in final:
	list_p.append(i[0])
	j=j+1
	if j==50:
	    break
w=list_p[0]


plt.plot(range(0,50), list_p[0:50], 'ro')
plt.axis([0, 50 ,0 ,w])
plt.show()
#print list_p
