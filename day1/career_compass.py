# ============================================================
# CAREER COMPASS
# A tool that helps students explore career options
# using basic programming ideas like loops and sorting.
# ============================================================

# ---------- DATA ----------
# Each career is stored as a dictionary (key → value pairs).
# Think of it like a profile card for each job.
careers = [
    {"title": "Software Developer",  "field": "tech",     "skills": ["coding", "math"],      "salary": 85000,  "years": 4},
    {"title": "Graphic Designer",    "field": "art",      "skills": ["drawing", "tech"],      "salary": 50000,  "years": 2},
    {"title": "Teacher",             "field": "people",   "skills": ["writing", "teamwork"],  "salary": 45000,  "years": 4},
    {"title": "Doctor",              "field": "people",   "skills": ["science", "teamwork"],  "salary": 120000, "years": 8},
    {"title": "Architect",           "field": "art",      "skills": ["drawing", "math"],      "salary": 70000,  "years": 5},
    {"title": "Marketing Manager",   "field": "business", "skills": ["writing", "teamwork"],  "salary": 65000,  "years": 4},
    {"title": "Data Scientist",      "field": "tech",     "skills": ["coding", "math"],       "salary": 95000,  "years": 4},
    {"title": "Wildlife Biologist",  "field": "nature",   "skills": ["science", "teamwork"],  "salary": 55000,  "years": 6},
]


# ---------- SHOW ALL CAREERS ----------
def show_careers():
    print("\n📋 ALL CAREERS:")
    number = 1
    for career in careers:
        skills_text = ", ".join(career["skills"])   # turn the list into a readable string
        print(f"{number}. {career['title']} | field: {career['field']} | skills: {skills_text} | ${career['salary']}/yr | {career['years']} yrs of study")
        number = number + 1


# ---------- FILTER BY FIELD ----------
# Goes through every career and keeps only the ones that match the field the user asked for.
# This is called a "linear search" — we check each item one by one.
def filter_by_field(field):
    print(f"\n🔍 CAREERS IN '{field}':")
    found_any = False

    for career in careers:
        if career["field"] == field:
            print(f"  - {career['title']}  (${career['salary']}/yr)")
            found_any = True

    if not found_any:
        print("  No careers found for that field.")


# ---------- SORT BY SALARY (Bubble Sort) ----------
# Bubble sort works by comparing two neighbours at a time.
# If they are in the wrong order, swap them.
# Keep doing this until everything is in order.
def sort_by_salary(ascending=True):
    # Make a copy so we don't mess up the original list
    sorted_careers = careers.copy()
    total = len(sorted_careers)

    for pass_number in range(total - 1):
        for i in range(total - 1 - pass_number):
            left  = sorted_careers[i]["salary"]
            right = sorted_careers[i + 1]["salary"]

            # Decide whether to swap based on the sort direction
            should_swap = False
            if ascending and left > right:
                should_swap = True
            if not ascending and left < right:
                should_swap = True

            if should_swap:
                sorted_careers[i], sorted_careers[i + 1] = sorted_careers[i + 1], sorted_careers[i]

    order_label = "lowest → highest" if ascending else "highest → lowest"
    print(f"\n💰 CAREERS SORTED BY SALARY ({order_label}):")
    for career in sorted_careers:
        print(f"   {career['title']}: ${career['salary']}/yr")


# ---------- MATCH BY SKILLS ----------
# Counts how many of the user's skills match each career.
# The careers with the most matches come first.
# This is called a "selection sort" — we find the best one, move it to the front, repeat.
def match_by_skills(user_skills):
    # Step 1: give each career a score (number of matching skills)
    scores = []
    for career in careers:
        match_count = 0
        for skill in user_skills:
            if skill in career["skills"]:
                match_count = match_count + 1
        scores.append((match_count, career))

    # Step 2: sort by score using selection sort (highest score first)
    for i in range(len(scores)):
        best_index = i
        for j in range(i + 1, len(scores)):
            if scores[j][0] > scores[best_index][0]:
                best_index = j
        scores[i], scores[best_index] = scores[best_index], scores[i]

    # Step 3: show the top 3 matches
    print("\n🎯 BEST MATCHES FOR YOUR SKILLS:")
    shown = 0
    for score, career in scores:
        if shown == 3:
            break
        if score > 0:
            print(f"   {career['title']}  (matched {score} skill(s) — ${career['salary']}/yr)")
            shown = shown + 1

    if shown == 0:
        print("   No matches found. Try different skills.")


# ---------- FILTER BY STUDY YEARS ----------
# Keeps only careers that need no more than the given number of study years.
def filter_by_study_years(max_years):
    print(f"\n⏱️  CAREERS THAT NEED {max_years} YEARS OF STUDY OR LESS:")
    found_any = False

    for career in careers:
        if career["years"] <= max_years:
            print(f"  - {career['title']}  ({career['years']} yrs of study — ${career['salary']}/yr)")
            found_any = True

    if not found_any:
        print("  No careers found within that study time.")


# ============================================================
# MAIN MENU
# This is the part the user actually sees and types into.
# ============================================================
print("🧭  CAREER COMPASS 🧭")
print("Explore careers using simple algorithms!\n")
print("COMMANDS YOU CAN TYPE:")
print("  list                    → show all careers")
print("  filter <field>          → field can be: tech, art, people, business, nature")
print("  sort salary asc         → sort by salary, lowest first")
print("  sort salary desc        → sort by salary, highest first")
print("  match <skill1,skill2>   → e.g.  match coding,math")
print("  max_years <number>      → e.g.  max_years 4")
print("  exit                    → quit the program")

while True:
    user_input = input("\n👩‍💻 > ").strip().lower()

    if user_input == "list":
        show_careers()

    elif user_input.startswith("filter"):
        parts = user_input.split()
        valid_fields = ["tech", "art", "people", "business", "nature"]
        if len(parts) == 2 and parts[1] in valid_fields:
            filter_by_field(parts[1])
        else:
            print("Please give a valid field. Options: tech, art, people, business, nature")
            print("Example: filter tech")

    elif user_input.startswith("sort salary"):
        parts = user_input.split()
        if len(parts) >= 3 and parts[2] == "desc":
            sort_by_salary(ascending=False)
        else:
            sort_by_salary(ascending=True)

    elif user_input.startswith("match"):
        parts = user_input.split(maxsplit=1)   # split only on the first space
        if len(parts) == 2:
            skill_list = parts[1].split(",")
            skill_list = [s.strip() for s in skill_list]   # remove any extra spaces
            match_by_skills(skill_list)
        else:
            print("Please list your skills after 'match', separated by commas.")
            print("Example: match coding,math")

    elif user_input.startswith("max_years"):
        parts = user_input.split()
        if len(parts) == 2 and parts[1].isdigit():
            filter_by_study_years(int(parts[1]))
        else:
            print("Please give a number after 'max_years'.")
            print("Example: max_years 4")

    elif user_input == "exit":
        print("\n🌟 Good luck on your career journey! 🌟\n")
        break

    else:
        print("I don't recognise that command. Try: list, filter tech, sort salary asc, match coding,math, max_years 4")