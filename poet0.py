
from collections import Counter
import re

# Stolen from http://stackoverflow.com/a/7995979/584121 
# Checks whether a word is a URL
def is_valid_url(url):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url) 

# Checks whether a word is a twitter user
def is_twitter_user(word): 
    twitter_username_re = re.compile(r'@([A-Za-z0-9_]+)')
    return twitter_username_re.search(word)

# Checks whether a word is a hashtag 
def is_hashtag(word): 
    hashtag_re = re.compile(r'#([A-Za-z0-9_]+)')
    return hashtag_re.search(word)

def writehaiku(trend, tweets):

    # Print preamble
    print "Poet0 is busy writing a haiku for trend " + trend + "...\n"

    # Create list of words in tweets
    allWords = []
    for tweet in tweets:
        allWords.extend(tweet.text.split())

    invalidWords = [] 
    for word in allWords: 
        # remove URLs and twitter users and hashtags
        if is_valid_url(word) or is_twitter_user(word) or is_hashtag(word): 
            invalidWords.append(word) 
        # remove non-alpha words
        if not word.isalpha(): 
            invalidWords.append(word) 
        # remove words fewer than four characters or more than 25
        if len(word)<4 or len(word)>25: 
            invalidWords.append(word) 

    filteredWords = [word for word in allWords if word not in invalidWords] 

    print "Filtered wordlist is now: "
    print filteredWords

    # Get the list of unique words with their counts
    uniqueWords = Counter(filteredWords)

    # Get the most common 5 words
    mostCommon = uniqueWords.most_common(100)
    print "Most common words are: "
    print mostCommon

    # Filter the word list (url, RT, @*, length >= 5)

    # For top common filtered words, get phrases of length 5 containing them

    # Compute the syllable length for each phrase

    # Select the two most commonly tweeted phrases with 5 syllables and the most commonly tweeted phrase with 7 syllables

    # Construct the haiku

