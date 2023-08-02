import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"  # Replace this with the actual API URL


def get_weather_data(date):
    # Make an API request to get the weather data for the given date
    response = requests.get(API_URL)
    if response.status_code == 200:
        weather_data = response.json()
        for item in weather_data["list"]:
            if item["dt_txt"].startswith(date):
                return item["main"]["temp"]
        print("Weather data not found for the specified date.")
        return None
    else:
        print("Failed to fetch weather data from the API.")
        return None


def get_wind_speed(date):
    # Make an API request to get the weather data for the given date
    response = requests.get(API_URL)
    if response.status_code == 200:
        weather_data = response.json()
        for item in weather_data["list"]:
            if item["dt_txt"].startswith(date):
                return item["wind"]["speed"]
        print("Weather data not found for the specified date.")
        return None
    else:
        print("Failed to fetch weather data from the API.")
        return None


def get_pressure(date):
    # Make an API request to get the weather data for the given date
    response = requests.get(API_URL)
    if response.status_code == 200:
        weather_data = response.json()
        for item in weather_data["list"]:
            if item["dt_txt"].startswith(date):
                return item["main"]["pressure"]
        print("Weather data not found for the specified date.")
        return None
    else:
        print("Failed to fetch weather data from the API.")
        return None


def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_weather_data(date)
            if temperature is not None:
                print(f"The temperature on {date} is {temperature} K.")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(date)
            if wind_speed is not None:
                print(f"The wind speed on {date} is {wind_speed} m/s.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(date)
            if pressure is not None:
                print(f"The pressure on {date} is {pressure} hPa.")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
