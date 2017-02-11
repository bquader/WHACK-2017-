import twitter
import json

def search(qstring, tweets):
    return list(filter(lambda x: x['text'].find(qstring) != -1, tweets))

def wordIsGood(word):
    return True

with open('ea-thesaurus.json') as thesaurus_f:
    thesaurus = json.loads(thesaurus_f.read(), 'lxml')
def getSynonyms(word):
    if word.upper() in thesaurus:
        return thesaurus[word.upper()]
    else:
        return [{ word.upper(): '20' }]

with open('stopwords.json') as stopwords_f:
    stopwords = json.loads(stopwords_f.read(), 'lxml')
def sortTweet(text):
    processedTweet = text.upper()
    processedTweet = processedTweet.split(' ')
    processedTweet = [word for word in processedTweet if not (word in stopwords)]
    wordScores = {}
    for word in processedTweet:
        synonyms = getSynonyms(word)
        synonyms.append({ word : '30' })
        for s in synonyms:
            synonym = list(s.keys())[0]
            score = int(s[synonym])
            if synonym in wordScores:
                wordScores[synonym] += score
            else:
                wordScores[synonym] = score
    return wordScores
