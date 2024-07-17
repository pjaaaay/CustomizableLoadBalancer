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

# Server Test Results
# Explanation of Each Scenario
# A-1: Request Distribution Across 3 Servers

Observation: The bar chart shows the request count handled by each server when launching 10,000 async requests across 3 server containers. The distribution is nearly even, with each server handling roughly one-third of the requests.
View on Performance: This even distribution indicates that the load balancer is effectively distributing the load among the servers, preventing any single server from becoming a bottleneck.
![Request Distribution Across 3 Servers](src/image-1.png)

# A-2: Average Load with Increasing Servers

Observation: The line chart illustrates the average load per server as the number of servers increases from 2 to 6. As the number of servers increases, the average load per server decreases.
View on Scalability: The decreasing average load demonstrates that the load balancer scales well with an increasing number of servers, effectively distributing the load and improving resource utilization.
![Average Load with Increasing Servers](src/image-2.png)

# A-3: Server Response Times Before and After Failure

Observation: The line chart shows the response times for 10 requests, with a noticeable increase in response time at the 5th request due to a server failure, followed by quick recovery.
View on Fault Tolerance: This quick recovery and stabilization of response times after the failure demonstrate the load balancer's ability to promptly spawn new instances to handle the load, ensuring minimal disruption.
![Server Response Times Before and After Failure](src/image-3.png)

# A-4: Request Distribution and Average Load with Modified Hash Functions

Observation (Request Distribution): The bar chart shows the request count handled by each server using modified hash functions. The distribution remains nearly even.
Observation (Average Load): The line chart shows the average load per server with increasing server counts using modified hash functions. The average loads are similar to the original hash function.
View on Performance: Modifying the hash functions did not significantly affect the distribution and average load, indicating that the load balancer's performance is robust to changes in the hash function. This suggests that the consistent hashing mechanism is effective and resilient.
![Loads](src/image-4.png)

![Request](src/image-5.png)





