# Education houses
EDUCATION_HOUSES = [2, 4, 5, 9]

def check_education(significators):
    result = {}

    for planet, info in significators.items():
        house = info["house"]

        if house in EDUCATION_HOUSES:
            result[planet] = "Supports Education"
        else:
            result[planet] = "No support"

    return result