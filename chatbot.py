import nltk
import numpy as np
import random
import string

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

tokenizer = RegexpTokenizer(r'\w+')
stemmer = SnowballStemmer('spanish')

#f=open('funcionamiento_chatbot.txt','r',errors = 'ignore')
#raw=f.read()
#raw=raw.lower()
def LemNormalize(text):
    tokens = tokenizer.tokenize(text.lower())
    tokens = [stemmer.stem(token) for token in tokens if token not in stopwords.words('spanish')]
    return tokens

GREETING_INPUTS = ("hola", "que tal", "saludos", "que hay", "que honda","holi",)
GREETING_RESPONSES = ["¡Hola!", "¡Hey!", "*asiente*", "¡Hola! ¿Cómo estás?", "¡Hola!", "¡Me alegra! Estás hablando conmigo"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words=None)
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"Lo siento no entiendo lo que dices"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

f = open('funcionamiento_chatbot.txt','r',errors = 'ignore') # Asegúrate de tener un archivo funcionamiento_chatbot_es.txt
raw = f.read()
raw = raw.lower()
sent_tokens = nltk.sent_tokenize(raw) 

flag=True
print("Ann: Hola, mi nombre es Ann, dime en que te puedo ayudar")
while(flag==True):
    user_response = input("Tu:")
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("Ann: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("Ann: "+greeting(user_response))
            else:
                print("Ann: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("Ann: Bye!!! Cuidate")

