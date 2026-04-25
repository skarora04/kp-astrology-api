# KP Exact Engine (Step 7 → Step 9)

# Dasha order
dasha_order = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]

# Dasha years
dasha_years = {
    "Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10,
    "Mars": 7, "Rahu": 18, "Jupiter": 16,
    "Saturn": 19, "Mercury": 17
}

# Total Nakshatra length
TOTAL_MIN = 800

# 🔰 STEP 7: Sub sizes
sub_sizes = {}
for planet in dasha_order:
    sub_sizes[planet] = (dasha_years[planet] / 120) * TOTAL_MIN

print("Sub Sizes (minutes):")
for k, v in sub_sizes.items():
    print(k, ":", round(v, 2))

# 🔰 STEP 8: Ashwini Sub Table
print("\n--- Ashwini Sub Table ---")

start = 0
for planet in dasha_order:
    size = sub_sizes[planet]
    end = start + size

    print(f"{planet}: {round(start,2)} → {round(end,2)} minutes")
    start = end

# 🔰 STEP 9: Degree → Nakshatra → Sub-Lord

nakshatras = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
    "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
    "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra",
    "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula",
    "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta",
    "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

nak_lords = [
    "Ketu", "Venus", "Sun", "Moon", "Mars",
    "Rahu", "Jupiter", "Saturn", "Mercury",
    "Ketu", "Venus", "Sun", "Moon", "Mars",
    "Rahu", "Jupiter", "Saturn", "Mercury",
    "Ketu", "Venus", "Sun", "Moon", "Mars",
    "Rahu", "Jupiter", "Saturn", "Mercury"
]

def get_sub_from_degree(degree):
    nak_length = 13 + 20/60

    # Nakshatra
    nak_index = int(degree / nak_length)
    nak = nakshatras[nak_index]
    star_lord = nak_lords[nak_index]

    # position inside nakshatra (in minutes)
    nak_start = nak_index * nak_length
    pos = (degree - nak_start) * 60

    # sequence start
    start_index = dasha_order.index(star_lord)
    sequence = dasha_order[start_index:] + dasha_order[:start_index]

    cumulative = 0

    for planet in sequence:
        sub_size = sub_sizes[planet]
        cumulative += sub_size

        if pos <= cumulative:
            return nak, star_lord, planet

    return nak, star_lord, sequence[-1]

# 🔰 TEST
test_degree = 15

nak, star, sub = get_sub_from_degree(test_degree)

print("\n--- Degree Test ---")
print("Degree:", test_degree)
print("Nakshatra:", nak)
print("Star Lord:", star)
print("Sub-Lord:", sub)