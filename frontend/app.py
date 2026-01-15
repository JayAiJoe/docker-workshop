import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Docker Workshop - Frontend", page_icon="🐳", layout="centered")

# Backend API URL - will work when both containers are running
BACKEND_URL = "http://backend:8000"

st.title("🐳 Docker Workshop - Streamlit Frontend")
st.write("Welcome to the Docker and Docker Compose workshop!")
st.write("This app connects to the FastAPI backend running in another container.")

st.divider()

# Create two columns for the buttons
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎉 Get Greeting")
    if st.button("Get Greeting", use_container_width=True, type="primary"):
        try:
            response = requests.get(f"{BACKEND_URL}/api/greeting")
            if response.status_code == 200:
                data = response.json()
                st.success(data["greeting"])
            else:
                st.error(f"Error: {response.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to backend. Make sure both containers are running!")
        except Exception as e:
            st.error(f"Error: {str(e)}")

with col2:
    st.subheader("🎲 Get Random Number")
    if st.button("Get Random Number", use_container_width=True, type="primary"):
        try:
            response = requests.get(f"{BACKEND_URL}/api/random-number")
            if response.status_code == 200:
                data = response.json()
                st.success(f"🎯 {data['message']}")
                st.balloons()
            else:
                st.error(f"Error: {response.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to backend. Make sure both containers are running!")
        except Exception as e:
            st.error(f"Error: {str(e)}")

st.divider()

# Info section
with st.expander("ℹ️ About this Workshop"):
    st.write("""
    **What you'll learn:**
    - How to containerize a Python FastAPI backend
    - How to containerize a Streamlit frontend
    - How to use Docker Compose to run multiple containers
    - How containers communicate with each other
    
    **Your Task:**
    1. Create a `Dockerfile` in the backend folder
    2. Create a `Dockerfile` in the frontend folder
    3. Create a `docker-compose.yml` in the root folder
    4. Run `docker-compose up` and see both services working together!
    """)
