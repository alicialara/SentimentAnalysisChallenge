# Sentiment Analysis Frontend

This is the frontend for the Sentiment Analysis application. It allows users to input text and analyze its sentiment.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/***.git
    cd sentiment-analysis-frontend
    ```

2. Install the dependencies:
    ```sh
    npm install
    ```

## Usage

To start the development server, run:
```sh
npm start
```

## Build the docker image locally

```
docker build -t sentiment-analysis-frontend .
docker run -p 80:80 sentiment-analysis-frontend
```

The application will be available on http://localhost.
