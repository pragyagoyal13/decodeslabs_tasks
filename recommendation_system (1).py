"""
Simple Recommendation System
------------------------------
A basic content-based recommender that suggests movies based on
the user's preferred genres. It uses simple similarity matching
(counting overlapping genres) rather than a machine learning model,
making it easy to understand the core recommendation concept.
"""

# A small predefined dataset of movies and their genre tags
MOVIES = [
    {"title": "The Matrix",           "genres": {"action", "sci-fi", "thriller"}},
    {"title": "Inception",            "genres": {"action", "sci-fi", "mystery"}},
    {"title": "The Notebook",         "genres": {"romance", "drama"}},
    {"title": "Superbad",             "genres": {"comedy", "coming-of-age"}},
    {"title": "The Conjuring",        "genres": {"horror", "thriller"}},
    {"title": "La La Land",           "genres": {"romance", "musical", "drama"}},
    {"title": "Interstellar",         "genres": {"sci-fi", "drama", "adventure"}},
    {"title": "The Hangover",         "genres": {"comedy"}},
    {"title": "Get Out",              "genres": {"horror", "mystery", "thriller"}},
    {"title": "Pride and Prejudice",  "genres": {"romance", "drama"}},
    {"title": "Mad Max: Fury Road",   "genres": {"action", "adventure", "sci-fi"}},
    {"title": "Coco",                 "genres": {"animation", "family", "adventure"}},
]

ALL_GENRES = sorted({genre for movie in MOVIES for genre in movie["genres"]})


def get_user_preferences():
    """Ask the user to pick genres they like from the available list."""
    print("Available genres:")
    print(", ".join(ALL_GENRES))
    print()

    raw_input_str = input("Enter genres you enjoy, separated by commas: ")
    chosen = {genre.strip().lower() for genre in raw_input_str.split(",") if genre.strip()}

    # Keep only genres that actually exist in our dataset
    valid_choices = chosen.intersection(ALL_GENRES)

    if not valid_choices:
        print("\nNo valid genres recognized. Please try again using the listed genres.\n")
        return get_user_preferences()

    return valid_choices


def score_movie(movie_genres, user_genres):
    """
    Score a movie based on how many of its genres overlap with the
    user's preferences. This is a simple similarity measure:
    the size of the intersection between the two genre sets.
    """
    return len(movie_genres.intersection(user_genres))


def recommend_movies(user_genres, top_n=5):
    """Rank all movies by similarity score and return the top matches."""
    scored_movies = []
    for movie in MOVIES:
        score = score_movie(movie["genres"], user_genres)
        if score > 0:  # only recommend movies with at least one matching genre
            scored_movies.append((movie["title"], score, movie["genres"]))

    # Sort by score (highest first); ties keep original order
    scored_movies.sort(key=lambda item: item[1], reverse=True)

    return scored_movies[:top_n]


def display_recommendations(recommendations):
    """Print the recommended movies in a readable format."""
    if not recommendations:
        print("Sorry, no matching movies found for your preferences.")
        return

    print("\n=== Recommended For You ===")
    for rank, (title, score, genres) in enumerate(recommendations, start=1):
        genre_list = ", ".join(sorted(genres))
        print(f"{rank}. {title}  (match score: {score}, genres: {genre_list})")


def main():
    print("=== Movie Recommendation System ===\n")
    user_genres = get_user_preferences()
    recommendations = recommend_movies(user_genres)
    display_recommendations(recommendations)


if __name__ == "__main__":
    main()
