import re
import emoji
import nltk

class Cleaner:
    """
    clean the data
    """

    def data_clean(self, df):
        df['original_text'] = df['original_text'].apply(self.row_cleaner)
        return df
    def row_cleaner(self, tweet):
        # Remove mentions
        tweet = re.sub(r"@[A-Za-z0-9_]+", "", tweet)
        # Remove URLs
        tweet = re.sub(r"http\S+|www\S+", "", tweet)
        # Remove extra spaces
        tweet = " ".join(tweet.split())
        # Remove emojis
        tweet = ''.join(c for c in tweet if not emoji.is_emoji(c))
        # Remove hashtag symbol but keep text
        tweet = tweet.replace("#", "").replace("_", " ")
        return tweet








