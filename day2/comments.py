# ============================================================
# COMMENTS
# Day 2 — Pyteen
# ============================================================

# A comment is a note inside your code that Python completely ignores.
# Comments start with the # symbol.
# Everything after # on that line is for PEOPLE to read — not the computer.

# WHY write comments?
#   - To explain WHY you did something a certain way
#   - To leave a note for your future self
#   - To help a teammate understand your code
#   - To temporarily "turn off" a line without deleting it

# ============================================================
# A RECIPE SCALER — reads like a story because of comments
# ============================================================

# The original recipe is written for 4 people
original_servings = 4

# Today we are cooking for a bigger group
actual_servings = 12

# This scale factor tells us: how many times bigger is the group?
# Example: 12 / 4 = 3.0 → we need 3x as much of everything
scale = actual_servings / original_servings

print("🍲 Recipe Scaler — Maryam's Ghormeh Sabzi")
print(f"Original recipe: for {original_servings} people")
print(f"Cooking for:     {actual_servings} people")
print(f"Scale factor:    x{scale}")
print()

# ---------- ORIGINAL INGREDIENT AMOUNTS ----------
lamb_g        = 400   # grams of lamb
beans_g       = 150   # kidney beans
spinach_g     = 200   # fresh spinach
dried_limes   = 3     # whole dried limes (limu omani)

# ---------- SCALED AMOUNTS ----------
# Multiply each ingredient by the scale factor
# :.0f means "show as a whole number, no decimals"
print("Ingredients you need:")
print(f"  Lamb:          {lamb_g * scale:.0f} g")
print(f"  Kidney beans:  {beans_g * scale:.0f} g")
print(f"  Spinach:       {spinach_g * scale:.0f} g")
print(f"  Dried limes:   {dried_limes * scale:.0f} pieces")

# ---------- COMMENTED-OUT CODE ----------
# Put a # in front of a line to "turn it off" temporarily.
# Remove the # to turn it back on. Try it!
# print("This line is turned off — Python does not see it.")

# ---------- YOUR TURN ----------
# Add a new ingredient below (saffron? turmeric?) and scale it too!
# Example:
# saffron_g = 1   # just a pinch!
# print(f"  Saffron:       {saffron_g * scale:.1f} g")