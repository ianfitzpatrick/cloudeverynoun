from random import randint, shuffle
import codecs, os

def shuffle_word_list(filename):
	full_filename = os.getcwd() + '/' + filename
	words = codecs.open(full_filename,"r", "utf-8").read().split('\n')
	shuffle(words)	

	new_file = open(os.getcwd() + '/' + 'new_word_list.txt', 'a')
	
	nwl = ''
	for item in words:
		nwl += item + '\n'

	new_file.write(nwl.encode('utf-8'))

