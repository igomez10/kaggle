# %%
from math import floor

import pandas as pd

# %%
df = pd.read_csv("./emails.csv")
print(df.head())

# %%
# split data in train and validation
sizedf = df.shape
print(sizedf)
number_records = sizedf[0]

# %%
# split in 80 train 20 test
limit = floor(number_records * 1)
train_df = df[:limit]
test_df = df[limit:]


# %%
# build matrix with
spam_count = df.query("spam == 1").count()
spam_ratio = spam_count / number_records
print("spam_count", spam_count)
print("spam_ratio", spam_ratio)

# %%
# get probabilities of being spam
# build vocabulary
vocabulary = {}
for i in train_df.iterrows():
    row = i[1]
    is_spam = row["spam"] == 1
    email_words = row["text"].split(" ")
    for word in email_words:
        word = word.lower().strip()
        if word not in vocabulary:
            vocabulary[word] = [0, 0]  # [spam_count, total_count]
        if is_spam:
            vocabulary[word][0] += 1
        vocabulary[word][1] += 1

word_stats = pd.DataFrame.from_dict(
    vocabulary, orient="index", columns=["spam_count", "total_count"]
)

# %%
# exclude . \ _ - , and empty string
# word_stats = word_stats.query(
#     # "index != '.' and index != '_' and index != '-' and index != ',' and index != ''"
# )

word_stats["spam_ratio"] = word_stats["spam_count"] / word_stats["total_count"]
print(word_stats.head(20))
#   .sort_values(by="spam_ratio", ascending=True

# %%

import math


def predict_spam(text: str) -> float:
    words = text.split(" ")
    result = math.log(spam_ratio["spam"] + 1, 10)
    for word in words:
        word = word.lower().strip()
        if word in word_stats.index:
            spam_prob = word_stats.loc[word]["spam_ratio"]
            result += math.log(spam_prob + 1, 10)
    # average spam probability
    return result / len(words)


print(
    "Free money!!! Click here to claim your prize, free viagra viagra free",
    predict_spam(
        "Free money!!! Click here to claim your prize, free viagra viagra free"
    ),
)
print(
    "Meeting at 10am tomorrow in the office",
    predict_spam("Meeting at 10am tomorrow in the office"),
)

# Subject: any med for your girl to be happy !  your girl is unsatisfied with your potency ? don ' t wait until she finds another men !  click here to choose from a great variety of llcensed love t @ bs ! best pri $ es , fast shippinq and guaranteed effect ! here you buy it riqht from warehouse !  the store is verified by bbb and approved by visa !
print(
    "Subject: any med for your girl to be happy !  your girl is unsatisfied with your potency ? don ' t wait until she finds another men !  click here to choose from a great variety of llcensed love t @ bs ! best pri $ es , fast shippinq and guaranteed effect ! here you buy it riqht from warehouse !  the store is verified by bbb and approved by visa !",
    predict_spam(
        "Subject: any med for your girl to be happy !  your girl is unsatisfied with your potency ? don ' t wait until she finds another men !  click here to choose from a great variety of llcensed love t @ bs ! best pri $ es , fast shippinq and guaranteed effect ! here you buy it riqht from warehouse !  the store is verified by bbb and approved by visa ! "
    ),
)

# Subject: 25 mg did thhe trick  ho receivable w to save on your medlcatlons over 70 % .  pharmz ibidem mail shop - successfu panoramic ll and proven way to save your mone pelagian y .  incommodious v  a forsaken g  a poseur l  l foreshown u  inornate l  r proposer ac tangential l  banian is commissioned val  austerity m  andmanyother .  * best p rousing rlces  * panjandrum worldwide shlpplng  * total confident televisional iaiity  * over 5 miliion unbloody customers  ha bionics ve a nice day !

print(
    "Subject: 25 mg did thhe trick  ho receivable w to save on your medlcatlons over 70 % .  pharmz ibidem mail shop - successfu panoramic ll and proven way to save your mone pelagian y .  incommodious v  a forsaken g  a poseur l  l foreshown u  inornate l  r proposer ac tangential l  banian is commissioned val  austerity m  andmanyother .  * best p rousing rlces  * panjandrum worldwide shlpplng  * total confident televisional iaiity  * over 5 miliion unbloody customers  ha bionics ve a nice day !",
    predict_spam(
        "Subject: 25 mg did thhe trick  ho receivable w to save on your medlcatlons over 70 % .  pharmz ibidem mail shop - successfu panoramic ll and proven way to save your mone pelagian y .  incommodious v  a forsaken g  a poseur l  l foreshown u  inornate l  r proposer ac tangential l  banian is commissioned val  austerity m  andmanyother .  * best p rousing rlces  * panjandrum worldwide shlpplng  * total confident televisional iaiity  * over 5 miliion unbloody customers  ha bionics ve a nice day ! "
    ),
)
