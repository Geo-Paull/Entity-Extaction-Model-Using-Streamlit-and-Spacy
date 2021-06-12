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
st.title("_paul.ai, your text-processing buddy!")
st.sidebar.title("_Welcome Human! 🤩")
st.sidebar.text("==================================")
st.sidebar.text("I'm paul.ai, your text buddy!\nView the Magic Box 📦 for my abilities.\nHow can I blow your mind today? :)")
st.sidebar.text("==================================")
st.sidebar.subheader("Pick a tool to start with:")

#Picking what NLP task you want to do
option = st.sidebar.selectbox('Magic Box 📦', ('Sentiment Analysis', 'Named Entity Recognition', 'Text Summarization', 'Entity Extraction'))


st.sidebar.title("_Curious about Me? 🤔")
st.sidebar.write(" I am an Intelligent Text processing \n creature, that auto-extracts entities,\n classifies entities, \n analyse sentiments, & summarises your texts...") 
st.sidebar.subheader("I'm popularly known for:")
st.sidebar.text("----------------------------------")
st.sidebar.text("1. Sentiment Analysis")
st.sidebar.text("2. Entity Extraction")
st.sidebar.text("3. Text Summarization")
st.sidebar.text("4. Name Entity Recognition [NER]")

st.sidebar.text("==================================")

# st.sidebar.subheader("_I was Created by:")

st.sidebar.header("_meet my creator 😇")
st.sidebar.text("----------------------------------")
st.sidebar.markdown('NAME: **Paul DADA**')

st.sidebar.markdown(
    """<a href="http://pauldada.xyz">| Personal Website</a>""", unsafe_allow_html=True,)

st.sidebar.markdown(
    """<a href="https://www.linkedin.com/in/pauldada/">| LinkedIn Page</a>""", unsafe_allow_html=True,)

st.sidebar.markdown(
    """<a href="https://github.com/Geo-Paull">| Github Page!</a>""", unsafe_allow_html=True,)

st.sidebar.text("==================================")
# st.sidebar.markdown('**http://pauldada.xyz/**')

st.sidebar.text('Copyright (c) 2021. \nAll rights reserved')

#Textbox for text user is entering
st.success('NOTE \nAlmost there, paste text & click run SERVICE.')
# st.text("Type/paste the text you'd like to analyze.")
# text = st.text_input('Enter text', 'Enter Text Here')
text = st.text_area('Type/paste your text in the box below', value='...', height=100, max_chars=None, help='Text must be more than a Sentence long.')

st.button("RUN Service")

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
    
    st.write ("Each word in the lexicon has scores for:")
    st.text ("1)     polarity: negative vs. positive    (-1.0 => +1.0)")
    st.text ("2) subjectivity: objective vs. subjective (+0.0 => +1.0)")
    #st.text ("3)    intensity: modifies next word?      (x0.5 => x2.0)")
    
    st.write ("The sentiment details of the overall text are:")
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
elif option == 'Named Entity Recognition':
    docx = nlp(text)
    res = spacy_streamlit.visualize_ner(docx, labels=nlp.get_pipe('ner').labels)
    st.write(res)
    st.subheader("Label KEYS")
    st.text("PERSON:      People, including fictional.\n
NORP:        Nationalities or religious or political groups.\n
FAC:         Buildings, airports, highways, bridges, etc.\n
ORG:         Companies, agencies, institutions, etc.\n
GPE:         Countries, cities, states.\n
LOC:         Non-GPE locations, mountain ranges, bodies of water.\n
PRODUCT:     Objects, vehicles, foods, etc. (Not services.)\n
EVENT:       Named hurricanes, battles, wars, sports events, etc.\n
WORK_OF_ART: Titles of books, songs, etc.\n
LAW:         Named documents made into laws.\n
LANGUAGE:    Any named language.\n
DATE:        Absolute or relative dates or periods.\n
TIME:        Times smaller than a day.\n
PERCENT:     Percentage, including ”%“.\n
MONEY:       Monetary values, including unit.\n
QUANTITY:    Measurements, as of weight or distance.\n
ORDINAL:     “first”, “second”, etc.\n
CARDINAL:    Numerals that do not fall under another type.")

#Text Summarization
elif option == 'Text Summarization':
    summWords = summarize(text)
    st.subheader("Text Summary")
    st.write(summWords)


