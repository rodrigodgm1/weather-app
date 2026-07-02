import requests
from config import API_KEY

city = str(input("Enter the city's name: "))

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

def getWeather():
        print(f"""
        ========   Weather App   ========
        
        City : {city}
        
        ☁️ Description: {weather_data["description"]}
        🌡️ Temperature: {weather_data["temp"]}°C
        🥶 Minimum: {weather_data["temp_min"]}°C
        🥵 Maximum: {weather_data["temp_max"]}°C
        💧 Humidity: {weather_data["humidity"]}%
        💨 Wind: {weather_data["wind"]} m/s
        
        """)

try:
    response = requests.get(url, timeout = 5)

    if response.status_code == 404:
        print("Error: City not found")
        exit()

    data = response.json()

# Organizing the key information

    weather_data = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "description": data["weather"][0]["description"]
    }

    getWeather()

except requests.exceptions.Timeout:
    print("Error: Request took too long (timeout)")

except requests.exceptions.ConnectionError:
    print("Error: Couldn't connect to the web")

except KeyError:
    print("Error: Unexpected API response format")

except Exception as e:
    print(f"Error: Unexpected error {e}")

