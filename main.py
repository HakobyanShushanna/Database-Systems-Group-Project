import streamlit as st
from UserInterface.Navigation import navigation

# Set page config
st.set_page_config(page_title="Banking App", page_icon="🏦", layout="centered")

if __name__ == "__main__":
    navigation()