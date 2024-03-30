import streamlit as st
import joblib
import bentoml
import numpy as np

# Chargement du modèle
model = bentoml.sklearn.load_model('iris_model:latest')

# Dictionnaire pour mapper les classes prédites aux noms des espèces d'iris
iris_species = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

def main():
    st.title("Application de Classification Iris")
    user_input = st.text_input("Entrez les caractéristiques (séparées par des virgules) : ")
    
    if st.button("Classe"):
        if user_input:
            # Convertir la chaîne d'entrée en une liste de valeurs flottantes
            user_input_list = [float(x.strip()) for x in user_input.split(',')]
            
            # Vérifier que nous avons les quatre attributs nécessaires
            if len(user_input_list) == 4:
                # Prédiction avec le modèle
                prediction = model.predict(np.array([user_input_list]))[0]
                
                # Affichage du résultat
                predicted_species = iris_species.get(prediction, "espèce inconnue")
                st.write(f"Analyse : C'est un iris de l'espèce {predicted_species}.")
            else:
                st.write("Veuillez entrer quatre caractéristiques.")
        else:
            st.write("Veuillez entrer des caractéristiques.")

if __name__ == "__main__":
    main()

