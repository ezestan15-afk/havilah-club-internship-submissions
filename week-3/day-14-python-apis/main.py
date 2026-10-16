# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

import requests
import os

# Load your API key from the environment (never hardcode it here).
# Copy .env.example to .env and fill in your key before running.
API_KEY = os.getenv("API_KEY", "0d4b7afbaa64b194e8bc02180af73c6f")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"  # TODO: set your chosen API's base URL


# ── Step 1: Fetch Data ────────────────────────────────────────────────────────
# Make a GET request to the API and return the parsed JSON response.
# Handle network errors and non-200 status codes gracefully.

def fetch_data(query):
    # TODO: build params dict and call requests.get()
    # TODO: check response.status_code before calling .json()
    pass
    if not API_KEY:
        print("Error: API_KEY is missing. Please set it in your environment.")
        return None

    # Set up the query parameters. 'units=metric' returns temperatures in Celsius.
    params = {
        "q": query,
        "appid": API_KEY,
        "units": "metric" 
    }

    try:
        response = requests.get(BASE_URL, params=params)
        
        # Check for specific expected errors before raising generic ones
        if response.status_code == 404:
            print(f"Error: City '{query}' not found. Please check your spelling.")
            return None
        elif response.status_code == 401:
            print("Error: Invalid API key. Make sure your OpenWeatherMap key is correct.")
            return None
            
        # Raise an exception for any other non-200 status codes (e.g., 500)
        response.raise_for_status()
        
        # Parse and return the JSON payload
        return response.json()
        
    except requests.exceptions.ConnectionError:
        print("Network Error: Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Timeout Error: The API took too long to respond.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected request error occurred: {e}")
    except ValueError:
        print("Data Error: Received invalid JSON from the API.")
        
    return None


# ── Step 2: Parse and Display ─────────────────────────────────────────────────
# Extract at least 3 useful pieces of information from the response.
# Print them in a clear, labelled format — not raw JSON.

def display_results(data):
    # TODO: navigate the JSON structure and print each field with a label
    pass
def display_results(data):
    try:
        # Extract 4 specific pieces of information from the nested JSON
        city_name = data.get("name", "Unknown")
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]

        # Print out the formatted UI
        print("\n" + "═" * 40)
        print(f" 🌤️  Current Weather in {city_name}, {country}")
        print("═" * 40)
        print(f"   Condition:   {weather_desc}")
        print(f"   Temperature: {temperature}°C")
        print(f"   Humidity:    {humidity}%")
        print("═" * 40 + "\n")
        
    except KeyError as e:
        print(f"Parsing Error: Could not find expected data field {e} in the response.")

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("Welcome to the Weather API CLI!")
    query = input("Enter your search query: ")
    data = fetch_data(query)
    if data:
        display_results(data)


if __name__ == "__main__":
    main()
