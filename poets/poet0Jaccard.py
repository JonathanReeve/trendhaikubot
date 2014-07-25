
from collections import Counter
import re
import supportFunctions as sf
import logging
import haiku as h
import distance as d

def writehaiku(trend, tweets):

    # Print preamble
    #print "Poet0: "

    # Create list of words in tweets
    allWords = []
    for tweet in tweets:
        allWords.extend(tweet.text.split())

    invalidWords = [] 
    for word in allWords: 
        # remove URLs and twitter users and hashtags
        if sf.is_valid_url(word) or sf.is_twitter_user(word) or sf.is_hashtag(word): 
            invalidWords.append(word) 
        # remove non-alpha words
        if not word.isalpha(): 
            invalidWords.append(word) 
        # remove words fewer than four characters or more than 25
        if len(word)<4 or len(word)>25: 
            invalidWords.append(word) 

    filteredWords = [word for word in allWords if word not in invalidWords] 

    #logging.debug("Filtered wordlist is now: ") 
    #logging.debug(filteredWords) 

    # Get the list of unique words with their counts
    uniqueWords = Counter(filteredWords)

    # Get the most common words
    topWords = uniqueWords.most_common(5)

    # For top common filtered words, get phrases of length 5 containing them
    phrases = []
    for n in range(2,7):
        for word in topWords:
            idx = n-1
            try:
                while filteredWords[idx:len(filteredWords)-n].index(word[0])>=0:
                    idx = filteredWords[idx:len(filteredWords)-n].index(word[0]) + idx
                    for i in range(0,n):
                        phrases.append(" ".join(filteredWords[(idx - i):(idx - i + n)]))
                    idx += 1
            except:
                idx = 0

    uniquePhrases = Counter(phrases)
    topPhrases = uniquePhrases.most_common(200)

    # Compute the syllable length for each phrase
    listPhrases = [list(phrase) for phrase in topPhrases]
    for phrase in listPhrases:
        phrase.append(sf.nsyllables(phrase[0]))

    # Use Jaccard similarity to choose top-tweeted phrases that are not similar to one another
    Phrase1 = ''
    Phrase2 = ''
    Phrase3 = ''

    # Populate 7-syllable phrase first with the top-tweeted phrase of five syllables
    for phrase in listPhrases:
        if phrase[2] == 7 and Phrase1 == '':
            Phrase2 = phrase[0]
            break


    # Get list of 5-syllable phrases and compute their Jaccard similarities from the 2nd
    # Choose the one that is popular with smaller Jaccard similarity
    if Phrase2 != '':
        for phrase in listPhrases:
            if phrase[2] == 5 and d.jaccard(Phrase2, phrase[0]) >= .4:
                if Phrase1 == '':
                    Phrase1 = phrase[0]

    # Get list of 5-syllable phrases and compute their Jaccard similarities from the 1st and 2nd
    # Choose the one that is popular with smaller Jaccard similarity
    if Phrase2 != '' and Phrase1 != '':
        for phrase in listPhrases:
            if phrase[2] == 5 and d.jaccard(Phrase2, phrase[0]) >= .6 and d.jaccard(Phrase1, phrase[0]) >= .6:
                if Phrase3 == '':
                    Phrase3 = phrase[0]


    myHaiku = h.Haiku()

    # Construct the haiku
    if Phrase1 != '' and Phrase2 != '' and Phrase3 != '':
        myHaiku.length = len(Phrase1) + len(Phrase2) + len(Phrase3)
        myHaiku.text = [Phrase1, Phrase2, Phrase3]
        #return [[Phrase1, Phrase2, Phrase3], len(Phrase1) + len(Phrase2) + len(Phrase3)]

    return myHaiku
