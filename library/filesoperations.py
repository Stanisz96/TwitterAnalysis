import pandas as pd
import library.process as proc 
import library.restructure as res
import numpy as np


def save_all_tweets_individuals():
    '''
    Save DataFrame objects, containing tweets data for every individual.
    Where individual refers to data for one following user and 
    all data of users that this user is following.
    Saved data are in feather format and filename is user following id.
    '''

    users_ids_df = proc.get_users_ids()
    users_following_ids_df = users_ids_df[users_ids_df['type'] == 'A']

    for tweets_df in res.gen_tweets_dataframes(users_following_ids_df):
        id = tweets_df.iloc[0]['author_id']
        tweets_df.to_feather(f'./data/tweets/{id}')


def save_users_data():
    '''
    Save DataFrame objects, containing users data from userData.json files.
    Saved data are in feather format.
    '''

    users_data_df = res.get_users_dataframe()
    users_data_df.to_feather('./data/users')

def save_all_tweets_types_count():
    '''
    Save DataFrame objects, containing count of all tweets types.
    Saved data are in feather format.
    '''

    users_ids_df = proc.get_users_ids()
    tweets_types_count_df = proc.get_all_tweets_types_count(users_ids_df)
    tweets_types_count_df.to_feather('./processed/tweets_types_count')  

def load_all_tweets_types_count() -> pd.DataFrame:
    '''
    Load feather format file and return DataFrame object containing count of all tweets types. 
    '''

    tweets_types_count_df = pd.read_feather('./processed/tweets_types_count')

    return tweets_types_count_df
   

def load_tweets_individual(user_id: np.uint64) -> pd.DataFrame:
    '''
    Load feather format file and return DataFrame object for specific user id individual. 
    Where individual refers to data for one following user and 
    all data of users that this user is following.
    '''

    tweets_df = pd.read_feather(f'./data/tweets/{user_id}')

    return tweets_df


def load_all_tweets_individual() -> list:

    users_ids_df = proc.get_users_ids()
    users_following_ids_df = users_ids_df[users_ids_df['type'] == 'A']
    tweets_df_list = []

    for index, row in users_following_ids_df.iterrows():
        id = row['id']
        tweets_df_list.append(pd.read_feather(f'./data/tweets/{id}'))
    
    return tweets_df_list

def load_users_data() -> pd.DataFrame:
    '''
    Load feather format file and return DataFrame object containing users data.
    '''

    users_df = pd.read_feather('./data/users')

    return users_df

