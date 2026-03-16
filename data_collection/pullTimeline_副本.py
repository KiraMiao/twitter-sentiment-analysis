# INPUT: 1) Text file of User IDs separated by newline characters
#        2) Number of pages of tweets we want for each supplied user (100 tweets per page)
#        3) Bearer token for Twitter API
# OUTPUT: Returns a nested array containing ID and Text pairs for each tweet. This array is to be used later to populate
# our database

# -*- coding: utf-8 -*-

import sys
import datetime
from twarc import Twarc2
import dateutil.parser as dp

def pullTimeline_inner(followerIDs, maxPages, bToken, startTime=datetime.datetime(2020, 12, 14), endTime=datetime.datetime.now(), replies=False, retweets=False):
    # Initialize client
    client = Twarc2(bearer_token = bToken)

    followerTweets = []

    # Canada began vaccinating on December 14th, 2020 so we should exclude Tweets from before then (could also use the
    # date that vaccines were announced)
    vaxStartDate = datetime.datetime(2020, 12, 14)


    # Pull timeline tweet IDs and text
    for ID in followerIDs:
        for n, tweet_page in enumerate(client.timeline(ID, start_time = startTime, end_time = endTime, exclude_replies = not replies, exclude_retweets = not retweets)):
            for tweet in tweet_page["data"]:
                epochDate = int(dp.parse(tweet['created_at']).timestamp())
                followerTweets.append([tweet["id"], tweet["text"].encode('utf-8'), tweet["author_id"], epochDate])
            if n + 1 == maxPages:
                break
            
    return followerTweets                 

def main(followerIDfile, maxPages, bToken):
    #Read the ID list and convert to array
    f = open(followerIDfile, 'r')
    followerIDs = f.read().splitlines()
    f.close()

    followerTweets = pullTimeline_inner(followerIDs, maxPages, bToken)
                

    print("Writing to file")
    # Write tweet data to file
    output = open('followerTweets.txt', 'w', encoding='utf-8')
    for tweet in followerTweets:
        output.write(str(tweet[0]))
        output.write(', ')
        output.write(tweet[1])
        output.write('\n')


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), sys.argv[3])
