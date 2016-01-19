
# -*- coding: utf-8 -*-
import re
import os
f = open("English1.txt","r")
corpus = f.read()
f.close()
data = re.findall("(?:(?:(?:|\n| |\?|\.|!|,|&|~|\(|\)|\*|_|;|\"|/|:|#| @|< | >|\^|{|}|\[|\]) ?([A-Za-z]+)|(<\w+>)|(\w+-\w+)|(\w+@?\.?\w+.\w+)|((?:\w*\W*\d+\w*\W*/)+\d+)|(/d+/w*/W*\?\w*\W*)|(\w+'\w+)|(\w* ?°? ?\w*)|((?:\d+,)*\d+)) ?((?:\n| |\?|\.|!|,|&|~|\(|\)|\*|_|;|\"|/|:|#| @|< | >|\^|{|}|\[|\]|\^)))",corpus)                                   
list_final = []
for i in data:
    for j in i:
        if len(j)>0 and j!=" " and j!="\n"and j!='\t' :
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
#os.system("rm bigram_english_output.txt")
os.system("touch bigram_english_output.txt")
r = open("bigram_english_output.txt","r+")

for i in final:
    string = "('" + i[1] + "')    " + str(i[0]) + "\n"
    r.write(string)

r.close()


	
