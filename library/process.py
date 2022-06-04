import pandas as pd
import pathlib as pl
import library.const as const
import os
import numpy as np


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