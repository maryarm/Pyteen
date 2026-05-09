# ============================================================
# IF / ELSE
# Day 2 — Pyteen
# ============================================================

# if/else lets your program MAKE DECISIONS.
#
# Structure:
#
#   if condition_is_true:
#       do this
#   elif another_condition_is_true:
#       do this instead
#   else:
#       do this when nothing above was true
#
# Python knows which lines belong to the if/elif/else
# because of the INDENTATION (the spaces at the start of the line).
# Always use 4 spaces (or one Tab key).

# ============================================================
# EXAMPLE 1 — Study Helper
# ============================================================
print("📚 STUDY HELPER")
print()

hours_studied = int(input("How many hours did you study today? "))

if hours_studied >= 3:
    print("Amazing work! You put in real effort today.")
elif hours_studied >= 1:
    print("Good start! Try to add one more hour tomorrow.")
else:
    print("Everyone has off days. Tomorrow is a fresh start!")

# ============================================================
# EXAMPLE 2 — Grade Checker
# ============================================================
print()
print("=" * 40)
print("         GRADE CHECKER")
print("=" * 40)

score = int(input("Enter your test score (0-100): "))

if score >= 90:
    grade   = "A"
    message = "Excellent! Keep it up!"
elif score >= 80:
    grade   = "B"
    message = "Well done!"
elif score >= 70:
    grade   = "C"
    message = "Good effort — keep going!"
elif score >= 60:
    grade   = "D"
    message = "You can do better. Let's study together."
else:
    grade   = "F"
    message = "Don't give up. Ask your teacher for help — that's brave."

print(f"\nScore: {score}")
print(f"Grade: {grade}")
print(f"       {message}")

# ============================================================
# EXAMPLE 3 — Weekend Planner (using AND / OR)
# ============================================================
# and  →  both conditions must be True
# or   →  at least one condition must be True
# not  →  flips True to False and False to True

print()
print("=" * 40)
print("       WEEKEND PLANNER")
print("=" * 40)

is_friday   = input("Is it Friday? (yes/no): ").strip().lower() == "yes"
is_saturday = input("Is it Saturday? (yes/no): ").strip().lower() == "yes"
has_homework = input("Do you have homework? (yes/no): ").strip().lower() == "yes"

is_weekend = is_friday or is_saturday

if is_weekend and not has_homework:
    print("\nYou are free! Enjoy your weekend.")
elif is_weekend and has_homework:
    print("\nFinish your homework first — then enjoy the rest of the day!")
else:
    print("\nIt is a school day. Stay focused, you are doing great!")