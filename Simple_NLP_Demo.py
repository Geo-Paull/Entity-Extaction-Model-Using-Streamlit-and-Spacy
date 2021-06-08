import streamlit as st
from textblob import TextBlob
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
#NER Imports
import spacy
import spacy_streamlit
from spacy import displacy

#Text_Summariser Imports
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
from collections import Counter
import en_core_web_sm
nlp = spacy.load("en_core_web_sm")


#Headings for Web Application
st.title("NLP Web Application Example")
st.subheader("Choose NLP service")

st.sidebar.title("About this Service")
st.sidebar.subheader("Demo service for:")
st.sidebar.text("                         ")
st.sidebar.text("1. Sentiment _Analysis")
st.sidebar.text("2. Entity _Extraction")
st.sidebar.text("3. Text _Summarization")
st.sidebar.text("4. Name _Entity Recognizer_(NER)")

st.sidebar.subheader("Authored By:")
st.sidebar.markdown('**Paul DADA**')
#Picking what NLP task you want to do
option = st.selectbox('NLP Service', ('Sentiment Analysis', 'Entity Extraction', 'Text Summarization', 'Named Entity Recognizer'))

#Textbox for text user is entering
st.subheader("Enter the text you'd like to analyze.")
# text = st.text_input('Enter text', 'Enter Text Here')
text = st.text_area('...', value='Type/Paste Text Here...', height=100, max_chars=None, help='Text must be more than a Sentence long')

#Display results of the NLP task
st.header("Results")

#Sentiment Analysis
if option == 'Sentiment Analysis':
    #Creating graph for sentiment across each sentence in the text inputted
    sents = sent_tokenize(text) #tokenizing the text data into a list of sentences
    entireText = TextBlob(text) #storing the entire text in one string
    sentScores = [] #storing sentences in a list to plot
    for sent in sents:
        text = TextBlob(sent) #sentiment for each sentence
        score = text.sentiment[0] #extracting polarity of each sentence
        sentScores.append(score)

    #Plotting sentiment scores per sentence in line graph
    st.line_chart(sentScores) #using line_chart st call to plot polarity for each sentence

    #Polarity and Subjectivity of the entire text inputted
    sentimentTotal = entireText.sentiment
    st.write("The sentiment of the overall text below.")
    st.write(sentimentTotal)

elif option == 'Entity Extraction':
    #Getting Entity and type of Entity
    entities = [] #list for all entities
    entityLabels = [] #list for type of entities
    doc = nlp(text) #this call extracts all entities, make sure the spacy en library is loaded
    #iterate through all entities
    for ent in doc.ents:
        entities.append(ent.text)
        entityLabels.append(ent.label_)
    entDict = dict(zip(entities, entityLabels)) #Creating dictionary with entity and entity types

    #Function to take in dictionary of entities, type of entity, and returns specific entities of specific type
    def entRecognizer(entDict, typeEnt):
        entList = [ent for ent in entDict if entDict[ent] == typeEnt]
        return entList

    #Using function to create lists of entities of each type
    entOrg = entRecognizer(entDict, "ORG")
    entCardinal = entRecognizer(entDict, "CARDINAL")
    entPerson = entRecognizer(entDict, "PERSON")
    entDate = entRecognizer(entDict, "DATE")
    entGPE = entRecognizer(entDict, "GPE")

    #Displaying entities of each type
    st.write("Organization Entities: " + str(entOrg))
    st.write("Cardinal Entities: " + str(entCardinal))
    st.write("Personal Entities: " + str(entPerson))
    st.write("Date Entities: " + str(entDate))
    st.write("GPE Entities: " + str(entGPE))

#Name Entity Recognizer
elif option == 'Named Entity Recognizer':
    docx = nlp(text)
    res = spacy_streamlit.visualize_ner(docx, labels=nlp.get_pipe('ner').labels)
    st.write(res)

#Text Summarization
else:
    summWords = summarize(text)
    st.subheader("Summary")
    st.write(summWords)


