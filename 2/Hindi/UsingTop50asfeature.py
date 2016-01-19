# -*- coding: utf-8 -*-
'''

STOP WORDS ARE TOP 50 AND NOT INCLUDED AS FEATURE WORDS

'''



import re
import os
import math
from random import randint

import matplotlib.pyplot as plt
def main():
	f = open("Hindi1.txt","r")
	corpus = f.read()
	" ".join(corpus.split())
	f.close()
	output=[]
	data = re.findall("(?:(?:|\n| |\?|\||\.|!|,|&|~|\(|\)|\*|_|;|\"|/|:|#| @|< | >|\^|{|}|\[|\]) ?([^\x00-x7F]*) ?((?:\n| |\||\?|\.|!|,|&|~|\(|\)|\*|_|;|\"|/|:|#| @|< | >|\^|{|}|\[|\]))|([^\x00-x7F]+-[^\x00-x7F])|((?:[^\x00-x7F]*\W*\d+[^\x00-x7F]*\W*/)+\d+)|(/d+[^\x00-x7F]*/W*\?[^\x00-x7F]\W*)|(<[^\x00-x7F]+>)|([^\x00-x7F]+'[^\x00-x7F]+)|(\|)|([^\x00-x7F]* ?° ?[^\x00-x7F]*)|((?:\d+,)*\d+))",corpus)




	final_tokens = []
	punc = (" ","\n",",","|","/",".","?",">","<",":",";","\"","}","]","{","[","\\","+","=","-","_",")","(","*","&","^","%","#","@","!","~")





	for i in data:
 	   	for j in i:
 	       		if len(j)>0 and j!=' ' and j!='\n' and j!='\t' and not j in punc:
 	       	    		final_tokens.append(j)
	dir_store= {}

	for i in final_tokens:
	    dir_store[i]=0
	
	for i in final_tokens :
    		dir_store[i]+=1

	dir_store.pop(" ",None)
	dir_store.pop("\n",None)


	final=[]
	for i in dir_store.viewitems():
	    p = list(i)
	    p.reverse()
	    final.append(p)
	#result1 is all the tokens
	final.sort()
	final.reverse()
	result1=final
	result2=[]
	punct='''!()-[]{};:'"\|,<>./?@#$%^&*_~'''
	stop_word = []
	j=0
	for i in result1:	
		stop_word.append(i[1])
		j=j+1
		if j==50:
			break


	#print final	
	#result2 is top words
        # tokens is the total of tokens
	tokens = []
	for i in xrange(0,len(result1)):
		if result1[i][1].lower() not in punct and result1[i][1].lower() not in stop_word:
			result2.append(result1[i][1])
	for i in xrange(0,len(final_tokens)):
		if final_tokens[i].lower() not in punct:
			tokens.append(final_tokens[i])
	#print result2
		
	feature=[]
	index={}
	for i in xrange(min(250,len(result2))):
		feature.append(result2[i])
		index[result2[i]]=len(feature)-1
	#print tokens
	#print feature
	matrix={}
	rmatrix={}
	for i in xrange(0,len(tokens)):
		if tokens[i] not in matrix:
			matrix[tokens[i]]=[]
			rmatrix[tokens[i]]=[]
			for j in xrange(0,len(feature)):
				matrix[tokens[i]].append(0.0)
				rmatrix[tokens[i]].append(0.0)
		if i-1>=0:
			if tokens[i-1] in feature:
				ind=index[tokens[i-1]]
				matrix[tokens[i]][ind]+=1
		if i+1<len(tokens):
			if tokens[i+1] in feature:
				ind=index[tokens[i+1]]
				rmatrix[tokens[i]][ind]+=1
	for i in matrix:	
		matrix[i].extend(rmatrix[i])
	print feature
	centroid=[]
	centers=[]
	#print matrix
	print tokens
	
	while len(centroid)!=50:
		x=randint(1,len(tokens))
		if x not in centroid:
			centroid.append(x)
			centers.append(matrix[tokens[x]])
#print centers
#	print len(centers)
	for i in xrange(0,50):
		group2[i]=[]
	change=100000
	while change>0:
	 	change*=0
		for i in matrix:
			assign(i,matrix[i],centers)
		calculate(matrix,centers)
	os.system("touch top_50_removed.txt")
	a = open("top_50_removed.txt","r+")
	for i in group2:
		a.write(str(i+1) + ':')
		for j in xrange(min(25,len(group2[i]))):
			a.write(str(group2[i][j]) + ' ')
		a.write("\n")
	


group={}
group2={}
global change
change=100000

def assign(word,vec,centers):
	l=[]
	change=0
	for i in xrange(0,len(centers)):
		dist=0.0
		for j in xrange(0,len(vec)):
			dist+=pow(float(centers[i][j])-float(vec[j]),2)
		dist=math.sqrt(dist)
		g=[]
		g.append(dist)
		g.append(i)
		l.append(g)
	l.sort()
	if(word not in group or l[0][1]!=group[word]):
		change+=1
		if word in group:
			group2[group[word]].remove(word)
	group[word]=l[0][1]
	group2[l[0][1]].append(word)
	
def calculate(matrix,centers):
	for i in group2:
		l=[]
		for k in xrange(len(centers[0])):
			l.append(0.0)
		for j in group2[i]:
		 	vec=matrix[j]
		 	for k in xrange(len(centers[0])):
				l[k]+=vec[k]
		for k in xrange(len(centers[0])):
			if len(group2[i])!=0:
				l[k]/=len(group2[i])
		centers[i]=l
		
main()	

