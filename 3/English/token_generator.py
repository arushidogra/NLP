import nltk
def trigram_generator(line):
	tri_dict = {}
	tri_list = []
	tokens = nltk.word_tokenize(line)
	for i in xrange(len(tokens)-2):
		var = tokens[i]+' '+tokens[i+1]+' '+tokens[i+2]
		tri_list.append(var)
		try:
			tri_dict[var] += 1
		except:
			tri_dict[var] = 1

	return tri_list, tri_dict 

def bigram_generator(line):
	bi_dict = {}
	bi_list = []
	tokens = nltk.word_tokenize(line)
	for i in xrange(len(tokens)-1):
		var = tokens[i]+' '+tokens[i+1]
		bi_list.append(var)
		try:
			bi_dict[var] += 1
		except:
			bi_dict[var] = 1

	return bi_list, bi_dict 

def unigram_generator(line):
	uni_dict = {}
	uni_list = []
	tokens = nltk.word_tokenize(line)
	for i in xrange(len(tokens)):
		var = tokens[i]
		uni_list.append(var)
		try:
			uni_dict[var] += 1
		except:
			uni_dict[var] = 1

	return uni_list, uni_dict 
