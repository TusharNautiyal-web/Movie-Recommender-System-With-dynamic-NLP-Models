import re
import pandas as pd
import streamlit as st
import requests
import random
from nltk.corpus import stopwords
import cloudpickle
import pickle
from urllib.request import urlopen

    

final_df = pd.read_csv('final_df.csv')
global similarity_bert
global similarity_bag_of_Words
global similarity_with_tf_idf_word_2_vec
global similarity_with_word_2_vec
global tf_idf_similarities
similarity = {'similarity_bert':'',
              'similarity_bag_of_Words':'',
              'tf_idf_similarities':'',
              'similarity_with_word_2_vec':'',
              'similarity_with_tf_idf_word_2_vec':''}

model_sentiment = pickle.load(open('model_sentiment.pkl','rb'))
tf_idf_vectorizer = pickle.load(open('tf_idf_vectorizer','rb'))


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
    result = []
    movie = movie.lower()
    titles = final_df['title_y'].str.lower().to_list()

    if movie in titles:
        index = final_df.loc[final_df['title_y'].str.lower() == movie].index[0]
    else:
        index = find_closest(movie)
    if index==4800:
        raise ValueError('Please Enter a correct movie name so that we can recommend properly Please recheck')
    if(model == 'bert'):
        similarity_bert = similarity['similarity_bert']
        distances = sorted(list(enumerate(similarity_bert[index])),reverse=True,key = lambda x: x[1])
    
    elif(model=='bag_of_words'):
        st.write(similarity['similarity_bag_of_Words'])
        similarity_bag_of_Words = similarity['similarity_bag_of_Words']
        distances = sorted(list(enumerate(similarity_bag_of_Words[index])), reverse=True,key = lambda x: x[1])
    
    elif(model=='tf-idf'):
        tf_idf_similarities = similarity['tf_idf_similarities']
        distances = sorted(list(enumerate(tf_idf_similarities[index])), reverse=True,key = lambda x: x[1])
    
    elif(model=='word2vec'):
        similarity_with_word_2_vec = similarity['similarity_with_word_2_vec']
        distances = sorted(list(enumerate(similarity_with_word_2_vec[index])), reverse=True,key = lambda x: x[1])
    
    elif(model=='tf-idf+word2vec'):
        similarity_with_tf_idf_word_2_vec = similarity['similarity_with_tf_idf_word_2_vec']
        distances = sorted(list(enumerate(similarity_with_tf_idf_word_2_vec[index])), reverse=True,key = lambda x: x[1])

    for i in distances[0:6]:
        result.append([final_df.iloc[i[0]].id, final_df.iloc[i[0]].title_y])
    return result

