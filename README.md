# Twitter Social Media Sentiment Analysis

This project builds a machine learning pipeline to analyze public sentiment toward COVID-19 vaccination using Twitter data.

The goal of the project is to collect tweets, process textual data, and classify sentiment using NLP techniques and transformer-based models.

---

## Project Overview

Social media sentiment analysis helps researchers and companies understand public opinion in real time. By analyzing tweets, we can identify trends, reactions to events, and public attitudes toward specific topics.

In this project we:

• Collected tweets using the Twitter API  
• Stored and processed data using Python and SQL databases  
• Applied NLP techniques for sentiment classification  
• Used transformer-based models with a zero-shot learning approach  
• Visualized sentiment trends and model confidence  

---

## Technologies Used

Python  
SQL  
Machine Learning  
Natural Language Processing (NLP)  
Jupyter Notebook  
Pandas  
Matplotlib  

---

## Project Structure

twitter-sentiment-analysis
│
├── data_collection
│   ├── pullFollowerID.py
│   ├── pullTimeline.py
│   └── pullUserID.py
│
├── database
│   ├── sql_classes.py
│   └── twitter_tile_db.py
│
├── modeling
│   └── CISC_499_Model.ipynb
│
└── README.md

## Dataset

Approximately 900 tweets were collected using the Twitter API and used for sentiment classification experiments.

---

## Future Improvements

• Improve multilingual tweet classification  
• Expand dataset size  
• Build an interactive dashboard for visualization
