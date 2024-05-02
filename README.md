# FastAPI, Prometheus, and Grafana Deployment Template

This repository serves as a template for deploying a FastAPI application with Prometheus monitoring and Grafana dashboards, all containerized with Docker.

## Overview

This template provides a ready-to-use setup for deploying a robust application monitoring solution. FastAPI gives you a modern, fast (high-performance) web framework for building APIs. Prometheus is set up to handle metrics collection and alerting, while Grafana is used for visualization and analytics of those metrics.

## Features

- **FastAPI**: Pre-configured FastAPI application setup **(The provided API is just an example, do replace it with your own API)**. For a working API, can refer to 3D BluePrint AI repository ( [3D_BluePrint](https://github.com/HiverlabResearchAndDevelopment/3dblueprinting) ).
- **Prometheus**: Configured to collect metrics from FastAPI.
- **Grafana**: Set up with dashboards for viewing FastAPI metrics.
- **Docker**: Everything containerized for easy deployment and scalability.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Quickstart](#quickstart)
- [Authors](#authors)


## Prerequisites

Ensure you have the following software tools installed:

### Docker

- **Installation:** Head to the [Install Docker Engine](https://www.docker.com/get-started) page.
- **Learning:** If Docker is unfamiliar, consider this [quick introduction](https://docs.docker.com/get-started/overview/).

### Windows Users

If you are using Windows, you will need to install the Windows Subsystem for Linux (WSL) to run the Docker commands natively in a Linux environment. Follow the official [WSL installation guide](https://docs.microsoft.com/en-us/windows/wsl/install) to set this up.

## Quickstart

1.  Clone the repository
```shell
git clone https://github.com/djchiamHiverlab/API_Prometheus_Grafana_Deployment.git
```
2. Modify the Dockerfile and Dockercompose yml based on your needs
3. Modify Prometheus yml based on your needs
4. Build the Docker Containers
```shell
docker-compose up -d
```
5. Access the Grafana dashboard
```shell
<localhost or vm ip address>:3000
```

## Authors

* Chiam Da Jie (AI/Backend Engineer Intern)



 
