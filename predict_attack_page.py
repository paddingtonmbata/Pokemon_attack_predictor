import streamlit as st
import pickle 
import numpy as np

def load_model():
    with open('saved_data.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
torf = (
    "True",
    "False",
)

def show_predict_page():
    st.title("Pokemon Attack Prediction Based on Other Stats")
    st.write(""" ### Enter your pokemon's stats to get the predicted attack stat""")

    total_points = st.slider("total points", 0, 720, 350)
    HP = st.slider("Health Points", 0, 255, 120)
    Defense = st.slider("Defense", 0, 230, 50)
    Generation = st.slider("Generation", 1, 6, 1)
    Legendary = st.selectbox("Is Legendary", torf)

    ok = st.button("Calculate Attack")

    if ok:
        X = np.array([[total_points, HP, Defense, Generation, int(bool(Legendary))]])
        X = X.astype(int)
        attack = regressor.predict(X)
        st.subheader(f"YOUR POKEMON'S ESTIMATED ATTACK IS {attack[0]}")
        