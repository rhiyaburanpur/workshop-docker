# Docker Cheatsheet

## Images

| Command | What it does |
|---------|-------------|
| `docker pull <image>` | Download an image from Docker Hub |
| `docker images` | List all local images |
| `docker rmi <image>` | Remove an image |
| `docker build -t <name> .` | Build an image from a Dockerfile in current directory |

## Containers

| Command | What it does |
|---------|-------------|
| `docker run <image>` | Create and start a container |
| `docker run -d <image>` | Run in detached (background) mode |
| `docker run -p 8080:80 <image>` | Map host port 8080 to container port 80 |
| `docker run --name myapp <image>` | Give the container a name |
| `docker run -e KEY=VALUE <image>` | Set an environment variable |
| `docker run -v /host/path:/container/path <image>` | Mount a volume |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers (including stopped) |
| `docker stop <name>` | Stop a running container |
| `docker start <name>` | Start a stopped container |
| `docker rm <name>` | Remove a stopped container |
| `docker logs <name>` | View container logs |
| `docker exec -it <name> bash` | Open a shell inside a running container |

## Dockerfile Instructions

| Instruction | Purpose |
|-------------|---------|
| `FROM` | Base image to build from |
| `WORKDIR` | Set the working directory inside the container |
| `COPY` | Copy files from host into the image |
| `RUN` | Execute a command during the build |
| `EXPOSE` | Document which port the container listens on |
| `ENV` | Set an environment variable in the image |
| `CMD` | Default command to run when the container starts |

## Docker Compose

| Command | What it does |
|---------|-------------|
| `docker compose up -d` | Start all services in the background |
| `docker compose ps` | List running services |
| `docker compose logs` | View logs for all services |
| `docker compose down` | Stop and remove all services |
| `docker compose build` | Rebuild images |

## Cleanup

| Command | What it does |
|---------|-------------|
| `docker system prune` | Remove stopped containers, unused images, networks |
| `docker volume prune` | Remove unused volumes |
