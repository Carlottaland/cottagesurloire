

import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Cottage sur Loire", layout="wide")

# Lire le CSV et construire les credentials
df = pd.read_csv("users.csv")

credentials = {
    "usernames": {
        row["email (fleurette@email.com)"]: {
            "name": row["name"],
            "email": row["email"],
            "password (motdepasse)": row["password"]
        } for _, row in df.iterrows()
    }
}

preauthorized = {"emails": []}

authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name="auth",
    key="tubercule_key",
    cookie_expiry_days=1,
    preauthorized=preauthorized
)

# Connexion (ne renvoie rien → pas de variables à gauche)
authenticator.login(location="sidebar", key="login")

# Gestion de session
auth_status = st.session_state.get("authentication_status", None)

if auth_status:
    authenticator.logout(location="sidebar", key="logout_button")
    st.sidebar.success(f"Bienvenue {st.session_state['name']}")
    st.title("Cottage sur Loire")
    st.write("Bienvenue dans votre jardin privé.")
elif auth_status is False:
    st.error("Nom d’utilisateur ou mot de passe incorrect")
elif auth_status is None:
    st.warning("Veuillez entrer vos identifiants")



# --- Sidebar ---
st.sidebar.title("Menu")
page = st.sidebar.radio("Navigation", ["Accueil", "Rosiers", "Vie du jardin"])

# --- Accueil ---
if page == "Accueil":
    st.title("Bienvenue dans mon joli jardin")
    st.image("cottage.png", use_container_width=True)

# --- Rosiers ---
elif page == "Rosiers":
    st.title("Avant, j'aimais pas trop les rosiers, mais c'était avant")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("fizzy_lady.png", caption="Fizzy Lady", use_container_width=True)
    with col2:
        st.image("roseromantic.png", caption="Rose Romantic", use_container_width=True)
    with col3:
        st.image("new_imagine.png", caption="New Imagine", use_container_width=True)

# --- Vie du jardin ---
elif page == "Vie du jardin":
    st.title("Vie du jardin")
    col1, col2 = st.columns(2)
    with col1:
        st.image("bourdon.png", caption="Bourdon", use_container_width=True)
    with col2:
        st.image("abeille_xylocope.png", caption="Abeille xylocope", use_container_width=True)
