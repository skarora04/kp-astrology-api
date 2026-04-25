LITIGATION_HOUSES = [6, 8, 12]

def check_litigation(significators):
    result = {}

    for planet, info in significators.items():
        house = info["house"]

        if house in LITIGATION_HOUSES:
            result[planet] = "Litigation Possible"
        else:
            result[planet] = "Safe"

    return result