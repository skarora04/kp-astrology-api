import swisseph as swe
from datetime import datetime

# Setup
swe.set_ephe_path('.')
swe.set_sid_mode(swe.SIDM_KRISHNAMURTI)

# Planets list
planets = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mars": swe.MARS,
    "Mercury": swe.MERCURY,
    "Jupiter": swe.JUPITER,
    "Venus": swe.VENUS,
    "Saturn": swe.SATURN,
}

# Nakshatra list
nakshatras = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
    "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
    "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra",
    "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula",
    "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta",
    "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

# Zodiac signs
zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# Get zodiac sign
def get_sign(degree):
    degree = degree % 360
    sign_index = int(degree / 30)
    sign_name = zodiac_signs[sign_index]
    sign_degree = degree % 30
    return sign_name, round(sign_degree, 2)

# Get nakshatra
def get_nakshatra(degree):
    degree = degree % 360
    index = int(degree / 13.333333)
    return nakshatras[index]

# Convert IST to UTC
def to_utc(hour, minute):
    return hour + minute / 60 - 5.5

# MAIN FUNCTION
def get_all_planets(dob, time):
    dt = datetime.strptime(dob + " " + time, "%Y-%m-%d %H:%M")

    utc_hour = to_utc(dt.hour, dt.minute)
    jd = swe.julday(dt.year, dt.month, dt.day, utc_hour)

    result = {}

    # Planets
    for name, p in planets.items():
        pos = swe.calc_ut(jd, p)
        degree = pos[0][0]

        sign, sign_deg = get_sign(degree)
        nak = get_nakshatra(degree)

        result[name] = {
            "degree": round(degree, 2),
            "sign": sign,
            "sign_degree": sign_deg,
            "nakshatra": nak
        }

    # Rahu
    rahu_pos = swe.calc_ut(jd, swe.MEAN_NODE)
    rahu_deg = rahu_pos[0][0]

    sign, sign_deg = get_sign(rahu_deg)

    result["Rahu"] = {
        "degree": round(rahu_deg, 2),
        "sign": sign,
        "sign_degree": sign_deg,
        "nakshatra": get_nakshatra(rahu_deg)
    }

    # Ketu
    ketu_deg = (rahu_deg + 180) % 360
    sign, sign_deg = get_sign(ketu_deg)

    result["Ketu"] = {
        "degree": round(ketu_deg, 2),
        "sign": sign,
        "sign_degree": sign_deg,
        "nakshatra": get_nakshatra(ketu_deg)
    }

    return result


# TEST
if __name__ == "__main__":
    data = get_all_planets("1982-12-04", "14:15")
    print(data)