# 📦 Variables and Data Types

A program needs to remember things — a name, a score, a temperature.
**Variables** are how we do that: named boxes that hold information.

**No libraries to install. Just run it.**

---

## 🤔 What Is a Variable?

Imagine you write your friend's phone number on a sticky note and stick it on your wall.

- The **sticky note** is the variable — it has a label (the name) and a value (the number).
- You can **look at it** any time you need the number.
- You can **cross it out and write a new number** if your friend changes their phone.
- Without the sticky note, you would have to memorise the number — or type it out every single time.

A variable in Python works exactly the same way:

```python
friends_number = "0912-555-1234"
```

Now anywhere in your program you can use `friends_number` instead of typing the full number.

---

### 📌 Real-Life Examples of Variables

You use variables every day without realising it:

| Real life | What changes | Variable in Python |
|-----------|-------------|-------------------|
| Your contact list | Each contact has a name and number | `sara_number = "0912-..."` |
| A school report | Your name, grade, and score per subject | `math_score = 18` |
| A shopping basket | Number of items, total price | `total_price = 45.50` |
| Weather app | Today's temperature, city name | `temperature = 32.5` |
| A quiz | Current question number, score so far | `score = 0` |

Every app you have ever used stores thousands of variables while it runs.

---

### 🏷️ Naming Rules

Not every name is allowed. Python has rules:

| Rule | Good | Bad |
|------|------|-----|
| Use letters, numbers, underscore `_` | `my_score`, `score2` | `my score`, `score-2` |
| Cannot start with a number | `score1` | `1score` |
| No spaces | `favorite_food` | `favorite food` |
| Case-sensitive | `Name` and `name` are different variables | — |
| Use lowercase and underscores (by convention) | `first_name` | `FirstName` (for variables) |

**Choose names that describe what the variable holds.** `x = 14` tells you nothing. `age = 14` is clear.

---

### 🔄 Variables Can Change

A variable can be updated at any point — that is why it is called a *variable* (it varies!):

```python
score = 0        # start of the game
score = score + 10   # player answered correctly
score = score + 10   # another correct answer
print(score)     # prints 20
```

The right side of `=` is calculated first, then stored in the variable on the left.

---

## 🧩 The Four Data Types — In Depth

Every variable holds a specific *kind* of data. Python needs to know the kind so it knows what operations make sense.

---

### 📝 `str` — String (Text)

A string is any sequence of characters — letters, numbers, symbols, spaces — wrapped in quotes.

```python
name    = "Zahra"
message = "Hello, how are you?"
phone   = "0912-555-1234"   # a phone number stored as TEXT, not a number
emoji   = "🌸"
```

**Real life:** Every word you see on a screen — app names, messages, usernames, captions — is a string.

**Key things to know:**
- Single quotes `'hello'` and double quotes `"hello"` both work.
- Numbers in quotes are strings: `"14"` is **not** the same as `14`.
- You can join two strings with `+`: `"Maryam" + " " + "Nemati"` → `"Maryam Nemati"`
- You can repeat a string with `*`: `"ha" * 3` → `"hahaha"`

---

### 🔢 `int` — Integer (Whole Number)

An integer is any whole number — positive, negative, or zero. No decimal point.

```python
age          = 14
grade        = 8
temperature  = -5    # below zero is fine
score        = 0
year         = 1402  # Hijri year
```

**Real life:** Counting things that cannot be split — number of students in a class, pages in a book, goals in a match.

**Key things to know:**
- No quotes around numbers.
- You can do math: `age + 1`, `score * 2`, `year - 1`.
- `int` cannot hold a decimal. `7 / 2` in Python gives `3.5` (a float), not `3`.

---

### 🌊 `float` — Float (Decimal Number)

A float is a number with a decimal point.

```python
height_cm    = 162.5
temperature  = 36.6    # body temperature
average      = 87.3
price        = 12.99
pi           = 3.14159
```

**Real life:** Measurements, prices, averages, scientific values — anything where fractions matter.

**Key things to know:**
- Even `3.0` is a float (not an int), because it has a decimal point.
- Be careful with very precise floats — computers cannot always store them exactly: `0.1 + 0.2` gives `0.30000000000000004` in Python!
- `round(3.14159, 2)` rounds to 2 decimal places → `3.14`

---

