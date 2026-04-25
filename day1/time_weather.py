# ============================================================
# CITY WEATHER & TIME DASHBOARD
# Shows the current time and live weather for a list of cities.
# It fetches real data from the internet using the wttr.in API.
# ============================================================

import time
from datetime import datetime

import pytz        # helps us convert time to different time zones
import requests    # lets us download data from the internet


# ---------- CITIES TO DISPLAY ----------
# Each entry is a pair: (name to show on screen, name to send to the API)
CITIES = [
    ("Kabul",   "Kabul"),
    ("Herat",   "Herat"),
    ("Hamburg", "Hamburg")
]

# ---------- WEATHER ICONS ----------
# A lookup table that maps a weather keyword to an emoji.
# We check if the weather description contains one of these words.
WEATHER_ICONS = {
    "Sunny":         "☀️",
    "Clear":         "☀️",
    "Partly cloudy": "⛅",
    "Cloudy":        "☁️",
    "Overcast":      "☁️",
    "Mist":          "🌫️",
    "Fog":           "🌫️",
    "Patchy rain":   "🌦️",
    "Light rain":    "🌦️",
    "Moderate rain": "🌧️",
    "Heavy rain":    "🌧️",
    "Light snow":    "❄️",
    "Moderate snow": "❄️",
    "Heavy snow":    "❄️",
    "Thunderstorm":  "⛈️",
    "default":       "🌡️",   # shown when nothing else matches
}


# ---------- GET WEATHER ICON ----------
# Looks through the icon table and returns the matching emoji.
# If no keyword matches, it returns the default thermometer icon.
def get_weather_icon(condition):
    for keyword in WEATHER_ICONS:
        if keyword.lower() in condition.lower():
            return WEATHER_ICONS[keyword]
    return WEATHER_ICONS["default"]


# ---------- GET LOCAL TIME ----------
# Each city has a timezone name (like "Asia/Kabul" or "Europe/Berlin").
# pytz uses that name to figure out what time it is right now in that city.
def get_local_time(city_name):
    city_timezones = {
        "Kabul":   "Asia/Kabul",
        "Herat":   "Asia/Kabul",     # Herat uses the same timezone as Kabul (Afghanistan Time)
        "Hamburg": "Europe/Berlin",
        "Tehran":  "Asia/Tehran",
    }

    timezone_name = city_timezones.get(city_name, "UTC")   # default to UTC if city not listed
    timezone      = pytz.timezone(timezone_name)
    local_time    = datetime.now(timezone)

    return local_time.strftime("%Y-%m-%d %H:%M:%S")   # e.g. "2025-04-25 14:30:00"


# ---------- FETCH WEATHER FROM THE INTERNET ----------
# Sends a request to wttr.in, a free weather service.
# The response comes back as JSON — a format Python can easily read as a dictionary.
def get_weather(city_name):
    url = f"https://wttr.in/{city_name}?format=j1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()   # if the website returned an error code, stop here

        data    = response.json()     # convert the raw text into a Python dictionary
        current = data["current_condition"][0]

        # Pull out just the pieces we want to display
        temperature = current["temp_C"]
        feels_like  = current["FeelsLikeC"]
        humidity    = current["humidity"]
        condition   = current["weatherDesc"][0]["value"]
        wind_speed  = current["windspeedKmph"]
        wind_dir    = current["winddir16Point"]

        return {
            "temperature": temperature,
            "feels_like":  feels_like,
            "humidity":    humidity,
            "condition":   condition,
            "wind_speed":  wind_speed,
            "wind_dir":    wind_dir,
        }

    except requests.exceptions.RequestException as error:
        # Something went wrong — no internet, bad city name, website down, etc.
        return {"error": f"Could not fetch weather: {error}"}


# ---------- DISPLAY ONE CITY ----------
# Combines the local time and weather into a neat printed box.
def display_city(display_name, api_name):
    local_time = get_local_time(display_name)
    weather    = get_weather(api_name)

    if "error" in weather:
        print(f"⚠️  Error for {display_name}: {weather['error']}")
        return

    icon      = get_weather_icon(weather["condition"])
    separator = "=" * 45

    print(separator)
    print(f"📍 {display_name.upper()}")
    print(separator)
    print(f"🕒 Time:        {local_time}")
    print(f"🌡️  Temperature: {weather['temperature']}°C  (feels like {weather['feels_like']}°C)")
    print(f"💧 Humidity:    {weather['humidity']}%")
    print(f"🌬️  Wind:        {weather['wind_dir']} at {weather['wind_speed']} km/h")
    print(f"🌟 Condition:   {weather['condition']} {icon}")
    print(separator)
    print()   # blank line between cities


# ============================================================
# MAIN PROGRAM
# Goes through each city in our list and displays its info.
# ============================================================
def main():
    print("\n🌟 Welcome to the City Weather & Time Dashboard! 🌟\n")
    print("Fetching the latest data...\n")

    for display_name, api_name in CITIES:
        display_city(display_name, api_name)
        time.sleep(1)   # a small pause so we don't hit the API too fast

    print("✅ All done!\n")


if __name__ == "__main__":
    main()