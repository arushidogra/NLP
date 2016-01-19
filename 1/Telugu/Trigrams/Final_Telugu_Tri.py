
# -*- coding: utf-8 -*-
import re
import os
import codecs
f = open("Telugu1.txt","r")
corpus = f.read()

corpus = corpus.decode("utf-8")
f.close()
output=[]
data = re.findall("(?:(?:|\n| |\?|\||\.|!|,|&|~|\(|\)|\*|_|;|\"|/|:|#| @|< | >|\^|{|}|\[|\]) ?([^\x00-x7F]*) ?((?:\n| |\||\?|\.|!|,|&|~|\(|\)|\*|_|;|\"|/|:|#| @|< | >|\^|{|}|\[|\]))|([^\x00-x7F]+-[^\x00-x7F])|((?:[^\x00-x7F]*\W*\d+[^\x00-x7F]*\W*/)+\d+)|(/d+[^\x00-x7F]*/W*\?[^\x00-x7F]\W*)|(<[^\x00-x7F]+>)|([^\x00-x7F]+'[^\x00-x7F]+)|(\|)|([^\x00-x7F]* ?° ?[^\x00-x7F]*)|((?:\d+,)*\d+))",corpus)                                     
list_final = []
#data = unicode(data)
for i in data:
    for j in i:
        if len(j)>0 and j!=' ' and j!='\n' and j!='\t' :
            list_final.append(j)


list2_final=[]
j=2
p=len(list_final)
for i in range(2,p):
    list2_final.append(list_final[i-2]+" " + list_final[i-1]+ " "+ list_final[i])
   

list_final = list2_final

dir_store= {}

for i in list_final:
    dir_store[unicode(i)]=0

for i in list_final :
    dir_store[unicode(i)]+=1


final=[]
for i in dir_store.viewitems():
    p = list(i)
    p.reverse()
    final.append(p)

final.sort()
final.reverse()

os.system("touch trigram_telugu_output.txt")
r = open("trigram_telugu_output.txt","wb")


for i in final:
    string = "('" + i[1] + "')    " + str(i[0]) + "\n"
    string = string.encode("UTF-8")
    r.write(string)

r.close()


