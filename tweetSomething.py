import tweepy

consumer_key = "T0ohellogCDRBWrwP"

consumer_secret="NguxUwhellohellohello6uNLEwbTrPamGoB"

access_token = "13655466hellohellohelloijcWPtW5PRC8"

access_token_secret = "HwgU78hello2NUhellohellohellohelloykmFGs6MitFBzo6KymJv"

bearer_token = "AAAAAAAAhelloAAAAAAAAAAhellohellohellohelloEF1VxB206UNzxZZcteW5taV9EEj9"

file_name = "hola.txt"

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret, bearer_token=bearer_token
)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Create Tweet

# The app and the corresponding credentials must have the Write permission

# Check the App permissions section of the Settings tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps

# Make sure to reauthorize your app / regenerate your access token and secret 
# after setting the Write permission

#response = client.create_tweet(
    #text="#lesson  #https://twitter.com/WealthInc247/status/1477993016321261575"
#)
users = client.get_users_following(id='1365546682990145537', max_results=1000)
with open(file_name, 'a+') as filehandler:
  for user in users.data:
    print(user)
    print("")
    filehandler.write(str(user))
    filehandler.write("\n")


#users = client.get_users(usernames=["dogon_matias"])
