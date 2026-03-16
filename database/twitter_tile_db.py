# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:12:24 2022

@author: yulun
"""
from twarc import Twarc2, expansions
from pullUserID import pullUserID_inner
from pullFollowerID import pullFollowerID_inner
from pullTimeline import pullTimeline_inner
import dateutil.parser as dp
import pickle
import os
import datetime
import tiledb

def get_tweets_info():
    pass

def get_users_info():
    pass

def add_seed_usernames(seed_names, user_tile_path, tweet_tile_path):
    # Check to see the supplied list is a list
    
    # Pull existing user id's from the database (Set)
    # Pull existing tweet id's from the database (Set)
    
    # Convert seed usernames to seed IDs through pullUserID_inner
    # Pull follower IDs from seed IDs
    
    # Compare new follower IDs to existing user IDs already in DB
    # Create list of 'new' ids while adding them to the user table with their data
    
    # Use pullTimeline_inner to grab timeline tweets from each new user
    # Ensure uniqueness before adding to the database

    

def add_users():
    pass




