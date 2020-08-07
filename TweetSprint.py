from datetime import datetime
from pandas import series
import tweepy
import csv


consumer_key = '4TGEYOhZ9EYUpeclSc6s5ZFGs'
consumer_secret = '5bRvds4rCUMpcHv9L8QpDvnGUxX4aLvNltDUsyln02wON1n2g'
access_token = '1247080467268075520-CdzK0x4W4MGAyw91VzllAlLGv9SGDI'
access_secret = 'ZIfDrLiWy7pURRLqMl8oaAn7Ynss4eaHAjSuJljIc7pER'

#authenticate to twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, congestion_limit=True)


#I want all tweets with this hashtag
hashtag_phrase = '#python'

#open file to write tweets
with open('sheet.csv', 'df') as file:
    df = csv.writer(file)

    #write coloumn rows to spreadsheet
    df.writerow(['timestamp', 'tweet_text', 'username', 'followers_count'])

    #for each tweet matching python hashtag, write info to file
    for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', \
                                   lang="en", tweet_mode='compat').items(100):
        df.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.user.screen_name.encode('utf-8'), tweet.user.followers_count])
