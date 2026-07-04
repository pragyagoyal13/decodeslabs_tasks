 PROJECT 1 : Rule-Based Chatbot

A simple command-line chatbot built in Python that responds to predefined user inputs using basic if-else logic. The chatbot runs in a continuous loop, accepting user messages and returning canned responses based on keyword matching.

 Features

- Recognizes common greetings (e.g., "hi", "hello", "hey")
- Responds to casual questions like "how are you" and "what's your name"
- Provides help when asked
- Exits cleanly when the user types "bye", "exit", or "quit"
- Falls back to a default response for unrecognized input

 How It Works

The program uses a `get_response()` function that checks the user's input against a list of predefined phrases using if-elif-else statements. The main loop keeps prompting the user for input until an exit command is entered, at which point the chatbot says goodbye and the program ends.

## Skills Demonstrated

- Control flow (if-else logic)
- Decision-making based on user input
- Foundational concepts behind rule-based AI systems (as opposed to machine-learning-based chatbots)

 
 Sample Output

<img width="1727" height="897" alt="image" src="https://github.com/user-attachments/assets/4e2bec59-d8c5-42aa-b5fd-8fd7ad58a331" />

 Requirements

No external libraries needed — runs with standard Python 3.


PROJECT 2 : Classification-Model
# Basic Classification Model

A beginner-friendly supervised learning project that demonstrates the core machine learning workflow: loading data, splitting it into training and testing sets, training a classifier, and evaluating its performance.

## Dataset

**Iris Flower Dataset** — a classic, small dataset built directly into scikit-learn (no download required). It contains 150 flower samples across 3 species (setosa, versicolor, virginica), with 4 measurements per flower: sepal length, sepal width, petal length, and petal width.

## Algorithm

**Decision Tree Classifier** — a simple, interpretable model that makes predictions by learning a series of if-else style splits based on the flower measurements.

## Features

- Loads and previews the dataset (shape, sample rows, class distribution)
- Splits data into training (80%) and testing (20%) sets, preserving class balance
- Trains a Decision Tree classifier on the training data
- Evaluates the model using accuracy and a full precision/recall/F1 report

## Skills Demonstrated

- Data handling and exploration with pandas
- Supervised learning fundamentals (train/test split, model fitting)
- Model evaluation using standard classification metrics

## How to Run

Install the required libraries:
```
pip install scikit-learn pandas
```

Then run the script:
```
python classification_model.py
```

## Sample Output

<img width="1912" height="998" alt="image" src="https://github.com/user-attachments/assets/d8277e11-fc10-42e6-a668-a77d35affdd2" />
<img width="1332" height="713" alt="image" src="https://github.com/user-attachments/assets/1121d2cd-dc3a-4a3d-b24f-fc9e09280313" />



## Requirements

- Python 3
- scikit-learn
- pandas


PROJECT 3-Recommendation-System
Simple Recommendation System

A content-based movie recommender built in Python that suggests movies based on a user's preferred genres. It uses simple similarity matching — comparing overlapping genres — rather than a machine learning model, making the core recommendation concept easy to follow.

## How It Works

1. The program displays a list of available genres pulled from a small built-in movie dataset.
2. The user types in the genres they enjoy (comma-separated).
3. Each movie is scored based on how many of its genres overlap with the user's chosen genres (a simple set-intersection similarity measure).
4. The top-scoring movies are displayed as recommendations, ranked from best match to lowest.

## Features

- Accepts free-text genre input from the user
- Validates input against a known list of genres, re-prompting if nothing valid is entered
- Scores and ranks movies using genre overlap (a basic form of content-based filtering)
- Displays the top 5 recommended movies along with their match score and genres

## Skills Demonstrated

- Logic building and input validation
- Pattern matching using set operations
- Core recommendation system concepts (content-based filtering, similarity scoring)

## How to Run

```
python recommendation_system.py
```

No external libraries required — runs with standard Python 3.

 Sample Output
<img width="1883" height="612" alt="image" src="https://github.com/user-attachments/assets/c1a87234-3a5e-4429-af2b-56ac23edd767" />

## Possible Extensions

- Add more movies or switch the dataset to books, music, or products
- Weight genres differently based on user ranking of preferences
- Use more advanced similarity measures (e.g., cosine similarity, Jaccard index)
- Incorporate actual user ratings data for collaborative filtering











