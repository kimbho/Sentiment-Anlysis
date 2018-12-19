import csv
import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 2 - Retrieve Tweets
public_tweets = api.search('Modi')



with open('output.txt', mode='w') as csv_file:
	writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	for tweet in public_tweets:
		#Step 3 Perform Sentiment Analysis on Tweets
		analysis = TextBlob(tweet.text)
		#Step 4 Write the results to a CSV file
		writer.writerow(['[Original tweet]', '[Analysis]'])
		writer.writerow([tweet.text, analysis.sentiment])
