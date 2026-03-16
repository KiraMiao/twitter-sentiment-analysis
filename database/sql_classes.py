# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 14:30:45 2022

@author: yulun
"""
import sqlmodel
from sqlmodel import Field, SQLModel, create_engine, Session, select
from typing import Optional

import os

# Define DB classes
class User_info(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    username:str
    follow_count: int
    location: str
    timestamp: int
    
class User_followers(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    from_id: Optional[str] = Field(default=None, foreign_key="user_info.id")
    username: str
    location: str
    timestamp: int
    
class Tweets(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    from_id: Optional[str] = Field(default=None, foreign_key="user_followers.id")
    timestamp: int
    # Text is stored in the TileDB
    reply: bool
    retweet: bool


def init_engine(filepath):
    sqlite_file_name = os.path.abspath(filepath)
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    
    return create_engine(sqlite_url, echo=False)