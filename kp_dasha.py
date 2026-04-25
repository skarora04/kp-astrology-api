from kp_planets_full import get_all_planets

# Vimshottari Dasha Years
DASHA_YEARS = {
    "Ketu": 7,
    "Venus": 20,
    "Sun": 6,
    "Moon": 10,
    "Mars": 7,
    "Rahu": 18,
    "Jupiter": 16,
    "Saturn": 19,
    "Mercury": 17
}

# Nakshatra Lords
NAK_LORDS = [
    "Ketu", "Venus", "Sun", "Moon", "Mars",
    "Rahu", "Jupiter", "Saturn", "Mercury"
] * 3

NAK_LIST = [
    "Ashwini","Bharani","Krittika","Rohini","Mrigashira",
    "Ardra","Punarvasu","Pushya","Ashlesha","Magha",
    "Purva Phalguni","Uttara Phalguni","Hasta","Chitra",
    "Swati","Vishakha","Anuradha","Jyeshtha","Mula",
    "Purva Ashadha","Uttara Ashadha","Shravana","Dhanishta",
    "Shatabhisha","Purva Bhadrapada","Uttara Bhadrapada","Revati"
]

# 🔹 STEP 1: Mahadasha
def get_current_mahadasha(dob, time):
    planets = get_all_planets(dob, time)

    moon = planets["Moon"]
    nak = moon["nakshatra"]
    degree = moon["degree"]

    index = NAK_LIST.index(nak)
    lord = NAK_LORDS[index]

    deg_in_nak = degree % 13.333333
    balance = (13.333333 - deg_in_nak) / 13.333333

    total_years = DASHA_YEARS[lord]
    balance_years = round(total_years * balance, 2)

    return lord, balance_years


# 🔹 STEP 2: Bhukti Order
def get_bhukti_sequence(mahadasha):
    seq = ["Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury"]
    i = seq.index(mahadasha)
    return seq[i:] + seq[:i]


# 🔹 STEP 3: Bhukti Duration
def get_bhukti_duration(mahadasha):
    seq = get_bhukti_sequence(mahadasha)
    md_years = DASHA_YEARS[mahadasha]

    result = []
    for b in seq:
        duration = (md_years * DASHA_YEARS[b]) / 120
        result.append({
            "bhukti": f"{mahadasha}/{b}",
            "years": round(duration, 2)
        })

    return result


# 🔹 STEP 4: Antara Duration
def get_antara_duration(mahadasha, bhukti):
    seq = ["Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury"]
    i = seq.index(bhukti)
    antara_seq = seq[i:] + seq[:i]

    md_years = DASHA_YEARS[mahadasha]
    b_years = DASHA_YEARS[bhukti]

    result = []

    for a in antara_seq:
        duration = (md_years * b_years * DASHA_YEARS[a]) / (120 * 120)

        result.append({
            "antara": f"{mahadasha}/{bhukti}/{a}",
            "years": round(duration, 3)
        })

    return result


# 🔹 TEST
if __name__ == "__main__":
    md, bal = get_current_mahadasha("1982-12-04", "14:15")

    print("MD:", md)
    print("Balance:", bal)

    bhukti = get_bhukti_duration(md)

    for b in bhukti:
        print(b)

    print("\nAntara Example:\n")
    antara = get_antara_duration(md, bhukti[0]["bhukti"].split("/")[1])

    for a in antara:
        print(a)