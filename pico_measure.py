
import ctypes
import numpy as np
# from picosdk.ps4000a import ps4000a as ps
from picosdk.ps3000a import ps3000a as ps
import matplotlib.pyplot as plt
from picosdk.functions import adc2mV, assert_pico_ok
import pyqtgraph as pg
from PySide.QtGui import *
from PySide.QtCore import *

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
        status_pico=ps.close_unit(device)


        serial=device.info.serial.decode("utf-8")
        variant=device.info.variant.decode("utf-8")
        print(serial)
        print(variant)
        result1=re.search("CZ775/050",serial)
        if result1:
            #paste the detail in gui at label_pico
             print(serial)
        else:
            print("not find device")
            print(serial)
        

       




def measure():
         # Create chandle and status ready for use
        chandle = ctypes.c_int16()
        status = {}

        # Open 4000 series PicoScope
        # Returns handle to chandle for use in future API functions
        status["openunit"] = ps.ps4000aOpenUnit(ctypes.byref(chandle), None)

        try:
            assert_pico_ok(status["openunit"])
        except: # PicoNotOkError:
            powerStatus = status["openunit"]

            if powerStatus == 286:
                status["changePowerSource"] = ps.ps4000aChangePowerSource(chandle, powerStatus)
            elif powerStatus == 282:
                status["changePowerSource"] = ps.ps4000aChangePowerSource(chandle, powerStatus)
            else:
                raise

            assert_pico_ok(status["changePowerSource"])



        # Set up channel A
        # handle = chandle
        # channel = PS4000a_CHANNEL_A = 0
        # enabled = 1
        # coupling type = PS4000a_DC = 1
        # range = PS4000a_2V = 7
        # analogOffset = 0 V
        chARange = 7
        status["setChA"] = ps.ps4000aSetChannel(chandle, 0, 1, 1, chARange, 0)
        assert_pico_ok(status["setChA"])

        # Set up channel B
        # handle = chandle
        # channel = PS4000a_CHANNEL_B = 1
        # enabled = 1
        # coupling type = PS4000a_DC = 1
        # range = PS4000a_2V = 7
        # analogOffset = 0 V
        chBRange = 7
        status["setChB"] = ps.ps4000aSetChannel(chandle, 1, 1, 1, chBRange, 0)
        assert_pico_ok(status["setChB"])

        # Set up channel C
        # handle = chandle
        # channel = PS4000a_CHANNEL_C = 2
        # enabled = 1
        # coupling type = PS4000a_DC = 1
        # range = PS4000a_2V = 7
        # analogOffset = 0 V
        chCRange = 7
        status["setChC"] = ps.ps4000aSetChannel(chandle, 2, 0, 1, chCRange, 0)
        assert_pico_ok(status["setChC"])

        # Set up channel D
        # handle = chandle
        # channel = PS4000a_CHANNEL_D = 3
        # enabled = 1
        # coupling type = PS4000a_DC = 1
        # range = PS4000a_2V = 7
        # analogOffset = 0 V
        chDRange = 7
        status["setChD"] = ps.ps4000aSetChannel(chandle, 3, 0, 1, chDRange, 0)
        assert_pico_ok(status["setChD"])

        # Set up single trigger
        # handle = chandle
        # enabled = 1
        # source = PS4000a_CHANNEL_A = 0
        # threshold = 1024 ADC counts
        # direction = PS4000a_RISING = 2
        # delay = 0 s
        # auto Trigger = 1000 ms
        status["trigger"] = ps.ps4000aSetSimpleTrigger(chandle, 1, 0, 1024, 2, 0, 100)
        assert_pico_ok(status["trigger"])

        # Set number of pre and post trigger samples to be collected
        preTriggerSamples = 2500
        postTriggerSamples = 2500
        maxSamples = preTriggerSamples + postTriggerSamples

        # Get timebase information
        # WARNING: When using this example it may not be possible to access all Timebases as all channels are enabled by default when opening the scope.  
        # To access these Timebases, set any unused analogue channels to off.
        # handle = chandle
        # timebase = 8 = timebase
        # noSamples = maxSamples
        # pointer to timeIntervalNanoseconds = ctypes.byref(timeIntervalns)
        # pointer to maxSamples = ctypes.byref(returnedMaxSamples)
        # segment index = 0
        timebase = 8
        timeIntervalns = ctypes.c_float()
        returnedMaxSamples = ctypes.c_int32()
        oversample = ctypes.c_int16(1)
        status["getTimebase2"] = ps.ps4000aGetTimebase2(chandle, timebase, maxSamples, ctypes.byref(timeIntervalns), ctypes.byref(returnedMaxSamples), 0)
        assert_pico_ok(status["getTimebase2"])

        # Run block capture
        # handle = chandle
        # number of pre-trigger samples = preTriggerSamples
        # number of post-trigger samples = PostTriggerSamples
        # timebase = 3 = 80 ns = timebase (see Programmer's guide for mre information on timebases)
        # time indisposed ms = None (not needed in the example)
        # segment index = 0
        # lpReady = None (using ps4000aIsReady rather than ps4000aBlockReady)
        # pParameter = None
        status["runBlock"] = ps.ps4000aRunBlock(chandle, preTriggerSamples, postTriggerSamples, timebase, None, 0, None, None)
        assert_pico_ok(status["runBlock"])

        # Check for data collection to finish using ps4000aIsReady
        ready = ctypes.c_int16(0)
        check = ctypes.c_int16(0)
        while ready.value == check.value:
            status["isReady"] = ps.ps4000aIsReady(chandle, ctypes.byref(ready))

        # Create buffers ready for assigning pointers for data collection
        bufferAMax = (ctypes.c_int16 * maxSamples)()
        bufferAMin = (ctypes.c_int16 * maxSamples)() # used for downsampling which isn't in the scope of this example
        bufferBMax = (ctypes.c_int16 * maxSamples)()
        bufferBMin = (ctypes.c_int16 * maxSamples)() # used for downsampling which isn't in the scope of this example

        # Set data buffer location for data collection from channel A
        # handle = chandle
        # source = PS4000a_CHANNEL_A = 0
        # pointer to buffer max = ctypes.byref(bufferAMax)
        # pointer to buffer min = ctypes.byref(bufferAMin)
        # buffer length = maxSamples
        # segementIndex = 0
        # mode = PS4000A_RATIO_MODE_NONE = 0
        status["setDataBuffersA"] = ps.ps4000aSetDataBuffers(chandle, 0, ctypes.byref(bufferAMax), ctypes.byref(bufferAMin), maxSamples, 0 , 0)
        assert_pico_ok(status["setDataBuffersA"])

        # Set data buffer location for data collection from channel B
        # handle = chandle
        # source = PS4000a_CHANNEL_B = 1
        # pointer to buffer max = ctypes.byref(bufferBMax)
        # pointer to buffer min = ctypes.byref(bufferBMin)
        # buffer length = maxSamples
        # segementIndex = 0
        # mode = PS4000A_RATIO_MODE_NONE = 0
        status["setDataBuffersB"] = ps.ps4000aSetDataBuffers(chandle, 1, ctypes.byref(bufferBMax), ctypes.byref(bufferBMin), maxSamples, 0 , 0)
        assert_pico_ok(status["setDataBuffersB"])

        # create overflow loaction
        overflow = ctypes.c_int16()
        # create converted type maxSamples
        cmaxSamples = ctypes.c_int32(maxSamples)

        # Retried data from scope to buffers assigned above
        # handle = chandle
        # start index = 0
        # pointer to number of samples = ctypes.byref(cmaxSamples)
        # downsample ratio = 0
        # downsample ratio mode = PS4000a_RATIO_MODE_NONE
        # pointer to overflow = ctypes.byref(overflow))
        status["getValues"] = ps.ps4000aGetValues(chandle, 0, ctypes.byref(cmaxSamples), 0, 0, 0, ctypes.byref(overflow))
        assert_pico_ok(status["getValues"])


        # find maximum ADC count value
        # handle = chandle
        # pointer to value = ctypes.byref(maxADC)
        maxADC = ctypes.c_int16(32767)

        # convert ADC counts data to mV
        adc2mVChAMax =  adc2mV(bufferAMax, chARange, maxADC)
        adc2mVChBMax =  adc2mV(bufferBMax, chBRange, maxADC)

        # Create time data
        time = np.linspace(0, (cmaxSamples.value - 1) * timeIntervalns.value, cmaxSamples.value)

        # plot data from channel A and B
        # plt.plot(time, adc2mVChAMax[:])
        # plt.plot(time, adc2mVChBMax[:])
        # plt.xlabel('Time (ns)')
        # plt.ylabel('Voltage (mV)')
        # plt.show()

        # Stop the scope
        # handle = chandle
        status["stop"] = ps.ps4000aStop(chandle)
        assert_pico_ok(status["stop"])

        # Close unitDisconnect the scope
        # handle = chandle
        status["close"] = ps.ps4000aCloseUnit(chandle)
        assert_pico_ok(status["close"])

        # display status returns
        print(status)
        
                
        time_a =[]
        for value in time:
            time_a.append(int(value)/1e9)

        volts_A = []
        for value in adc2mVChAMax:
            value = value/1e3
            volts_A.append(value)
        volts_B = []
        for value in adc2mVChBMax:
            value = value/1e3
            volts_B.append(value)

        

        # graphWidget_current = pg.PlotWidget()
        # graphWidget_current.resize(1620,380)  

        # graphWidget_current.move(30,10)
        # graphWidget_current.showGrid(x=False,y=False)
        # graphWidget_current.setBackground((0,0,0))

        # graphWidget_current.setLabel('left', text='Current', units='A', **styles)
        # graphWidget_current.getAxis("left").tickFont = font
        # graphWidget_current.getAxis("left").setPen(QColor(255,255,255))


        # graphWidget_current.setLabel('bottom', text='Time Scale', units='S', **styles)
        # graphWidget_current.getAxis("bottom").tickFont = font
        # graphWidget_current.getAxis("bottom").setPen(QColor(255,255,255))
        # graphWidget_current.setMenuEnabled(False)
        # graphWidget_current.hideButtons()

        # graphWidget_current.setXRange(x_min,x_max,0)
        # graphWidget_current.setYRange(y_min,y_max)
        # graphWidget_current.plot(time,current_scaled,pen=pg.mkPen((255,255,0), width=2),clear=False)

        print(time_a)
        print(volts_A)
        print(volts_B)




connect_detect()    
# measure()
