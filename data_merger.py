import pandas as pd


def merger(filename1, filename2):
    file1 = pd.read_csv(f"data/{filename1}.csv")
    file2 = pd.read_csv(f"data/{filename2}.csv")

    merged_data = file1.merge(file2, on="title")

    # after checking the data I decided to keep only a certain columns and remove all others
    merged_data = merged_data[["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]]

    merged_data.to_csv("data/merged_data.csv", index=False)
    print("total data:", merged_data.shape)


if __name__ == "__main__":
    merger("tmdb_5000_movies", "tmdb_5000_credits")
