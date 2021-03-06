import twitter
import private
import poets.poet0
import poets.poet13
import poets.poet0Jaccard

# Set access variables from private.py
api = twitter.Api(consumer_key=private.consumer_key,
        consumer_secret=private.consumer_secret,
        access_token_key = private.access_token, 
        access_token_secret = private.access_token_secret) 

# Location code
woeid = 23424977 # United States

# Get list of top 10 trends for location code
trends = api.GetTrendsWoeid(woeid)

# print "Trends are: " 
# for t in trends: 
#     print t.name

# Get list of top tweets for top trend
for trend in trends:
    result = api.GetSearch(term=trend.name, count=300)

    print "Haikus for trend: " + trend.name

    # print "\nResult size is: " + str(len(result)) 
    # print "\nTweets # (length) for top trend: \n" 
    # i=1
    # for r in result: 
    #     print "Tweet " + str(i) + " (" + str(len(r.text)) + "): " + r.text.encode('utf-8') + "\n"
    #     i=i+1

    # Construct Haikus
    print "Poet0: " + str(poets.poet0.writehaiku(trend.name, result).text)
    print "Teenage poet: " + str(poets.poet13.writehaiku(trend.name, result))
    print "Poet0Jaccard: " + str(poets.poet0Jaccard.writehaiku(trend.name, result).text)

    print "\n"