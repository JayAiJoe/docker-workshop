# 🐳 Docker & Docker Compose Workshop

Welcome to the Docker and Docker Compose workshop! This repository contains a simple FastAPI backend and Streamlit frontend application for you to practice containerization.

## 📋 Workshop Overview

You will learn how to:
- Create Dockerfiles to containerize Python applications
- Use Docker Compose to orchestrate multiple containers
- Enable container-to-container communication
- Run a full-stack application in Docker

## 🏗️ Project Structure

```
philhealth-docker-training/
├── backend/
│   ├── main.py              # FastAPI application (already completed)
│   └── requirements.txt      # Python dependencies (already completed)
├── frontend/
│   ├── app.py               # Streamlit application (already completed)
│   └── requirements.txt      # Python dependencies (already completed)
└── README.md                # This file
```

## ✅ What's Already Done

The application code is complete! You don't need to modify any Python files.

**Backend (FastAPI):**
- Runs on port 8000
- Two endpoints:
  - `/api/greeting` - Returns a random greeting
  - `/api/random-number` - Returns a random number

**Frontend (Streamlit):**
- Runs on port 8501
- Two buttons that call the backend APIs and display responses

## 🎯 Your Tasks

### Task 1: Create Backend Dockerfile

Create a file named `Dockerfile` in the `backend/` folder with the following requirements:
- Use Python 3.11 as the base image
- Set the working directory to `/app`
- Copy `requirements.txt` and install dependencies
- Copy the application code
- Expose port 8000
- Run the FastAPI app using: `uvicorn main:app --host 0.0.0.0 --port 8000`

### Task 2: Create Frontend Dockerfile

Create a file named `Dockerfile` in the `frontend/` folder with the following requirements:
- Use Python 3.11 as the base image
- Set the working directory to `/app`
- Copy `requirements.txt` and install dependencies
- Copy the application code
- Expose port 8501
- Run the Streamlit app using: `streamlit run app.py --server.port=8501 --server.address=0.0.0.0`

### Task 3: Create Docker Compose File

Create a file named `docker-compose.yml` in the root folder with the following requirements:
- Define two services: `backend` and `frontend`
- Backend service:
  - Build from `./backend`
  - Map port 8000:8000
  - Service name should be `backend`
- Frontend service:
  - Build from `./frontend`
  - Map port 8501:8501
  - Should depend on the backend service

## 🚀 Running the Application

Once you've created all three files, run:

```bash
docker-compose up --build
```

Then open your browser and navigate to:
- **Frontend**: http://localhost:8501
- **Backend API**: http://localhost:8000

Click the buttons in the Streamlit app to test the connection between containers!

## 🛑 Stopping the Application

Press `Ctrl+C` in the terminal, then run:

```bash
docker-compose down
```

## 💡 Hints

<details>
<summary>Dockerfile Structure Hint</summary>

A typical Dockerfile follows this pattern:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE <port>
CMD ["command", "to", "run", "app"]
```
</details>

<details>
<summary>Docker Compose Structure Hint</summary>

A typical docker-compose.yml follows this pattern:
```yaml
version: '3.8'

services:
  service-name:
    build: ./folder
    ports:
      - "host:container"
    depends_on:
      - other-service
```
</details>

## 🎓 Learning Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)

## ✨ Success Criteria

You've successfully completed the workshop when:
1. Both containers build without errors
2. Both services are accessible on their respective ports
3. The Streamlit buttons successfully call the FastAPI backend
4. You see responses displayed in the frontend

Happy containerizing! 🐳
