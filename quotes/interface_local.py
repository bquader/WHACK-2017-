import twitter
import json

import db_local as db

def search(qstring, tweets):
    return list(filter(lambda x: x['text'].find(qstring) != -1, tweets))

def doRunTweet(tweet):
    sTweet = sortTweet(tweet['text'])
    tweetScores = processSortedTweet(sTweet)
    db.store(tweet, tweetScores)

def getSynonyms(word):
    if word.upper() in thesaurus:
        return thesaurus[word.upper()]
    else:
        return [{ word.upper(): '10' }]
with open('ea-thesaurus.json') as thesaurus_f:
    thesaurus = json.loads(thesaurus_f.read())

def sortTweet(text):
    processedTweet = text.upper()
    processedTweet = processedTweet.replace('.', ' ').replace('\n', ' ')
    processedTweet = ''.join(filter(lambda x: str.isalpha(x) or x == ' ', processedTweet))
    print(processedTweet)
    processedTweet = processedTweet.split()
    processedTweet = [word for word in processedTweet if not (word in stopwords)]
    wordScores = {}
    for word in processedTweet:
        synonyms = getSynonyms(word)
        synonyms.append({ word : '80' })
        for s in synonyms:
            synonym = list(s.keys())[0]
            score = int(s[synonym])
            if synonym in wordScores:
                wordScores[synonym] += score
            else:
                wordScores[synonym] = score
    return wordScores
with open('stopwords.json') as stopwords_f:
    stopwords = json.loads(stopwords_f.read())

def processSortedTweet(scores, threshold=10):
    s = list(scores.items())
    s = [item for item in s if item[1] >= threshold]
    s = sorted(s, key=lambda x: x[1], reverse=True)
    return s
