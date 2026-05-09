# 💬 Input & Output

So far our programs have shown the same thing every time.
With **input**, the program can ask the user a question and use the answer — making every run feel personal.

**No libraries to install. Just run it.**

---

## 🤔 What Are Input and Output?

Every program in existence does some version of the same three things:

```
INPUT  →  PROCESS  →  OUTPUT
```

- **Input** — the program receives information from somewhere (the user, a file, the internet)
- **Process** — the program does something with that information (calculates, decides, transforms)
- **Output** — the program sends a result somewhere (the screen, a file, another program)

Today we focus on the simplest form: the user types something → Python works with it → the screen shows a result.

---

## 🖥️ Output — `print()` In Depth

`print()` is how Python talks to the user. It puts text on the screen.

### Basic usage

```python
print("Hello!")                  # prints text
print(42)                        # prints a number
print(3.14)                      # prints a decimal
print(True)                      # prints a boolean
print()                          # prints a blank line (empty parentheses)
```

### Printing multiple things at once

You can put several values inside one `print()`, separated by commas. Python adds a space between them automatically:

```python
name = "Sara"
age  = 15
print("Name:", name, "| Age:", age)
# output: Name: Sara | Age: 15
```

### f-strings — the clearest way to print variables

An **f-string** (formatted string) lets you embed variables directly inside text. Put `f` before the opening quote and wrap variable names in `{}`:

```python
name = "Leila"
city = "Isfahan"
print(f"Hello, {name}! You are from {city}.")
# output: Hello, Leila! You are from Isfahan.
```

You can also do math inside the `{}`:

```python
score = 85
print(f"You scored {score}/100 — that is {score}%.")
print(f"Double your score would be {score * 2}.")
```

### Controlling the ending

By default, `print()` moves to the next line after printing. You can change that with `end=`:

```python
print("Loading", end="")
print("...", end="")
print(" done!")
# output: Loading... done!
```

### Repeating a character to make borders

```python
print("=" * 30)   # prints 30 equal signs in a row — great for borders
print("-" * 30)
```

---

## ⌨️ Input — `input()` In Depth

`input()` pauses the program, shows a message (the **prompt**), and waits for the user to type something and press **Enter**. Whatever the user types is stored as a string.

### Basic usage

```python
answer = input("What is your name? ")
print(f"Nice to meet you, {answer}!")
```

**What happens step by step:**
1. Python prints `What is your name? ` on the screen
2. The cursor blinks — the program is waiting
3. The user types something and presses Enter
4. Python stores what was typed as a string in `answer`
5. The next line runs

### The prompt is optional

```python
x = input()   # shows nothing, just waits — less friendly but valid
```

### `input()` ALWAYS gives back a string

This is the most important rule to remember. Even if the user types `25`, Python gives you the string `"25"`, not the number `25`.

```python
age = input("How old are you? ")
print(type(age))   # <class 'str'> — always!
```

This means you cannot do math with it directly:

```python
age = input("How old are you? ")
print(age + 1)   # ERROR — you cannot add a number to a string
```

---

## 🔄 Type Conversion — Turning Text into Numbers

Because `input()` always returns a string, we need to **convert** it before doing math.

### `int()` — converts to a whole number

```python
age_text = input("How old are you? ")   # "15" (a string)
age      = int(age_text)                # 15  (a number)
print(age + 1)                          # 16  — works!
```

You can do it in one step:

```python
age = int(input("How old are you? "))
```

### `float()` — converts to a decimal number

```python
height = float(input("Your height in cm? "))   # "162.5" → 162.5
```

### `str()` — converts a number back to text

```python
score = 95
message = "Your score is " + str(score) + " out of 100"
print(message)
```

### What happens if conversion fails?

If the user types `fifteen` when you try to do `int(input(...))`, Python will crash with a `ValueError`. We will learn how to handle this safely in a later session. For now, just be aware it can happen.

---

## 🧩 Summary Table