### ✅ `bool` — Boolean (True / False)

A boolean can only ever be one of two values: `True` or `False`. Nothing else.

```python
loves_coding   = True
has_homework   = False
is_logged_in   = True
is_weekend     = False
```

**Real life:** Any yes/no question. Is the alarm on? Is the user logged in? Did the student pass?

**Key things to know:**
- `True` and `False` must start with a capital letter. `true` will cause an error.
- Booleans come from comparisons: `10 > 5` gives `True`. `10 < 5` gives `False`.
- They are used constantly with `if` statements: `if is_weekend:` — do something.

---

## 🔍 How Python Knows the Type

You never have to *declare* a type in Python. Python figures it out from what you write:

```python
x = "hello"    # str  — because of the quotes
x = 42         # int  — whole number, no quotes
x = 3.14       # float — has a decimal point
x = True       # bool — the keyword True or False
```

This is called **dynamic typing** — the type is determined at the moment you assign a value.

Use `type()` to check at any time:

```python
print(type("Maryam"))   # <class 'str'>
print(type(14))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type(True))       # <class 'bool'>
```

---

## 🎯 What Are We Doing Today?

- Reading code that stores information in variables
- Learning the four basic data types Python uses
- Printing a profile card using our variables
- Making small changes to see what happens

---

## 🧩 The Four Data Types

| Type | Name | Examples |
|------|------|---------|
| `str` | String (text) | `"Maryam"`, `"Tehran"`, `"hello"` |
| `int` | Integer (whole number) | `14`, `8`, `100` |
| `float` | Float (decimal number) | `162.5`, `87.3`, `3.14` |
| `bool` | Boolean (yes/no) | `True`, `False` |

> **Remember:** text always goes inside quotes. Numbers never do.

---

## ▶️ How to Run It

```bash
python variables_and_types.py
```

You will see a profile card printed in the terminal.

---

## 🧪 Activities — Try These One at a Time!

Run the program after each change so you can see what happened.

---

### 1. 🪪 Make the card yours

Find these lines near the top:

```python
name             = "Maryam"
city             = "Tehran"
favorite_subject = "Mathematics"
```

Change the values to your own name, city, and favorite subject. Run it — does the card update?

---

### 2. 🔢 Change the numbers

Try changing `age` to `15` or `height_cm` to `170.0`. What do you notice about how Python prints them?

---

### 3. 🔀 Flip a boolean

Change `loves_coding = True` to `loves_coding = False`. What changes in the output?

> **Question:** what does `True` with a capital T mean? Try typing `true` (lowercase) instead — what happens?

---

### 4. ➕ Add a new variable

Add a new variable for your favorite food:

```python
favorite_food = "Tahdig"
```

Then add a new line in the print section:

```python
print(f"  Favorite food:    {favorite_food}")
```

---

### 5. 🔍 Use type()

Find this section at the bottom:

```python
print(f"  name  →  {type(name)}")
```

Add lines for `age`, `average_score`, and `loves_coding`. What does Python tell you about each one?

---

### 6. 🧮 Mix types (careful!)

Try this in the Python shell or add it to the file:

```python
result = age + height_cm
print(result)
```

Now try:

```python
result = name + age
print(result)
```

What happens? Why?

---

## ❓ Questions to Think About

- Why does Python need to know the *type* of data — why not just store everything as text?
- What would happen if you stored a phone number as an `int` instead of a `str`? Would anything go wrong?
- Can a variable hold a different type than what it started with? Try changing `age = 14` to `age = "fourteen"` — does Python complain?

---

## 📚 For Teachers — Concepts Covered

| Concept | Where it appears |
|---------|-----------------|
| Variable assignment | `name = "Maryam"`, `age = 14` |
| `str` type | `name`, `city`, `favorite_subject` |
| `int` type | `age`, `grade`, `number_of_books` |
| `float` type | `height_cm`, `average_score` |
| `bool` type | `loves_coding`, `has_homework`, `is_weekend` |
| f-strings | `f"  Name:  {name}"` |
| `type()` function | Bottom section of the file |

---

## 🚀 Challenge Ideas

- Add a list variable: `hobbies = ["reading", "coding", "drawing"]` and print it
- Try: what is `type("14")`? What is `type(14)`? Are they the same?
- Create a "shop receipt" using variables: item name (str), quantity (int), price (float)