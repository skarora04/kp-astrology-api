WEALTH_HOUSES = [2, 6, 10, 11]

def check_wealth(significators):
    result = {}

    for planet, info in significators.items():
        house = info["house"]

        if house in WEALTH_HOUSES:
            result[planet] = "Wealth Support"
        else:
            result[planet] = "Weak Financial Support"

    return result