# ============================================================
# BASIC OPERATORS
# Day 2 — Pyteen
# ============================================================

# ---------- ARITHMETIC OPERATORS ----------
#  +   addition
#  -   subtraction
#  *   multiplication
#  /   division          (result is always a decimal)
#  //  integer division  (chops off the decimal, rounds DOWN)
#  %   modulo            (gives the REMAINDER after dividing)
#  **  power / exponent

print("📐 ARITHMETIC OPERATORS")
print()

a = 20
b = 6

print(f"{a} + {b}   = {a + b}")
print(f"{a} - {b}   = {a - b}")
print(f"{a} * {b}   = {a * b}")
print(f"{a} / {b}   = {a / b:.2f}")    # .2f shows exactly 2 decimal places
print(f"{a} // {b}  = {a // b}")       # 20 ÷ 6 = 3 remainder 2 → gives 3
print(f"{a} % {b}   = {a % b}")        # remainder of 20 ÷ 6 → gives 2
print(f"{a} ** 2   = {a ** 2}")        # 20 to the power of 2 = 400

# ---------- PRACTICAL EXAMPLE: Quiz Score Calculator ----------
print()
print("=" * 42)
print("       QUIZ SCORE CALCULATOR")
print("=" * 42)
print()

# Each question is worth 10 points
q1 = 8
q2 = 7
q3 = 9
q4 = 6
q5 = 10

total         = q1 + q2 + q3 + q4 + q5
max_possible  = 5 * 10
percentage    = (total / max_possible) * 100
average       = total / 5

print(f"Scores:      {q1}, {q2}, {q3}, {q4}, {q5}")
print(f"Total:       {total} / {max_possible}")
print(f"Average:     {average:.1f}")
print(f"Percentage:  {percentage:.1f}%")

# ---------- COMPARISON OPERATORS ----------
# These compare two values and always give back True or False.
#
#  ==   equal to
#  !=   not equal to
#  >    greater than
#  <    less than
#  >=   greater than or equal to
#  <=   less than or equal to

print()
print("🔍 COMPARISON OPERATORS")
print()
print(f"10 == 10  →  {10 == 10}")
print(f"10 != 5   →  {10 != 5}")
print(f"8 > 10    →  {8 > 10}")
print(f"8 < 10    →  {8 < 10}")
print(f"10 >= 10  →  {10 >= 10}")
print(f"7 <= 10   →  {7 <= 10}")

# ---------- IMPORTANT: = vs == ----------
# =   is ASSIGNMENT   →  puts a value into a variable   (x = 5)
# ==  is COMPARISON   →  checks if two things are equal  (x == 5)
# This is one of the most common mix-ups in programming!
print()
print("Remember:")
print("  x = 5      saves the value 5 into x")
print("  x == 5     asks: is x equal to 5? (True or False)")