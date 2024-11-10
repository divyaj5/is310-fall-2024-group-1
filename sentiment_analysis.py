import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download necessary NLTK data
nltk.download('vader_lexicon')

# Load the dataset
df_reviews = pd.read_csv('user_reviews.csv')

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to get sentiment score
def get_sentiment(text):
    score = analyzer.polarity_scores(text)
    return score['compound']

# Apply sentiment analysis to the reviews
df_reviews['sentiment_score'] = df_reviews['review_text'].apply(get_sentiment)

# Categorize the sentiment
df_reviews['sentiment_category'] = df_reviews['sentiment_score'].apply(
    lambda x: 'positive' if x > 0.05 else ('negative' if x < -0.05 else 'neutral')
)

# Display the processed reviews with sentiment categories
print(df_reviews.head())

# Set the style of seaborn plots
sns.set_style("whitegrid")

# Plot the sentiment distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df_reviews, x='sentiment_category', palette='coolwarm')
plt.title('Sentiment Distribution of User Reviews for Dress-Up Games')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.show()

# Convert 'YOR' to numeric for analysis
df_reviews['YOR'] = pd.to_numeric(df_reviews['YOR'], errors='coerce')

# Create a column to label pre- and post-2011
df_reviews['period'] = df_reviews['YOR'].apply(lambda x: 'pre-2011' if x < 2011 else 'post-2011')

# Boxplot to compare sentiment scores pre- and post-2011
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_reviews, x='period', y='sentiment_score', palette='viridis')
plt.title('Sentiment Scores Pre- and Post-2011')
plt.xlabel('Period')
plt.ylabel('Sentiment Score')
plt.show()

# Save the processed dataset with sentiment scores and categories
df_reviews.to_csv('processed_user_reviews.csv', index=False)
