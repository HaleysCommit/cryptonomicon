
# import the module
import tweepy
  
consumer_key = 'x'
consumer_secret = 'gon'
access_token = 'give'
access_token_secret = 'it to ya'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# the ID of the user - use https://commentpicker.com/twitter-id.php
id = 1366256262921523205
  
# fetching the user
user = api.get_user(id)
  
# fetching the followers_count
followers_count = user.followers_count
  
print("The number of followers of the user are : " + str(followers_count))