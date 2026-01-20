# TripGenius

# FastAPI Backend (Dockerized)

This repository contains a **FastAPI backend** fully set up with **Docker** so that all developers run the **same environment**, regardless of operating system (Linux, Windows, macOS).

The goal of this setup is to avoid:

- Different Python versions
    
- Dependency mismatches
    
- “It works on my machine” problems
    

Docker is the **single source of truth** for the runtime environment.

---

## 🧠 High-level idea (important)

Instead of installing Python and dependencies directly on your machine:

- Docker runs a **Linux container**
    
- With a **fixed Python version**
    
- And all dependencies installed inside the container
    

So:

> Your local machine does NOT need Python, pip, or virtualenv.

---

## 📦 Tech stack

- **Python 3.11**
    
- **FastAPI**
    
- **Uvicorn**
    
- **Docker & Docker Compose**
    

---

## 📁 Project structure

```TEXT
.
├── app/                  # FastAPI application code
│   ├── main.py           # App entry point
│   ├── api/              # API routes
│   └── core/             # Config and core logic
├── Dockerfile            # Defines the backend environment
├── docker-compose.yml    # Runs the backend in development
├── requirements.txt      # Python dependencies (source of truth)
├── .env.example          # Example environment variables
├── .dockerignore         # Files ignored by Docker
├── .gitignore
└── README.md
```

---

## 🐳 Why Docker?

Docker guarantees:

- Same OS (Linux)
    
- Same Python version
    
- Same dependencies
    
- Same behavior on Ubuntu & Windows
    

The container itself **replaces virtual environments**.

---

## 🔧 Prerequisites

### Ubuntu

```
sudo apt update sudo apt install -y docker.io docker-compose-plugin sudo usermod -aG docker $USER
```

Log out and back in, then verify:

```
docker --version docker compose version
```

---

### Windows

1. Install **Docker Desktop**  
    👉 [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
    
2. Enable **WSL 2** during setup
    
3. Use **Linux containers** (default)
    

Verify:

```
docker --version docker compose version
```

---

## 🚀 Getting started (first run)

### 1️⃣ Clone the repository

```
git clone <REPO_URL> cd fastapi-backend
```

---

### 2️⃣ Create your environment file

```
cp .env.example .env
```

> `.env` contains local configuration and is **not committed to git**.

---

### 3️⃣ Build and start the backend

```
docker compose up --build
```

What this does:

1. Builds a Docker image with Python 3.11
    
2. Installs dependencies from `requirements.txt`
    
3. Starts the FastAPI server
    

---

### 4️⃣ Open the app

- API: http://localhost:8000
    
- Swagger docs: http://localhost:8000/docs
    

You should see the API documentation and test endpoints.

---

## 🔁 Daily development workflow

### Start the backend

```
docker compose up
```

### Stop the backend

```
Ctrl + C
```

### Stop and remove containers

```
docker compose down
```

---

## 🔥 Hot reload (important)

The setup uses volume mounting and `--reload`, so:

- Code changes reload automatically
    
- No rebuild needed when editing Python files
    

---

## 📦 Managing dependencies (VERY IMPORTANT)

### Source of truth

`requirements.txt` is the **only** place where dependencies are defined.

---

### Adding a new dependency

1. Add it to `requirements.txt`
    
```
sqlalchemy
```
    
2. Rebuild the Docker image:
    
```
docker compose up --build
```
    
3. Use it in the code.
    

⚠️ **Do NOT run `pip install` locally**  
Docker does not see your local Python environment.

---

## ❌ What NOT to do

- ❌ Do not create or activate a virtualenv
    
- ❌ Do not install Python dependencies locally
    
- ❌ Do not edit dependencies without rebuilding Docker
    

---

## 🧠 Mental model to remember

- **Dockerfile** → how the environment is built
    
- **docker-compose.yml** → how the app is run
    
- **Image** → frozen environment
    
- **Container** → running backend
    
- **Docker = the virtual environment**
    

---

## 🧪 Common commands summary

```
docker compose up           # Start backend
docker compose up --build   # Rebuild after dependency changes
docker compose down         # Stop backend
```
---

## 🆘 Troubleshooting

### Permission denied error on Linux

If you see:

`permission denied while trying to connect to the Docker daemon`

Run:

`sudo usermod -aG docker $USER`

Then log out and back in.

---

## 📌 Notes for the team

- This setup works the same on **Ubuntu and Windows**
    
- No Python installation is required on the host
    
- All developers run the **exact same backend**
