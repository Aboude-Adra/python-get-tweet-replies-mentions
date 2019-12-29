# python-get-tweet-replies-mentions
## Intro: 
Script for getting all mentions in replies to a specific tweet.

Note: I wrote this script in a hurry(for a one time thing) so didn't take much time to improve it (validate, handle errors, refactor...etc)
## Usage:
1. Install required packages: **tweepy** and **searchtweets**
`pip install PACKAGE_NAME`
2. You'll need to have a Twitter developer account and an app created, refer to [Creating Twitter API Authentication Credentials section in this tutorial](https://realpython.com/twitter-bot-python-tweepy/#creating-twitter-api-authentication-credentials).
2. Replace YOUR_APP_CONSUMER_KEY_HERE and YOUR_APP_CONSUMER_SECRET_HERE with your keys after you create your twitter app.
3. Replace YOUR_ENDPOINT_HERE with your twitter search api endpoint (refer to [Twitter Search API documentation here](https://developer.twitter.com/en/docs/tweets/search/api-reference)).
4. Replace YOUR_SEARCH_API_ACCESS_TYPE with your access type, i.e either standard, premium, or enterprise.
5. Change QUERY_MAX and TOTAL_MAX to your prefered values. Note that QUERY_MAX is limited by your type of twitter API access (currently it's 100 for sandbox and 500 for premium).
6. Run the script (tested with python 3.7 only)
## Results:
Results are displayed in console in the following format:
`mention_screen_name,X`
Where `mention_screen_name` is the handle of the mentioned account (in comments) and `X` is the number of times this handle was mentioned in comments.

Note that results can also be improved by removing duplicate comments by the same user and duplicate mentions in the same comment.

It's also noteworthy that the replies collected and filtered are the most recent ones, which means this script won't be as effective for old tweets.
