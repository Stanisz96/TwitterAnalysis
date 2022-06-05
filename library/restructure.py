from matplotlib.pyplot import get
import pandas as pd
import pathlib as pl
import library.const as const
import os
import json
import numpy as np



def convert_tweets_from_json_to_df(users_ids_df: pd.DataFrame):
    users_following_ids_df = users_ids_df[users_ids_df['tpye'] == 'A']

    for index, row in users_following_ids_df.iterrows(): 
        tweets_df = pd.DataFrame(list(generator_tweets(row['id'])),
                                         columns=const.TWEET_COLUMN_NAMES).astype(const.TWEET_TYPES_LIST)
        
    tweets_df = tweets_df.reset_index()

    return tweets_df



def generator_tweets(user_following_id: np.uint64):
    users_ids_array = [user_following_id]
    users_ids_array.append(get_following_ids_of_an_user(user_following_id))

    for users_following_id in users_ids_array:
        tweets_path = pl.Path(const.USERS_PATH,users_following_id,"tweets")

        for idx, tweet_type in enumerate(const.TWEET_TYPE_NAMES):
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
                           json_temp['Public_metrics']['Quote_count']]



def get_following_ids_of_an_user(user_following_id: np.uint64):
    json_path = os.path.join(const.USERS_PATH, user_following_id, "metaData.json")
    json_file = json.load(open(json_path, encoding="utf8"))
    following_ids_of_an_user = json_file['Following']

    return following_ids_of_an_user