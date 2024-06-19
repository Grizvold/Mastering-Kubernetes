# Mastering-Kubernetes

Mastering Kubernetes step by step.

# Dummy App

This is a simple Flask application named `dummy-app` used for testing and learning purposes. It handles API requests and responds with a simple message.

## Application Endpoints

- **Home**: `GET /`
  - Returns: "Welcome to dummy-app!"
- **API**: `GET /api`
  - Returns: JSON response with message

## Requirements

- Python 3.11.5
- Flask 3.0.3
- Docker
- Helm (for Kubernetes deployment)

## Setup

### Create and Activate Virtual Environment

1. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    ```

2. **Activate the virtual environment:**
    ```bash
    source venv/bin/activate
    ```

3. **Install Flask:**
    ```bash
    pip install Flask
    ```
