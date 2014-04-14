
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
	print uniqueWords.most_common(30)

	# For top common filtered words, get phrases of length 5 containing them

	# Compute the syllable length for each phrase

	# Select the two most commonly tweeted phrases with 5 syllables and the most commonly tweeted phrase with 7 syllables

	# Construct the haiku

