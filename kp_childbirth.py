# Childbirth houses
CHILD_HOUSES = [2, 5, 11]

def check_childbirth(significators):
    result = {}

    for planet, info in significators.items():
        house = info["house"]

        if house in CHILD_HOUSES:
            result[planet] = "Supports Childbirth"
        else:
            result[planet] = "No support"

    return result