import tweepy
import twitter_credentials

client = tweepy.Client(bearer_token=twitter_credentials.BEARER_TOKEN)
query = 'covid'
response = client.search_recent_tweets(query=query, max_results=20)
print(response)

auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN,twitter_credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)