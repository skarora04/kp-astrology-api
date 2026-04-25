from fastapi import FastAPI, Query
import requests
import swisseph as swe

from fastapi.middleware.cors import CORSMiddleware

import os
from fastapi.staticfiles import StaticFiles
from kp_timing import get_marriage_timing
from kp_chart import generate_kp_chart

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 STATIC FILES (IMPORTANT FOR WORDPRESS)
app.mount("/static", StaticFiles(directory="D:/static"), name="static")


# 🔹 Convert Place → Lat/Lon
def get_lat_lon(place: str):
    try:
        url = f"https://nominatim.openstreetmap.org/search?format=json&q={place}"

        headers = {
            "User-Agent": "kp-astrology-app"
        }

        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

        if len(data) > 0:
            return float(data[0]["lat"]), float(data[0]["lon"])

    except:
        pass

    return None, None


# 🔹 Home route
@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "KP Astrology API Running 🚀"
    }


# 🔹 Marriage Timing API
@app.get("/marriage-timing")
def marriage_timing(
    name: str = Query(None),
    dob: str = Query(...),
    time: str = Query(...),
    place: str = Query(...)
):

    lat, lon = get_lat_lon(place)

    if lat is None or lon is None:
        return {"error": "Invalid birth place"}

    data = get_marriage_timing(dob, time, lat, lon)

    return {
        "input": {
            "name": name,
            "dob": dob,
            "time": time,
            "place": place,
            "lat": lat,
            "lon": lon
        },
        "result": data
    }


# 🔥 KP CHART (WORDPRESS READY VERSION)
@app.get("/kp-chart")
def kp_chart_api(
    dob: str = Query(...),
    time: str = Query(...),
    place: str = Query("Delhi")
):

    # 🔹 Convert date-time → Julian Day
    year, month, day = map(int, dob.split("-"))
    hour, minute = map(int, time.split(":"))

    jd = swe.julday(year, month, day, hour + minute / 60)

    # 🔹 Real planets from Swiss Ephemeris
    planets_list = {
        "Sun": swe.SUN,
        "Moon": swe.MOON,
        "Mars": swe.MARS,
        "Mercury": swe.MERCURY,
        "Jupiter": swe.JUPITER,
        "Venus": swe.VENUS,
        "Saturn": swe.SATURN
    }

    planets = {}

    for name, p in planets_list.items():
        pos = swe.calc_ut(jd, p)[0][0]
        planets[name] = {"degree": pos}

    # 🔥 Generate chart image (local file)
    file_name = generate_kp_chart(planets)

    # 🔥 Convert to URL for WordPress
    chart_url = f"http://127.0.0.1:8000/static/{file_name}"

    return {
        "input": {
            "dob": dob,
            "time": time,
            "place": place
        },
        "chart": chart_url,
        "planets": planets
    }