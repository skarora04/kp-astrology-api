from kp_significator import get_full_significators
from kp_marriage import check_marriage
from kp_dasha import get_current_mahadasha, get_bhukti_duration, get_antara_duration


def get_marriage_timing(dob, time, lat, lon):
    sig = get_full_significators(dob, time, lat, lon)

    marriage = check_marriage(sig)

    # Support planets
    support_planets = [
        p for p, status in marriage.items()
        if status == "Strong Marriage Support"
    ]

    md, balance = get_current_mahadasha(dob, time)
    bhukti_list = get_bhukti_duration(md)

    result = []

    for b in bhukti_list:
        bhukti_planet = b["bhukti"].split("/")[1]

        if bhukti_planet in support_planets:

            antara = get_antara_duration(md, bhukti_planet)

            result.append({
                "bhukti": b["bhukti"],
                "duration": b["years"],
                "antara": antara
            })

    return {
        "current_md": md,
        "support_planets": support_planets,
        "favourable": result
    }


# 🔹 TEST
if __name__ == "__main__":
    data = get_marriage_timing("1982-12-04", "14:15", 28.6139, 77.2090)

    print("Current MD:", data["current_md"])
    print("Support Planets:", data["support_planets"])

    print("\n=== FAVOURABLE PERIODS ===\n")

    for item in data["favourable"]:
        print(item["bhukti"], "→", item["duration"], "years")

        print("  Antara:")
        for a in item["antara"]:
            print("   ", a["antara"], "→", a["years"])
        print()