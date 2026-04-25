# 🧭 Career Compass

A program that helps students **explore career options** using real algorithms — right in your terminal!

**No libraries to install. Just run it.**

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
| `careers = [...]` | A list of job profile cards — each card has a title, field, skills, salary, and study years |
| `show_careers()` | Prints every career in the list, numbered |
| `filter_by_field()` | Finds all careers in one field (e.g. only "tech" jobs) |
| `sort_by_salary()` | Sorts careers from cheapest to most expensive using **bubble sort** |
| `match_by_skills()` | Scores each career based on how many of your skills it needs, using **selection sort** |
| `filter_by_study_years()` | Finds careers that take no more than N years to study for |
| The `while True` loop | The menu — keeps asking for commands until you type `exit` |

---

## ▶️ How to Run It

Open your terminal and type:

```bash
python career_compass.py
```

You will see a menu. Type a command and press Enter. Try `list` first!

---

## 🧪 Activities — Try These One at a Time!

Each activity is a **tiny change**. Run the program after every change to see what happens. You can always undo if something breaks.

---

### 1. 📋 List all careers

Run the program and type:
```
list
```
You should see all 8 careers printed. Count them — does the numbering look right?

---

### 2. 🔍 Filter by field

Type:
```
filter tech
```
Only tech careers show up. Now try:
```
filter art
filter people
filter nature
filter business
```
What happens if you type a field that doesn't exist, like `filter sports`?

---

### 3. 💰 Sort by salary

Type:
```
sort salary asc
```
Careers appear from lowest to highest salary. Now try:
```
sort salary desc
```
The order flips! Can you spot which job pays the most?

---

### 4. 🎯 Match your skills

Type:
```
match coding,math
```
The program tells you which careers match your skills best. Try your own combination:
```
match drawing,teamwork
match science,writing
```

> **For teachers:** this is a great moment to ask — "what does it mean when a career matches 2 skills vs 1 skill?" It introduces the idea of a **score** as a way to rank results.

---

### 5. ⏱️ Filter by study years

Type:
```
max_years 4
```
Only careers that take 4 years or less appear. Try `max_years 2` — what's left?

---

### 6. ✏️ Add your own career

Find the `careers` list at the top of the file and add a new line:
```python
{"title": "Game Designer", "field": "tech", "skills": ["coding", "drawing"], "salary": 60000, "years": 3},
```
Run the program. Type `list` — does your new career appear?

> **For teachers:** encourage students to pick a career they are curious about. They can look up a real salary and study length online and add it to the list.

---

### 7. 🗑️ Comment out a career

Put a `#` at the start of any career line to hide it:
```python
# {"title": "Doctor", "field": "people", ...},
```
The `#` turns it into a comment — Python ignores it. Run the program and type `list`. Doctor is gone!

---

### 8. 🔀 Change the welcome message

Find these lines near the bottom of the file:
```python
print("🧭  CAREER COMPASS 🧭")
print("Explore careers using simple algorithms!\n")
```
Change the text to anything you like — your class name, a fun slogan, your school!

---

## ❓ Questions to Think About

These are great to discuss as a group:

- What happens if two careers have the same salary? How does bubble sort handle a tie?
- Why does `filter_by_field()` use a `found_any` variable — what is it for?
- What does `careers.copy()` do in `sort_by_salary()`? What would happen without it?
- Can you think of a career that doesn't fit into any of our 5 fields? What field would you add?

---

## 📚 For Teachers — Concepts Covered

| Concept | Where it appears |
|---------|-----------------|
| Variables | `found_any`, `match_count`, `order_label` |
| Lists | `careers`, `scores`, `skill_list` |
| Dictionaries | Each career profile card |
| Functions | `show_careers()`, `filter_by_field()`, `sort_by_salary()`, etc. |
| For loops | Iterating through `careers` in every function |
| Nested loops | Bubble sort and selection sort both use a loop inside a loop |
| Boolean logic | `should_swap`, `found_any`, `ascending` |
| Algorithms | Linear search, bubble sort, selection sort |
| User input | `input()` in the `while True` menu loop |
| String methods | `.split()`, `.strip()`, `.lower()`, `.isdigit()` |

---

## 🚀 Challenge Ideas for Later Sessions

When students are ready (session 2 or 3):

- Add a new field (e.g. `"sport"` or `"music"`) and create careers for it
- Add a new command: `max_salary <number>` — show only careers below a salary limit
- Add a `"description"` key to each career and display it in the output
- Let the user add a new career by typing its details into the terminal
- Sort careers alphabetically by title instead of by salary