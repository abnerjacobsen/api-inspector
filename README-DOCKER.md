# API Inspector - Docker Usage

This document provides instructions on how to build and run the API Inspector application using Docker.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your system.

## Building the Docker Image

To build the Docker image for the API Inspector, navigate to the root directory of the project (where the `Dockerfile` is located) and run the following command:

```bash
docker build -t api-inspector .
```

This command will:
1.  Use the `Dockerfile` in the current directory.
2.  Create a Docker image tagged with the name `api-inspector`.

## Running the Docker Container

Once the image is built, you can run the application as a container using the following command:

```bash
docker run -p 8000:8000 --name api-inspector-container api-inspector
```

This command will:
-   `docker run`: Start a new container.
-   `-p 8000:8000`: Map port 8000 of your local machine to port 8000 inside the container.
-   `--name api-inspector-container`: Assign a name to the container for easier management.
-   `api-inspector`: Specify the image to use for creating the container.

The server will start, and you will see the Uvicorn logs in your terminal.

## Accessing the Application

With the container running, open your web browser and navigate to:

[http://localhost:8000](http://localhost:8000)

You should see the API Inspector web dashboard.

## Stopping and Removing the Container

To stop the container, you can press `Ctrl+C` in the terminal where it's running, or run:

```bash
docker stop api-inspector-container
```

To remove the container after it has been stopped:

```bash
docker rm api-inspector-container
