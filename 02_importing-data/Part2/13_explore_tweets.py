from __future__ import print_function

import pandas as pd
import json
import re
import matplotlib.pyplot as plt
import seaborn as sns


def word_in_text(word, tweet):
    """
    Return the number of words in a tweet [str]
    """
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, tweet)

    if match:
        return True
    return False


# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialise empty list to store tweets: tweets_data
tweets_data = []

# Open a connection to file
tweets_file = open(tweets_data_path, 'r')

# Read and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())

# Create a dataframe from tweets_data
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

# Print head of DataFrame
print(df.head())

# Initialize list to store counts
[clinton, trump, sanders, cruz, rt] = [0, 0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])
    rt += word_in_text('RT', row['text'])

# === Plot Results ===
# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz', 'RT']

# Plot histogram
ax = sns.barplot(cd, [clinton, trump, sanders, cruz, rt])
ax.set(ylabel="count")
plt.show()
