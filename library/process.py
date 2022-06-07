import pandas as pd
import pathlib as pl
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


def get_individual_tweets_date(tweets_individual: pd.DataFrame) -> pd.DataFrame:
    '''
    Get individual tweets data in DataFrame object.
    Where individual refers to data for one following user and 
    all data of users that this user is following.
    '''

    tweets_date = pd.to_datetime(tweets_individual['created_at']).round('H')

    return tweets_date


def count_tweets_date(tweets_df_list: list):

    tweets_date_dict = col.defaultdict(int)

    for tweets_df in tweets_df_list:
        tweets_date = get_individual_tweets_date(tweets_df)

        for indx, tweet_date in tweets_date.items():
                tweets_date_dict[tweet_date] += 1