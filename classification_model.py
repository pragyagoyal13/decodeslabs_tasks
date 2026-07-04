"""
Basic Classification Model
---------------------------
Demonstrates the core supervised learning workflow:
1. Load and understand a dataset
2. Split data into training and testing sets
3. Train a simple classification algorithm
4. Evaluate its performance

Dataset: Iris flower dataset (built into scikit-learn, no download needed).
Algorithm: Decision Tree Classifier
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd


def load_and_explore_data():
    """Load the Iris dataset and print basic info about it."""
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["species"] = [iris.target_names[i] for i in iris.target]

    print("=== Dataset Preview ===")
    print(df.head(), "\n")

    print("=== Dataset Shape ===")
    print(f"{df.shape[0]} rows, {df.shape[1]} columns\n")

    print("=== Class Distribution ===")
    print(df["species"].value_counts(), "\n")

    return iris


def split_data(iris, test_size=0.2, random_state=42):
    """Split features and labels into training and testing sets."""
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data,
        iris.target,
        test_size=test_size,
        random_state=random_state,
        stratify=iris.target,  # keeps class proportions balanced in both sets
    )
    print(f"=== Data Split ===")
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples:  {len(X_test)}\n")
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    """Train a simple Decision Tree classifier."""
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test, target_names):
    """Evaluate the trained model on the test set."""
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print("=== Model Evaluation ===")
    print(f"Accuracy: {accuracy:.2%}\n")
    print("Classification Report:")
    print(classification_report(y_test, predictions, target_names=target_names))


def main():
    iris = load_and_explore_data()
    X_train, X_test, y_train, y_test = split_data(iris)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test, iris.target_names)


if __name__ == "__main__":
    main()
