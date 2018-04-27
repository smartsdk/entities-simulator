from __future__ import print_function
from datetime import datetime
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
    entity = {
        "id": entity_id,
        "type": "AirQualityObserved",
        "address": {
            "streetAddress": "streetname",
            "addressLocality": "Antwerpen",
            "addressCountry": "BE"
        },
        "dateObserved": datetime.now().isoformat(),
        "location": {
            "type": "Point",
            "coordinates": random.choice(COORDS),
        },
        "source": "http://random.data.from.quantumleap",
        "precipitation": 0,
        "relativeHumidity": 0.54,
        "temperature": 12.2,
        "windDirection": 186,
        "windSpeed": 0.64,
        "airQualityLevel": "moderate",
        "airQualityIndex": 65,
        "reliability": 0.7,
        "CO": 500,
        "NO": 45,
        "NO2": 69,
        "NOx": 139,
        "SO2": 11,
        "CO_Level": "moderate",
        "refPointOfInterest": "28079004-Pza.deEspanya"
    }
    return entity


def get_attrs_to_update():
    attrs_to_update = {
        'dateObserved': {
            'type': 'DateTime',
            'value': datetime.now().isoformat()},
        "precipitation": {'type': 'Number', 'value': random.randint(0, 200)},
        "relativeHumidity": {'type': 'Number', 'value': random.random()},
        "temperature": {'type': 'Number', 'value': -20 + random.random() * 50},
        "windDirection": {'type': 'Number', 'value': random.random() * 200},
        "windSpeed": {'type': 'Number', 'value': random.random()},
        "airQualityLevel": {
            'type': 'Text',
            'value': random.choice(["poor", "moderate", "good"])},
        "airQualityIndex": {'type': 'Number', 'value': random.random() * 100},
        "reliability": {'type': 'Number', 'value': random.random()},
        "CO": {'type': 'Number', 'value': random.random() * 500},
        "NO": {'type': 'Number', 'value': random.random() * 100},
        "NO2": {'type': 'Number', 'value': random.random() * 100},
        "NOx": {'type': 'Number', 'value': random.random() * 150},
        "SO2": {'type': 'Number', 'value': random.random() * 20},
        "CO_Level": {
            'type': 'Text',
            'value': random.choice(["low", "moderate", "high"])},
    }
    return attrs_to_update
