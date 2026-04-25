HEALTH_HOUSES = [1, 6, 8, 12]

def check_health(significators):
    result = {}

    for planet, info in significators.items():
        house = info["house"]

        if house in HEALTH_HOUSES:
            result[planet] = "Health Issues Possible"
        else:
            result[planet] = "Stable"

    return result