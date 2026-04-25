from kp_planets_full import get_all_planets
from kp_cusps import get_cusps

# Nakshatra mapping
nakshatra_list = [
    "Ashwini","Bharani","Krittika","Rohini","Mrigashira",
    "Ardra","Punarvasu","Pushya","Ashlesha","Magha",
    "Purva Phalguni","Uttara Phalguni","Hasta","Chitra",
    "Swati","Vishakha","Anuradha","Jyeshtha","Mula",
    "Purva Ashadha","Uttara Ashadha","Shravana","Dhanishta",
    "Shatabhisha","Purva Bhadrapada","Uttara Bhadrapada","Revati"
]

nakshatra_lords = [
    "Ketu", "Venus", "Sun", "Moon", "Mars",
    "Rahu", "Jupiter", "Saturn", "Mercury"
] * 3

# House finder
def get_house(degree, cusps):
    for i in range(12):
        start = cusps[f"House_{i+1}"]["degree"]
        end = cusps[f"House_{(i+1)%12+1}"]["degree"]

        if start < end:
            if start <= degree < end:
                return i+1
        else:
            if degree >= start or degree < end:
                return i+1

    return None

# Get sub lord from cusp (approx link)
def get_cusp_sub_lord(house, cusps):
    return cusps[f"House_{house}"]["sub_lord"]

# MAIN FUNCTION
def get_full_significators(dob, time, lat, lon):
    planets = get_all_planets(dob, time)
    cusps = get_cusps(dob, time, lat, lon)

    result = {}

    for planet, data in planets.items():
        degree = data["degree"]
        nak = data["nakshatra"]

        # 1. Occupied house
        house = get_house(degree, cusps)

        # 2. Star lord
        nak_index = nakshatra_list.index(nak)
        star_lord = nakshatra_lords[nak_index]

        # 3. Sub lord (via house)
        sub_lord = get_cusp_sub_lord(house, cusps)

        result[planet] = {
            "house": house,
            "star_lord": star_lord,
            "sub_lord": sub_lord
        }

    return result


# TEST
if __name__ == "__main__":
    data = get_full_significators("1982-12-04", "14:15", 28.6139, 77.2090)
    print(data)