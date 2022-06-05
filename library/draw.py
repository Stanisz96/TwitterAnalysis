from matplotlib import pyplot as plt
import pandas as pd


def tweets_types_count(tweet_types_count: pd.DataFrame):
    fig, ax = plt.subplots()
    names_of_x_axis = tweet_types_count.columns
    data = tweet_types_count.values
    ax.bar(names_of_x_axis.values, data[0])
    plt.savefig('./images/tweets_types_count.png')    