# Docker Essentials Lab

This project demonstrates a containerized microservice backend using Docker and Docker Compose.

## Architecture

Browser
 ↓
FastAPI API
 ↓
Redis Cache
 ↓
PostgreSQL Database
 ↓
Docker Volume (persistent storage)

## Services

- FastAPI backend
- Redis caching layer
- PostgreSQL database
- Docker Compose orchestration

## Features

- API containerization with Docker
- Multi-container architecture
- Redis caching
- PostgreSQL persistence
- Docker networking
- Health check endpoint
- Restart policies
- Automatic database initialization

## Endpoints

/          - Root endpoint (Redis cached)
/health    - Health check
/redis     - Redis test
/db        - Database test
/visit     - Page visit counter

## Run Locally

Build and start the stack:

docker compose up --build

Access API:

http://localhost:8000

Stop services:

docker compose down

## Tech Stack

Python  
FastAPI  
Redis  
PostgreSQL  
Docker  
Docker Compose