def main():
    st.set_page_config(layout="wide")
    hide_footer_style = """
    <style>
    .css-2ykyy6 { 
        visibility: hidden;
    }
    </style> 
    """
    st.markdown(hide_footer_style, unsafe_allow_html=True)
    
    #We will use session states. This will help in saving models once loaded so that for one instance you don't have to do downloads again. 
        
        
    with st.form("my_form"):
        st.title('Movie Recommeder System')
        st.text('You Can Switch Between models to see the performance of recommendation')
        st.markdown('We have used Bag of Words ,**BERT** specifically **(multi-qa-MiniLM-L6-cos-v1)** , **TF-IDF**, and implemented **TF-IDF + Word2Vec** Model Check repo to understand better. By Default the Flow is in BERT if you want to swith select a model from below. This recommender system is a content base recommendation system.')
        model = st.selectbox('Select A Model Procedure',('Bert', 'Bag of Words','TF-IDF','Word2Vec','TF-IDF + Word2Vec'))
        query = st.text_input('Enter Any Movie Name or something related to that movie')
        submitted = st.form_submit_button("RECOMMEND")
        
        if st.session_state.get('button') != True:
             st.session_state['button'] = submitted # Saved the state

        
    if st.session_state['button'] == True:
        if(model=='Bert'):
            model= 'bert'
            if 'similarity_bert' not in st.session_state:
                with st.spinner('Wait Model is Loading.....Till Then How much you like movies'):
                    st.session_state.similarity_bert = ''
                    similarity['similarity_bert'] = cloudpickle.load(urlopen('https://drive.google.com/uc?export=download&id=131DguHzk9ZF6AGNozHRawwdFupgycqUT'))
                    st.session_state.similarity_bert = similarity['similarity_bert']
            else:
                similarity['similarity_bert'] = st.session_state['similarity_bert']
            st.success(f'Done!')
            

        elif(model == 'Bag of Words'):
            model = 'bag_of_words'
            
            if 'similarity_bag_of_Words' not in st.session_state:
                with st.spinner('Wait Model is Loading.....Till Then How much you like movies'):
                    st.session_state.similarity_bag_of_Words = ''
                    similarity['similarity_bag_of_Words'] = cloudpickle.load(urlopen('https://drive.google.com/uc?export=download&id=1o7pWZfaku_43do0beNfOI6Pz9JeAM6n3&confirm=t&uuid=ccc39f37-f727-49fb-8a30-c9214b30e5f3'))
                    st.session_state['similarity_bag_of_Words'] = similarity['similarity_bag_of_Words']
            else:
               similarity['similarity_bag_of_Words'] = st.session_state['similarity_bag_of_Words']
            st.success(f'Done!')

                    
        elif(model == 'TF-IDF'):
            model = 'tf-idf'
            
            if 'tf_idf_similarities' not in st.session_state:
                with st.spinner('Wait Model is Loading.....Till Then How much you like movies'):
                    st.session_state.tf_idf_similarities = ''
                    similarity['tf_idf_similarities'] = cloudpickle.load(urlopen("https://drive.google.com/uc?export=download&id=1ZcL60svASwVrLoAgBnj43tM8i9IkES_E&confirm=t&uuid=e38591c2-777b-490e-a574-700b33ea642e"))
                    st.session_state.tf_idf_similarities = similarity['tf_idf_similarities']
            else:
                similarity['tf_idf_similarities'] = st.session_state.tf_idf_similarities
            st.success(f'Done!')

        elif(model == 'TF-IDF + Word2Vec'):
            model = 'tf-idf+word2vec'
            if 'similarity_with_tf_idf_word_2_vec' not in st.session_state:
                with st.spinner('Wait Model is Loading.....Till Then How much you like movies?'):
                    st.session_state.similarity_with_tf_idf_word_2_vec = ''
                    similarity['similarity_with_tf_idf_word_2_vec'] = cloudpickle.load(urlopen("https://drive.google.com/uc?export=download&id=1Ykoqty6n9uXn1oBXRCjuFr6mnqUuIVq6&confirm=t&uuid=12d331b1-5ff7-4c7b-92eb-884dfd7525ab"))
                    st.session_state.similarity_with_tf_idf_word_2_vec = similarity['similarity_with_tf_idf_word_2_vec']
            else:
                similarity['similarity_with_tf_idf_word_2_vec'] = st.session_state.similarity_with_tf_idf_word_2_vec
            st.success(f'Done!')

                
        elif(model == 'Word2Vec'):
            model = 'word2vec'
            if 'similarity_with_word_2_vec' not in st.session_state:
                with st.spinner('Wait Model is Loading.....Till Then How much you like movies'):
                    st.session_state.similarity_with_word_2_vec = ''
                    similarity['similarity_with_word_2_vec'] = cloudpickle.load(urlopen("https://drive.google.com/uc?export=download&id=1dpWQotH3TEPVyJTaBonwTILY3DCtTodb"))
                    st.session_state.similarity_with_word_2_vec = similarity['similarity_with_word_2_vec']
            else:
                similarity['similarity_with_word_2_vec'] = st.session_state.similarity_with_word_2_vec
            st.success(f'Done!')

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
           review = st.text_input(f"How much you liked the movie {output_names[0]}",key='review1')
           btn0 = st.button('submit',key = 'btn0')
           if btn0:
                review = re.sub('[^a-zA-Z0-9 ]','',review)
                review = tf_idf_vectorizer.transform([review])
                ans = model_sentiment.predict(review)
                if  ans == 0:
                    review = 'Thanks for your positive review'
                else:
                    review = 'Sorry for your negative review'
                st.write(review)
        with col2:
           st.image(output_images[1])
           st.markdown(output_names[1].upper())
           review = st.text_input(f"How much you liked the movie {output_names[1]}",key='review2')
           btn1 = st.button('submit',key = 'btn1')
           if btn1:
                review = re.sub('[^a-zA-Z0-9 ]','',review)
                review = tf_idf_vectorizer.transform([review])
                ans = model_sentiment.predict(review)
                if  ans == 0:
                    review = 'Thanks for your positive review'
                else:
                    review = 'Sorry for your negative review'
                st.write(review)
        
        with col3:
           st.image(output_images[2])
           st.markdown(output_names[2].upper())
           review = st.text_input(f"How much you liked the movie {output_names[2]}",key='review3')
           btn2 = st.button('submit',key = 'btn2')
           if btn2:
                review = re.sub('[^a-zA-Z0-9 ]','',review)
                review = tf_idf_vectorizer.transform([review])
                ans = model_sentiment.predict(review)
                if  ans == 0:
                    review = 'Thanks for your positive review'
                else:
                    review = 'Sorry for your negative review'
                st.write(review)
        
        col4, col5, col6 = st.columns(3)
        
        with col4:
           st.image(output_images[3])
           st.markdown(output_names[3].upper())
           review = st.text_input(f"How much you liked the movie {output_names[3]}",key='review4')
           if st.button('submit',key='btn3'):
                review = re.sub('[^a-zA-Z0-9 ]','',review)
                review = tf_idf_vectorizer.transform([review])
                ans = model_sentiment.predict(review)
                if  ans == 0:
                    review = 'Thanks for your positive review'
                else:
                    review = 'Sorry for your negative review'
                st.write(review)
        
        with col5:
           st.image(output_images[4])
           st.markdown(output_names[4].upper())
           review = st.text_input(f"How much you liked the movie {output_names[4]}",key='review5')
           if st.button('submit',key='btn4'):
                review = re.sub('[^a-zA-Z0-9 ]','',review)
                review = tf_idf_vectorizer.transform([review])
                ans = model_sentiment.predict(review)
                if  ans == 0:
                    review = 'Thanks for your positive review'
                else:
                    review = 'Sorry for your negative review'
                st.write(review)
        
        with col6:
           st.image(output_images[5])
           st.markdown(output_names[5].upper())
           review = st.text_input(f"How much you liked the movie {output_names[5]}",key='review6')
           if st.button('submit',key = 'btn5'):
                review = re.sub('[^a-zA-Z0-9 ]','',review)
                review = tf_idf_vectorizer.transform([review])
                ans = model_sentiment.predict(review)
                if  ans == 0:
                    review = 'Thanks for your positive review'
                else:
                    review = 'Sorry for your negative review'
                st.write(review)
        

if __name__ == '__main__':
    main()