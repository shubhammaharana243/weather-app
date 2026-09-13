# 🌤️ Weather App

A simple command-line weather app built with Python and the OpenWeatherMap API.

## Features

- Search weather by city name
- Temperature
- Feels-like temperature
- Humidity
- Pressure
- Weather condition
- Wind speed
- Check weather for multiple cities
- Handles invalid city names
- Handles internet connection errors

## Technologies

- Python
- Requests
- python-dotenv
- OpenWeatherMap API

## Setup

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your API key:

```env
API_KEY=your_api_key_here
```

Run the application:

```bash
python main.py
```

## Security

The API key is stored in `.env` and is not uploaded to GitHub.

## What I Learned

- Working with APIs
- HTTP GET requests
- JSON data
- Environment variables
- API key security
- Exception handling
- Functions and loops
