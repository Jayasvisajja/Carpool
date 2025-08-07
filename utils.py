import re
from math import radians, sin, cos, sqrt, atan2
from datetime import datetime, timedelta

# Static location coordinates
location_coords = {
    "VIT AP(collage campus)": (16.5083, 80.6412),
    "Vijayawada airport": (16.5304, 80.7968),
    "VIT AP Bus stop": (16.5100, 80.6420),
    "Vijayawada Bus Station": (16.5184, 80.6305),
    "Vijayawada Railway Station": (16.5122, 80.6291),
}

def validate_email(email):
    return re.match(r"^[\w\.-]+@vitapstudent\.ac\.in$", email)

def validate_phone(phone):
    return re.match(r"^\d{10}$", phone)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # meters
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)

    a = sin(dphi/2)**2 + cos(phi1) * cos(phi2) * sin(dlambda/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c  # Distance in meters

def time_within_30min(time1, time2):
    fmt = "%H:%M"
    t1 = datetime.strptime(time1, fmt)
    t2 = datetime.strptime(time2, fmt)
    return abs((t1 - t2).total_seconds()) <= 1800  # 30 min
