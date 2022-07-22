from random import random, randrange
import library.process as proc
import library.filesoperations as fo
import library.draw as draw
import pandas as pd
import sys
import collections as col
import matplotlib.pyplot as plt
import numpy as np
import library.restructure as res



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
        tweets_date_count_df = proc.count_tweets_date(tweets_df_gen, 'H')
        fo.save_tweets_date_count(tweets_date_count_df)
        draw.tweets_date_count(tweets_date_count_df, 10)

    if step_number == 7:
        tweets_date_count_df = fo.load_tweets_date_count()
        tweets_date_count_df_clean = res.clean_tweets_date_count(tweets_date_count_df)
        draw.tweets_date_count(tweets_date_count_df_clean, 1)
    
    if step_number == 8:
        tweets_df_gen = fo.load_by_one_all_individual()
        tweets_text_len_count_df = proc.count_tweets_text_len(tweets_df_gen)
        fo.save_tweets_text_len_count(tweets_text_len_count_df)
        draw.tweets_text_len_count(tweets_text_len_count_df)

    if step_number == 9:
        # tweet_individual = fo.load_tweets_individual(22594291)
        # tweet_text = tweet_individual.loc[tweet_individual['id'] == 1480555038330265600].text.values[0]
        # tweet_text = tweet_text[31:]
        # print(bytes(tweet_text,'utf-8').decode('utf-32'))
        tweets_text_len_count_df = fo.load_tweets_text_len_count()
        draw.tweets_text_len_count(tweets_text_len_count_df)

    if step_number == 10:
        tweets_df_gen = fo.load_by_one_all_individual()
        users_tweets_per_day = proc.count_users_tweets_per_day(tweets_df_gen)
        fo.save_tweets_freq(users_tweets_per_day)

    if step_number == 11:
        tweets_freq_df = fo.load_tweets_freq()
        draw.tweets_freq(tweets_freq_df, 1)

if __name__=="__main__":
    main(1)