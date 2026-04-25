MARRIAGE_HOUSES = [2, 7, 11]

def check_marriage(significators):
    result = {}

    for planet, info in significators.items():
        houses = []

        # 1. Planet house
        houses.append(info["house"])

        # 2. Star lord house
        star_lord = info["star_lord"]
        if star_lord in significators:
            houses.append(significators[star_lord]["house"])

        # 3. Sub lord house (FINAL DECISION)
        sub_lord = info["sub_lord"]
        if sub_lord in significators:
            houses.append(significators[sub_lord]["house"])

        # FINAL RESULT
        if any(h in MARRIAGE_HOUSES for h in houses):
            result[planet] = "Strong Marriage Support"
        else:
            result[planet] = "No Marriage Promise"

    return result