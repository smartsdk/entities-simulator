from __future__ import print_function
from datetime import datetime, timedelta
import random

COORDS = [
    [51.235170, 4.421283],
    [51.233103, 4.423617],
    [51.257595, 4.432838],
    [51.260580, 4.426038],
    [51.208525, 4.437985],
    [51.210266, 4.425305],
    [51.204714, 4.416675],
    [51.208948, 4.418556],
    [51.217179, 4.341202],
    [51.218305, 4.336690],
]


def create_entity(entity_id):
    pivot = 10
    date_from = (datetime.now() - timedelta(seconds=pivot)).isoformat()
    date_to = datetime.now().isoformat()
    intensity = random.randint(0, pivot)
    avg_hw_time = 0 if intensity == 0 else float(pivot/intensity)
    avg_speed = 1 + random.random() * 250
    avg_length = 2 + random.random() * 8

    entity = {
        "id": entity_id,
        "type": "TrafficFlowObserved",
        "laneId": random.randint(0, 1),
        "address": {
            "streetAddress": "streetname",
            "addressLocality": "Antwerpen",
            "addressCountry": "BE"
        },
        "location": {
            "type": "LineString",
            "coordinates": random.choice(COORDS),
        },
        # Not supported by orion
        # "dateObserved": "2016-12-07T11:10:00/2016-12-07T11:15:00"
        "dateObservedFrom": date_from,
        "dateObservedTo": date_to,
        # avg time between two consecutive vehicles
        "averageHeadwayTime": avg_hw_time,
        "intensity": intensity,        # Total number of vehicles detected
        # "capacity": 0.76,            # Not in spec, only in example :/
        "averageVehicleSpeed": avg_speed,    # km/h
        "averageVehicleLength": avg_length,  # meters
        "reversedLane": False,
        "laneDirection": "forward",
    }
    return entity


def get_attrs_to_update():
    pivot = 10
    date_from = (datetime.now() - timedelta(seconds=pivot)).isoformat()
    date_to = datetime.now().isoformat()
    intensity = random.randint(0, pivot)
    avg_hw_time = 0 if intensity == 0 else float(pivot/intensity)
    avg_speed = 10 + random.random() * 90
    avg_length = 2 + random.random() * 8

    attrs_to_update = {
        'dateObservedFrom': {'type': 'DateTime', 'value': date_from},
        'dateObservedTo': {'type': 'DateTime', 'value': date_to},
        'intensity': {'type': 'Number', 'value': intensity},
        'averageHeadwayTime': {'type': 'Number', 'value': avg_hw_time},
        'averageVehicleSpeed': {'type': 'Number', 'value': avg_speed},
        'averageVehicleLength': {'type': 'Number', 'value': avg_length},
    }
    return attrs_to_update
