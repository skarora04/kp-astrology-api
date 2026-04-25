import swisseph as swe

swe.set_ephe_path('.')

year = 1982
month = 12
day = 4
hour = 14.25

jd = swe.julday(year, month, day, hour)

planets = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mars": swe.MARS,
    "Mercury": swe.MERCURY,
    "Jupiter": swe.JUPITER,
    "Venus": swe.VENUS,
    "Saturn": swe.SATURN,
}

nakshatras = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
    "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
    "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra",
    "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula",
    "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta",
    "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

dasha_order = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]

dasha_years = {
    "Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10,
    "Mars": 7, "Rahu": 18, "Jupiter": 16,
    "Saturn": 19, "Mercury": 17
}

def get_nakshatra(degree):
    nak_length = 13 + 20/60
    index = int(degree / nak_length)
    return nakshatras[index], index

def get_sub_lord(degree):
    nak_length = 13 + 20/60
    total_minutes = 800

    nak_index = int(degree / nak_length)
    nak_start = nak_index * nak_length

    pos_in_nak = (degree - nak_start) * 60  # convert to minutes

    # Start from Nakshatra lord
    start_lord = dasha_order[nak_index % 9]

    # Rotate order
    start_index = dasha_order.index(start_lord)
    sequence = dasha_order[start_index:] + dasha_order[:start_index]

    cumulative = 0

    for planet in sequence:
        sub_size = (dasha_years[planet] / 120) * total_minutes
        cumulative += sub_size

        if pos_in_nak <= cumulative:
            return planet

    return sequence[-1]

print("=== REAL KP SUB LORD ===")

for name, p in planets.items():
    pos = swe.calc_ut(jd, p)
    degree = pos[0][0]

    nak, _ = get_nakshatra(degree)
    sub = get_sub_lord(degree)

    print(f"{name}: {degree:.2f}° → {nak} → Sub: {sub}")

# Rahu
rahu_pos = swe.calc_ut(jd, swe.MEAN_NODE)
rahu_deg = rahu_pos[0][0]
rahu_nak, _ = get_nakshatra(rahu_deg)
rahu_sub = get_sub_lord(rahu_deg)

print(f"Rahu: {rahu_deg:.2f}° → {rahu_nak} → Sub: {rahu_sub}")

# Ketu
ketu_deg = (rahu_deg + 180) % 360
ketu_nak, _ = get_nakshatra(ketu_deg)
ketu_sub = get_sub_lord(ketu_deg)

print(f"Ketu: {ketu_deg:.2f}° → {ketu_nak} → Sub: {ketu_sub}")