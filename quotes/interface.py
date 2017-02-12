import twitter
import json

import db

def search(qstring, tweets):
    return list(filter(lambda x: x['text'].find(qstring) != -1, tweets))

def getQuotes(word):
    noQuotes = json.dumps([['No quotes found!', 'sorry']])
    s = db.scoreSearch(word)
    if s:
        return json.dumps(s)

    syns = [list(a.keys())[0] for a in getSynonyms(word)]
    if len(syns) == 0:
        return noQuotes

    for synonym in syns:
        s = db.scoreSearch(synonym)
        if s:
            return json.dumps(s)

    return noQuotes

def doRunTweet(tweet):
    sTweet = sortTweet(tweet['text'])
    tweetScores = processSortedTweet(sTweet)
    db.store(tweet, tweetScores)

def getSynonyms(word):
    if word.upper() in thesaurus:
        return thesaurus[word.upper()]
    else:
        return []
with open('ea-thesaurus.json') as thesaurus_f:
    thesaurus = json.loads(thesaurus_f.read())

def isRealWord(word):
    return word in dictionary
with open('wordlist') as dictionary_f:
    dictionary = [w.upper() for w in dictionary_f.readlines()]

def sortTweet(text):
    processedTweet = text.upper()
    processedTweet = processedTweet.replace('.', ' ').replace('\n', ' ')
    processedTweet = ''.join(filter(lambda x: str.isalpha(x) or x == ' ', processedTweet))
    print(processedTweet)
    processedTweet = processedTweet.split()
    processedTweet = [word for word in processedTweet if not (word in stopwords)]
    wordScores = {}
    for word in processedTweet:
        if isRealWord(word):
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
