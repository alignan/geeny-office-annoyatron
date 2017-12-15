## Account

````bash
elias+delta@superscale.io
deltadelta
````

## About the devices itself

### Things
`GET https://labs.geeny.io/things/api/v1/things/`

````bash
{
    "meta": {
        "offset": 0,
        "limit": 50
    },
    "data": [
        {
            "id": "e705edaa-329a-42b7-96a9-64359d8859db",
            "name": "Window Sensor",
            "serial_number": "0015bc001e00322d",
            "thing_type": "d6e479ea-c4fc-4204-9534-fc310a54ecd2",
            "created": "2017-12-15T09:07:27.902Z"
        },
        {
            "id": "953fc4fa-1a64-4cd8-ba9d-b43a3e095360",
            "name": "Power Outlet",
            "serial_number": "0015bc002f00208d",
            "thing_type": "d5d51e47-34d0-418d-afe5-404b73c512b5",
            "created": "2017-12-15T09:09:25.826Z"
        },
        {
            "id": "8e227358-e309-4213-99de-89e3e4f2f3f8",
            "name": "Motion Sensor",
            "serial_number": "0015bc001a0069a1",
            "thing_type": "db5c4e3e-4dab-4526-bd90-392971369b83",
            "created": "2017-12-15T09:12:13.940Z"
        },
        {
            "id": "2c662faa-7a69-4d94-ae81-b6ff9f2dd664",
            "name": "Bulb",
            "serial_number": "00158d000150c256",
            "thing_type": "2db4d5b5-44d1-4f03-9aff-564a2785e8ff",
            "created": "2017-12-15T09:13:01.866Z"
        }
    ]
}
````

These are my `ThingTypes`:

Window sensor:
`GET https://labs.geeny.io/things/api/v1/thingTypes/d6e479ea-c4fc-4204-9534-fc310a54ecd2/resources`
````bash
{
    "meta": {
        "offset": 0,
        "limit": 50
    },
    "data": [
        {
            "id": "86099f21-d026-44ae-8400-50e425add0f8",
            "uri": "develco/data",
            "method": "pub",
            "message_type": "54121087-14f1-4c2a-835f-117681618cc9"
        }
    ]
}
````

Power Outlet:
`GET https://labs.geeny.io/things/api/v1/thingTypes/d5d51e47-34d0-418d-afe5-404b73c512b5/resources`

````bash
{
    "meta": {
        "offset": 0,
        "limit": 50
    },
    "data": [
        {
            "id": "24e343eb-ac59-4062-b4a2-7be66d38c7df",
            "uri": "develco/data",
            "method": "pub",
            "message_type": "54121087-14f1-4c2a-835f-117681618cc9"
        },
        {
            "id": "8229d482-9a72-4da8-a73e-58eaecd27d65",
            "uri": "develco/command",
            "method": "sub",
            "message_type": "5d610b4f-5532-4e24-b46f-c355bdd99958"
        }
    ]
}
````

Motion Sensor:
`GET https://labs.geeny.io/things/api/v1/thingTypes/db5c4e3e-4dab-4526-bd90-392971369b83/resources`
````bash
{
    "meta": {
        "offset": 0,
        "limit": 50
    },
    "data": [
        {
            "id": "2a04e8b6-0c85-4ccf-9df9-d1f2e50b8ffb",
            "uri": "develco/data",
            "method": "pub",
            "message_type": "54121087-14f1-4c2a-835f-117681618cc9"
        }
    ]
}
````

Bulb:
`GET https://labs.geeny.io/things/api/v1/thingTypes/db5c4e3e-4dab-4526-bd90-392971369b83/resources`
````bash
{
    "meta": {
        "offset": 0,
        "limit": 50
    },
    "data": [
        {
            "id": "2a04e8b6-0c85-4ccf-9df9-d1f2e50b8ffb",
            "uri": "develco/data",
            "method": "pub",
            "message_type": "54121087-14f1-4c2a-835f-117681618cc9"
        }
    ]
}
````