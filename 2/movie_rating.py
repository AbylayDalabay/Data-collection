import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    titles = pd.merge(movies, movie_rating, on='movie_id', how='inner')
    names_titles = pd.merge(users, titles, on='user_id', how='inner')
    
    names_titles_feb_20 = names_titles[names_titles.created_at.apply(lambda x: x.year == 2020 and x.month == 2)]
    movie_mean_rating = names_titles_feb_20.groupby('title').agg({'rating' : 'mean'}).reset_index()
    best_title = movie_mean_rating.sort_values(by=['rating', 'title'], ascending=[False, True]).iloc[0, 0]

    users_count = names_titles.groupby('name').agg({'rating' : 'count'}).reset_index()
    best_user = users_count.sort_values(by=['rating', 'name'], ascending=[False, True]).iloc[0, 0]

    return pd.DataFrame({'results' : [best_user, best_title]})