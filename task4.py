# Step 1: Sample movie data
movies = {
    "Movie A": ["Action", "Adventure"],
    "Movie B": ["Romance", "Drama"],
    "Movie C": ["Action", "Thriller"],
    "Movie D": ["Comedy"],
    "Movie E": ["Action", "Adventure", "Sci-Fi"]
}

# Step 2: User preferences (Movies they like)
user_likes = ["Movie A"]

# Step 3: Count genre preferences based on liked movies
genre_score = {}
for movie in user_likes:
    for genre in movies[movie]:
        genre_score[genre] = genre_score.get(genre, 0) + 1

# Step 4: Score other movies based on same genres
recommendations = {}
for movie, genres in movies.items():
    if movie not in user_likes:
        score = 0
        for genre in genres:
            score += genre_score.get(genre, 0)
        recommendations[movie] = score

# Step 5: Sort and display recommendations
sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

print("Recommended Movies:")
for movie, score in sorted_recommendations:
    if score > 0:
        print(f"{movie} (score: {score})")
