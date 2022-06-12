from matplotlib import pyplot as plt
import pandas as pd


def tweets_types_count(tweet_types_count: pd.DataFrame):

    fig, ax = plt.subplots()
    names_of_x_axis = tweet_types_count.columns
    data = tweet_types_count.values
    ax.bar(names_of_x_axis.values, data[0])

    plt.savefig('./images/tweets_types_count.png')    
    plt.clf()

def tweets_date_count(tweets_date_count_df: pd.DataFrame, nth_date_xtick: int):
    plt.figure(figsize=(800/96, 800/96), dpi=96)
    ax = tweets_date_count_df.plot.bar(x='date', y='count')
    ax_xticks = tweets_date_count_df.iloc[::nth_date_xtick, :]
    ax.tick_params(axis='x', which='both', labelsize=6)
    ax.set_xticks(ax_xticks.date.index)
    ax.set_xticklabels(ax_xticks.date)   
    plt.show()
    plt.clf()


def tweets_text_len_count(tweets_text_len_count_df: pd.DataFrame):
    ax = tweets_text_len_count_df.plot(x='text_len', y='count')
    plt.show()
    plt.clf()