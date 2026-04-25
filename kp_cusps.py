import swisseph as swe
from datetime import datetime

# Setup
swe.set_ephe_path('.')
swe.set_sid_mode(swe.SIDM_KRISHNAMURTI)

# Nakshatra list
nakshatras = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
    "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
    "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra",
    "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula",
    "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta",
    "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

# Vimshottari proportion
dasha_sequence = [
    ("Ketu", 7),
    ("Venus", 20),
    ("Sun", 6),
    ("Moon", 10),
    ("Mars", 7),
    ("Rahu", 18),
    ("Jupiter", 16),
    ("Saturn", 19),
    ("Mercury", 17)
]

# Convert IST → UTC
def to_utc(hour, minute):
    return hour + minute / 60 - 5.5

# Get nakshatra
def get_nakshatra(degree):
    degree = degree % 360
    index = int(degree / 13.333333)
    return nakshatras[index]

# REAL KP Sub Lord
def get_sub_lord(degree):
    # degree within nakshatra
    deg_in_nak = degree % 13.333333

    total = 13.333333
    accumulated = 0

    for planet, years in dasha_sequence:
        portion = total * (years / 120)
        accumulated += portion

        if deg_in_nak <= accumulated:
            return planet

    return "Mercury"  # fallback

# MAIN FUNCTION
def get_cusps(dob, time, lat, lon):
    dt = datetime.strptime(dob + " " + time, "%Y-%m-%d %H:%M")

    utc_hour = to_utc(dt.hour, dt.minute)
    jd = swe.julday(dt.year, dt.month, dt.day, utc_hour)

    # Houses (Placidus)
    cusps, ascmc = swe.houses(jd, lat, lon)

    result = {}

    for i in range(12):
        deg = cusps[i]

        result[f"House_{i+1}"] = {
            "degree": round(deg, 4),
            "nakshatra": get_nakshatra(deg),
            "sub_lord": get_sub_lord(deg)
        }

    result["Ascendant"] = round(ascmc[0], 4)

    return result


# TEST
if __name__ == "__main__":
    data = get_cusps("1982-12-04", "14:15", 28.6139, 77.2090)
    print(data)