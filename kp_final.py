# FINAL KP Prediction Engine

# Example input (you will later connect real data)
cusp_sub_lord = "Venus"

# Corrected significator logic (simplified but closer to KP)
significators = {
    "Sun": [1, 10],
    "Moon": [4, 5],
    "Mars": [3, 6],
    "Mercury": [3, 11],
    "Jupiter": [2, 5, 11],
    "Venus": [2, 7, 11],
    "Saturn": [6, 10],
    "Rahu": [6, 8, 12],
    "Ketu": [8, 12]
}

houses = significators.get(cusp_sub_lord, [])

# Marriage houses
good = [2, 7, 11]
bad = [6, 8, 12]

# FINAL LOGIC
if any(h in bad for h in houses):
    result = "❌ NO / Delay / Obstacle"
elif all(h in good for h in houses):
    result = "✅ STRONG YES (Certain Marriage)"
elif any(h in good for h in houses):
    result = "⚖️ YES (with effort/delay)"
else:
    result = "❓ Neutral"

# Output
print("Cusp Sub-Lord:", cusp_sub_lord)
print("Signifies Houses:", houses)
print("Final Prediction:", result)