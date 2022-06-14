from typing import Generator
import pandas as pd
import pathlib as pl

from traitlets import Instance
import library.const as const
import os
import numpy as np
import sys
import collections as col

def get_users_ids():
    '''
    Get all users ids and type from userList file.
    Return DataFrame object with two columns: type, id.
    '''
    
    lines = []

    with open(pl.Path(const.MAIN_PATH,"usersList.dat")) as file:
        for line in file:
            line = line.strip()
            lines.append([line[0],line[1:]])

    users_ids_array = np.array(lines)
    users_ids_df = pd.DataFrame(users_ids_array, columns = ['type','id'])

    return users_ids_df.reset_index()


def get_all_tweets_types_count(users_ids_df: pd.DataFrame):
    '''
    Count all tweets types. Return DataFrame object with four columns: const.TWEET_TYPE_NAMES.
    '''
    
    tweet_type_count = [0,0,0,0]

    for index, row in users_ids_df.iterrows():
        tweets_path = pl.Path(const.USERS_PATH,row['id'],"tweets")
        for idx, tweet_type in enumerate(const.TWEET_TYPE_NAMES):
            tweets_type_path = pl.Path(tweets_path,tweet_type)
            tweet_type_count[idx] += len([name for name in os.listdir(tweets_type_path) 
                                            if os.path.isfile(os.path.join(tweets_type_path, name))])

    tweet_type_count_df = pd.DataFrame([tweet_type_count], columns=const.TWEET_TYPE_NAMES)
                                            
    return tweet_type_count_df


def get_individual_tweets_date(tweets_individual: pd.DataFrame, round_hours: str) -> pd.DataFrame:
    '''
    Get individual tweets data in DataFrame object.
    Where individual refers to data for one following user and 
    all data of users that this user is following.
    '''

    tweets_date = pd.to_datetime(tweets_individual['created_at']).dt.date

    return tweets_date


def get_individual_tweets_text_len(tweets_individual: pd.DataFrame) -> pd.DataFrame:
    '''
    Get individual tweets text in DataFrame object.
    Where individual refers to data for one following user and 
    all data of users that this user is following.
    '''
    for index, row in tweets_individual.iterrows():
        mention_index = row['text'].rfind('@')
        text = row['text'][mention_index:]
        text = text[text.find(' ')+1:]
        if mention_index != -1:
            tweets_individual.at[index, 'text'] = text 

    tweets_text_len_df = tweets_individual['text'].str.len()

    return tweets_text_len_df   

def count_tweets_date(tweets_df_gen: Generator[list, None, None], round_hours: str) -> pd.DataFrame:

    tweets_date_dict = col.defaultdict(int)

    for tweets_df in tweets_df_gen:
        tweets_date = get_individual_tweets_date(tweets_df, round_hours)

        for indx, tweet_date in tweets_date.items():
                tweets_date_dict[tweet_date] += 1

    sorted_tweets_date_dict = col.OrderedDict(sorted(tweets_date_dict.items()))
    tweets_date_count_df = pd.DataFrame.from_dict(sorted_tweets_date_dict, orient='index')\
                                       .reset_index()
    tweets_date_count_df.columns = ['date','count']

    return tweets_date_count_df


def count_tweets_text_len(tweets_df_gen: Generator[list, None, None]) -> pd.DataFrame:
    tweets_text_len_dict = col.defaultdict(int)

    for tweets_df in tweets_df_gen:
        tweets_text_df = get_individual_tweets_text_len(tweets_df)

        for indx, tweet_text_len in tweets_text_df.items():
                tweets_text_len_dict[tweet_text_len] += 1        


    sorted_tweets_text_len_dict = col.OrderedDict(sorted(tweets_text_len_dict.items()))
    tweets_text_len_count_df = pd.DataFrame.from_dict(sorted_tweets_text_len_dict, orient='index')\
                                           .reset_index()
    tweets_text_len_count_df.columns = ['text_len','count']

    return tweets_text_len_count_df