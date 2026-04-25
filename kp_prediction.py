from kp_significator import get_full_significators

# Marriage houses
MARRIAGE_HOUSES = [2, 7, 11]

def check_marriage(dob, time, lat, lon):
    data = get_full_significators(dob, time, lat, lon)

    result = {}

    for planet, info in data.items():
        house = info["house"]

        # Simple rule: agar house match kare
        if house in MARRIAGE_HOUSES:
            result[planet] = "Supports Marriage"
        else:
            result[planet] = "No direct support"

    return result


# TEST
if __name__ == "__main__":
    data = check_marriage("1982-12-04", "14:15", 28.6139, 77.2090)
    print(data)