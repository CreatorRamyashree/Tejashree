from datetime import datetime

def calculate_daylight_duration(sunrise, sunset):
    sunrise_time = datetime.strptime(sunrise, "%H:%M")
    sunset_time = datetime.strptime(sunset, "%H:%M")
    daylight_duration = sunset_time - sunrise_time
    return daylight_duration


locations = {
    "Kinshasa": {"sunrise": "06:00", "sunset": "18:00"},
    "Lubumbashi": {"sunrise": "05:45", "sunset": "18:15"},
}

print("Daylight Duration for Summer in Congo:")
for city, times in locations.items():
    duration = calculate_daylight_duration(times["sunrise"], times["sunset"])
    print(f"{city}: {duration}")
