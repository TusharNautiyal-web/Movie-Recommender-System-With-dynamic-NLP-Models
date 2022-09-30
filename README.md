# Dynamic NLP Model Movie-Recommender-system With Sentiment Analysis  
<a href = 'https://huggingface.co/spaces/TusharNautiyal/Dynamic-Movie-Recommender-With-Sentiment-Analysis'/>***Check Deployment***</a>

<a href="https://www.linkedin.com/in/tusharnautiyal/"> <img src = "https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a> <img src = "https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/> <img src = "https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white"/> 

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

# Understanding TF-IDF with Word2Vec Embeddings.

**TF-IDF** is a term frequency-inverse document frequency. It helps to calculate the importance of a given word relative to other words in the document and in the corpus. It calculates in two quantities, TF and IDF. Combining two will give a TF-IDF score.

Calculate the TF-IDF vector for each word in corpus. Let’s call the **TF-IDF** vectors as ***tf1, tf2, tf3, ... and so on*** till n. 

![chart](https://user-images.githubusercontent.com/74553737/193222385-02e7c10d-2589-4539-a981-3bb398fc4d38.png)

After that we can Calculate the **Word2Vec** for each word in the description lets call it as ***W2V1,W2V2,W2V3..........and so on*** till n.

![chart](https://user-images.githubusercontent.com/74553737/193222528-e04ef47b-5725-4ee9-a4da-8a6ff72bd64c.png)


**Multiply** the ***TF-IDF*** score and ***Word2Vec vector*** representation of each word and **sum** all of it.

![chart](https://user-images.githubusercontent.com/74553737/193222659-aba7160d-db53-4b45-9915-a13608b8c254.png)


Then **divide** the total by sum of TF-IDF vectors.These will be our new vectors that we will use for our cosine similarity to create a recommender model.

Considering each word with i and total words as n. **The Complete Formula will be**

![chart](https://user-images.githubusercontent.com/74553737/193220196-d32d1ac3-3aae-40b5-a1c4-a52cd1b27a4d.png)

/ This sign means divide and this Formula image was created using atomurl.net. For more detailed understanding on ***tf-idf+word2vec*** ***Follow me on medium*** where i have posted a full article on it. <a href = 'https://medium.com/@tsa.vevo.music'><img src = 'https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white'/></a>

# Updates
This project is deployed on hugging face spaces here is the link for the deployed applications <a href = 'https://huggingface.co/spaces/TusharNautiyal/Dynamic-Movie-Recommender-With-Sentiment-Analysis'/>***Check Deployment***</a>
