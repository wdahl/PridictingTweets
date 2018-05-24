#William Dahl
#ICSI 431 Data Mining
#April 11th, 2018

#imports regualr expression procesor
import re

#Node class to hold word and count of word
class Node:
	data = "" #holds the word
	count = 0 #holds the count of the word

#checks if the word is already in the list
def inList(word, link):
	#loops through the list
	for node in link:
		#checks if the word equals to the current node
		if node.data == word:
			node.count += 1 #increases the count of the word
			return True

	return False

#sorts the list based on count of words
def sort(link):
	#bubble sort algorithm
	for i in range(len(link)-1, 0, -1):
		for j in range(i):
			if link[j].count < link[j+1].count:
				temp = link[j]
				link[j] = link[j+1]
				link[j+1] = temp

	return link #returns the sorted list 

#prints the 10 most common words
def print_list(link):
	for i in range(0, 10):
		print link[i].data

#checks if the word is a number
def isInt(s):
	try:
		int(s)
		return True

	except ValueError:
		return False

#opens the labled tweets file for reading
with open("labled_tweets.txt", "r") as f:
	words = f.read().lower()#reads the words from the file as all lowercase 
	words = re.split("[, ; \" . ! ? \' ( ) '\n' \\ : # & / * \[ \] -]", words)#splits the words up based on special charecters

link = list()#list of nodes
#loops through words
for word in words:
	#checks if the word is longer or than 2 letters and the it is not one of these generic words
	if len(word) > 2 and word != "https" and word != "the" and word != "and" and word != "you" and word != "for" and word != "are" and word != "this" and word != "that" and word != "have" and word != "que" and word != "with" and word != "but" and word != "from" and word != "because" and word != "their" and word != "these" and word != "they" and word != "about" and word != "has" and word != "out" and word != "without" and word != "little" and word != "crying" and word != "left" and word != "favorite":
		#checks if the word is a number
		if isInt(word) == False:
			#checks if the word is a user name
			if "@" not in word and "\\" not in word:
				#checks if the word is already in the list
				if inList(word, link) == False:
					node = Node() # creastes a new node
					node.data = word #sets the data of the node to the word
					link.append(node)#adds the node to the list

link = sort(link)#sorts the list
print_list(link)#prints ten most frequent words in list