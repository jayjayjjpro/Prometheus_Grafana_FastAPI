# FastAPI, Prometheus, and Grafana Deployment Template

This repository serves as a template for deploying a FastAPI application with Prometheus monitoring and Grafana dashboards, all containerized with Docker.

## Overview

This template provides a ready-to-use setup for deploying a robust application monitoring solution. FastAPI gives you a modern, fast (high-performance) web framework for building APIs. Prometheus is set up to handle metrics collection and alerting, while Grafana is used for visualization and analytics of those metrics.

## Features

- **FastAPI**: Pre-configured FastAPI application setup **(The provided API is just a basic example, do replace it with your own API)**.
- **Prometheus**: Configured to collect metrics from FastAPI.
- **Grafana**: Set up with dashboards for viewing FastAPI metrics.
- **Docker**: Everything containerized for easy deployment and scalability.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Quickstart](#quickstart)
- [DockerConfiguration](#dockerconfiguration)
- [Documentation](#documentation)
- [Reference](#reference)


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
2. Modify the Dockerfile and Dockercompose yml to use your own Fast API. **Remember to create a .env file and update the ports for docker-compose.yml**
3. Copy your Fast API code into the repository. **Remember to Instrument the app for Prometheus(Refer to the line of code in fast_app.py)**
4. Modify Prometheus yml(**Refer to the comments and readme in the Prometheus Folder for more information)**
5. Build the Docker Containers
```shell
docker-compose up -d
```
6. Access the Grafana dashboard
```shell
<localhost or vm ip address>:3000
```
7. Set up the dashboard according to the documentation
## DockerConfiguration
To customize this Docker Compose file for your specific needs, consider the following modifications:

- Ports: To change the ports on which services are accessible, modify the numbers in the ports settings for each service. Ensure the first number (host port) is available on your system.
- Volumes: If you wish to store data in different directories on your host, change the device paths under volumes.
- Build context and Dockerfile: The build directive in the web service assumes you have a Dockerfile in the current directory. If your Dockerfile is elsewhere, modify the path accordingly.
- Network names: The default network is named fastapi. You can rename it under networks to better reflect your project or environment.

## Documentation
[Documentation(Maintenance and dashboard set up)](https://docs.google.com/document/d/1uBQXvvmeXGqjy7l8ETGz3Nr9CqCfObo7x6c8A5BKqRk/edit#heading=h.hnstmjjlgnbw)

## Reference

[FastAPI-Prometheus-Grafana](https://dev.to/ken_mwaura1/getting-started-monitoring-a-fastapi-app-with-grafana-and-prometheus-a-step-by-step-guide-3fbn)



 
