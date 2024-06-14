# CustomizableLoadBalancer

Implementation of a load balancer that routes the requests coming from several clients asynchronously
among several servers so that the load is nearly evenly distributed among them.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Project Directory](#project-directory)
- [Development Environment](#development-environment)
- [Contributing](#contributing)
- [License](#license)

## Overview
A Customizable Load Balancer is a system designed to distribute incoming network or application traffic across multiple servers. The goal is to ensure that no single server becomes overwhelmed with too many requests, leading to efficient resource utilization and high availability of services.

## Features
- Asynchronous Request Handling: Processes requests concurrently without waiting.
- Customizable Load Distribution: Supports algorithms like Round Robin, Least Connections, and custom methods.
- Dynamic Server Pool: Easily add or remove servers; health monitoring ensures requests go to operational servers.
- Event-Driven Model: Utilizes non-blocking I/O for high throughput and low latency.

## Getting Started
Follow the steps below to get CustomizableLoadBalancer up and running on your local machine.

### Prerequisites
- [Visual Studio Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/) for coding.
- [Python](https://www.python.org/) installed on your machine.
- [Docker](https://docs.docker.com/desktop/install/windows-install/) installed on your machine.


### Installation
1. Clone the CustomizableLoadBalancer repository to your local machine:
    ```bash
    git clone git@github.com:your-username/CustomizableLoadBalancer.git
    ```
2. Install flask
    ```bash
    pip install flask
    ```

### Project Directory
    ```bash
    	/project-directory
  		/server.py
  		/consistent_hash.py
  		/loadbalancer.py
  		/Dockerfile
  		/docker-compose.yml
  		/Makefile

    ```


You've successfully set up CustomizableLoadBalancer on your machine.
3. Run the Load Balancer
    ```bash
    .PHONY: build up down

	build:
		docker-compose build

	up:
		docker-compose up -d

	down:
		docker-compose down
    ```
## Development Environment
	OS: Ubuntu 20.04 LTS or above
	• Docker: Version 20.10.23 or above
	• Languages: Python



### Python Development
- Ensure you have the required Python packages installed by running:
  ```bash
  pip install -r requirements.txt
  ```
