import tweepy
from tweepy import OAuthHandler
import TwitterStreamer
from tweepy import Stream

class TwitterReader:

	def __init__(self):
		with open("keys.txt") as f:
			consumer_key = f.readline()
			consumer_secret = f.readline()
			access_token = f.readline()
			access_secret = f.readline()

		self.auth = OAuthHandler(consumer_key, consumer_secret)
		self.auth.set_access_token(access_token, access_secret)
		self.api = tweepy.API(self.auth)
		
	def getMyTweets(self):
		resultSet = []
		for tweet in self.api.user_timeline():
		    resultSet.append(tweet.text)
		return resultSet

	def getUserTweets(self, user, count=100):
		resultSet = []
		for tweet in self.api.user_timeline(user):
		    resultSet.append(tweet.text)
		return resultSet
	
	def getHomeTweets(self):
		resultSet = []
		for tweet in self.api.home_timeline():
			resultSet.append(tweet.text)
		return resultSet
		
	def getMyFriends(self):
		pass

	def streamATopic(self, topic, file):
		twitter_stream = Stream(self.auth, TwitterStreamer.MyListener(file))
		twitter_stream.filter(track=[topic])

