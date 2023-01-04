import re
import subprocess
from influxdb import InfluxDBClient

response = subprocess.Popen('sudo apt-get update -y && sudo apt-get upgrade -y', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
#print(response)
upgraded = re.search('(.*?)\s+upgraded,', response, re.MULTILINE)
#print(upgraded)
upgraded = upgraded.group(1)
#print(upgraded)
upgrade_data = [
    {
        "measurement" : "upgrades",
        "tags" : {
            "host": "RaspberryPi-1"
        },
        "fields" : {
            "upgraded": float(upgraded)
        }
    }
]
#print(upgrade_data)
client = InfluxDBClient('localhost', 8086, '********', '********', '********')
#print(client)
client.write_points(upgrade_data)
client.close()