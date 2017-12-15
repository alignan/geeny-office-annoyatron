import json
import time
import requests

# Simple application which listens to messages and post to a slack channel
# It retrieves the last message only

GEENY_URL = 'http://1ffbd1bc-5530-40f4-b7b7-6d1ead22f915-v-21.formula.geeny.io/last-msg'
IFTTT_URL = 'https://maker.ifttt.com/trigger/window/with/key/fIqVcICnrftFtxYYO4QfPHHFWirpcDHdVcWdvz5lC5X' 

WINDOW_SENSOR_ID = 'e705edaa-329a-42b7-96a9-64359d8859db'

# Dictionary for parsing the message 
params = dict(
    userId='',
    thingId='',
    messageTypeId='',
    data=''
)

# Dictionary to load the data content
things = dict(
    CurrentSummationDelivered = '',
    InstantaneousDemand = '',
    MeasuredValue_Illuminance = '',
    MeasuredValue_Temperature = '',
    NetworkLinkAddress = '',
    NetworkLinkDevice = '',
    NetworkLinkFer = '',
    NetworkLinkPer = '',
    NetworkLinkRssi = '',
    NetworkLinkStrength = '',
    Occupancy = '',
    OnOff = '',
    PrimarySwVersion = '',
    ZoneStatus = '',
    created = ''
)

def post_to_ifttt(status):
    try:
        resp = requests.post(url=IFTTT_URL, data = {'value1':status})
    except Exception, e:
        print str(e)
        pass

def main():
    while(True):
        try:
            resp = requests.get(url=GEENY_URL, params=params)
            geeny = json.loads(resp.text)
            # print json.dumps(geeny, indent=4, sort_keys=True)
            if geeny['thingId'] == WINDOW_SENSOR_ID:
                # print geeny['data']
                data = json.loads(geeny['data'])
                print json.dumps(data, indent=4, sort_keys=True)
                if str(data['ZoneStatus']) is not "null":
                    post_to_ifttt(data['ZoneStatus'])

        except Exception, e:
            print str(e)
            pass
        time.sleep(0.2)

if __name__ == '__main__':
    main()
