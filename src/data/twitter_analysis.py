
# import the module
import tweepy
  
consumer_key = 'JLeTg8YiNoh7B89X9XUZx5ftm'
consumer_secret = 'TDBs2ZLqx7UmQQOLyUXvvpzIIRSIiyvPlfG39HxEhifV3A5JYr'
access_token = '1384697559931756548-mERvdpO7ECoaVNHQd8RKmQ37R3T74x'
secret_token = 'lIGhfJvU0GlF3sb7VOdxO3FpN01LlMonGhJ96RKsF1Kq5'

bearer_token = 'AAAAAAAAAAAAAAAAAAAAANUyOwEAAAAAQ%2BG3hHsiUozETzs6gfPT2%2BpKECM%3DYhiwSSHQ2urFuvbEBsED9jPcQYtSxHC8OW5xz6g5EFL4k37x7X'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, secret_token)
api = tweepy.API(auth)

# the ID of the user - use https://commentpicker.com/twitter-id.php
id = 1366256262921523205
  
# fetching the user
user = api.get_user(id)
  
# fetching the followers_count
followers_count = user.followers_count
  
print("The number of followers of the user are : " + str(followers_count))