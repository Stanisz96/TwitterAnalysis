import pandas as pd
import pathlib as pl
import library.const as con
import os
import json
import numpy as np
import library.process as proc


def gen_tweets_dataframes(users_following_ids_df: pd.DataFrame):
    '''
    Generate DataFrame objects for every individual.
    Where individual refers to data for one following user and 
    all data of users that this user is following.
    '''
    
    for index, row in users_following_ids_df.iterrows(): 
        yield pd.DataFrame(list(gen_tweets_array(row['id'])),
                           columns=con.TWEET_COLUMN_NAMES)\
                                .astype(con.TWEET_TYPES_LIST)\
                                .reset_index()


def gen_tweets_array(user_following_id: np.uint64):
    '''
    Generate array of tweets data converted from json file for individual.
    Where individual refers to data for one following user and 
    all data of users that this user is following.
    '''

    users_ids_array = get_all_ids_for_individual(user_following_id)

    for users_following_id in users_ids_array:
        tweets_path = pl.Path(con.USERS_PATH,str(users_following_id),"tweets")

        for idx, tweet_type in enumerate(con.TWEET_TYPE_NAMES):
            tweets_type_path = pl.Path(tweets_path,tweet_type)

            for json_file in os.listdir(tweets_type_path): 
                json_path = os.path.join(tweets_type_path, json_file)
                if os.path.isfile(json_path):
                    json_temp = json.load(open(json_path, encoding="utf8"))

                    yield [json_temp['Author_id'],json_temp['Id'],
                           json_temp['Text'],json_temp['Created_at'],
                           json_temp['Lang'],json_temp['Source'],
                           json_temp['Referenced_tweets'][0]['Type'],
                           json_temp['Referenced_tweets'][0]['Id'],
                           json_temp['Public_metrics']['Retweet_count'],
                           json_temp['Public_metrics']['Reply_count'],
                           json_temp['Public_metrics']['Like_count'],
                           json_temp['Public_metrics']['Quote_count'],
                           json_temp['DownloadedDateTime'],
                           json_temp['Conversation_id']]

def get_users_dataframe() -> pd.DataFrame:
    '''
    Get users DataFrame object. Function return DataFrame containing all users data from userData.json files.
    '''
    
    users_dataframe = pd.DataFrame(list(gen_users_data_array(proc.get_users_ids())),
                           columns=con.USER_COLUMN_NAMES)\
                                .astype(con.USER_TYPES_LIST)\
                                .reset_index()

    return users_dataframe

def gen_users_data_array(users_ids_df: pd.DataFrame):
    '''
    Generate list containing all users data.
    '''

    for index, row in users_ids_df.iterrows():
        json_path = pl.Path(con.USERS_PATH,row['id'],"userData.json")
        json_temp = json.load(open(json_path, encoding="utf-8"))
        if row['type'] == 'A':
            json_temp = json_temp['data']
        
            yield [row['type'], json_temp['id'], json_temp['name'], json_temp['username'],
                json_temp['created_at'], json_temp['description'],
                json_temp['public_metrics']['followers_count'],
                json_temp['public_metrics']['tweet_count'],
                json_temp['verified'],json_temp['protected']]
        
        if row['type'] == 'B':
            yield [row['type'], json_temp['Id'], json_temp['Name'], json_temp['Username'],
                json_temp['Created_at'], json_temp['Description'],
                json_temp['Public_metrics']['Followers_count'],
                json_temp['Public_metrics']['Tweet_count'],
                json_temp['Verified'],json_temp['Protected']]


def get_all_ids_for_individual(user_following_id: np.uint64) -> list:
    '''
    Get all ids for individual user given in fun parm.
    Where individual refers to data for one following user and 
    all data of users that this user is following.
    '''

    ids_array = [user_following_id]
    ids_array.extend(get_following_ids_of_an_user(user_following_id))

    return ids_array

def get_following_ids_of_an_user(user_following_id: np.uint64) -> list:
    '''
    Get all ids of users that are followed by user given in fun parm.
    '''

    json_path = os.path.join(con.USERS_PATH, user_following_id, "metaData.json")
    json_file = json.load(open(json_path, encoding="utf8"))
    following_ids_of_an_user = list(json_file['Following'])

    return following_ids_of_an_user


def clean_tweets_date_count(tweets_date_count_df: pd.DataFrame):
    df = tweets_date_count_df.tail(1000)
    df.reset_index(drop=True, inplace=True)

    return df