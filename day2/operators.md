# ➕ Basic Operators

Operators are the symbols that let you **do things with values** — add them, compare them, combine them.

**No libraries to install. Just run it.**

---

## 🎯 What Are We Doing Today?

- Learning the arithmetic operators (+, -, *, /, //, %, **)
- Learning the comparison operators (==, !=, >, <, >=, <=)
- Building a real quiz score calculator
- Understanding the crucial difference between `=` and `==`

---

## 🧩 Arithmetic Operators

| Symbol | Name | Example | Result |
|--------|------|---------|--------|
| `+` | Addition | `8 + 5` | `13` |
| `-` | Subtraction | `8 - 5` | `3` |
| `*` | Multiplication | `8 * 5` | `40` |
| `/` | Division | `8 / 5` | `1.6` |
| `//` | Integer division | `8 // 5` | `1` (drops the decimal) |
| `%` | Modulo (remainder) | `8 % 5` | `3` |
| `**` | Power | `2 ** 8` | `256` |

> **Modulo tip:** `20 % 6` gives `2`, because 20 = 3×6 + 2.
> It is great for checking if a number is even: `n % 2 == 0`.

---

## 🧩 Comparison Operators

| Symbol | Meaning | Example | Result |
|--------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `8 > 10` | `False` |
| `<` | Less than | `8 < 10` | `True` |
| `>=` | Greater than or equal | `10 >= 10` | `True` |
| `<=` | Less than or equal | `7 <= 10` | `True` |

> Comparison operators always return `True` or `False`.
> We use them most often inside `if` statements.

---

## ⚠️ `=` vs `==` — Very Important!

```python
x = 5       # assignment  → puts 5 into x
x == 5      # comparison  → asks "is x equal to 5?" → True or False
```

Mixing these up is one of the most common beginner mistakes. Python will either give an error or a very confusing result.

---

## ▶️ How to Run It

```bash
python operators.py
```

You will see the arithmetic table and a quiz score calculator.

---

## 🧪 Activities — Try These One at a Time!

---

### 1. 📋 Read the table first

Before running, look at the operator table at the top of the file.
For each row, try to guess the result in your head, then run the file and check.

---

### 2. ✏️ Change the scores

Find the quiz scores:

```python
q1 = 8
q2 = 7
q3 = 9
q4 = 6
q5 = 10
```

Change them to your own imaginary scores. Does the percentage update automatically?

---

### 3. ➕ Add more questions

Add `q6 = 8` and include it in the `total` calculation. Also update `max_possible` to `6 * 10`.

---

### 4. 🔍 Experiment with integer division

In the Python shell (type `python` in your terminal), try:

```
>>> 7 / 2
>>> 7 // 2
>>> 7 % 2
```

What is the difference between `/` and `//`? When would `//` be useful?

---

### 5. 🧮 Check if a number is even or odd

Add this to the bottom of `operators.py`:

```python
number = int(input("Enter any number: "))
remainder = number % 2
print(f"{number} % 2 = {remainder}")
```

If `remainder` is 0, the number is even. If it is 1, the number is odd.

---

### 6. 🔍 Explore comparison results

Add these lines and run:

```python
print(type(10 == 10))   # what type is a comparison result?
print(10 == 10.0)       # is an int equal to a float with the same value?
print("10" == 10)       # is text "10" equal to the number 10?
```

---

## ❓ Questions to Think About

- What is the result of `10 / 3`? What about `10 // 3`? Which would you use if you wanted to know how many full groups of 3 fit into 10?
- Why does `%` (modulo) exist? Can you think of a real situation where knowing the remainder is useful?
- What happens if you try `"hello" + "world"`? What about `"hello" * 3`? Can you predict it?

---

## 📚 For Teachers — Concepts Covered

| Concept | Where it appears |
|---------|-----------------|
| Arithmetic operators | Top section and quiz calculator |
| Integer division `//` | Operator table |
| Modulo `%` | Operator table |
| Exponentiation `**` | Operator table |
| Format specifier `.2f` | Division result display |
| Comparison operators | Bottom section |
| `=` vs `==` | Closing note |

---

## 🚀 Challenge Ideas

- Build a "split the bill" calculator: ask how many people and the total cost, then use `//` and `%` to show the fair share and any leftover
- Use `**` to calculate compound interest after 5 years
- Ask the user for two numbers and print all six comparison results between them