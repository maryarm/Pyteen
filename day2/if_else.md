# 🔀 If / Else

Until now our programs ran the same steps every time.
`if/else` lets your program **choose a different path** based on what the user does or what the data says.

**No libraries to install. Just run it.**

---

## 🤔 What Is an if/else and Why Do We Need It?

Imagine you are at a shop. The shopkeeper says:

> "If you have enough money, you can buy the book. Otherwise, I will put it aside for you."

That is exactly what `if/else` does in code — it makes a **decision** and picks one path over another.

Without `if/else`, every program would be a straight line — the same steps, the same result, every single time. No matter who runs it, no matter what they type, it would always do the same thing.

`if/else` is what gives programs **intelligence** — the ability to react differently depending on the situation.

**Real-life decisions that become `if/else` in code:**

| Real life | Code |
|-----------|------|
| "If the alarm goes off, wake up" | `if alarm_ringing: wake_up()` |
| "If the password is correct, log in" | `if password == correct: allow_access()` |
| "If the score is above 90, show 'A'" | `if score >= 90: grade = "A"` |
| "If it is raining, take an umbrella" | `if is_raining: bring_umbrella()` |
| "If the battery is below 20%, warn the user" | `if battery < 20: show_warning()` |

Every app you have ever used is full of thousands of these decisions running every second.

---

## ⚙️ How It Works in the Background

When Python reaches an `if` statement, here is exactly what happens inside:

### Step 1 — Evaluate the condition

Python looks at the condition — the expression after `if` — and calculates whether it is `True` or `False`.

```python
score = 85
score >= 90        # Python evaluates this → False
```

### Step 2 — Choose a branch

- If the condition is `True` → run the indented block below the `if`.
- If the condition is `False` → skip that block entirely and check the next `elif` (if there is one).

### Step 3 — Check elif one by one (if needed)

Python checks each `elif` condition **in order**, from top to bottom. The moment one is `True`, it runs that block and **skips all the rest** — even if a later `elif` would also be `True`.

```python
score = 85

if score >= 90:       # False → skip
    grade = "A"
elif score >= 80:     # True → run this, then jump out
    grade = "B"
elif score >= 70:     # never even checked
    grade = "C"
else:                 # never even checked
    grade = "F"
```

### Step 4 — The else is the fallback

`else` has no condition. It runs **only if every single `if` and `elif` above it was False**. Think of it as the "none of the above" option.

### Step 5 — Continue after the block

Once Python finishes whichever branch it chose (or skips all of them if there is no `else`), it moves on to the next line of code after the entire `if/elif/else` structure.

---

## 🔍 Conditions — What Can Go Inside an `if`?

A condition is any expression that evaluates to `True` or `False`. That is it — anything that gives back a boolean works.

### Comparison operators (from the operators lesson)

```python
if score >= 90:       # greater than or equal to
if name == "Sara":    # equal to
if age != 18:         # not equal to
if price < 100:       # less than
```

### Checking a boolean variable directly

```python
is_weekend = True

if is_weekend:        # same as: if is_weekend == True:
    print("Enjoy!")

if not is_weekend:    # same as: if is_weekend == False:
    print("School day.")
```

Writing `if is_weekend:` is cleaner and more natural than `if is_weekend == True:`. Both work, but the first is preferred.

### Checking if text matches

```python
answer = input("yes or no? ").strip().lower()

if answer == "yes":
    print("Great!")
```

> `.strip()` removes any extra spaces the user might have accidentally typed.
> `.lower()` converts to lowercase so "Yes", "YES", "yes" all match.

### Checking membership with `in`

```python
city = "Mashhad"

if city in ["Tehran", "Isfahan", "Mashhad", "Shiraz"]:
    print("You are in a major Iranian city.")
```

---

## 🧱 Structure — Every Possible Form

### Just an `if` (no else)

```python
if score > 100:
    print("That score seems too high — are you sure?")

# if score is 100 or below, nothing happens — that is fine
```

### `if` and `else`

```python
if score >= 60:
    print("PASS")
else:
    print("FAIL")
```

### `if`, `elif`, `else`

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### Nested `if` — an `if` inside an `if`

```python
if is_weekend:
    if has_homework:
        print("Do your homework first.")
    else:
        print("You are completely free!")
else:
    print("It is a school day.")
```

Nested `if` statements are fine but try not to go more than 2–3 levels deep — it becomes hard to read.

---

## 🔗 Combining Conditions: `and`, `or`, `not`

### `and` — both must be True

```python
if is_weekend and not has_homework:
    print("Perfect free day!")
```

Python checks left to right. If the first part is already `False`, it does not even look at the second part — there is no way the whole thing can be `True`. This is called **short-circuit evaluation**.

```python
# Truth table for AND
True  and True   →  True
True  and False  →  False
False and True   →  False   ← stops here, does not check True
False and False  →  False
```

### `or` — at least one must be True

```python
if is_friday or is_saturday or is_sunday:
    is_weekend = True
```

If the first part is already `True`, Python does not check the rest — the whole thing must be `True`.

```python
# Truth table for OR
True  or True   →  True    ← stops here, does not check True
True  or False  →  True    ← stops here
False or True   →  True
False or False  →  False
```

### `not` — flips True to False and False to True

```python
has_homework = False
if not has_homework:      # not False → True → runs
    print("You are free!")
```

---

## ⚠️ The Most Common Mistakes

### 1. Using `=` instead of `==`

```python
if score = 90:    # WRONG — this is assignment, not comparison → error
if score == 90:   # CORRECT
```

### 2. Forgetting the colon `:`

