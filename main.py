import os
from dotenv import load_dotenv
import requests

load_dotenv()

def weathe():
    city = input("Enter City: ")
    print("---------------------")
    not_found={"cod":"404","message":"city not found"}

    
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"

        api_key = os.getenv("API_KEY")

        params = {
        "q":city,
        "appid":api_key
        }

        response = requests.get(
            url,
            params=params,
        )

        
        data = response.json()
        if data==not_found:
            print("Enter valid city name (this city not in my range)")

        else:
            print("City: ",city)
            
            print(f"🌡️ Temperature: {data["main"]["temp"]-273.15}°C")
            print(f"🤒 Feels like: {data["main"]["feels_like"]-273.15}°C")
            print(f"💧 Humidity: {data["main"]['humidity']}%")
            print(f"🫳 Pressure: {data["main"]["pressure"]}hPa / mb")
            print(f"☁️ Condition: {data["weather"][0]["description"]}")
            print(f"💨 Wind Speed: {data["wind"]["speed"]} m/s")
    except requests.exceptions.HTTPError :
        print("Enter a valid city name\nThank You")
    except requests.exceptions.ConnectionError :
        print("Please connect your internet")

print("\n=== Welcome to my Weather App===\n")
weathe()
while True:
    loo = input("\nWant to check another city's weather:(Y/N) ")
    if loo.lower()=="y":
        weathe()
    elif loo.lower()=="n":
        break
    else:
        print("Enter Y/N", end="")
