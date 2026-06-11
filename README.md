# AI Recommendation System

## Overview
This project is a simple AI-powered recommendation system built using Python. It recommends courses based on user interests using Content-Based Filtering, TF-IDF Vectorization, and Cosine Similarity.

## Features
- Takes user interests as input
- Converts text data into numerical vectors using TF-IDF
- Calculates similarity using Cosine Similarity
- Sorts recommendations based on relevance
- Displays the Top-N recommendations

## Technologies Used
- Python
- Pandas
- Scikit-Learn
- TF-IDF Vectorizer
- Cosine Similarity

## Project Structure

```
PROJECT_3_DECODELABS/
│
├── app.py
├── dataset.csv
├── requirements.txt
├── README.md
└── .venv/
```

## Dataset

The dataset contains course titles and their corresponding tags.

Example:

| Title | Tags |
|---------|---------|
| Python for Beginners | python programming coding |
| Machine Learning Basics | machine learning ai python |
| Deep Learning Guide | deep learning neural networks ai |

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project folder

```bash
cd PROJECT_3_DECODELABS
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

```bash
python app.py
```

## Example

### Input

```text
python ai machine learning
```

### Output

```text
Top Recommendations:

Machine Learning Basics --> Score: 1.00
Deep Learning Guide --> Score: 0.39
Python for Beginners --> Score: 0.19
```

## Working Principle

1. User enters interests.
2. TF-IDF converts text into feature vectors.
3. Cosine Similarity compares user interests with available courses.
4. Courses are ranked according to similarity scores.
5. Top recommendations are displayed.

## Future Improvements

- Web interface using Streamlit
- Larger dataset
- Personalized recommendations
- Recommendation score visualization

## Author

**Adheip Srivastava**  
B.Tech Computer Science Engineering  
SRM Institute of Science and Technology

## License

This project is created for educational and learning purposes.
