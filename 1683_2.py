


import pandas as pd



def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    mask = len(tweets['content'].str) > 15

    return tweets[mask]['tweet_id']