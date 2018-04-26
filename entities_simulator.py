"""
See README.md for instructions.
"""
from __future__ import print_function
import json
import os
import pprint
import requests
import time


################################################################################
# INPUT
################################################################################
ORION_URL = os.environ.get('ORION_URL', 'http://0.0.0.0:1026')
FIWARE_SERVICE = os.environ.get('FIWARE_SERVICE', None)
FIWARE_SERVICEPATH = os.environ.get('FIWARE_SERVICEPATH', '/')

ENTITY_TYPE = os.environ.get('ENTITY_TYPE', 'AirQualityObserved')
ID_PREFIX = os.environ.get('ID_PREFIX', ENTITY_TYPE.lower())
N_ENTITIES = int(os.environ.get('N_ENTITIES', 9))

SLEEP = int(os.environ.get('SLEEP', 3))


################################################################################
# HELPERS
################################################################################
HEADERS = {}
if FIWARE_SERVICE is not None:
    HEADERS['Fiware-Service'] = FIWARE_SERVICE
    HEADERS['Fiware-ServicePath'] = FIWARE_SERVICEPATH
HEADERS_PUT = HEADERS.copy()
HEADERS_PUT['Content-Type'] = 'application/json'


def insert_entities(orion_url, entities, sleep):
    for e in entities:
        time.sleep(sleep)
        url = '{}/v2/entities?options=keyValues'.format(orion_url)
        r = requests.post(url, data=json.dumps(e), headers=HEADERS_PUT)
        if not r.ok:
            if "Already Exists" in r.text:
                print("Already exists: {}".format(e['id']))
                continue
            raise RuntimeError(r.text)
        print("Inserted: {}".format(json.dumps(e)))


def update_entity(orion_url, entity, attrs_to_update):
    url = '{}/v2/entities/{}/attrs'.format(orion_url, entity['id'])
    r = requests.patch(url, data=json.dumps(attrs_to_update),
                       headers=HEADERS_PUT)
    if not r.ok:
        raise RuntimeError(r.text)
    print("Updated {} with {}".format(entity['id'], attrs_to_update))


def iter_entities(n_entities, create_entity):
    for n in range(n_entities):
        entity_id = '{}_{}'.format(ID_PREFIX, n)
        entity = create_entity(entity_id)
        yield entity


################################################################################
# MAIN
################################################################################
if __name__ == '__main__':
    print("Starting 'Entities Simulator' with options:")
    pprint.pprint(locals())

    if ENTITY_TYPE == 'AirQualityObserved':
        from air_quality_observed import create_entity
        from air_quality_observed import get_attrs_to_update
    elif ENTITY_TYPE == 'TrafficFlowObserved':
        from traffic_flow_observed import create_entity
        from traffic_flow_observed import get_attrs_to_update
    else:
        print("{} is not a supported ENTITY_TYPE. Check the docs!")

    entities = list(iter_entities(N_ENTITIES, create_entity))
    insert_entities(ORION_URL, entities, SLEEP)

    while True:
        for e in entities:
            time.sleep(SLEEP)
            attrs_to_update = get_attrs_to_update()
            update_entity(ORION_URL, e, attrs_to_update)
