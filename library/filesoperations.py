import pandas as pd
import library.process as proc 
import library.restructure as res



def save_all_tweets_individual():
    '''
    Save DataFrame objects, containing tweets data for every individual.
    Where individual refers to data for one following user and 
    all data of users that this user is following.
    Saved data are in feather format and filename is user following id.
    '''

    users_ids_df = proc.get_users_ids()
    users_following_ids_df = users_ids_df[users_ids_df['type'] == 'A']

    for tweets_df in res.gen_tweets_dataframes(users_following_ids_df):
        tweets_df.to_feather('./data/test')


def load_tweets_individual() -> pd.DataFrame:
    '''
    Load feather format file and return DataFrame object for specific user id individual. 
    Where individual refers to data for one following user and 
    all data of users that this user is following.
    '''
    
    tweets_df = pd.read_feather('./data/test')

    return tweets_df