import swisseph as swe

swe.set_ephe_path('.')
swe.set_sid_mode(swe.SIDM_KRISHNAMURTI)

# 👉 USER INPUT
year = 1982
month = 12
day = 4
hour = 14.25

lat = 28.6139
lon = 77.2090

# 👉 Julian Day
jd = swe.julday(year, month, day, hour)

# 👉 Cusps (Sidereal KP)
cusps, ascmc = swe.houses_ex(jd, lat, lon, b'P', swe.FLG_SIDEREAL)

# Nakshatra + Lords
nakshatras = [
    "Ashwini","Bharani","Krittika","Rohini","Mrigashira","Ardra",
    "Punarvasu","Pushya","Ashlesha","Magha","Purva Phalguni",
    "Uttara Phalguni","Hasta","Chitra","Swati","Vishakha",
    "Anuradha","Jyeshtha","Mula","Purva Ashadha","Uttara Ashadha",
    "Shravana","Dhanishta","Shatabhisha","Purva Bhadrapada",
    "Uttara Bhadrapada","Revati"
]

nak_lords = [
    "Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury",
    "Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury",
    "Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury"
]

# Dasha
dasha_order = ["Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury"]
dasha_years = {
    "Ketu":7,"Venus":20,"Sun":6,"Moon":10,
    "Mars":7,"Rahu":18,"Jupiter":16,"Saturn":19,"Mercury":17
}

TOTAL_MIN = 800

# Sub sizes
sub_sizes = {p:(dasha_years[p]/120)*TOTAL_MIN for p in dasha_order}

# 🔰 Function: Degree → Sub-Lord
def get_sub(degree):
    nak_len = 13 + 20/60
    nak_index = int(degree / nak_len)

    star = nak_lords[nak_index]

    nak_start = nak_index * nak_len
    pos = (degree - nak_start) * 60

    start_index = dasha_order.index(star)
    seq = dasha_order[start_index:] + dasha_order[:start_index]

    cum = 0
    for p in seq:
        cum += sub_sizes[p]
        if pos <= cum:
            return star, p

    return star, seq[-1]

# 🔰 7th Cusp
cusp7 = cusps[6]

star, sub = get_sub(cusp7)

# 🔰 Simple KP Rule (Marriage)
significators = {
    "Sun":[1,10],"Moon":[4,5],"Mars":[3,6],
    "Mercury":[3,11],"Jupiter":[2,5,11],
    "Venus":[2,7,11],"Saturn":[6,10],
    "Rahu":[6,8,12],"Ketu":[8,12]
}

houses = significators.get(sub, [])

good = [2,7,11]
bad = [6,8,12]

if any(h in bad for h in houses):
    result = "❌ NO / Delay"
elif any(h in good for h in houses):
    result = "✅ YES"
else:
    result = "Neutral"

# 🔰 OUTPUT
print("7th Cusp Degree:", round(cusp7,2))
print("Star Lord:", star)
print("Sub-Lord:", sub)
print("Houses:", houses)
print("Prediction:", result)