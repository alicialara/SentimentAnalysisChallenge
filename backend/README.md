# Sentiment Analysis API

This project is a FastAPI-based web application for sentiment analysis. It uses a pre-trained model from the `transformers` library to analyze the sentiment of given text inputs and stores the results in a MySQL database.

## Features

- Analyze the sentiment of text inputs (positive or negative).
- Store the analysis results in a MySQL database with a timestamp.
- RESTful API endpoints for sentiment analysis.

## Requirements

- Python 3.9
- MySQL
- Docker (optional, for containerization)

## Setup

### Environment Variables

Create a `.env` file in the root directory of the project and add the following environment variables:

### Install Dependencies

```bash
pip install -r requirements.txt
```


## Running the API

### locally

```bash
uvicorn backend.app.main:app --host 0.0.0.0 --port 5000
```

### with Docker

```bash
docker build -t sentiment-analysis-api .
docker run -p 5000:5000 sentiment-analysis-api
```

## Running Tests

```bash
pytest backend/tests
```

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── services.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_services.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Deployment

### Using git pre-commit hooks

This project uses `pre-commit` to run checks before committing changes. To install the pre-commit hooks, run the following command:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```
