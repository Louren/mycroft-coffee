import requests
import sys

try:
    # TODO: Fix turnOnAndMakeEspresso routine on Arduino
    r1 = requests.get(f"http://192.168.2.251/routines/turnOn",timeout=5)
    r1.raise_for_status()

    r2 = requests.get(f"http://192.168.2.251/button/espresso",timeout=5)
    r2.raise_for_status()
except requests.exceptions.Timeout:
    print("timeout")
except:
    e = sys.exc_info()[0]
    print("other" )
    print(e)