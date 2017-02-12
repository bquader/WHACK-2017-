import twitter
import interface

name = input('Source Twitter handle?')
tweets = twitter.getTweetsFromUser(name)
for t in tweets:
    interface.doRunTweet(t)
