# ============================================================
# VARIABLES AND DATA TYPES
# Day 2 — Pyteen
# ============================================================

# A variable is a box that stores information.
# You give the box a name, and put something inside it.
#
#   box_name = value
#
# Python has four basic types of data:
#   str   — text (anything in quotes)
#   int   — whole numbers
#   float — decimal numbers
#   bool  — True or False (yes or no)

# ---------- TEXT (str) ----------
name             = "Maryam"
city             = "Tehran"
favorite_subject = "Mathematics"

# ---------- WHOLE NUMBERS (int) ----------
age              = 14
grade            = 8
number_of_books  = 23

# ---------- DECIMAL NUMBERS (float) ----------
height_cm        = 162.5
average_score    = 87.3

# ---------- TRUE / FALSE (bool) ----------
loves_coding     = True
has_homework     = True
is_weekend       = False

# ---------- PRINTING THE PROFILE CARD ----------
print("=" * 42)
print("        MY DIGITAL PROFILE CARD")
print("=" * 42)
print(f"  Name:             {name}")
print(f"  City:             {city}")
print(f"  Age:              {age}")
print(f"  Grade:            {grade}")
print(f"  Favorite subject: {favorite_subject}")
print(f"  Height:           {height_cm} cm")
print(f"  Average score:    {average_score}")
print(f"  Loves coding:     {loves_coding}")
print("=" * 42)

# ---------- CHECKING THE TYPE ----------
# type() tells you what kind of data a variable holds.
print()
print("What TYPE is each variable?")
print(f"  name             →  {type(name)}")
print(f"  age              →  {type(age)}")
print(f"  height_cm        →  {type(height_cm)}")
print(f"  loves_coding     →  {type(loves_coding)}")