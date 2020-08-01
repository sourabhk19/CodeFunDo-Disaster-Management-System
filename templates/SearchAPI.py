import _credentials
import time

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

API_MAX = 100

def fetch(query, geocode = None, count = 100, filter_out_retweets = True):
    # return AT LEAST 'count' tweets
    # Note: Twitter Search API allows searching only in the past 7 days
    oauth = OAuth(_credentials.ACCESS_TOKEN,_credentials.ACCESS_SECRET,
                  _credentials.CONSUMER_KEY, _credentials.CONSUMER_SECRET)
    twitter = Twitter(auth=oauth)

    tweets = []
    next_max_id = None

    if filter_out_retweets:
        query += ' -filter:retweets'

    while len(tweets) < count:
        try:
            results = twitter.search.tweets(q=query, count=API_MAX,
                                          max_id = next_max_id, geocode = geocode)
        except Exception as e:
            print(e)
            print ('[%s] Sleeping 5 minutes...' % time.ctime())
            time.sleep(10)
            continue

        for result in results["statuses"]:
            text = result["text"].encode('utf-8').strip()
            location = result["user"]["location"].encode('utf-8').strip()
            #coordinates =result["coordinates"].encode('utf-8').strip()
            #name=result["name"].encode('utf-8').strip()
            tweet = {"timestamp" : result["created_at"],
                     "text" : text,
                     "location" : location,
                     "coordinates" : result["coordinates"],
                     "retweet" : result["retweet_count"],
                     }
            print ('[%d] %s' % (len(tweets),tweet))
            tweets.append(tweet)
            if not next_max_id:
                next_max_id = result["id"]
            else:
                next_max_id = min(result["id"], next_max_id)
        next_max_id -= 1


    return tweets