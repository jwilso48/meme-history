from twitterscraper import query_tweets
import json
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import matplotlib
import twitterscraper
matplotlib.style.use("ggplot")

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

def getTweetString(tweet):
	return(str(tweet.user)+"\t"+str(tweet.id)+"\t"+str(tweet.timestamp)+"\t"+str(tweet.fullname)+"\t"+str(tweet.text)+"\t"+str(tweet.replies)+"\t"+str(tweet.retweets)+"\t"+str(tweet.likes))

query = input("What tweets do you want to search for?")
amount = input("How many tweets would you like to get?")

tweets = query_tweets(query, int(amount))


with open("output.txt", "w", encoding="utf-8") as out:
	for tweet in tweets:
		out.write(getTweetString(tweet)+"\n")



# completed = subprocess.call(args= ["cd",  "C:\Users\Kevin\Documents\Bowdoin\Fall 2017\MHacks")
# completed = subprocess.call(args=["twitterscraper", query, "--limit", amount, "--output=tweets.json"], shell=True)

# tweetpopular = []
# for tweet in tweets:
#   tweetpopular.append(popularity(tweet))

# s = pd.Series(tweetpopular)

# tester = s.plot()
# fig = tester.get_figure()
# fig.savefig("tester.png")



# tweets = sorted(tweets, key = popularity, reverse=True)


# for tweet in tweets:
#   print(tweet.text)
#   print(str(popularity(tweet)))
#   print(str(tweet.likes)+str(tweet.retweets)+str(tweet.replies) + "\n")

