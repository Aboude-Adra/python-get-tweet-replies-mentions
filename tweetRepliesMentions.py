import tweepy, searchtweets
import random, os, math, re, json, base64, hmac, hashlib, requests
from datetime import datetime, timedelta
from collections import Counter, OrderedDict

# Configuration (refer to README for more info)
CONSUMER_KEY= "YOUR_APP_CONSUMER_KEY_HERE"
CONSUMER_SECRET= "YOUR_APP_CONSUMER_SECRET_HERE"
ENDPOINT= "YOUR_ENDPOINT_HERE"
TYPE= "YOUR_SEARCH_API_ACCESS_TYPE"
QUERY_MAX = 500
TOTAL_MAX = 2500

def main():
    # Tweepy and SearchTweets initialization
    auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    api = tweepy.API(auth)
    os.environ["SEARCHTWEETS_CONSUMER_KEY"] = CONSUMER_KEY
    os.environ["SEARCHTWEETS_CONSUMER_SECRET"] = CONSUMER_SECRET
    os.environ["SEARCHTWEETS_ENDPOINT"] = ENDPOINT
    os.environ["SEARCHTWEETS_ACCOUNT_TYPE"] = TYPE
    premium_search_args = searchtweets.load_credentials()
    #TODO: Validate input
    print("\nKindly input the Tweet link:")
    link = input()
    #TODO: handle API errors
    print("\nConnecting to Twitter...")
    tweetId = link.split('/')[-1]
    userTweet = api.get_status(id=tweetId, tweet_mode="extended")
    screen_name = userTweet.author.screen_name
    queryText = "to:" + screen_name
    query = {"query":queryText,"maxResults":500}
    replies = searchtweets.collect_results(query,max_results=2500,result_stream_args=premium_search_args)
    
    print("\nGetting Tweet comments...")
    comments = []
    for reply in replies:
        if reply.in_reply_to_status_id==tweetId:
            comments.append(reply)
    
    print("\nProcessing comments...")
    mentions = []
    for comment in comments:
        for mention in comment['entities']['user_mentions']:
            if mention['screen_name'] != screen_name: # appending screen_name only if it's not the author of the tweet
                mentions.append(mention['screen_name'])
    # Using collections.Counter to get count of each mention
    uniqueMentions = Counter(mentions)
    orderedMentions = OrderedDict(uniqueMentions.most_common())
    print("\n========== Accounts mentioned in the comments (sorted) ==========\n")
    for key in orderedMentions:
        print(key + "," + str(orderedMentions[key])) #printing separated by a comma for the ability to use as a csv

main()
