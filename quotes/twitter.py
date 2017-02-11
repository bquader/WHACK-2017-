from twython import Twython

APP_KEY='0Xiv1GS7kKlK3lL2ruJLa1MQ8'
ACC_TOKEN='AAAAAAAAAAAAAAAAAAAAALTihAAAAAAA8%2FgU%2BrbioqEBxQ9W3npH7vlHj20%3DVtyK9oW9thmN7HVnmmAaRbKSC43fN3GbgGVmNh1F5uK4RnIy2w'

twitter = Twython(APP_KEY, access_token=ACC_TOKEN, oauth_version=2)

def getTweetsFromUser(user, limit=1000):
    BATCH_SIZE = 100
    res = []
    lastId = None
    
    for i in range(0, limit, BATCH_SIZE):
        if lastId:
            apiResponse = twitter.get_user_timeline(screen_name=user,count=BATCH_SIZE, max_id=lastId)
        else:
            apiResponse = twitter.get_user_timeline(screen_name=user,count=BATCH_SIZE)

        lastId = apiResponse[-1]['id']

        for tweet in apiResponse:
            res.append(readTweet(tweet))

    return res

def readTweet(tweet):
    return {
        'retweet_count': tweet['retweet_count'],
        'text': tweet['text']
    }
