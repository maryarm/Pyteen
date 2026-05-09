# ============================================================
# INPUT & OUTPUT
# Day 2 — Pyteen
# ============================================================

# print()  →  OUTPUT: shows a message on the screen
# input()  →  INPUT: pauses and waits for the user to type something

# ---------- SIMPLE OUTPUT ----------
print("Welcome to your Name Card Generator!")
print("Answer a few questions and we will make your card.")
print()   # an empty print() adds a blank line — good for spacing

# ---------- COLLECTING INPUT ----------
# input() always gives back TEXT, even if the user types a number.
# We store the answer in a variable so we can use it later.

name           = input("What is your name? ")
city           = input("What city are you from? ")
favorite_color = input("What is your favorite color? ")

# To do math with a number from input(), we must convert it first.
# int(...)   turns text like "14" into the number 14
age = int(input("How old are you? "))

# ---------- USING INPUT IN OUTPUT ----------
print()
print("=" * 40)
print("           YOUR NAME CARD")
print("=" * 40)
print(f"  Name:   {name}")
print(f"  City:   {city}")
print(f"  Age:    {age} years old")
print(f"  Color:  {favorite_color}")
print("=" * 40)

years_until_20 = 20 - age
print(f"\nHello, {name}! You are {age} years old.")
print(f"In {years_until_20} years you will be 20.")
print("Keep coding — you are doing great!")