import pickle
import pandas as pd
import streamlit as st
import requests
import random
from nltk.corpus import stopwords
 
final_df = pd.read_csv('final_df.csv')
similarity_bert = pickle.load(open('similarity_with_bert.pkl','rb'))
similarity_bag_of_Words = pickle.load(open('similarity_with_bag_of_words.pkl','rb'))

def find_closest(text):
    text = text.strip()
    new_text = text.split(' ')
    for word in new_text[:]:
        if word in stopwords.words('english'):
            new_text.remove(word)
    index = random.randint(0,len(new_text)-1)
    text = new_text[index]
    spliteer = final_df['title_y'].str.split(' ')
    i = 0
    for val in spliteer.to_list():
        if text in val:
            break
        i+=1
    return i
def recommend(movie,model):
    movie = movie.lower()
    titles = final_df['title_y']
    if movie in titles.to_list():
        index = final_df[final_df['title_y'] == movie].index[0]
    else:
        index = find_closest(movie)
    if index==4800:
        raise ValueError('Please Enter a correct movie name so that we can recommend properly Please recheck')
    result = []
    if(model == 'bert'):
        distances = sorted(list(enumerate(similarity_bert[index])),reverse=True,key = lambda x: x[1])
    else:
        distances = sorted(list(enumerate(similarity_bag_of_Words[index])), reverse=True,key = lambda x: x[1])

    for i in distances[0:6]:
        result.append([final_df.iloc[i[0]].id,final_df.iloc[i[0]].title_y])
    return result
def main():
    st.set_page_config(layout="wide")
    st.title('Movie Recommeder System')
    st.text('You Can Switch Between models to see the performance of recommendation')
    st.markdown('We have used Bag of Words and **BERT** specifically **(multi-qa-MiniLM-L6-cos-v1)**. By Default the Flow is in BERT if you want to swith select a model from below. This recommender system is a content base recommendation system.')
    model = st.selectbox('Select A Model Procedure',('bert', 'Bag of Words','TFIDF'))
    query = st.text_input('Enter Any Movie Name or something related to that movie')
    submit = st.button('RECOMMEND')
    if submit:
        output_images = []
        output_names = []
        if query!=None:
            res = recommend(query,model)
        if len(res)<=1:
            raise TypeError("Hi Looks Like The Query You have entered iam not able to find Please Try Again dont add spaces during the start of the text or Don't Add special characters like @ - # etc")
        for ele in res:
            image = requests.get(f'https://api.themoviedb.org/3/movie/{ele[0]}/images?api_key=81428e7817728a742c8e842120989817')
            data = image.json()
            data = data['backdrops'][0]['file_path']
            output_images.append('http://image.tmdb.org/t/p/w500/'+data)
            output_names.append(ele[1])
        
        col1, col2, col3 = st.columns(3)
        with col1:
           st.image(output_images[0])
           st.markdown(output_names[0].upper())
        
        with col2:
           st.image(output_images[1])
           st.markdown(output_names[1].upper())
        
        with col3:
           st.image(output_images[2])
           st.markdown(output_names[2].upper())
        
        col4, col5, col6 = st.columns(3)
        
        with col4:
           st.image(output_images[3])
           st.markdown(output_names[3].upper())
        
        with col5:
           st.image(output_images[4])
           st.markdown(output_names[4].upper())
        
        with col6:
           st.image(output_images[5])
           st.markdown(output_names[5].upper())

if __name__ == '__main__':
    main()