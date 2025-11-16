# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Install uv, the package installer
RUN pip install uv

# Copy the dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --no-cache

# Copy the rest of the application code
COPY api-inspector.py .

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["uv", "run", "uvicorn", "api-inspector:app", "--host", "0.0.0.0", "--port", "8000"]
