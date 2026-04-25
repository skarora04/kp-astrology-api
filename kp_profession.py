PROFESSION_HOUSES = [2, 6, 10]

def check_profession(significators):
    result = {}

    for planet, info in significators.items():
        house = info["house"]

        if house in PROFESSION_HOUSES:
            result[planet] = "Supports Profession"
        else:
            result[planet] = "No support"

    return result