# Grief Counseling AI

A FastAPI-powered platform for personalized grief counseling and support. This application provides tools to help users with grief management through AI-powered analysis, personalized scheduling, and content recommendations.

## Features

- **Daily Schedule Builder**: Generate personalized daily schedules for grief management
- **Sentiment Analysis Toolkit**: Analyze emotional state and receive tailored recommendations
- **Personalized Content**: Get customized grief support content based on user needs

## Tech Stack

- **Backend Framework**: FastAPI
- **API Documentation**: Swagger UI (automatic via FastAPI)
- **Containerization**: Docker & Docker Compose
- **Web Server**: Nginx (as reverse proxy)
- **Process Manager**: Gunicorn with Uvicorn workers
- **AI/ML Services**:
  - Gemini API (Google AI for schedule building and other AI features)
  - Tavily API (for recommendations)

## Prerequisites

- Docker and Docker Compose
- API keys for external services:
  - Gemini API key (Google AI)
  - Tavily API key

## Project Structure

```
.
├── com/
│   └── mhire/
│       └── app/
│           ├── main.py                        # FastAPI application entry point
│           ├── common/                        # Common utilities
│           ├── config/                        # Configuration utilities
│           └── services/                      # Service modules
│               ├── personalized_content/      # Personalized content generation
│               ├── schedule_builder/          # Daily schedule building
│               └── sentiment_toolkit/         # Sentiment analysis toolkit
├── nginx/
│   └── nginx.conf                             # Nginx configuration
├── docker-compose.yml                         # Docker Compose configuration
├── Dockerfile                                 # Docker image definition
├── gunicorn_config.py                         # Gunicorn configuration
├── requirements.txt                           # Python dependencies
└── .env                                       # Environment variables (not in repo)
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Grief
```

### 2. Configure Environment Variables

Create a `.env` file in the project root with the following variables:

```
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 3. Start the Application

```bash
docker-compose up -d
```

This command builds the Docker images and starts the containers in detached mode.

### 4. Access the API

- **API Endpoints**: http://localhost:5004/
- **API Documentation**: http://localhost:5004/docs

## API Endpoints

### Health Check

```
GET /health
```

### Daily Schedule

```
POST /api/v1/daily-schedule
```

Create a personalized daily schedule based on user input.

### Sentiment Analysis

```
POST /api/v1/sentiment-analyze
```

Analyze grief input and provide personalized tool recommendations with sentiment analysis.

### Personalized Content

```
POST /api/v1/personalized-content
```

Generate personalized grief content based on user input.

## Development

### Running Locally (Without Docker)

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn com.mhire.app.main:app --reload
```

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure all required API keys are correctly set in the `.env` file.
2. **Port Conflicts**: If port 5004 is already in use, modify the `docker-compose.yml` file to use a different port.

## License

[Specify your license here]