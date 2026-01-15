# FastAPI + Streamlit Demo Application

A full-stack application demonstrating containerized microservices architecture with a Python FastAPI backend and Streamlit frontend.

## 🏗️ Architecture

This application consists of two containerized services:

**Backend (FastAPI)**
- REST API service running on port 8000
- Provides two endpoints:
  - `/api/greeting` - Returns random greeting messages
  - `/api/random-number` - Generates random numbers with messages
- CORS-enabled for cross-origin requests

**Frontend (Streamlit)**
- Interactive web UI running on port 8501
- Two buttons to interact with backend APIs
- Real-time response display with visual feedback

## 📁 Project Structure

```
.
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Backend dependencies
│   └── Dockerfile           # Backend container config
├── frontend/
│   ├── app.py               # Streamlit application
│   ├── requirements.txt     # Frontend dependencies
│   └── Dockerfile           # Frontend container config
├── docker-compose.yml       # Multi-container orchestration
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Docker
- Docker Compose

### Running with Docker Compose

1. Clone the repository
2. Navigate to the project directory
3. Start the application:

```bash
docker-compose up --build
```

### Accessing the Application

Once the containers are running:
- **Frontend UI**: http://localhost:8501
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

### Stopping the Application

```bash
docker-compose down
```

## 🛠️ Development

### Running Locally (without Docker)

**Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py --server.port=8501
```

Note: When running locally, update the `BACKEND_URL` in `frontend/app.py` to `http://localhost:8000`

## 🐳 Container Details

- **Base Image**: Python 3.11-slim
- **Backend Port**: 8000
- **Frontend Port**: 8501
- **Inter-container Communication**: Docker internal networking

## 📝 API Endpoints

### GET /api/greeting
Returns a random greeting message.

**Response:**
```json
{
  "greeting": "Hello from FastAPI!",
  "status": "success"
}
```

### GET /api/random-number
Generates a random number between 1 and 100.

**Response:**
```json
{
  "number": 42,
  "message": "Your lucky number is 42!",
  "status": "success"
}
```

## 🔧 Technologies Used

- **Backend**: FastAPI, Uvicorn
- **Frontend**: Streamlit, Requests
- **Containerization**: Docker, Docker Compose
- **Language**: Python 3.11
