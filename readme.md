# Environment Variables API

A simple FastAPI service that exposes environment variables via a REST API.

## Features

- Get all environment variables via `/api/env` endpoint
- Interactive API documentation at `/docs`
- Built with FastAPI and Python
- Environment variables loaded from `.env` file
- Containerized with Docker

## Getting Started

### Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your environment variables (see `.env.example`)

3. Run the application:
   ```bash
   python main.py
   ```

4. Open your browser to http://localhost:8000/docs to view the API documentation

### Docker Development

1. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```
   This will:
   - Build the Docker image
   - Start the service on port 8000
   - Mount the current directory as a volume for development
   - Use the `.env` file for environment variables

2. Or build and run with plain Docker:
   ```bash
   # Build the image
   docker build -t env-var-service .
   
   # Run the container
   docker run -d --name env-var-service -p 8000:8000 --env-file .env env-var-service
   ```

3. The API will be available at http://localhost:8000

## API Endpoints

- `GET /` - Welcome message and API information
- `GET /api/env` - Get all environment variables

## Security Note

Be cautious when exposing environment variables in production as they may contain sensitive information.