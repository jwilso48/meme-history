from twitterscraper import query_tweets
import json
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use("ggplot")

json_file = "tweets.json"

def popularity(tweet):
	try:
		# might want to revise this popularity metric to account for number of followers
		return int(tweet.likes + 3*tweet.retweets + tweet.replies)
	except KeyError:
		return 0

def chrono(tweet):
	try:
		return str(tweet.timestamp)
	except KeyError:
		return ""

tweets = query_tweets("rlcs", 100)
tweetpopular = []
for tweet in tweets:
	tweetpopular.append(popularity(tweet))

s = pd.Series(tweetpopular)

tester = s.plot()
fig = tester.get_figure()
fig.savefig("tester.png")


# tweets = sorted(tweets, key = popularity, reverse=True)


# for tweet in tweets:
# 	print(tweet.text)
# 	print(str(popularity(tweet)))
# 	print(str(tweet.likes)+str(tweet.retweets)+str(tweet.replies) + "\n")

