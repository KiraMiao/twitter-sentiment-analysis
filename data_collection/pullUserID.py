# INPUT: 1)Text file of Twitter usernames separated by '\n'
#        2)Desired file name for ID output
#        3)Desired file name for Info output
#
# OUTPUT: 1) Text file with User IDs separated by '\n'
#         2) Text file containing Username, UserID and follower count for each supplied user
#
# Since we can't access User IDs on normal Twitter, this script is designed to pull the IDs associated with
# the provided usernames, to be used later. Also outputs an info file for human-readability

import os
import sys
import math
import datetime
from twarc import Twarc2, expansions, Twarc
import dateutil.parser as dp

def pullUserID_inner(userList):
    ### Initialize V2 client
    ##client = Twarc2(bearer_token = bToken)
    ##
    ##userIDs = []
    ##
    ##for n, user_page in enumerate(client.user_lookup(userList, usernames=True)):
    ##    print("Retrieved user page: " + str(n))
    ##    for user in user_page['data']:
    ##        userIDs.append(user['id'])

    # Initialize standard v1.1 endpoint client since we can't grab follower count from the v2 endpoint
    client = Twarc()

    userIDs = []
    for n, user in enumerate(client.user_lookup(userList, id_type='screen_name')):
        print("[PUID] Seed users retreived: " + str(n + 1) + "    ", end='\r')
        
        timestamp = int(dp.parse(user['created_at']).timestamp()) # Convert ISO 8601 to Epoch time
        userIDs.append([user['screen_name'], user['id_str'], user['followers_count'], user['location'], timestamp])
    print("\n[PUID] Done!")

    # Sort list based on follower count
    userIDs.sort(key = lambda x: x[2], reverse=True)
    return userIDs


def main(userFile, outputFileName, outputInfoName):
    # Read the username list
    f = open(userFile, 'r')
    userList = f.read().splitlines()
    f.close()

    userIDs = pullUserID_inner(userList)
    
    # Write user IDs to file
    IDfile = open(outputFileName, 'w')
    InfoFile = open(outputInfoName, 'w')
    for n, entry in enumerate(userIDs):
        IDfile.write(entry[1] + '\n')

        userString = "USER: " + entry[0]
        IDstring = "ID: " + entry[1]
        FollowString = "FOLLOWERS: " + str(entry[2])
        LocationString = "LOCATION(If present): " + str(entry[3])
        CreatedAtString = "CREATED: " + str(entry[4])
        
        InfoFile.write("{: <25} {: <25} {: <10} {: <10} {: <10}".format(userString, IDstring, FollowString, LocationString, CreatedAtString))
        InfoFile.write("\n")
      
    IDfile.close()
    InfoFile.close()
    

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])



    
