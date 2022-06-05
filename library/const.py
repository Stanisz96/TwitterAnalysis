import pathlib as pl
import numpy as np

MAIN_PATH = pl.Path('C:/Magisterka/data')
USERS_PATH = pl.Path(MAIN_PATH,"users")
TWEET_TYPE_NAMES = ["quoted","replied_to","retweeted","tweeted"]
TWEET_COLUMN_NAMES = ['author_id','id','text','created_at','lang','source','type',
                      'ref_id','retweet_count','reply_count','like_count','quote_count']
TWEET_TYPES_LIST = {'author_id': np.uint64,'id': np.uint64, 'text': str, 'created_at': str, 'lang': str,
                    'source': str, 'type': str, 'ref_id': np.uint64, 'retweet_count': np.uint32,
                    'reply_count': np.uint32,'like_count': np.uint32,'quote_count': np.uint32}