# 💬 Comments

Comments are notes you write inside your code — **for people, not for the computer**.
Python ignores everything after a `#` on a line.

**No libraries to install. Just run it.**

---

## 🎯 What Are We Doing Today?

- Understanding what comments are and why we write them
- Reading a program full of comments to see how they help
- Practicing "commenting out" lines to turn them off temporarily
- Adding our own comments to existing code

---

## 🧩 Key Ideas

```python
# This is a comment — Python skips this line completely

name = "Sara"   # this is an inline comment — code runs, then Python ignores the rest

# print("This line is turned off")   ← commented-out code
```

**Two kinds of comments:**

| Kind | When to use |
|------|-------------|
| Explanation comment | Explain *why* — a hidden reason, a tricky step, a choice you made |
| Commented-out code | Temporarily disable a line without deleting it |

> **Tip:** A good comment explains WHY, not WHAT.
> `x = x + 1` is already clear — "increment x" adds nothing.
> But *why* are we incrementing? That is worth a comment.

---

## ▶️ How to Run It

```bash
python comments.py
```

You will see a recipe scaler that calculates ingredient amounts for a larger group.

---

## 🧪 Activities — Try These One at a Time!

---

### 1. 🍲 Read before running

Before you run the file, read it carefully with the comments.
Can you predict what numbers the program will print? Write them down, then run it and check.

---

### 2. 🔢 Change the group size

Change `actual_servings` from `12` to `20`. Run it — do all the ingredient amounts update automatically?

> **Question:** why do all amounts change when you only changed one number?

---

### 3. ✏️ Add a new ingredient

Add your own ingredient at the bottom (after the existing ones):

```python
turmeric_tsp = 2   # teaspoons of ground turmeric
print(f"  Turmeric:      {turmeric_tsp * scale:.1f} tsp")
```

---

### 4. 💬 Comment out an ingredient

Put a `#` at the start of the lamb lines to remove it from the output:

```python
# lamb_g = 400
# print(f"  Lamb:  {lamb_g * scale:.0f} g")
```

Run it. Lamb disappears! Remove the `#` to bring it back.

---

### 5. ✍️ Write your own comments

Find these lines which have no comment yet:

```python
scale = actual_servings / original_servings
```

Add a comment above it explaining what this calculation is doing and why. There is no single correct answer — write it in your own words.

---

### 6. 🧪 Try a bad comment

Replace the comment above `scale` with this:

```python
# divide actual_servings by original_servings
scale = actual_servings / original_servings
```

This comment just restates what the code already says — it does not add any new information.
Can you write a better version that explains *why* we calculate this?

---

## ❓ Questions to Think About

- If comments are ignored by Python, why bother writing them at all?
- What would happen if you deleted every comment from this file? Would the program still work? Would it be easy to understand?
- Is there such a thing as too many comments? When does a comment make code *harder* to read?

---

## 📚 For Teachers — Concepts Covered

| Concept | Where it appears |
|---------|-----------------|
| Single-line comments | Throughout the file |
| Inline comments | After variable assignments |
| Commented-out code | The disabled `print` at the bottom |
| Variables and arithmetic | `scale`, ingredient calculations |
| f-strings with formatting | `:.0f` and `:.1f` format specifiers |

---

## 🚀 Challenge Ideas

- Copy one of the day1 files into day2 and add a comment to **every** line explaining what it does
- Write a short "story" version of this recipe scaler where the comments tell a narrative about cooking
- Find a piece of code online (or from day1) that has no comments — add your own comments to explain it