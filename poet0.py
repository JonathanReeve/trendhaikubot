
from collections import Counter
import re

def writehaiku(trend, tweets):

	# Print preamble
	print "Poet0 is busy writing a haiku for trend " + trend + "...\n"

	# Create list of words in tweets
	allWords = []
	for tweet in tweets:
		allWords.extend(tweet.text.split())

	# Filter the word list (url, RT, @*, length >= 5)


	# Get the list of unique words with their counts
	uniqueWords = Counter(allWords)

	# Get the most common 5 words
	topWords = uniqueWords.most_common(5)

	# For top common filtered words, get phrases of length 5 containing them
	phrases = []
	n = 5
	for word in topWords:
		idx = n-1
		try:
			while allWords[idx:len(allWords)-n].index(word[0])>=0:
				idx = allWords[idx:len(allWords)-n].index(word[0]) + idx
				for i in range(0,n):
				    phrases.append(" ".join(allWords[(idx - i):(idx - i + n)]))
				idx += 1
		except:
			idx = 0


	uniquePhrases = Counter(phrases)
	print uniquePhrases.most_common(20)

	# Compute the syllable length for each phrase

	# Select the two most commonly tweeted phrases with 5 syllables and the most commonly tweeted phrase with 7 syllables

	# Construct the haiku

