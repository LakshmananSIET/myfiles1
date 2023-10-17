from picosdk.ps4000a import ps4000a as ps
from picosdk.functions import adc2mV, assert_pico_ok
import uuid
import re
# E0-4C-00-5B-1E-L

def get_mac():
    mac_addres =hex(uuid.getnode()).replace("0x",'').upper()
    mac='-'.join(mac_addres[i :i+2] for i in range(0,11,2))
    return mac

#connect and detect pico scope 
def connect_detect():
    mac_addres=get_mac()
    # print(mac_addres)
    result=re.search("E0-4C-00-5B-1E-L",mac_addres)
    if result:
        # print("okk")
        device=ps.open_unit()
        serial=device.info.serial.decode("utf-8")
        variant=device.info.variant.decode("utf-8")
        print(serial)
        print(variant)

connect_detect()    
