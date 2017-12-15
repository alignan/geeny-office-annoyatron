import json
import time
import requests

# Simple application which listens to messages and post to a slack channel
# It retrieves the last message only
URL = 'http://1ffbd1bc-5530-40f4-b7b7-6d1ead22f915-v-12.formula.geeny.io/last-msg'

# Dictiionary 
params = dict(
    userId='',
    thingId='',
    messageTypeId='',
    data=''
)

#{"userId":"24fd7855-77f2-4852-9979-564b200eeb67","thingId":"e705edaa-329a-42b7-96a9-64359d8859db",
#"messageTypeId":"54121087-14f1-4c2a-835f-117681618cc9","data":"{\"CurrentSummationDelivered\":null,\"InstantaneousDemand\":null,\"MeasuredValue_Illuminance\":null,\"MeasuredValue_Temperature\":\"25.3 C\",\"NetworkLinkAddress\":\"\",\"NetworkLinkDevice\":\"GW\",\"NetworkLinkFer\":\"4 %\",\"NetworkLinkPer\":\"0 %\",\"NetworkLinkRssi\":\"RSSI: -79.0 dBm\",\"NetworkLinkStrength\":\"96 %\",\"Occupancy\":null,\"OnOff\":null,\"PrimarySwVersion\":\"3.4.9\",\"ZoneStatus\":\"closed\"}","created":"2017-12-15T12:23:29.103Z"}


def main():
    while(True):
        try:
            resp = requests.get(url=URL)
            print resp.text
            # json.dumps(resp, indent=4, sort_keys=True) 

        except Exception, e:
            print str(e)
            pass
        time.sleep(0.5)

if __name__ == '__main__':
    main()






resp = requests.get(url=url, params=params)
