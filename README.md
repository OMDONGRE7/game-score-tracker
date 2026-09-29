# Game Score Tracker

A simple Flask web application developed as a college DevOps Lab mini-project.

The project demonstrates an end-to-end DevOps pipeline using GitHub, Jenkins, pytest, Docker, and AWS EC2.

## DevOps Pipeline

GitHub → Jenkins → Automated Testing → Docker → AWS EC2 → Health Check

## Application Features

- Simple Game Score Tracker homepage
- View game scores
- View leaderboard
- Health check endpoint

## Technologies Used

- Python
- Flask
- HTML
- pytest
- Git
- GitHub
- Jenkins
- Docker
- AWS EC2

## Testing

Automated tests are written using pytest.

The project currently contains 4 tests covering the application's important routes and health check.

## Docker

The application runs inside a Docker container on port 5000.

## AWS Deployment

The Docker container is deployed directly on an Ubuntu AWS EC2 instance.

The application can be accessed using the EC2 public IP on port 5000.

## Health Check

The `/health` endpoint returns:

```json
{
  "status": "healthy"
}