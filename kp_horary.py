# KP Horary - Basic Engine (Number → Nakshatra → Star → Sub → Simple Prediction)

# Nakshatra list
nakshatras = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
    "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
    "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra",
    "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula",
    "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta",
    "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

# Nakshatra Lords
nak_lords = [
    "Ketu", "Venus", "Sun", "Moon", "Mars",
    "Rahu", "Jupiter", "Saturn", "Mercury",
    "Ketu", "Venus", "Sun", "Moon", "Mars",
    "Rahu", "Jupiter", "Saturn", "Mercury",
    "Ketu", "Venus", "Sun", "Moon", "Mars",
    "Rahu", "Jupiter", "Saturn", "Mercury"
]

# Vimshottari Dasha order
dasha_order = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]

# Dasha years
dasha_years = {
    "Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10,
    "Mars": 7, "Rahu": 18, "Jupiter": 16,
    "Saturn": 19, "Mercury": 17
}

# 🔢 INPUT
num = 128   # Horary number (1–249)

# 🔰 STEP 1: Nakshatra index
nak_index = int((num - 1) / 9)

# 🔰 STEP 2: Nakshatra & Star Lord
nak = nakshatras[nak_index]
star_lord = nak_lords[nak_index]

# 🔰 STEP 3: Approx Degree
nak_length = 13 + 20/60
degree = nak_index * nak_length

# 🔰 STEP 4: Sub-Lord calculation
def get_sub_lord(num, nak_index):
    total_minutes = 800

    start_num = nak_index * 9 + 1
    pos = (num - start_num) * (800 / 9)

    start_lord = nak_lords[nak_index]
    start_index = dasha_order.index(start_lord)

    sequence = dasha_order[start_index:] + dasha_order[:start_index]

    cumulative = 0

    for planet in sequence:
        sub_size = (dasha_years[planet] / 120) * total_minutes
        cumulative += sub_size

        if pos <= cumulative:
            return planet

    return sequence[-1]

sub_lord = get_sub_lord(num, nak_index)

# 🔰 STEP 5: Simple YES/NO (demo logic)
significators = {
    "Rahu": [6, 8, 12],
    "Jupiter": [2, 5, 11],
    "Saturn": [6, 10],
    "Venus": [2, 7, 11],
    "Sun": [1, 10],
    "Moon": [4, 5],
    "Mars": [3, 6],
    "Mercury": [3, 11],
    "Ketu": [8, 12]
}

houses = significators.get(sub_lord, [])

if any(h in [6, 8, 12] for h in houses):
    prediction = "NO / Delay / Obstacle"
else:
    prediction = "YES"

# 🔰 OUTPUT
print("Horary Number:", num)
print("Nakshatra:", nak)
print("Star Lord:", star_lord)
print("Approx Degree:", round(degree, 2))
print("Sub-Lord:", sub_lord)
print("Prediction:", prediction)