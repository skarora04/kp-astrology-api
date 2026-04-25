CAREER_HOUSES = [2, 6, 10, 11]

def check_career(significators):
    result = {}

    for planet, info in significators.items():
        house = info["house"]

        if house in CAREER_HOUSES:
            result[planet] = "Supports Career"
        else:
            result[planet] = "No support"

    return result