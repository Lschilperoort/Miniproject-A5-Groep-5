from TwitterAPI import *
import csv
import datetime
import time

CONSUMER_KEY = 'Lr8Fyk842NTJBE7vqwvfOWMj4'
CONSUMER_SECRET = 'uAc3qvGnk49p4aFYmtEEAeaEBLOw8WjDHBwFjq87bD3RL6OhUS'
ACCESS_TOKEN_KEY = '793404803615428608-vXxKpDgWHud5PQpSi7E5XrFmA5tCS6n'
ACCESS_TOKEN_SECRET = 'lPAbEYvKyznrTN1jn9Rw7wwrOt7JIVixFI5vMmxVMUWQb'
api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
teller = 0


def tweetLezen():
    """Leest de tweets uit bestand"""
    global teller

    with open('tweetfile.csv') as TweetBestand:
        infile = csv.reader(TweetBestand, delimiter='\n')
        tweets = list(infile)
        if teller < len(tweets):
            tweet = tweets[teller][0]
            teller += 1
            return tweet
        TweetBestand.close







def tweetuploaden(TWEET_TEXT):
    """Upload een tweet naar twitter"""
    r = api.request('statuses/update', {'status': TWEET_TEXT})
    tweet = tweetLezen()
    print('SUCCESS' if r.status_code == 200 else 'FAILURE')

def Tweetlog(tweet):
    """Slaat tweet op in logbestand met datum"""
    datum = datetime.datetime.now()
    csv = open('rejectedTweets.csv', 'a')
    csv.write(str(tweet) + ' - ')
    csv.write(str(datum) + '\n')
    csv.close()

def quit():
    """wist bestand die tweets bevat"""
    csv = open('tweetfile.csv', 'w+')
    csv.close()

def tweet_raw(tweet):
    """Checkt. of de tweet niet te lang is en anders wordt het opgeslagen in tweet bestand"""
    if len(tweet) >= 141 or len(tweet) < 1:
        print('tweet is te lang, of u heeft niks ingevuld ')
    else:
        csv = open('tweetfile.csv', 'a')
        csv.write(tweet + '\n')
        return tweet




def tweetweergeven():
    """Haalt tweets op van twitter en laat ze zien"""
    i = 0
    tweets = ['', '', '']
    pager = TwitterRestPager(api, 'search/tweets', {'q': 'from:NSZuilTestGr5', 'count': 3})
    for item in pager.get_iterator():
        tweets[i] = item['text']
        i = i + 1
        if i == 3:
            i = 0
            return tweets



