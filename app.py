import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from streamlit_lottie import st_lottie
import json

translator = Translator()
st.title('Uso de TextBlob')

st.subheader("Ingresa en el campo de texto la frase que quieres analizar")
with st.sidebar:
               st.subheader("Polaridad y Subjetividad")
               ("""
                Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
                Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
                
               Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
               (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.

                 """
               ) 


with st.expander('Evaluar la polaridad y subjetividad de un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:

        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        #blob = TextBlob(text1)
       
        
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( 'Es una emoción positiva 😊')
        elif x <= -0.5:
            st.write( 'Es una emoción negativa 😔')
        else:
            st.write( 'Es una emoción neutral 😐')

with st.expander('Corrección en inglés'):
       text2 = st.text_area('Por favor, escribe: ',key='4')
       if text2:
          blob2=TextBlob(text2)
          st.write((blob2.correct())) 

with open('graficos.json') as source:
      animation=json.load(source)
st. lottie (animation,width =350)
