# Docker Workshop

**Session time:** 10:45 AM – 12:15 PM

This repository contains all resources for the Docker fundamentals workshop — slides, the sample application, and a Docker Compose example.

---

## Prerequisites

Please have the following installed **before** the session starts:

| Tool | Purpose | Install |
|------|---------|---------|
| Docker Desktop | Run everything | https://www.docker.com/products/docker-desktop |
| Git | Clone this repo | https://git-scm.com/downloads |
| VS Code (or any editor) | Edit files | https://code.visualstudio.com |

Verify your setup by running:

```bash
docker --version
docker run hello-world
```

If you see `Hello from Docker!` in the output, you are ready.

---

## Repository Structure

```
workshop-docker/
├── README.md
├── CHEATSHEET.md
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
└── compose/
    └── docker-compose.yml
```

---

## Hands-on 1 — Pull and run a container

```bash
docker pull nginx
docker run -d -p 8080:80 --name my-nginx nginx
```

Open http://localhost:8080 in your browser. You should see the Nginx welcome page.

```bash
docker ps
docker stop my-nginx
docker rm my-nginx
```

---

## Hands-on 2 — Build your own image

```bash
git clone https://github.com/YOUR_USERNAME/workshop-docker.git
cd workshop-docker/app

docker build -t flask-demo .
docker run -d -p 5000:5000 --name flask-app flask-demo
```

Open http://localhost:5000 in your browser.

```bash
docker logs flask-app
docker stop flask-app
docker rm flask-app
```

---

## Hands-on 3 — Docker Compose (demo)

```bash
cd ../compose
docker compose up -d
docker compose ps
docker compose down
```

---

## Cleanup

Remove all stopped containers and unused images:

```bash
docker system prune
```
