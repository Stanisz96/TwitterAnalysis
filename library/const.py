import pathlib as pl
import numpy as np

MAIN_PATH = pl.Path('C:/Magisterka/dataV2')
USERS_PATH = pl.Path(MAIN_PATH,"users")
TWEET_TYPE_NAMES = ["quoted","replied_to","retweeted","tweeted"]
TWEET_COLUMN_NAMES = ['author_id','id','text','created_at','lang','source','type','ref_id',
                      'retweet_count','reply_count','like_count','quote_count','downloaded_date_time','conversation_id']
TWEET_TYPES_LIST = {'author_id': np.uint64,'id': np.uint64, 'text': str, 'created_at': str, 'lang': str,
                    'source': str, 'type': str, 'ref_id': np.uint64, 'retweet_count': np.uint32,'reply_count': np.uint32,
                    'like_count': np.uint32,'quote_count': np.uint32, 'downloaded_date_time': str,'conversation_id': np.uint64}
USER_COLUMN_NAMES = ['type','id','name','username','created_at','description','followers_count',
                      'tweet_count','verified','protected']
USER_TYPES_LIST = {'type': str,'id': np.uint64, 'name': str, 'username': str, 'created_at': str,
                    'description': str, 'followers_count': np.uint32, 'tweet_count': np.uint32, 'verified': bool,
                    'protected': bool}