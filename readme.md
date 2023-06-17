
# Random Quote Micorservice

This repository contains the necessary files and configurations to set up a CI/CD pipeline for a microservice called "quote-microservice." The pipeline automates the build and deployment process of the microservice using GitHub Actions, EC2 instance (AWS) and Elastic Container Registry (ECR)

## Microservice Description
The microservice code is written in Python using the Flask framework. It provides the following endpoints:

- **/:** Landing page of the microservice. 
- **/hello**: Returns a JSON response with a greeting message. (Rate limited to 10 calls per minute)
- **/quote**: Returns a JSON response with a random quote obtained from the ZenQuotes API.(Rate limited to 5 calls per minute)
The microservice uses the Prometheus Flask Exporter library to export metrics for monitoring. The metrics are exposed on the **/metrics** endpoint.

## Prerequisites
Setup these Github actions secrets used in the CI/CD pipeline
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- EC2_IP
- EC2_USER
- GIT_PAT - Github repo is private so you need to create Personal access token for script
- GIT_REPO
- SSH_PEM - EC2 instance SSH private key

## Testing

Unit tests are located at `tests.py`

## Monitoring with Prometheus and Grafana

### Prometheus 

Access the Prometheus dashboard by navigating to the EC2 instance's public IP address or hostname in a web browser on port `9090`. Prometheus scrapes monitoring data published on endpoint `/metrics`
### Grafana
Access the Grafana dashboard by navigating to the EC2 instance's public IP address or hostname in a web browser on port `3000`.
Log in to Grafana using the default credentials (username: `admin`, password: `admin`).
