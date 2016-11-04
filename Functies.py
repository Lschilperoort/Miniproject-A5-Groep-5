from TwitterAPI import *
import csv
import datetime
import time
# De eerste versie van het programma. Eerst vraagt het om input, slaat het op in een csv bestand, waarna het vraagt voor een acceptatie.
# Als het geaccepteerd word, (door "accepted" in te vullen) word het geupload naar dit twitteraccount: https://twitter.com/NSzuiltestGr5 , waarna tweetfile.csv word gewiped.
# Als je rejected invult, dan word het opgeslagen in een apart logbestand, en word tweetfile.csv ook gewiped.
#Na het draaien van deze functies laat het programma de laatste 5 tweets zien, dat om de 5 minuten ververst.

CONSUMER_KEY = 'Lr8Fyk842NTJBE7vqwvfOWMj4'
CONSUMER_SECRET = 'uAc3qvGnk49p4aFYmtEEAeaEBLOw8WjDHBwFjq87bD3RL6OhUS'
ACCESS_TOKEN_KEY = '793404803615428608-vXxKpDgWHud5PQpSi7E5XrFmA5tCS6n'
ACCESS_TOKEN_SECRET = 'lPAbEYvKyznrTN1jn9Rw7wwrOt7JIVixFI5vMmxVMUWQb'
api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)



def tweetLezen():

    with open('tweetfile.csv') as TweetBestand:
        infile = csv.reader(TweetBestand, delimiter='\n')
        tweets = list(infile)
    return tweets






def tweetuploaden(TWEET_TEXT):
    r = api.request('statuses/update', {'status': TWEET_TEXT})
    global tweet
    time.sleep(10)
    tweet = tweetLezen()
    print('SUCCESS' if r.status_code == 200 else 'FAILURE')

def Tweetlog(tweet):
    datum = datetime.datetime.now()
    csv = open('rejectedTweets.csv', 'a')
    csv.write(tweet + ' - ')
    csv.write(str(datum) + '\n')
    csv.close()

def quit():
    csv = open('tweetfile.csv', 'w+')
    csv.close()

def tweet_raw(tweet):
    if len(tweet) >= 141 or len(tweet) < 1:
        print('tweet is te lang, of u heeft niks ingevuld ')
    else:
        csv = open('tweetfile.csv', 'a')
        csv.write(tweet + '\n')
        return tweet




def tweetweergeven():
    i = 0
    tweets = ['', '', '']
    pager = TwitterRestPager(api, 'search/tweets', {'q': 'from:NSZuilTestGr5', 'count': 3})
    for item in pager.get_iterator():
        tweets[i] = item['text']
        i = i + 1
        if i == 3:
            i = 0
            return tweets


