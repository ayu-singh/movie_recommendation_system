import json
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv = CountVectorizer(max_features=5000, stop_words="english")

df = pd.read_csv("data/final_data.csv")
# print(df.head())
print("*************** making vectors")
vectors = cv.fit_transform(df["tags"]).toarray()
print("*************** calculating similarity")
similarity = cosine_similarity(vectors)


def recommendations_top10(scores):
    sorted_scores = sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)[1:11]
    output = [df["title"][id] for id, score in sorted_scores]
    return output


print("****************** calculating recommendations")
recommendations = {}
for i, scores in enumerate(similarity):
    movie_name = df["title"][i]
    movie_id = df["movie_id"][i]
    recommendations[int(movie_id)] = {"name": movie_name, "recommendations": recommendations_top10(scores)}

print("************** saving recommendations")
with open("data/recommendations.json", "w") as fp:
    json.dump(recommendations, fp)
