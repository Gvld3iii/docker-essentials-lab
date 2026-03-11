# Docker Essentials Lab

# Tech Stack

# Containerization

Docker

Docker Compose

# Backend Application

Python

FastAPI

Uvicorn ASGI Server

# Databases

PostgreSQL

Redis

# Infrastructure & Environment

Linux containers

Docker networking

Docker volumes for persistent storage

# Development & DevOps

Git

GitHub

Environment variables (.env configuration)

# Overview

A containerized microservice application built with FastAPI, Redis, and PostgreSQL, orchestrated with DoThis project demonstrates real-world DevOps and Cloud Engineering practices including containerization, Architecture
Internet
 |
AWS EC2 Instance
 |
Docker Compose
 |---- FastAPI (API Service)
 |---- Redis (Cache Layer)
 |---- PostgreSQL (Database)

# Tech Stack

Backend: Python, FastAPI, Uvicorn
Containers: Docker, Docker Compose
Database: PostgreSQL
Caching: Redis
Infrastructure: Terraform, AWS EC2

# Run Locally

git clone https://github.com/Gvld3iii/docker-essentials-lab.git
cd docker-essentials-lab
cp .env.example .env
docker compose up --build
Open: http://localhost:8000

# API Endpoints
/ Root endpoint
/health Health check
/redis Redis connectivity test
/db Database connectivity test
/visit Visit counter example
/docs Swagger documentation

# Deploy to AWS with Terraform
cd terraform
terraform init
terraform plan
terraform apply
Terraform provisions:
- AWS EC2 instance
- Security group (ports 22 and 8000)
- Docker installation
- Application deployment with Docker Compose

# Troubleshooting Learned
Cloud-init debugging:
sudo cat /var/log/cloud-init-output.log
Docker container debugging:
docker compose logs
docker ps
docker compose restart
Permissions fix:
sudo chown -R ubuntu:ubuntu docker-essentials-lab

# Future Improvements
CI/CD with GitHub Actions
Kubernetes deployment
Nginx load balancer
Auto-scaling infrastructure
Observability with Prometheus and Grafana

# Author
Kharee Bellamy
Cloud / DevOps Engineer
GitHub: https://github.com/Gvld3iii
