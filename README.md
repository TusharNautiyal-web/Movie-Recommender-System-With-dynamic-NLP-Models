# Dynamic NLP Model Movie-Recommender-system With Sentiment Analysis
Content Based Movie Recommender System Using NLP Dynamic model selection between Bert Pre Trained Model , Bag of Words, TF-IDF, Word2Vec, And TF-IDF+Word2Vec on TMDB Dataset.

This movie recommender was created to better understand each and every NLP model based recommendation working and effective ness based on multiple paramenters.
For each movie you can also enter a review on which a Sentiment Analysis model will work and tell if your review was a good or bad one. 
Sometimes if not able to find movie recommendation just try to refresh and do it again one more time or change the name to a similar name of a moive.
If you like this repository do star it.
# How to Use
Models are loaded using cloud pickle and **session states** are used to stop model from getting downloaded again and again this increases loading speed and loading times. App is created using **streamlit**. Below is a quick demonstration of how it works.

***Run This command in CLI***

```
streamlit run app.py
```

**Recommender Demo**:

https://user-images.githubusercontent.com/74553737/193135421-80a4c790-d14e-4322-982c-36ec7a16aea9.mp4

Sometimes index are not found because either the movie poster is not avalible in the api or the name of the movie was not able to found try to add some variations in your name for eg pirates, carrabiean, sea, monster words that can be in a movie.

**Sentiment Analysis Demo**:

https://user-images.githubusercontent.com/74553737/193136299-185453fa-3235-49a3-99df-c7c2f45ff19c.mp4

Try to write review with more words for better sentiment analysis recommender 20-50 words. We have trained model on **random forest** as it was giving good accuracy and **Tf-idf** vecotrizer for  sentiment analysis model. For more you can check the notebook.

# Updates
Going to upload this whole app on **hugging face Spaces** and will be deployed with full **CI/CD** and **Dockers**. 
Please Do support the repository if you liked it. Thank you Happy Learning
