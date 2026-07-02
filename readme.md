# 🌤️ Weather App (Python)

This is a simple Python project that allows you to check the weather of any city using the OpenWeatherMap API.

---

## 📌 Features

- Search weather by city name
- Displays:
  - Weather description ☁️
  - Current temperature 🌡️
  - Minimum and maximum temperature 🥶🥵
  - Humidity 💧
  - Wind speed 💨
- Error handling (invalid city, timeout, connection errors, etc.)

---

## 🚀 How it works

The user enters a city name, and the program sends a request to the OpenWeatherMap API.  
The response data is processed and displayed in a clean format in the terminal.

---

## 🧰 Technologies used

- Python 🐍
- requests (HTTP requests)
- OpenWeatherMap API 🌍

---

## ⚙️ Installation

Clone the repository:
git clone https://github.com/rodrigodgm1/weather-app.git

Install dependencies:
pip install requests

---

## 🔑 API Configuration

This project requires an API key from OpenWeatherMap.

1. Create an account: https://openweathermap.org/api

2. Create a file called `config.py` and add:
API_KEY = "your_api_key_here"

---

## ▶️ How to run

Run the script:
python your_file_name.py

Then enter the city name when prompted.

---

## 💡 Example

Enter the city's name: Porto

Output:
City: Porto
Description: clear sky
Temperature: 22°C
Minimum: 20°C
Maximum: 24°C
Humidity: 55%
Wind: 3.5 m/s

---

## 🧠 What I learned

- How to work with external APIs using Python
- How to make HTTP requests using the `requests` library
- How to handle JSON responses and extract useful data
- How to implement error handling (try/except) for network requests
- How to structure a small Python project properly
- How to separate sensitive data (like API keys) into a config file

---

## ⚠️ Possible errors

- City not found
- No internet connection
- Missing or invalid API key
- Request timeout

---
