def rev_sentence(sentence):
	#first split the sentence into words
	words = sentence.split(' ')
	#then reverse the split string list and join using space
	reverse_sentence = ' '.join(reversed(words))
	#finaly return the joined string
	return reverse_sentence 

if __name__ == "__main__":
	input = 'geeks quiz practice code'
	print(rev_sentence(input))
