import twitter

def search(qstring, tweets):
    return list(filter(lambda x: x['text'].find(qstring) != -1, tweets))
