# Recomendar_Libros
Desarrollé un sistema de recomendación utilizando técnicas de Procesamiento de Lenguaje Natural (NLP) y machine learning.
## ¿Qué hice?
* Trabajé con un dataset de miles de libros, y seleccioné las variables más relevantes para el proyecto (título, autor, descripción, categoría).
* Unifiqué y reorganicé automáticamente varias categorías en grupos más generales como Fiction, Mystery, Romance, etc.
* Apliqué técnicas de NLP: tokenización, eliminación de stopwords y stemming para preparar los textos.
* Apliqué TF-IDF para convertir el contenido textual en vectores.
* Calculé la similitud entre libros usando cosine similarity, para recomendar libros similares al seleccionado.
* Y finalmente implementé una interfaz en Streamlit para que el usuario pueda ingresar un libro y recibir recomendaciones de forma interactiva.

## Tecnologías utilizadas:
* Python
* Pandas & NumPy
* Scikit-learn (TF-IDF, cosine similarity)
* NLTK (procesamiento y limpieza de texto)
* Joblib (persistencia del modelo)
* Streamlit (interfaz web)

## Resultado
Ingresás un libro y recibís 10 recomendaciones personalizadas basadas en su contenido textual.
![image](https://github.com/user-attachments/assets/f7d7c3d0-5194-486a-bda2-1c62870216a7)
![image](https://github.com/user-attachments/assets/c317ee7e-fff2-4ddb-9647-3894dbf95f92)
![image](https://github.com/user-attachments/assets/2c834da4-aebc-4248-890f-edabd40d52ba)
![image](https://github.com/user-attachments/assets/0913839f-c54c-4fd2-bd37-6fd30e9c9989)

Link del dataset usado: https://www.kaggle.com/datasets/abdallahwagih/books-dataset

