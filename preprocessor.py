import numpy as np
import pandas as pd
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

df = pd.read_csv("data/merged_data.csv")

# since we need all the information, we have to drop any row with null values
print(df.shape)
df = df.dropna()
print(df.shape)


# helper function to extract genres in the correct format
def convert(obj):
    l = []
    for i in eval(obj):
        l.append(i["name"])
    return l


df["genres"] = df["genres"].apply(convert)
df["keywords"] = df["keywords"].apply(convert)
print("****************   genres and keywords have been converted")


def convert2(obj):
    l = []
    for count, i in enumerate(eval(obj)):
        if count < 3:
            l.append(i["name"])
        else:
            break
    return l


df["cast"] = df["cast"].apply(convert)
print("****************   cast have been converted")


def convert3(obj):
    l = []
    for i in eval(obj):
        if i["job"] == "Director":
            l.append(i["name"])
            break
    return l


df["crew"] = df["crew"].apply(convert3)
print("****************   crew have been converted")
df["overview"] = df["overview"].apply(lambda x: x.split())


def joiner(obj):
    return [i.replace(" ", "") for i in obj]


df["genres"] = df["genres"].apply(joiner)
df["keywords"] = df["keywords"].apply(joiner)
df["cast"] = df["cast"].apply(joiner)
df["crew"] = df["crew"].apply(joiner)
df["tags"] = df["overview"]+df["genres"]+df["keywords"]+df["cast"]+df["crew"]
df = df[["movie_id", "title", "tags"]]


def stemmer(obj):
    output = []
    for i in obj:
        output.append(ps.stem(i))
    return output


df["tags"] = df["tags"].apply(stemmer)
print("**************** done with stemming")
df["tags"] = df["tags"].apply(lambda x: " ".join(x).lower())


df.to_csv("data/final_data.csv", index=False)
print("****************   final data has been saved")