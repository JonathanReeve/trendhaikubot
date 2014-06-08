
import re
import nltk



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



# Return the number of syllables in a sentence
from nltk.corpus import cmudict
d = cmudict.dict()
# Stolen from http://stackoverflow.com/a/4103234/1467617
def nsyl(word):
    return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]

def nsyllables(sentence):
    numSyls = 0
    words = sentence.strip().split(' ')
    for word in words:
        numSyls = numSyls + nsyl(word)
    return numSyls

