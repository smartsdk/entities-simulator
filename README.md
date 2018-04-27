# NGSI Entities Simulator

[![License badge](https://img.shields.io/badge/license-Apache-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Docker Status](https://img.shields.io/docker/pulls/smartsdk/entities-simulator.svg)](https://hub.docker.com/r/smartsdk/entities-simulator/)

## Description

The goal of this project is to have a **QUICK** and **SIMPLE** way to inject [NGSIv2 Entities](https://orioncontextbroker.docs.apiary.io/#introduction/specification/terminology) to an [Orion Context Broker](http://fiware-orion.readthedocs.io/en/latest/index.html) instance. In particular, instances of [FIWARE DataModels](https://github.com/Fiware/dataModels).

This script first creates N of an specified NGSI Type, then keeps on making random updates to their attributes.

For more complex scenarios such as load testing, you may want to checkout [FIWARE Device Simulator](https://fiware-device-simulator.readthedocs.io).

## Getting Started

Using Python

```
# if necessary, pip install requests
ORION_URL=http://YOUR_ORION_IP_HERE:1026 python entities_simulator.py
```

Using Docker

```
$ docker run -ti --rm -e ORION_URL=http://127.0.0.1:1026 smartsdk/entities-simulator
```

## Configurable INPUT


| Environment Variable | DESCRIPTION |
| -------------------- | ----------- |
| **ORION_URL** | The url where to reach Orion to insert / update entities. |
| **FIWARE_SERVICE** | Optional. The [FIWARE-Service header](http://fiware-orion.readthedocs.io/en/latest/user/multitenancy/index.html) used in communications with Orion.|
| **FIWARE_SERVICEPATH** | Optional. |
| **ENTITY_TYPE** | The NGSI Entity Type you want to create Entities of. For now only `AirQualityObserved` and `TrafficFlowObserved` are supported |
| **ID_PREFIX** | Optional. Prefix for the ID of the created NGSI entities. |
| **N_ENTITIES** | The number of different entities of the specified type that will be created. |
| **SLEEP** | Number of seconds to wait between each interaction (insert or update) with Orion |

## Notes

This was setup in a very quick way to simulate `AirQualityObserved` and
`TrafficFlowObserved`.

This repo should **NOT** evolve by coding more python modules for the rest
of the dataModels. If anything, the random instances should be dynamically
generated from the schemas defined in the [FIWARE DataModels repo](https://github.com/Fiware/dataModels).

Finally, the simplicity of usage should remain the same. After all, we just
want to inject in Orion entities of a certain type with random updates. **Keep it simple**.
