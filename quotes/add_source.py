import twitter
import interface_local as interface

name = input('Source Twitter handle?')
tweets = twitter.getTweetsFromUser(name)
for t in tweets:
    interface.doRunTweet(t)
