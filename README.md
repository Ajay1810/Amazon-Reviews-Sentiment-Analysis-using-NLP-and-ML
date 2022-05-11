# Amazon-Reviews-Sentiment-Analysis-using-NLP-and-ML
Classifying a review as Positive or Negative by training the model using NLP technique like Tf-Idf vectorizer, 
then training the model using Logistic Regression Classification algorithm to predict the nature of the review.

There are 4 files in this project
1. data_transform.py - Which is used to transform the data from JSON format to usable CSV format for further usage of the data.

2. model.py - In this file the CSV is further subdivided into Training and Testing data with Features and Labels. Then using the Tf-Idf vectorizer technique of NLP words
                transformed into dictionary with Keys as Words and Value as their Occurance frequency in the CSV file, which is then fed to the Logictic Regression for 
                model building and stored using pickel library.
 
3. scrapper.py - Scrapper is used to scrap reviews form Amazon site which are then stored as a CSV to fed to the build model to check the sentiment of the review.

4. visualization.py - Here, a interface has been made to showcase the sentiment of the scrapped reviews.
