from token_generator import *
from english_unigrams import unigram_len, unigram_dict
from english_bigrams import bigram_len, bigram_dict
from english_trigrams import trigram_len, trigram_dict

def laplace_tri(line):
	lis_tokens, dic_tokens = trigram_generator(line)
	probability = float(1)
	for token in lis_tokens:
		bigram = token.split()[0]+' '+token.split()[1]
		if token in trigram_dict:
			c = trigram_dict[token]	
		else:
			c = 0
		if bigram in bigram_dict:
			N = bigram_dict[bigram]
		else:
			N = 0
		V = unigram_len
		probability = probability*float((c+1)/float(N+V))
	return probability

def laplace_bi(line):
	lis_tokens, dic_tokens = bigram_generator(line)
	probability = float(1)
	for token in lis_tokens:
		unigram = token.split()[0]
		if token in bigram_dict:
			c = bigram_dict[token]	
		else:
			c = 0
		if unigram in unigram_dict:
			N = unigram_dict[unigram]
		else:
			N = 0
		V = unigram_len
		probability = probability*float((c+1)/float(N+V))
	return probability

def laplace_uni(line):
	lis_tokens, dic_tokens = unigram_generator(line)
	probability = float(1)
	for token in lis_tokens:
		if token in unigram_dict:
			c = unigram_dict[token]	
		else:
			c = 0
		V = unigram_len
		probability = probability*float((c+1)/float(V+V))
	return probability


def laplace():
	f = open('English.txt', 'r')
	i = 1
	print 'Probabilities'
	for line in f.readlines():
		probability = laplace_tri(line)
		print 'line', i, ':', probability
		i = i+1
	f.close()


def laplace_interpolation():
	f = open('English.txt', 'r')
	i = 1
	print 'Probabilities'
	for line in f.readlines():
		probability = 0.5*laplace_tri(line) + 0.3*laplace_bi(line) + 0.2*laplace_uni(line)
		print 'line', i, ':', probability
		i = i+1
	f.close()

def calculate_prob(token, bins, gram_dict, gram_len):
	if token in gram_dict:
		rstar = -1
		r = gram_dict[token]
		for key, value in sorted(bins.iteritems()):
			if key>r and value>0:
				rstar = float((r+1)*value/float(bins[r]))
				break
		if rstar == -1:
			rstar = r+1
		rstar = float(rstar/float(gram_len))
	else:
		rstar = float(bins[1]/float(gram_len))
	return rstar

def good_turing():
	bins = {}
	for key, value in sorted(trigram_dict.iteritems()):
		if value in bins:
			bins[value] += 1
		else:
			bins[value] = 1
	f = open('English.txt', 'r')
	i = 1
	print 'Probabilities'
	for line in f.readlines():
		probability = float(1)
		lis_tokens, dic_tokens = trigram_generator(line)
		for token in lis_tokens:
			probability = probability*float(calculate_prob(token, bins, trigram_dict, trigram_len)) 
		print 'line', i, ':', probability
		i = i+1

def good_turing_interpolation():
	bins_tri = {}
	bins_bi = {}
	bins_uni = {}
	for key, value in sorted(trigram_dict.iteritems()):
		if value in bins_tri:
			bins_tri[value] += 1
		else:
			bins_tri[value] = 1
	for key, value in sorted(bigram_dict.iteritems()):
		if value in bins_bi:
			bins_bi[value] += 1
		else:
			bins_bi[value] = 1
	for key, value in sorted(unigram_dict.iteritems()):
		if value in bins_uni:
			bins_uni[value] += 1
		else:
			bins_uni[value] = 1

	f = open('English.txt', 'r')
	i = 1
	print 'Probabilities'
	for line in f.readlines():
		
		final_prob = float(0)

		probability = float(1)
		lis_tokens, dic_tokens = trigram_generator(line)
		for token in lis_tokens:
			probability = probability*float(calculate_prob(token, bins_tri, trigram_dict, trigram_len)) 
		
		final_prob += 0.5*probability

		probability = float(1)
		lis_tokens, dic_tokens = bigram_generator(line)
		for token in lis_tokens:
			probability = probability*float(calculate_prob(token, bins_bi, bigram_dict, bigram_len)) 
		
		final_prob += 0.3*probability

		probability = float(1)
		lis_tokens, dic_tokens = unigram_generator(line)
		for token in lis_tokens:
			probability = probability*float(calculate_prob(token, bins_uni, unigram_dict, unigram_len)) 
				
		final_prob += 0.2*probability

		print 'line', i, ':', final_prob
		i = i+1

if __name__ == '__main__':
	laplace()
	print
	laplace_interpolation()
	print 
	good_turing()
	print
	good_turing_interpolation()
	print