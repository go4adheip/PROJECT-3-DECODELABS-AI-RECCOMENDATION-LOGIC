import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("dataset.csv")

# Convert text into vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["tags"])

# User input
user_interest = input("Enter your interests: ")

# Convert user input into vector
user_vector = vectorizer.transform([user_interest])

# Calculate similarity
similarity_scores = cosine_similarity(user_vector, tfidf_matrix)

# Add scores
df["score"] = similarity_scores.flatten()

# Sort recommendations
recommendations = df.sort_values(by="score", ascending=False)

print("\nTop Recommendations:\n")

for _, row in recommendations.head(3).iterrows():
    print(f"{row['title']} --> Score: {row['score']:.2f}")