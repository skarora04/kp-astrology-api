import swisseph as swe

swe.set_ephe_path('.')

swe.set_sid_mode(swe.SIDM_KRISHNAMURTI)

# Birth details
year = 1982
month = 12
day = 4
hour = 14.25

lat = 28.6139
lon = 77.2090

jd = swe.julday(year, month, day, hour)

# Get cusps
cusps, ascmc = swe.houses_ex(jd, lat, lon, b'P', swe.FLG_SIDEREAL)

# Nakshatra list
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

    pos_in_nak = (degree - nak_start) * 60

    start_lord = nak_lords[nak_index]
    start_index = dasha_order.index(start_lord)
    sequence = dasha_order[start_index:] + dasha_order[:start_index]

    cumulative = 0

    for planet in sequence:
        sub_size = (dasha_years[planet] / 120) * total_minutes
        cumulative += sub_size

        if pos_in_nak <= cumulative:
            return planet

    return sequence[-1]

print("=== KP CUSPAL SUB LORDS ===")

for i in range(12):
    degree = cusps[i]
    nak, _ = get_nakshatra(degree)
    star_lord = nak_lords[int(degree / (13 + 20/60))]
    sub = get_sub_lord(degree)

    print(f"House {i+1}: {degree:.2f}° → {nak} → Star: {star_lord} → Sub: {sub}")