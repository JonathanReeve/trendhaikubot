import re
import supportFunctions as sf
import logging
import haiku as h
import nltk

def writehaiku(trend, tweets): 

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

    tagged = nltk.pos_tag(filteredWords) 
    
    line1 = "" 
    for word in tagged: 
        if line1 != "": 
            continue
        else: 
            if sf.nsyl(word[0]) == 2 and word[1]=='NN': 
                if word[0][0] in ['a', 'e', 'i', 'o', 'u', 'y']:  
                    line1 = "I am an "+word[0]+"."
                else: 
                    line1 = "I am a "+word[0]+"."
    
    word2 = "" 
    for word in tagged: 
        if word2 != "": 
            continue
        else: 
            if sf.nsyl(word[0]) == 3 and word[1]=='NNP': 
                word2 = word[0]

    word3 = ""
    for word in tagged: 
        if word3 != "": 
            continue
        else: 
            if sf.nsyl(word[0])== 1 and word[1]=='NN': 
                word3 = word[0]

    line2 = "and {} is my {}.".format(word2, word3) 

    line3 = ''
    for word in tagged: 
        if line3 != "": 
            continue
        else: 
            if sf.nsyl(word[0]) == 1 and word[1]=='VB': 
                line3 = "I {} with the night!".format(word[0])

    out = line1 + '\n' + line2 + '\n' + line3

    return out
