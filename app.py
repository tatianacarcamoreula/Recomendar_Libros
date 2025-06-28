'''App para interactur con el modelo de recomendación de libros con streamlit'''
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import base64

#extraer los datos que se van a usar para la app
X = joblib.load("modelo/X_entrenado.pkl")
df = pd.read_csv("modelo/df.csv")

#fondo de app
with open("fondo.jpg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()
#se usa la imagen fondo.jpg como fondo
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

#estilos
st.markdown("""
    <style>
    /* establecer todo el texto en negro */
    .stApp {
        color: black;
    }

    /* asegurar que los labels y elementos de formularios estén en negro */
    label, .st-cw, .st-bx, .st-ef, .st-em, .st-eb, .css-16huue1 {
        color: black !important;
    }
    
    /* texto de selectbox en blanco */
    .stSelectbox input {
        color: white !important;
    }

    /* estilo del botón */
    div.stButton > button {
        background-color: #1c1b1b;  /* fondo del botón negro */
        color: white !important;    /* texto blanco */
        border-radius: 6px;
        padding: 0.5em 1em;
        font-weight: bold;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #000000;  /* más oscuro al pasar el mouse */
    }
    </style>
""", unsafe_allow_html=True)

#titulo de la app
st.title("📚 Recomendar Libros 📚")

#indice de los libros
books = pd.Series(df.index, index=df['title_author'].str.strip())

#función para reomendar libros
def recomendar_libros(book_title, X, df, books):
    if book_title not in books:
        return []
    
    id_book = books[book_title]
    query = X[id_book].toarray()
    similitud = cosine_similarity(query, X).flatten()
    indices_recomendados = (-similitud).argsort()[1:11]
    
    return df['title_author'].iloc[indices_recomendados].tolist()

#interfaz de Streamlit
st.subheader("Selecciona un libro para obtener recomendaciones:")
libros_seleccionados = st.selectbox("Libros disponibles", sorted(books.index.tolist()))

if st.button("🔎Recomendar"):
    recomendaciones = recomendar_libros(libros_seleccionados, X, df, books)
    st.write("### Libros recomendados:")
    for i, rec in enumerate(recomendaciones, start=1):
        st.write(f"{i}. {rec}")
