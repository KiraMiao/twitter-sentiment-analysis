# INPUT: 1) Text file of User IDs separated by newline characters
#        2) Desired name for the output file
#        3) Number follwer pages per user (15 page pulls per 15 minutes)
#        4) Bearer Token for API
# OUTPUT: 1)Text file containing all combined follower user IDs
#
# This script grabs the followers for the supplied user ID list. The output is meant to be used to pull timeline
# Tweets from these followers
# NOTE:

import os
import sys
import math
import datetime
from twarc import Twarc2, expansions
import dateutil.parser as dp

def pullFollowerID_inner(userIDs, maxPages, bToken):
    # Initialize return array
    spent_followers = set()
    followerInfo = []
    
    # Initialize client
    client = Twarc2(bearer_token = bToken)

    # Pull followers from API
    for ID in userIDs:
        for n, follower_page in enumerate(client.followers(ID, user_fields='created_at,location')):
            for follower in follower_page["data"]:
                if follower["id"] not in spent_followers:
                    spent_followers.add(follower["id"])
                    try:
                        epochDate = int(dp.parse(follower['created_at']).timestamp()) # Convert iso8601 to epoch time to store as int
                    except KeyError as e:
                        epochDate = 0
                        
                    try:
                        follower_location = follower['location']
                    except KeyError as e:
                        follower_location = 'none'
                    
                    followerInfo.append([follower['id'], follower['username'], follower_location, epochDate, ID])
                    
            if n + 1 == maxPages:
                break
            
    return followerInfo


def main(inputFile, outputFile, maxPages, bearer_token):

    # Read follower IDs, format into int and add to list
    f = open(inputFile, 'r')
    userIDs = f.read().splitlines()
    f.close()

    # Convert IDs to INT
    i = 0
    for i in range(len(userIDs)):
        userIDs[i] = int(userIDs[i])
        i = i + 1

    # Call API function
    followerInfo = pullFollowerID_inner(userIDs, maxPages, bearer_token)

    output = open(outputFile, 'w')

    for ID in followerInfo:
        output.write(str(ID))
        output.write('\n')

    output.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    

