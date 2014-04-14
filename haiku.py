
import twitter
import private

# Set access variables from private.py
api = twitter.Api(consumer_key=private.consumer_key,
        consumer_secret=private.consumer_secret,
        access_token_key = private.access_token, 
        access_token_secret = private.access_token_secret) 

# Location code
woeid = 23424977 # United States

# Get list of top 10 trends for location code
trends = api.GetTrendsWoeid(woeid)
print "Trends are: " 
for t in trends: 
    print t.name

# Get list of top tweets for top trend
result = api.GetSearch(term=trends[0].name, count=100)
print "Result size is: " + str(len(result)) 
print "Tweets # (length) for top trend: " 
i=1
for r in result: 
    print "Tweet " + str(i) + " (" + str(len(r.text)) + "): " + r.text + "\n"
    i=i+1


