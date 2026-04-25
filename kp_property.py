PROPERTY_HOUSES = [4, 11]

def check_property(significators):
    result = {}

    for planet, info in significators.items():
        house = info["house"]

        if house in PROPERTY_HOUSES:
            result[planet] = "Property Gain"
        else:
            result[planet] = "No property support"

    return result