# SimpleTimeService - Particle41 DevOps Challenge

### Author

**Pavan Gajjala**  
This challenge was completed as part of the Particle41 DevOps evaluation.

---

## Description

This is a minimalist microservice built for the Particle41 DevOps challenge.  
It returns the current UTC timestamp and the IP address of the caller in JSON format.

The application is Dockerized with a focus on best practices:
- Small image using `python:3.10-slim`
- Runs as a **non-root user**
- Ready to be deployed on ECS, Lambda, or Kubernetes

---

## JSON Response Format

```json
{
  "timestamp": "2025-04-15T18:30:00.000000",
  "ip": "203.0.113.1"
}
```

---

## Run the App

### Prerequisites

- Docker installed: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

---

### Option 1: Run from DockerHub (RECOMMENDED)

```bash
docker run -p 8080:8080 yourdockerhubusername/simpletimeservice:latest
```

Then open your browser or run:

```bash
curl http://localhost:8080
```

---

### Option 2: Build and Run Locally

```bash
cd app
docker build -t simpletimeservice .
docker run -p 8080:8080 simpletimeservice
```

---

## Security & Best Practices

- The container is configured to **run as a non-root user** (`appuser`), following container security best practices.
- The image uses a lightweight base: `python:3.10-slim` to keep size and attack surface minimal.
- The app listens on port `8080` and binds to `0.0.0.0`, making it suitable for Docker and cloud deployments.

---

## Project Structure

```plaintext
devops-challenge-senior/
├── app/
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
├── terraform/      # Terraform infrastructure will go here (Task 2)
└── README.md
```

---

## Test

After running the container, you can verify it with:

```bash
curl http://localhost:8080
```

Expected response:

```json
{
  "timestamp": "2025-04-15T00:00:00",
  "ip": "127.0.0.1"
}
```

---