```python
if score >= 90    # WRONG — missing colon → error
    grade = "A"

if score >= 90:   # CORRECT
    grade = "A"
```

### 3. Wrong indentation

```python
if score >= 90:
grade = "A"       # WRONG — not indented → Python thinks it is outside the if

if score >= 90:
    grade = "A"   # CORRECT — 4 spaces inside
```

### 4. Order matters in elif chains

```python
# WRONG — score 95 matches both, but the FIRST match wins
if score >= 80:
    grade = "B"   # this runs for score = 95 (should be A!)
elif score >= 90:
    grade = "A"   # never reached for any score above 80

# CORRECT — most specific (highest) condition first
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
```

Always put the **most specific condition first** in an `elif` chain.

---

## 🧩 Structure

```python
if condition:
    # runs when condition is True
elif other_condition:
    # runs when the first condition was False but this one is True
else:
    # runs when nothing above was True
```

**Indentation matters.** Python uses the 4-space indent (or one Tab) to know which code belongs inside the `if`. If the indentation is wrong, Python will give an error.

---

## 🧩 `and`, `or`, `not`

| Keyword | Meaning | Example |
|---------|---------|---------|
| `and` | Both must be True | `x > 0 and x < 10` |
| `or` | At least one must be True | `is_friday or is_saturday` |
| `not` | Flips True to False | `not has_homework` |

---

## ▶️ How to Run It

```bash
python if_else.py
```

The program has three parts. Answer each question when prompted.

---

## 🎯 What Are We Doing Today?

- Making programs that take different actions based on conditions
- Using `if`, `elif`, and `else` together
- Combining conditions with `and`, `or`, and `not`
- Building three small real-world examples

---

## 🧩 Structure

```python
if condition:
    # runs when condition is True
elif other_condition:
    # runs when the first condition was False but this one is True
else:
    # runs when nothing above was True
```

**Indentation matters.** Python uses the 4-space indent (or one Tab) to know which code belongs inside the `if`. If the indentation is wrong, Python will give an error.

---

## 🧩 `and`, `or`, `not`

| Keyword | Meaning | Example |
|---------|---------|---------|
| `and` | Both must be True | `x > 0 and x < 10` |
| `or` | At least one must be True | `is_friday or is_saturday` |
| `not` | Flips True to False | `not has_homework` |

---

## ▶️ How to Run It

```bash
python if_else.py
```

The program has three parts. Answer each question when prompted.

---

## 🧪 Activities — Try These One at a Time!

---

### 1. 🎓 Test every branch

Run the grade checker several times with different scores:
- Try `95` — which branch runs?
- Try `82` — which branch?
- Try `55` — which branch?

**Goal:** make sure every `elif` and `else` runs at least once.

---

### 2. ✏️ Add your own grade level

The current scale goes: A (90+), B (80+), C (70+), D (60+), F.
Add a new level between A and B — `A-` for scores 85–89:

```python
elif score >= 85:
    grade   = "A-"
    message = "So close to an A! Great job."
```

Where exactly should this `elif` go? Why does the order matter?

---

### 3. 🔢 Change the study hours thresholds

In the Study Helper, change `3` to `4` and `1` to `2`. Run it with `3` hours — which message do you get now?

> **Discussion:** is there a "right" threshold, or does it depend on the situation?

---

### 4. 🔀 Explore and / or

In the Weekend Planner, try answering:
- Friday = yes, Saturday = no, homework = yes → what prints?
- Friday = no, Saturday = no, homework = no → what prints?

Can you predict the result *before* running it?

---

### 5. ➕ Add a Sunday

Add a `is_sunday` question and include it in the `is_weekend` check:

```python
is_sunday = input("Is it Sunday? (yes/no): ").strip().lower() == "yes"
is_weekend = is_friday or is_saturday or is_sunday
```

---

### 6. 🎨 Build your own if/else

At the bottom of the file, add a small "Mood Advisor":

```python
mood = input("\nHow are you feeling? (great/okay/tired): ").strip().lower()

if mood == "great":
    print("Wonderful! Channel that energy into something creative.")
elif mood == "okay":
    print("That is fine — steady progress beats waiting for motivation.")
elif mood == "tired":
    print("Rest is important too. Take a short break, then come back.")
else:
    print("I do not know that mood, but I hope you feel better soon!")
```

---

## ❓ Questions to Think About

- What happens if you swap two `elif` branches — does the output change? Try it with the grade checker.
- In the Weekend Planner, `not has_homework` is used. What would happen if you wrote `has_homework == False` instead? Are they the same?
- Can you have an `if` with no `else`? What happens if the condition is False and there is no else?

---

## 📚 For Teachers — Concepts Covered

| Concept | Where it appears |
|---------|-----------------|
| `if` statement | All three examples |
| `elif` | Study Helper and Grade Checker |
| `else` | All three examples |
| Boolean `and` | Weekend Planner |
| Boolean `or` | `is_weekend = is_friday or is_saturday` |
| Boolean `not` | `not has_homework` |
| Comparison operators | Score and hour checks |
| `input()` with `.strip().lower()` | Weekend Planner questions |
| Indentation rules | Implicitly throughout |

---

## 🚀 Challenge Ideas

- Add a `pass` or fail result to the grade checker: if `score >= 60`, print "PASS", otherwise print "FAIL"
- Write a number-guessing hint program: ask for a secret number (1–100) and the user's guess, then print "too high", "too low", or "correct!"
- Combine today's topics: ask the user for their name, score, and hours studied, then give a personalized message using all three in `if/else` conditions