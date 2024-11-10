# Sentiment Analysis of User Reviews for Dress-Up Games

This repository contains a comprehensive sentiment analysis of user reviews for dress-up games, focusing on understanding user perceptions regarding inclusivity, customization, and overall satisfaction. By analyzing sentiment data pre- and post-2011, we aim to observe trends in user attitudes towards these games over time.

## Overview

The sentiment analysis is performed on user reviews collected for various dress-up games, with the purpose of gaining qualitative insights into player sentiment. This analysis also looks at how specific game features, such as the number of skin tones and gender options, correlate with user satisfaction.

## Folder Structure

- **sentiment_analysis_reviews/**
  - `sentiment_analysis.py`: Python script for conducting sentiment analysis on user reviews.
  - `user_reviews.csv`: Dataset containing user reviews of dress-up games.
  - `dress_up_games.csv`: Dataset containing metadata about the dress-up games (e.g., number of skin tones, developer, gender options).
  - **visuals/**: Contains visualizations generated during the analysis, such as:
    - `sentiment_distribution.png`: Sentiment distribution of user reviews.
    - `sentiment_pre_post_2011.png`: Comparison of sentiment scores for games released pre- and post-2011.

## How to Run

1. **Install Required Libraries**:
   - Run `pip install pandas nltk matplotlib seaborn` to install the necessary Python libraries.

2. **Download VADER Lexicon**:
   - Run the following command in a Python environment to download the lexicon required for sentiment analysis:
     ```python
     import nltk
     nltk.download('vader_lexicon')
     ```

3. **Run the Analysis**:
   - Execute the script `sentiment_analysis.py` to perform the sentiment analysis and generate visualizations.

4. **Results**:
   - Processed results will be saved in `processed_user_reviews.csv`.
   - Visualizations will be saved in the `visuals/` folder for easy access.

## Results Overview

- **Sentiment Distribution**: The sentiment distribution plot helps us understand how users perceive inclusivity and customization across the different dress-up games.
- **Pre- vs Post-2011 Comparison**: The boxplot comparison reveals changes in user sentiment before and after 2011, potentially indicating improvements in customization options or inclusivity.

## Future Directions

- **Feature Correlation**: Further analysis can be done to explore how game features, such as the number of skin tones and gender options, correlate with user satisfaction.
- **Data Visualization**: More visualizations may be created to better understand trends in the sentiment data.

This repository aims to shed light on the evolution of user preferences in dress-up games, focusing on diversity and inclusivity, and to offer insights into the changes in player sentiment over time.
