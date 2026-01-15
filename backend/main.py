from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Backend!"}

@app.get("/api/greeting")
def get_greeting():
    greetings = [
        "Hello from FastAPI!",
        "Kumusta from the backend!",
        "Mabuhay! Welcome to our API!",
        "Good day from the server!",
        "Greetings from the Docker container!"
    ]
    return {
        "greeting": random.choice(greetings),
        "status": "success"
    }

@app.get("/api/random-number")
def get_random_number():
    number = random.randint(1, 100)
    return {
        "number": number,
        "message": f"Your lucky number is {number}!",
        "status": "success"
    }
