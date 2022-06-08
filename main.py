from random import random, randrange
import library.process as proc
import library.filesoperations as fo
import library.draw as draw
import pandas as pd
import sys
import collections as col
import matplotlib.pyplot as plt
import numpy as np

def main(step_number: int):
    if step_number == 1:
        fo.save_all_tweets_individuals()
    
    if step_number == 2:
        fo.save_users_data()

    if step_number == 3:
        users_data = fo.load_users_data()
        print(users_data.info(verbose=False, memory_usage="deep"))

    if step_number == 4:
        fo.save_all_tweets_types_count()
        tweets_types_count_df = fo.load_all_tweets_types_count()
        print(tweets_types_count_df.info(verbose=False, memory_usage="deep"))

    if step_number == 5:
        tweets_types_count_df = fo.load_all_tweets_types_count()
        draw.tweets_types_count(tweets_types_count_df)

    if step_number == 6:
        tweets_df_gen = fo.load_by_one_all_individual()
        tweets_date_count_df = proc.count_tweets_date(tweets_df_gen, '24H')
        fo.save_tweets_date_count(tweets_date_count_df)
        draw.tweets_date_count(tweets_date_count_df, 10)

if __name__=="__main__":
    main(7)