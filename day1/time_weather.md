# 🌍 City Weather & Time Dashboard

A program that shows the **current time and live weather** for cities around the world — right in your terminal!

**No account or API key needed. Just install two libraries and run it.**

---

## 🎯 What Are We Doing Today?

We are **not** writing new code from scratch. Instead, we are:

- 👀 Reading code that already works
- 🔍 Understanding what each part does
- ✏️ Making small changes to see what happens
- 🌟 Making the program feel like **ours**

This is exactly how real programmers work every day!

---

## 🧩 What Each Part Does

Think of the program like a team of helpers. Each function has one job:

| Part of the code | What it does in simple words |
|------------------|------------------------------|
| `CITIES = [...]` | The list of cities we want to check |
| `WEATHER_ICONS = {...}` | A cheat sheet: "Sunny" → ☀️, "Rain" → 🌧️ |
| `get_weather_icon()` | Looks up the right emoji for the weather |
| `get_local_time()` | Asks Python: "What time is it right now in Kabul?" |
| `get_weather()` | Goes to the internet and downloads live weather data |
| `display_city()` | Prints a nice info box for one city |
| `main()` | The boss — tells the other helpers what to do and in what order |

---

## ▶️ How to Run It (First Time Setup)

Open your terminal and type these commands one by one:

```bash
pip install requests pytz
python time_weather.py
```

You should see weather boxes appear for each city. If you see an error, check that you have an internet connection!

---

## 🧪 Activities — Try These One at a Time!

Each activity is a **tiny change**. Run the program after every change to see what happens. You can always undo if something breaks.

---

### 1. 🎨 Change the separator line

Find this line inside `display_city()`:
```python
separator = "=" * 45
```
Change `=` to `-` or `*` or `~`. What does it look like now?

---

### 2. 💬 Change the welcome message

Find:
```python
print("\n🌟 Welcome to the City Weather & Time Dashboard! 🌟\n")
```
Change the text to anything you like — your name, your school, a fun greeting!

---

### 3. 🏙️ Add your own city

Find the `CITIES` list at the top and add a new line:
```python
("Paris", "Paris"),
```
Run it. Does it work? Try your hometown!

> **For teachers:** students may need to look up their city's timezone if they later try to add it to `city_timezones` inside `get_local_time()`.

---

### 4. 🔀 Swap the order of info

Inside `display_city()`, move the humidity line **above** the temperature line. Run the program. Notice anything?

---

### 5. 🗑️ Remove a city

In the `CITIES` list, put a `#` at the start of one line, like this:
```python
# ("Hamburg", "Hamburg"),
```
The `#` turns it into a comment — Python ignores it. Run the program. That city disappears!

---

### 6. 🚀 Add a fake city and break things (on purpose!)

Add this to `CITIES`:
```python
("Mars", "Mars"),
```
Run the program. It shows a warning but **does not crash**. That is the `try/except` block doing its job — catching errors so the program keeps going.

---

### 7. ⏱️ Change the speed

Find:
```python
time.sleep(1)
```
Change `1` to `3` (slower) or `0` (no wait at all). What changes?

---

## ❓ Questions to Think About

These are great to discuss as a group:

- What happens if you remove the `import requests` line at the top?
- Why do we write `weather["temperature"]` instead of just `temperature`?
- What does `try/except` do? What would happen without it?
- Why does `get_local_time()` need to know the city name — can't it just use the computer's clock?

---

## 📚 For Teachers — Concepts Covered

| Concept | Where it appears |
|---------|-----------------|
| Variables | `separator`, `local_time`, `temperature` |
| Lists | `CITIES` |
| Dictionaries | `WEATHER_ICONS`, the weather data returned from the API |
| Functions | `get_weather_icon()`, `get_local_time()`, etc. |
| For loops | `main()` loops through `CITIES` |
| Error handling | `try/except` in `get_weather()` |
| Libraries / imports | `pytz`, `requests` |
| APIs | Fetching live data from wttr.in |

---

## 🚀 Challenge Ideas for Later Sessions

When students are ready (session 2 or 3):

- Add a city they care about — and find its timezone on [Wikipedia's timezone list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
- Change the date format from `YYYY-MM-DD` to `DD/MM/YYYY` (hint: look at `strftime`)
- Add a Fahrenheit display: `int(temp) * 9/5 + 32`
- Save the output to a text file instead of printing it
- Ask the user to type a city name instead of using the hardcoded list