| Tool | What it does | Returns |
|------|-------------|---------|
| `print("text")` | Shows text on the screen | nothing |
| `print()` | Prints a blank line | nothing |
| `print(a, b, c)` | Prints multiple values with spaces | nothing |
| `f"Hello {name}"` | Embeds a variable inside a string | a string |
| `input("question")` | Shows prompt, waits for user to type | always a `str` |
| `int(input(...))` | Gets input and converts to whole number | `int` |
| `float(input(...))` | Gets input and converts to decimal | `float` |
| `str(number)` | Converts a number to text | `str` |

> **`input()` always returns a string** — convert it before doing math.

---

## 🌍 Real-Life Connection

Every app you use runs on input and output constantly:

| App | Input | Output |
|-----|-------|--------|
| Instagram | You type a caption | Caption appears on your post |
| Calculator | You press numbers and `+` | Screen shows the result |
| Google | You type a search | Page shows results |
| A quiz app | You select an answer | App shows "correct" or "wrong" |
| Your Name Card program | You type your name and age | Terminal prints your card |

The only difference between a simple terminal program and a phone app is how the input arrives (keyboard vs. touchscreen) and where the output goes (terminal vs. a beautiful screen). The logic in the middle is the same Python ideas you are learning right now.

---

## ▶️ How to Run It

```bash
python input_output.py
```

The program will ask you questions. Type your answer and press **Enter** after each one.

---

## 🎯 What Are We Doing Today?

- Using `print()` to show messages (output)
- Using `input()` to collect answers from the user (input)
- Converting text input into numbers so we can do math
- Building a personalized Name Card from user answers

---

## 🧩 Key Ideas

| Tool | What it does |
|------|-------------|
| `print("text")` | Shows text on the screen |
| `print()` | Prints a blank line (useful for spacing) |
| `input("question")` | Shows a question and waits for the user to type |
| `int(input(...))` | Converts typed text into a whole number |
| `float(input(...))` | Converts typed text into a decimal number |

> **Important:** `input()` always gives back **text**, even if the user types `14`.
> To use it as a number, you must wrap it: `int(input("Age? "))`.

---

## ▶️ How to Run It

```bash
python input_output.py
```

The program will ask you questions. Type your answer and press **Enter** after each one.

---

## 🧪 Activities — Try These One at a Time!

---

### 1. 🪪 Run it as yourself

Run the program and answer the questions with your real name, city, color, and age.
Does the card look the way you expected?

---

### 2. 👯 Run it as a friend

Run it again but type a classmate's details. The card should change completely — same code, different data!

> This is the power of variables: one program can work for millions of different people.

---

### 3. 💬 Add a new question

Add a new `input()` line to collect one more piece of information:

```python
favorite_food = input("What is your favorite food? ")
```

Then add it to the card:

```python
print(f"  Food:   {favorite_food}")
```

---

### 4. 🔢 Try entering a word when asked for a number

When the program asks "How old are you?" type `fourteen` instead of `14`. What happens?

This is called a **crash**. We will learn how to prevent it in a later session.

---

### 5. 🧮 Do math with the input

After collecting `age`, add a new line:

```python
years_until_100 = 100 - age
print(f"You will be 100 years old in {years_until_100} years!")
```

---

### 6. 🎨 Redesign the card

Change the `=` border to something different, like `-` or `*`. Change the column widths. Make the card look exactly the way you want it.

---

## ❓ Questions to Think About

- `input()` always returns a string. Why does Python not just look at what the user typed and figure out the type automatically?
- What is the difference between `print(name)` and `print("name")`? Try both and see!
- If you forget `int(...)` around `input()` and try to do `age - 1`, what error do you get? Can you read the error message and understand it?

---

## 📚 For Teachers — Concepts Covered

| Concept | Where it appears |
|---------|-----------------|
| Output with `print()` | Greeting lines and the card |
| Input with `input()` | All four user questions |
| Type conversion | `int(input(...))` for age |
| f-strings | Inside the card printing block |
| Variables storing user input | `name`, `city`, `favorite_color`, `age` |
| Simple arithmetic on input | `years_until_20 = 20 - age` |

---

## 🚀 Challenge Ideas

- Ask for the user's score in 3 subjects and print their average
- Ask for two numbers and print their sum, difference, and product
- Add an `if` statement (day 2 topic!) to give a different greeting depending on the city the user enters