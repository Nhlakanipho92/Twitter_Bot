import tweepy
import time


# API Keys to get access the tweepy API.
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()

print(user.name)  # prints your name.
print(user.screen_name)
print(user.followers_count)

search = ' '
number_of_tweets = 2  # Can be abjects to fit bot needs


# intent of rate limits is to protect you from unintended use,
# and consequently an unexpected increase in cost
def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)  # Delays after ratelimit is hit then restarts


# Fellows everyone back
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Username':
        print(follower.name)
        follower.follow()


# Tweets, retweet anything with the keywords
for tweet in tweepy.Cursor(api.search, search).items(number_of_tweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

