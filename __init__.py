# Communication module header file of ClientBridge for communication with
#  LXI device.
#
#  Copyright (C) 1988 - 2020, Pickering Interfaces ltd.
#
#  Support: support@pickeringswitch.com
#  Supported OS: Mac OS 10.9.2, Windows XP/7/8/10, Linux
#
# Licence:
# This agreement is made between Pickering Interfaces Ltd ("Pickering") and you,
# the person who makes use of Pickering software products ("You"). You must agree
# all terms in this agreement in order to use Pickering software legally. If you
# don't agree all terms in the agreement, please don't use Pickering software, and
# delete all related files from your computer.
#
# 1. OWNERSHIP: Pickering software is fully owned by Pickering, this license
# agreement doesn't change the ownership.
#
# 2. LICENSE: Pickering grants You the license to use Pickering software, free of
# charge, if you accept all the conditions listed in this agreement. "Use" means
# loading the product to CPU, memory, and/or other storage on your computer.
#
# 3. CONDITIONS: To be licensed to use Pickering software, You must:
#    a) Not modify any part of Pickering software;
#    b) Agree to release Pickering from all liabilities caused directly or
#       indirectly by using Pickering software;
#    c) Agree not to attempt to reverse engineer, de-compile or use any other
#       tools to extract source code from Pickering Software.
#
# 4. CONSEQUENTIAL LICENSES: Some functions of Pickering software requires
# additional licenses to fully operate. Pickering accepts no responsibility for
# the provision of said licenses.
#
# 5. REDISTRIBUTION:. You may freely re-distribute Pickering software in any way
# unless explicitly stated to the contrary for a particular product.

from math import floor
from sys import version_info
import ctypes
import platform
from enum import IntEnum

__version__ = "2.0.3"

#region Enums

class BattConversionTime(IntEnum):
    T_50us      = 0x0
    T_84us      = 0x1
    T_150us     = 0x2
    T_280us     = 0x3
    T_540us     = 0x4
    T_1052us    = 0x5
    T_2074us    = 0x6
    T_4120us    = 0x7


class BattNumSamples(IntEnum):
    SAMPLES_1       = 0x0
    SAMPLES_4       = 0x1
    SAMPLES_16      = 0x2
    SAMPLES_64      = 0x3
    SAMPLES_128     = 0x4
    SAMPLES_256     = 0x5
    SAMPLES_512     = 0x6
    SAMPLES_1024    = 0x7


class BattOperationMode(IntEnum):
    CONTINUOUS = 0xB
    TRIGGERED  = 0x3


class AccessTypes(IntEnum):
    MULTIUSER = 1,
    EXCLUSIVE = 2,
    FORCE_EXCLUSIVE = 3

class CardTypes(IntEnum):
    CARD_PIC = 0,
    CARD_PS = 1,
    CARD_743 = 2,
    CARD_620 = 3,
    CARD_PXM78XX = 5,
    CARD_PX773X = 6,
    CARD_PXA72XX = 7

class Attributes(IntEnum):
    TYPE				= 0x400,	# Gets/Sets DWORD attribute value of Type of the Sub-unit (values: TYPE_MUXM, TYPE_MUXMS) 
    MODE				= 0x401,	# Gets/Sets DWORD attribute value of Mode of the Card 

    # Current monitoring attributes 
    CNFGREG_VAL			= 0x402,	# Gets/Sets WORD value of config register 
    SHVLREG_VAL			= 0x403,	# Gets WORD value of shuntvoltage register 
    CURRENT_VAL			= 0x404,	# Gets double current value in Amps 

    # Read-only Power Supply attributes 
    INTERLOCK_STATUS			= 0x405,	# Gets BOOL value of interlock status 
    OVERCURRENT_STATUS_MAIN		= 0x406,	# Gets BOOL value of main overcurrent status 
    OVERCURRENT_STATUS_CH		= 0x407,	# Gets BOOL value of overcurrent status on specific channel 

    # Read/Write Power Supply attributes
    OUTPUT_ENABLE_MAIN			= 0x408,	# Gets/Sets BOOL value. Enables/Disables main 
    OUTPUT_ENABLE_CH			= 0x409,	# Gets/Sets BOOL value. Enables/Disables specific channel 

    # Read/Write Thermocouple Simulator functions
    TS_SET_RANGE				= 0x40A,		# Gets/Sets Auto range which toggles between based on the value 
    #Read-only function
    TS_LOW_RANGE_MIN			= 0x40B,        # Gets DOUBLE value for minimum of the low range on Themocouple
    TS_LOW_RANGE_MED			= 0x40C,        # Gets DOUBLE value for median of the low range on Themocouple
    TS_LOW_RANGE_MAX			= 0x40D,        # Gets DOUBLE value for maxmium of the low range on Themocouple
    TS_LOW_RANGE_MAX_DEV		= 0x40E,        # Gets DOUBLE value for maximum deviation on the low range on Themocouple
    TS_LOW_RANGE_PREC_PC		= 0x40F,        # Gets DOUBLE value for precision percentage on the low range on Themocouple
    TS_LOW_RANGE_PREC_DELTA	    = 0x410,        # Gets DOUBLE value for precision delta on the low range on Themocouple
    TS_MED_RANGE_MIN			= 0x411,        # Gets DOUBLE value for minimum of the mid range on Themocouple
    TS_MED_RANGE_MED			= 0x412,        # Gets DOUBLE value for median of the mid range on Themocouple
    TS_MED_RANGE_MAX			= 0x413,        # Gets DOUBLE value for maximum of the mid range on Themocouple
    TS_MED_RANGE_MAX_DEV		= 0x414,        # Gets DOUBLE value for maximum deviation on the mid range on Themocouple
    TS_MED_RANGE_PREC_PC		= 0x415,        # Gets DOUBLE value for precision percentage on the mid range on Themocouple
    TS_MED_RANGE_PREC_DELTA	    = 0x416,        # Gets DOUBLE value for precision delta on the mid range on Themocouple
    TS_HIGH_RANGE_MIN			= 0x417,        # Gets DOUBLE value for minimum of the high range on Themocouple
    TS_HIGH_RANGE_MED			= 0x418,        # Gets DOUBLE value for median of the high range on Themocouple
    TS_HIGH_RANGE_MAX			= 0x419,        # Gets DOUBLE value for maximum of the high range on Themocouple
    TS_HIGH_RANGE_MAX_DEV		= 0x41A,        # Gets DOUBLE value for maximum deviation on the high range on Themocouple
    TS_HIGH_RANGE_PREC_PC		= 0x41B,        # Gets DOUBLE value for precision percentage on the high range on Themocouple
    TS_HIGH_RANGE_PREC_DELTA	= 0x41C,        # Gets DOUBLE value for precision delta on the high range on Themocouple
    TS_POT_VAL					= 0x41D,        # Gets UCHAR value for the pot settings on Thermocouple
        #Write-only function
    TS_SET_POT					= 0x41E,        # Sets UCHAR value for the pot settings on Thermocouple 
    TS_SAVE_POT				    = 0x41F,        # Sets UCHAR value for the pot settings on Thermocouple
    TS_DATA_DUMP				= 0x420,
    MUXM_MBB					= 0x421,

    #Thermocouple Complentation function
    TS_TEMPERATURES_C   = 0x42E, # Read 7 sensors on 1192r0 41-760 I2C Compensation Block in degrees Celsius
    TS_TEMPERATURES_F   = 0x42F, # Read 7 sensors on 1192r0 41-760 I2C Compensation Block in degrees Farenheit

    TS_EEPROM           = 0x430, # Read/write 34LC02 eeprom
    TS_EEPROM_OFFSET    = 0x431,  # Supply offset to eeprom

    CARD_PCB_NUM        = 0x43D, #Card PCB Number.
    CARD_PCB_REV_NUM    = 0x43E, #Card PCB Revision Number.
    CARD_FW_REV_NUM     = 0x43F, #Card FPGA Firmware Revision Number.

    CURRENT_MA  = 0x440,    # Sets/Gets DOUBLE value of Current in mA
    VOLTAGE_V   = 0x441,    # Sets/Gets DOUBLE value of Voltage in V
    SLEW_RATE   = 0x442,    # Sets/Gets BYTE value Upper nibble <StepSize> Lower nibble <Clock-Rate>
    IS_SLEW     = 0x443,	# Gets BOOL to check if Slew Mode functionality if on or off.
    CURRENT_A   = 0x404     # Sets/gets double value of current in A
    MEASURE_CONFIG  = 0x481 # Sets config for measurement device (DWORD)
    LOAD        = 0x482     # Sets/gets DWORD load value 0 - 300 (0 - 300 mA)
    C_SET_MEASURE_SET = 0x1101 # Set voltage/current, measure, set again (BOOL)


    # VDT attributes
    VDT_AUTO_INPUT_ATTEN			= 0x450,	# Sets/Gets DWORD (0-100) for input gain (Default = 100)
    VDT_ABS_POSITION				= 0x451,	# Sets/Gets DWORD (0-32767) for Both Outputs on LVDT_5_6 WIRE & OutputA on LVDT_4_WIRE  
    VDT_ABS_POSITION_B				= 0x452,	# Sets/Gets DWORD (0-32767)  for OutputB on LVDT_4_WIRE  
    VDT_PERCENT_POSITION			= 0x453,	# Sets/Gets DOUBLE (-100.00% to 100.00%) for Both Out on LVDT_5_6 WIRE & OutA on LVDT_4_WIRE 
    VDT_PERCENT_POSITION_B			= 0x454,	# Sets/Gets DOUBLE (-100.00% to 100.00%) for OutB on LVDT_4_WIRE 
    VDT_VOLTAGE_SUM				    = 0x455,   # Sets/Gets DOUBLE in Volts  for VSUM value  
    VDT_VOLTAGE_DIFF				= 0x456,	# Sets/Gets DOUBLE in Volts  for VDIFF value (the limit is +/- VSUM)  
    VDT_OUT_GAIN					= 0x457,	# Sets/Gets DWORD (1 or 2) for 1x or 2x output multiplier  #CALIBRATION ONLY
    VDT_MANUAL_INPUT_ATTEN			= 0x458,	# Sets/Gets DWORD (0-255) Pot Value on LVDT  
    VDT_MODE					    = 0x459,	# Sets/Gets DWORD to set mode 1 = LVDT_5_6_WIRE, mode 2=  LVDT_4_WIRE.
    VDT_DELAY_A					    = 0x45A,	# Sets/Gets DWORD (0-6499) delay for OutputA   
    VDT_DELAY_B					    = 0x45B,	# Sets/Gets DWORD (0-6499) delay for OutputB   
    VDT_INPUT_LEVEL				    = 0x45C,	# Sets/Gets DWORD (0-65520) for Input Value  
    VDT_INPUT_FREQ					= 0x45D,	# Sets/Gets DWORD (300-20000 Hz) for Input Frequency   
    VDT_OUT_LEVEL					= 0x45E,	# Sets/Gets DWORD (0-4096)  output level  

    # LVDT Mk2 Get only
    ATTR_VDT_DSPIC_VERSION			= 0x45F,	# Gets DWORD value of for dsPIC firmware version 104 = v0.01.04 

    # LVDT Mk2 Set/Get
    VDT_INVERT_A        		    = 0x460,	# Sets/Gets DWORD (0 or 1)  for OutA 
    VDT_INVERT_B				    = 0x461,    # Sets/Gets DWORD (0 or 1)  for OutB  
    VDT_PHASE_TRACKING			    = 0x462,	# 'TP' Phase tracking mode on or off  -CALIBRATION ONLY 
    VDT_SAMPLE_LOAD				    = 0x463,	# Sets DWORD comprises of Top 16 bits is GAIN (0-100) and lower 16 frequency (300-20000 Hz) 
    ATTR_VDT_INPUT_FREQ_HI_RES		= 0x464,	# Gets DWORD value of frequency in Hz  
    ATTR_VDT_LOS_THRESHOLD			= 0x465,	# Sets/Gets DWORD (0 to 32768) for LOS Threshold (Default = 32768) 
    VDT_SMPL_BUFFER_SIZE			= 0x466,	# Sets/Gets DWORD (1 to 500) for Sample buffer size (Default = 500) 
    VDT_NULL_OFFSET				    = 0x467,	# Sets/Gets WORD (0 to 100) for null offset (Default = 0) 
    #LVDT Get Only
    VDT_STATUS				        = 0x468,    # Gets BYTE value (0x00 or 0x01) checking LOS status 
    VDT_MAX_OUT_VOLTAGE		        = 0x469,    # Gets DOUBLE value for maximum output voltage 
    VDT_MIN_OUT_VOLTAGE		        = 0x46A,    # Gets DOUBLE value for minimum output voltage 
    VDT_MAX_IN_VOLTAGE			    = 0x46B,    # Gets DOUBLE value for maximum input voltage 
    VDT_MIN_IN_VOLTAGE			    = 0x46C,    # Gets DOUBLE value for minimum input voltage 
    VDT_PHASE_DELAY_A				= 0x46D,	# Sets/Gets DOUBLE value for DOUBLE in degrees for OutA. 
    VDT_PHASE_DELAY_B				= 0x46E,	# Sets/Gets DOUBLE value for DOUBLE in degrees for OutB. 

    RESOLVER_START_STOP_ROTATE		= 0x470,	# Sets/Gets BOOL TRUE for Start, FALSE of Stop
    RESOLVER_NUM_OF_TURNS			= 0x471,	# Sets/ Gets WORD Number of turns (1-65535)
    RESOLVER_ROTATE_SPEED			= 0x472,	# Sets/Gets DOUBLE rotating speed (RPM speed upto 655.35 RPM)
    RESOLVER_POSITION				= 0x473,	# Sets/Gets DOUBLE rotation between -180.00 to 180.00 Degrees
    RESOLVER_POSITION_0_360		    = 0x474,	# Sets/Gets DOUBLE rotation between 0.00 to 360.00 Degrees

    SETTLE_DELAY_ZERO				= 0x480,	# Sets/Gets BOOL, settling time set to zero for the ouput subunits
    
    # DIO card.
    DIO_PATTERN_MODE				= 0x490,	# Sets/Gets Pattern Mode (BOOL) 
    DIO_EXT_CLOCK_MODE				= 0x491,	# Sets/Gets External Clock Mode (DWORD) 
    DIO_PATTERN					    = 0x492,	# Sets/Gets each pattern for individual ports (BYTE) 
    DIO_PATTERN_OFFSET				= 0x493,	# Sets/Gets offset of the pattern to be read from individual ports (DWORD) 
    DIO_PATTERN_TOTAL_COUNT		    = 0x494,	# Gets pattern count for individual ports (DWORD) 
    DIO_EXT_CLK_IO_STATE			= 0x495,	# Sets/Gets port clk pin state when IO Mode is set (BOOL) 
    DIO_EXT_CLK_IO_DIR				= 0x496,	# Sets/Gets port clk pin direction when IO Mode is set (BOOL)

    #	**************** Card level Attributes ****************
    #   C_ attributes are for card level operations.
    #	Attributes range should be handled in the SetAttribute/GetAttribute Functions.
    #	Range 0x1000 to 0x1999 is reserved for card level attributes.
    #	Subunit Parameter for SetAttribute() and GetAttribute() will be insignificant for these Attributes.
    C_DIO_INT_CLOCK_ENABLE			= 0x1000,	# Sets/Gets Internal Clock Enable/Disable (BOOL) 
    C_DIO_INT_CLOCK_FREQ			= 0x1001,	# Sets/Gets Internal Clock Frequency (DOUBLE) 
    C_DIO_START_POSITION			= 0x1002,	# Sets/Gets Start postion of pattern capture engine (DWORD) 
    C_DIO_END_POSITION				= 0x1003,	# Sets/Gets End postion of pattern capture engine (DWORD) 
    C_DIO_DYNAMIC_CONTINUOUS		= 0x1004,	# Sets/Gets continuous run status of pattern capture engine (BOOL) 
    C_DIO_DYNAMIC_ONELOOP			= 0x1005,	# Sets/Gets one loop execution status of pattern generation/acquisition engine (BOOL) 
    C_DIO_LOAD_PATTERN_FILE		    = 0x1007,	# Loads pattern file data to DIO card memory (CHAR*) 
    C_DIO_SOFTWARE_TRIGGER			= 0x1008,	# Send Software trigger for pattern mode operation (BOOL) 
    C_DIO_DYNAMIC_BUSY				= 0x1009,	# Check the status of the capture engine (BOOL) 
    C_DIO_ALL_PORT_DATA			    = 0x100A,	# Load/Retreive patterns for all ports for an address offset (DWORD*) 
    C_DIO_ALL_PORT_DATA_OFFSET		= 0x100B,	# Used to get/set the offset to/from which data should be loaded/retrieved (DWORD) 
    C_DIO_FIFO_POS					= 0x100C,	# Gets FIFO postion or number of dynamic operations for the card (DWORD) 
    C_DIO_ABORT					    = 0x100D,	# Aborts any existing trigger 
    C_DIO_PATTERN_FILE_ERR			= 0x100E,	# Get the errors found in the Pattern File 
    C_DIO_SAVE_PATTERN_FILE		    = 0x100F,	# Saves to pattern file from DIO card memory (CHAR*) 
    C_DIO_VERIFY_PATTERN_FILE		= 0x1010,	# Sets/Gets the output clock delay (DWORD) 
    
class TS_Range(IntEnum):
    AUTO    = 0,
    LOW     = 1,
    MED     = 2,
    HIGH    = 3

class CL_Mode(IntEnum):
    MODE_4_20_MA        = 1, # 4-20mA Mode (Set by Default)
    MODE_0_24_MA        = 2, # 0-20mA Mode
    MODE_MINUS24_24_MA  = 3, # +/-24mA Mode
    MODE_0_5_V          = 4, # 0-5V Mode
    MODE_MINUS12_12_V   = 5, # +/-12V Mode
    MODE_MINUS5_5_V     = 6  # +/-5V

class DM_Mode(IntEnum):
    LVDT_5_6_WIRE = 1,
    LVDT_4_WIRE   = 2,
    RESOLVER      = 3

class RES_Mode(IntEnum):

    SET = 0,  # Legacy/Default mode to support existing break before make with settling delay
    MBB = 1,  # New mode to suport make before break with settling delay
    APPLY_PATTERN_IMMEDIATE = 2,  # Apply new pattern immediately and wait till settling delay
    NO_SETTLING_DELAY = 4,  # Disable settling delay,same as DriverMode NO_WAIT, but at sub-unit level
    DONT_SET = 999,  # Do the calculations but don't set the card
    END = 9999


#endregion



class Error(Exception):
    """Base error class provides error message and optional error code from driver."""

    def __init__(self, message, errorCode=None):
        self.message = message
        self.errorCode = errorCode

    def __str__(self):
        return self.message


class Pi_Base:
    """Base class provides base functionality, LXI device discovery functions"""
    def __init__(self):
        if platform.system() == "Windows":
            arch = platform.architecture()
            if "64bit" in arch:
                self.handleCMLX = ctypes.windll.LoadLibrary("Picmlx_w64")
                self.handlePLX = ctypes.windll.LoadLibrary("Piplx_w64")
            else:
                self.handleCMLX = ctypes.windll.LoadLibrary("Picmlx_w32")
                self.handlePLX = ctypes.windll.LoadLibrary("Piplx_w32")
        elif platform.system() == "Darwin":
            self.handleCMLX = ctypes.cdll.LoadLibrary("Bin/libpicmlx.so")
            self.handlePLX = ctypes.cdll.LoadLibrary("Bin/libpiplx.so")
        elif platform.system() == "Linux":
            self.handleCMLX = ctypes.cdll.LoadLibrary("libpicmlx.so")
            self.handlePLX = ctypes.cdll.LoadLibrary("libpiplx.so")

        self.pythonMajorVersion = version_info[0]

    def _handlePIPLXError(self, error):
        """Internal method to raise exceptions based on error codes from piplx."""
        if error:
            errorString = ctypes.create_string_buffer(100)
            self.handlePLX.PIPLX_ErrorCodeToMessage(error, ctypes.byref(errorString), 100)
            errorString = self._pythonString(errorString.value)
            raise Error(errorString, errorCode=error)
        return

    def _handlePICMLXError(self, error):
        """Internal method to raise exceptions based on error codes from picmlx."""
        if error:
            errorString = ctypes.create_string_buffer(100)
            self.handleCMLX.PICMLX_ErrorCodeToMessage(error, ctypes.byref(errorString), 100)
            errorString = self._pythonString(errorString.value)
            raise Error(errorString, errorCode=error)
        return

    def _calc_dwords(self, bits):
        dwords = (bits / 32)
        if ((bits) % 32 > 0):
            dwords += 1
        return int(floor(dwords))

    def _stringToStr(self, inputString):
        """Take a string passed to a function in Python 2 or Python 3 and convert to
           a ctypes-friendly ASCII string"""

        # Check for Python 2 or 3
        if self.pythonMajorVersion < 3:
            if type(inputString) is str:
                return inputString
            if type(inputString) is unicode:
                return inputString.encode()
        else:
            if type(inputString) is bytes:
                return inputString
            elif type(inputString) is str:
                return inputString.encode()

    def _pythonString(self, inputString):
        """Ensure returned strings are native in Python 2 and Python 3"""

        # Check for Python 2 or 3
        if self.pythonMajorVersion < 3:
            return inputString
        else:
            return inputString.decode()

    # Discovery Functions
    def EchoDirectEx(self, address, port, timeout):
        address = self._stringToStr(address)
        port = ctypes.c_uint32(port)
        timeout = ctypes.c_uint32(timeout)
        listen_port = ctypes.c_uint(0)
        card_count = ctypes.c_uint(0)
        client_count = ctypes.c_uint(0)
        open_card_count = ctypes.c_uint(0)
        description_size = ctypes.c_uint(256)
        description = ctypes.create_string_buffer(description_size.value)
        lxi_address_size = ctypes.c_uint(100)
        lxi_address = ctypes.create_string_buffer(lxi_address_size.value)
        err = self.handleCMLX.PICMLX_EchoDirectEx(address, port, timeout,
                                                  ctypes.byref(listen_port),
                                                  ctypes.byref(card_count),
                                                  ctypes.byref(client_count),
                                                  ctypes.byref(open_card_count),
                                                  ctypes.byref(description),
                                                  description_size,
                                                  ctypes.byref(lxi_address),
                                                  lxi_address_size)
        self._handlePICMLXError(err)
        return listen_port.value, card_count.value, client_count.value, open_card_count.value, self._pythonString(description.value), \
               self._pythonString(lxi_address.value)

    def EchoBroadcast(self, listen_port, timeout):
        listen_port = ctypes.c_uint32(listen_port)
        timeout = ctypes.c_uint32(timeout)
        available_lxi_count = ctypes.c_uint(0)

        err = self.handleCMLX.PICMLX_EchoBroadcast(listen_port, timeout, ctypes.byref(available_lxi_count))
        self._handlePICMLXError(err)
        return int(available_lxi_count.value)

    def GetAvailableLXICount(self):
        ret = self.handleCMLX.PICMLX_GetAvailableLXICount()
        return int(ret)

    def GetAvailableLXIEntryEx(self, index):
        listen_port = ctypes.c_uint(0)
        card_count = ctypes.c_uint(0)
        client_count = ctypes.c_uint(0)
        open_card_count = ctypes.c_uint(0)
        description_size = ctypes.c_uint(256)
        description = ctypes.create_string_buffer(description_size.value)
        lxi_address_size = ctypes.c_uint(100)
        lxi_address = ctypes.create_string_buffer(lxi_address_size.value)
        index = ctypes.c_uint32(index)

        err = self.handleCMLX.PICMLX_GetAvailableLXIEntryEx(index,
                                                            ctypes.byref(listen_port),
                                                            ctypes.byref(card_count),
                                                            ctypes.byref(client_count),
                                                            ctypes.byref(open_card_count),
                                                            ctypes.byref(description),
                                                            description_size,
                                                            ctypes.byref(lxi_address),
                                                            lxi_address_size)
        self._handlePICMLXError(err)
        return listen_port.value, card_count.value, client_count.value, open_card_count.value, self._pythonString(description.value), \
               self._pythonString(lxi_address.value)

    def Discover(self, port=1024, timeout=5000, address=None):
        """Sends a broadcast message to all LXIs in the address (default 255.255.255.255).
        Returns a list of tuple pairs containing IP addresses and descriptions."""

        port = ctypes.c_uint32(port)
        timeout = ctypes.c_uint32(timeout)
        LXIcount = ctypes.c_uint32(50)

        if address is None:
            error = self.handleCMLX.PICMLX_EchoBroadcast(port, timeout, ctypes.byref(LXIcount))

        else:
            address = self._stringToStr(address)
            error = self.handleCMLX.PICMLX_EchoBroadcastEx(address, port, timeout, ctypes.byref(LXIcount))

        self._handlePICMLXError(error)

        LXIcount.value = self.handleCMLX.PICMLX_GetAvailableLXICount()

        listenPort = ctypes.c_uint32()
        cardCount = ctypes.c_uint32()
        clientCount = ctypes.c_uint32()
        openCardCount = ctypes.c_uint32()
        descLength = 100
        description = ctypes.create_string_buffer(descLength)
        LXIAddressLen = 100
        LXIAddress = ctypes.create_string_buffer(LXIAddressLen)

        LXIs = []
        for lxi in range(0, LXIcount.value):
            error = self.handleCMLX.PICMLX_GetAvailableLXIEntryEx(lxi,
                                                                  ctypes.byref(listenPort),
                                                                  ctypes.byref(cardCount),
                                                                  ctypes.byref(openCardCount),
                                                                  ctypes.byref(description),
                                                                  descLength,
                                                                  ctypes.byref(LXIAddress),
                                                                  LXIAddressLen)

            LXIs.append((self._pythonString(LXIAddress.value), self._pythonString(description.value)))

        return LXIs

    def Version(self):
        ver1 = self.handleCMLX.PICMLX_GetVersion()
        ver2 = self.handlePLX.PIPLX_GetVersion()
        return int(ver1), int(ver2)

    def ErrorCodeToMessage(self, code):
        str_length = ctypes.c_int(100)
        string = ctypes.create_string_buffer(str_length.value)
        self.handleCMLX.PICMLX_ErrorCodeToMessage(code, ctypes.byref(string), str_length)
        return self._pythonString(string.value)


class _SubState:
    def __init__(self, rows, columns, subunit, stateData):
        self.stateData = stateData
        self.rows = rows
        self.columns = columns
        self.subunit = subunit

    def _SetBit(self, bitNum, state):
        dwordNum = int(floor(bitNum / 32))
        dwordBit = int(bitNum % 32)

        if state:
            self.stateData[dwordNum] = self.stateData[dwordNum] | (1 << dwordBit)
        else:
            self.stateData[dwordNum] = self.stateData[dwordNum] & ~(1 << dwordBit)

        return

    def PreSetCrosspoint(self, row, column, state):
        if not 1 <= row <= self.rows:
            raise Error("Row value out of card subunit range")
        if not 1 <= column <= self.columns:
            raise Error("Column value out of card subunit range")

        switchNum = ((row - 1) * self.columns) + (column - 1)

        self._SetBit(switchNum, state)

        return

    def PreClearSub(self):
        self.stateData = [0] * len(self.stateData)

        return

    def PreSetBit(self, bitNum, state):
        if not 1 <= bitNum <= self.columns:
            raise Error("Switch value out of card subunit range")

        bitNum -= 1

        self._SetBit(bitNum, state)

        return


class Pi_Session(Pi_Base):
    """Pi_Session class provides LXI session functionality"""
    def __init__(self, address, port=1024, timeout=1000, board=0):

        Pi_Base.__init__(self)

        self.AccessTypes = {
            "MULTIUSER_ACCESS": 1,
            "EXCLUSIVE_ACCESS": 2,
            "FORCE_EXCLUSIVE_ACCESS": 3
        }

        self.session = ctypes.c_long(0)
        self.disposed = False

        if address.lower() == "pxi":
            self.closeable = False
        else:
            self.closeable = True

        # Connect picmlx session
        self._Connect(address, port, timeout, board=board)

    def __del__(self):
        if not self.disposed:
            self.Close()
        return

    def _Connect(self, address, port, timeout, board=0):
        board = ctypes.c_uint32(board)
        port = ctypes.c_uint32(port)
        timeout = ctypes.c_uint32(timeout)
        address = self._stringToStr(address)

        err = self.handleCMLX.PICMLX_Connect(board, address, port, timeout, ctypes.byref(self.session))
        self._handlePICMLXError(err)

        return

    def OpenCard(self, bus, device):
        """Method to open a card by bus and device number"""

        card = Pi_Card_ByDevice(self.session, bus, device)
        return card

    def OpenCardByID(self, cardID, accessType=1):
        """Method to open a card by Card ID and access mode"""
        card = Pi_Card_ByID(self.session, cardID, accessType)
        return card

    def CountFreeCards(self):
        count = ctypes.c_uint(0)
        err = self.handlePLX.PIPLX_CountFreeCards(self.session, ctypes.byref(count))
        self._handlePIPLXError(err)

        return int(count.value)

    def FindFreeCards(self):
        count = self.CountFreeCards()
        buses = (ctypes.c_uint32 * count)()
        devices = (ctypes.c_uint32 * count)()

        err = self.handlePLX.PIPLX_FindFreeCards(self.session, count, ctypes.byref(buses), ctypes.byref(devices))
        self._handlePIPLXError(err)

        return [(int(buses[i]), int(devices[i])) for i in range(0, len(devices))]

    def Close(self):
        if self.closeable:
            err = self.handleCMLX.PICMLX_Disconnect(self.session)
            self.disposed = True
        return

    def SbVersion(self):
        ver = self.handleCMLX.PICMLX_SbVersion(self.session)
        return ver

    def GetUsableCards(self, card_type):
        totalCardCount = self.GetTotalCardsCount()
        cards = (ctypes.c_uint32 * totalCardCount)()
        num_cards = ctypes.c_uint(totalCardCount)
        card_type = ctypes.c_uint32(card_type)

        err = self.handleCMLX.PICMLX_GetUsableCards(self.session, card_type, ctypes.byref(cards), ctypes.byref(num_cards))
        self._handlePICMLXError(err)

        return [int(card) for card in cards]

    def GetUsedCards(self, card_type):
        totalCardCount = self.GetTotalCardsCount()
        cards = (ctypes.c_uint32 * totalCardCount)()
        num_cards = ctypes.c_uint(totalCardCount)
        card_type = ctypes.c_uint32(card_type)

        err = self.handleCMLX.PICMLX_GetUsedCards(self.session, card_type, ctypes.byref(cards), ctypes.byref(num_cards))
        self._handlePICMLXError(err)

        return [int(card) for card in cards]

    def GetTotalCardsCount(self):
        count = ctypes.c_uint32(0)
        err = self.handleCMLX.PICMLX_GetTotalCardsCount(self.session, ctypes.byref(count))
        self._handlePICMLXError(err)
        return int(count.value)

    def GetTotalOpenedCards(self):
        count = ctypes.c_uint32(0)
        err = self.handleCMLX.PICMLX_GetTotalOpenedCards(self.session, ctypes.byref(count))
        self._handlePICMLXError(err)
        return int(count.value)

    """............................."""

    """ SESSION RELATED FUNCTIONS """

    def GetSessionsCount(self):
        """Function to receive a number of all live sessions."""
        count = ctypes.c_uint32()
        err = self.handleCMLX.PICMLX_GetSessionsCount(self.session, ctypes.byref(count))
        self._handlePICMLXError(err)

        return int(count.value)

    def GetCardSessionsCount(self, card_types, card):
        """Function to receive a number of all live sessions."""
        count = ctypes.c_uint32(0)
        err = self.handleCMLX.PICMLX_GetCardSessionsCount(self.session, card_types, card, ctypes.byref(count))
        self._handlePICMLXError(err)

        return int(count.value)

    def UseForeignSession(self, session):
        length = ctypes.c_int(100)
        token = ctypes.create_string_buffer(length.value)

        err = self.handleCMLX.PICMLX_UseForeignSession(self.session, session, ctypes.byref(token), length)
        self._handlePICMLXError(err)

        return self._pythonString(token.value)

    def ReleaseForeignSession(self, session):
        session = ctypes.c_uint32(session)
        err = self.handleCMLX.PICMLX_ReleaseForeignSession(self.session, session)
        self._handlePICMLXError(err)

        return

    def GetForeignSessions(self):

        numSessions = ctypes.c_uint32(100)
        sessions = (ctypes.c_uint32 * numSessions.value)()

        err = self.handleCMLX.PICMLX_GetForeignSessions(self.session, ctypes.byref(sessions), ctypes.byref(numSessions))
        self._handlePICMLXError(err)

        return [int(session) for session in sessions]

    def GetActiveSession(self):
        session = ctypes.c_uint32(0)
        length = ctypes.c_int(100)
        token = ctypes.create_string_buffer(length.value)
        err = self.handleCMLX.PICMLX_GetActiveSession(self.session, ctypes.byref(session), ctypes.byref(token), length)
        self._handlePICMLXError(err)
        return int(session.value), self._pythonString(token.value)

    def IsCardUsed(self, card_type, card, owner_type):
        is_used = ctypes.c_bool()
        card_type = ctypes.c_uint32(card_type)
        owner_type = ctypes.c_uint32(owner_type)

        err = self.handleCMLX.PICMLX_IsCardUsed(self.session, card_type, card, owner_type, ctypes.byref(is_used))
        self._handlePICMLXError(err)

        return is_used.value

    def CloseCards(self):
        err = self.handlePLX.PIPLX_CloseCards(self.session)
        self._handlePIPLXError(err)

        return

    def GetSessionID(self):
        """Returns the session handle for opening other libraries with the LXI Session ID."""
        return self.session

    def Identify(self, enabled):
        enabled = ctypes.c_bool(enabled)

        err = self.handleCMLX.PICMLX_Identify(self.session, enabled)
        self._handlePICMLXError(err)

        return


class Pi_Card_Base(Pi_Base):
    """Card class provides card specific functionality"""
    def __init__(self):

        Pi_Base.__init__(self)

        self.session = None
        self.card = None
        self.bus = None
        self.slot = None
        self.disposed = False

        # Error Code Enum
        self.ERRORCODE = {
            "NO_ERR" : 0,                       # No error
            "ER_NO_CARD" : 1,                   # No card present with specified number
            "ER_NO_INFO" : 2,                   # Card information unobtainable - hardware problem
            "ER_CARD_DISABLED" : 3,             # Card disabled - hardware problem
            "ER_BAD_SUB" : 4,                   # Card has no subunit-unit with specified number
            "ER_BAD_BIT" : 5,                   # Sub-unit has no bit with specified number
            "ER_NO_CAL_DATA" : 6,               # Sub-unit has no calibration data to write/read
            "ER_BAD_ARRAY" : 7,                 # Array type, size or shape is incorrect
            "ER_MUX_ILLEGAL" : 8,               # Non-zero write data is illegal for MUX subunit-unit
            "ER_EXCESS_CLOSURE" : 9,            # Sub-unit closure limit exceeded
            "ER_ILLEGAL_MASK" : 10,             # One or more of the specified channels cannot be masked
            "ER_OUTPUT_MASKED" : 11,            # Cannot activate an output that is masked
            "ER_BAD_LOCATION" : 12,             # Cannot open a Pickering card at the specified location
            "ER_READ_FAIL" : 13,                # Failed read from hardware
            "ER_WRITE_FAIL" : 14,               # Failed write to hardware
            "ER_DRIVER_OP" : 15,                # Hardware driver failure
            "ER_DRIVER_VERSION" : 16,           # Incompatible hardware driver version
            "ER_SUB_TYPE" : 17,                 # Function call incompatible with subunit-unit type or capabilities
            "ER_BAD_ROW" : 18,                  # Matrix row value out of range
            "ER_BAD_COLUMN" : 19,               # Matrix column value out of range
            "ER_BAD_ATTEN" : 20,                # Attenuation value out of range
            "ER_BAD_VOLTAGE" : 21,              # Voltage value out of range
            "ER_BAD_CAL_INDEX" : 22,            # Calibration reference out of range
            "ER_BAD_SEGMENT" : 23,              # Segment number out of range
            "ER_BAD_FUNC_CODE" : 24,            # Function code value out of range
            "ER_BAD_SUBSWITCH" : 25,            # Subswitch value out of range
            "ER_BAD_ACTION" : 26,               # Action code out of range
            "ER_STATE_CORRUPT" : 27,            # Cannot execute due to corrupt subunit-unit state
            "ER_BAD_ATTR_CODE" : 28,            # Unrecognised attribute code
            "ER_EEPROM_WRITE_TMO" : 29,         # Timeout writing to EEPROM
            "ER_ILLEGAL_OP" : 30,               # Operation is illegal in the subunit-unit's current state
            "ER_BAD_POT" : 31,                  # Unrecognised pot number requested
            "ER_MATRIXR_ILLEGAL" : 32,          # Invalid write pattern for MATRIXR subunit-unit
            "ER_MISSING_CHANNEL" : 33,          # Attempted operation on non-existent channel
            "ER_CARD_INACCESSIBLE" : 34,        # Card cannot be accessed (failed/removed/unpowered)
            "ER_BAD_FP_FORMAT" : 35,            # Unsupported internal floating-point format (internal error)
            "ER_UNCALIBRATED" : 36,             # Sub-unit is not calibrated
            "ER_BAD_RESISTANCE" : 37,           # Unobtainable resistance value
            "ER_BAD_STORE" : 38,                # Invalid calibration store number
            "ER_BAD_MODE" : 39,                 # Invalid mode value
            "ER_SETTINGS_CONFLICT" : 40,        # Conflicting device settings
            "ER_CARD_TYPE" : 41,                # Function call incompatible with card type or capabilities
            "ER_BAD_POLE" : 42,                 # Switch pole value out of range
            "ER_MISSING_CAPABILITY" : 43,       # Attempted to activate a non-existent capability
            "ER_MISSING_HARDWARE" : 44,         # Action requires hardware that is not present
            "ER_HARDWARE_FAULT" : 45,           # Faulty hardware
            "ER_EXECUTION_FAIL" : 46,           # Failed to execute (e.g. blocked by a hardware condition)
            "ER_BAD_CURRENT" : 47,              # Current value out of range
            "ER_BAD_RANGE" : 48,                # Invalid range value
            "ER_ATTR_UNSUPPORTED" : 49,         # Attribute not supported
            "ER_BAD_REGISTER" : 50,             # Register number out of range
            "ER_MATRIXP_ILLEGAL" : 51,          # Invalid channel closure or write pattern for MATRIXP subunit-unit
            "ER_BUFFER_UNDERSIZE" : 52,         # Data buffer too small
            "ER_ACCESS_MODE" : 53,              # Inconsistent shared access mode
            "ER_POOR_RESISTANCE" : 54,          # Resistance outside limits
            "ER_BAD_ATTR_VALUE" : 55,           # Bad attribute value
            "ER_INVALID_POINTER" : 56,          # Invalid pointer
            "ER_ATTR_READ_ONLY" : 57,           # Attribute is read only
            "ER_ATTR_DISABLED" : 58,            # Attribute is disabled
            "ER_PSU_MAIN_OUTPUT_DISABLED" : 59  # Main output is disabled, cannot enable the channel
        }

        # Attribute Codes Enum
        self.ATTR = {
            "TYPE" : 0x400,  # Gets/Sets DWORD attribute value of Type of the Sub-unit (values: TYPE_MUXM, TYPE_MUXMS) 
            "MODE" : 0x401, # Gets/Sets DWORD attribute value of Mode of the Card 

            # Current monitoring attributes 
            "CNFGREG_VAL" : 0x402,	# Gets/Sets WORD value of config register 
            "SHVLREG_VAL" : 0x403,	# Gets WORD value of shuntvoltage register 
            "CURRENT_VAL" : 0x404,	# Gets double current value in Amps 

            # Read-only Power Supply attributes 
            "INTERLOCK_STATUS" : 0x405,	# Gets BOOL value of interlock status 
            "OVERCURRENT_STATUS_MAIN" : 0x406,	# Gets BOOL value of main overcurrent status 
            "OVERCURRENT_STATUS_CH" : 0x407,	# Gets BOOL value of overcurrent status on specific channel 

            # Read/Write Power Supply attributes 
            "OUTPUT_ENABLE_MAIN" : 0x408,	# Gets/Sets BOOL value. Enables/Disables main 
            "OUTPUT_ENABLE_CH" : 0x409,	# Gets/Sets BOOL value. Enables/Disables specific channel 

            # Read/Write Thermocouple Simulator functions 
            "TS_SET_RANGE" : 0x40A,		# Gets/Sets Auto range which toggles between based on the value 
            #Read-only function
            "TS_LOW_RANGE_MIN" : 0x40B,
            "TS_LOW_RANGE_MED" : 0x40C,
            "TS_LOW_RANGE_MAX" : 0x40D,
            "TS_LOW_RANGE_MAX_DEV" : 0x40E,
            "TS_LOW_RANGE_PREC_PC" : 0x40F,
            "TS_LOW_RANGE_PREC_DELTA" : 0x410,
            "TS_MED_RANGE_MIN" : 0x411,
            "TS_MED_RANGE_MED" : 0x412,
            "TS_MED_RANGE_MAX" : 0x413,
            "TS_MED_RANGE_MAX_DEV" : 0x414,
            "TS_MED_RANGE_PREC_PC" : 0x415,
            "TS_MED_RANGE_PREC_DELTA" : 0x416,
            "TS_HIGH_RANGE_MIN" : 0x417,
            "TS_HIGH_RANGE_MED" : 0x418,
            "TS_HIGH_RANGE_MAX" : 0x419,
            "TS_HIGH_RANGE_MAX_DEV" : 0x41A,
            "TS_HIGH_RANGE_PREC_PC" : 0x41B,
            "TS_HIGH_RANGE_PREC_DELTA" : 0x41C,
            "TS_POT_VAL" : 0x41D, #Read Pot Value from user store
            #Write-only function
            "TS_SET_POT" : 0x41E,
            "TS_SAVE_POT" : 0x41F,
            "TS_DATA_DUMP" : 0x420,
            "MUXM_MBB" : 0x421,

            "TS_TEMPERATURES_C" : 0x42E, # Read 7 sensors on 1192r0 41-760 I2C Compensation Block in degrees Celsius
            "TS_TEMPERATURES_F" : 0x42F, # Read 7 sensors on 1192r0 41-760 I2C Compensation Block in degrees Farenheit
            "TS_EEPROM" : 0x430, # Read/write 34LC02 eeprom
            "TS_EEPROM_OFFSET" : 0x431,  # Supply offset to eeprom
            
            # VDT attributes   
            "VDT_AUTO_INPUT_ATTEN"				: 0x450,	# Sets/Gets DWORD (0-100) for input gain (Default = 100)
            "VDT_ABS_POSITION"                  : 0x451,	# Sets/Gets DWORD (0-32767) for Both Outputs on LVDT_5_6 WIRE & OutputA on LVDT_4_WIRE
            "VDT_ABS_POSITION_B"                : 0x452,	# Sets/Gets DWORD (0-32767)  for OutputB on LVDT_4_WIRE
            "VDT_PERCENT_POSITION"              : 0x453,	# Sets/Gets DOUBLE (-100.00% to 100.00%) for Both Out on LVDT_5_6 WIRE & OutA on LVDT_4_WIRE
            "VDT_PERCENT_POSITION_B"            : 0x454,	# Sets/Gets DOUBLE (-100.00% to 100.00%) for OutB on LVDT_4_WIRE
            "VDT_VOLTAGE_SUM"                   : 0x455,    # Sets/Gets DOUBLE in Volts  for VSUM value
            "VDT_VOLTAGE_DIFF"                  : 0x456,	# Sets/Gets DOUBLE in Volts  for VDIFF value (the limit is +/- VSUM)
            "VDT_OUT_GAIN"                      : 0x457,	# Sets/Gets DWORD (1 or 2) for 1x or 2x output multiplier */ #CALIBRATION ONLY
            "VDT_MANUAL_INPUT_ATTEN"            : 0x458,	# Sets/Gets DWORD (0-255) Pot Value on LVDT
            "VDT_MODE"                          : 0x459,	# Sets/Gets DWORD to set mode 1 = LVDT_5_6_WIRE, mode 2=  LVDT_4_WIRE.
            "VDT_DELAY_A"                       : 0x45A,	# Sets/Gets DWORD (0-6499) delay for OutputA
            "VDT_DELAY_B"                       : 0x45B,	# Sets/Gets DWORD (0-6499) delay for OutputB
            "VDT_INPUT_LEVEL"                   : 0x45C,	# Sets/Gets DWORD (0-65520) for Input Value
            "VDT_INPUT_FREQ"                    : 0x45D,	# Sets/Gets DWORD (300-20000 Hz) for Input Frequency
            "VDT_OUT_LEVEL"                     : 0x45E,	# Sets/Gets DWORD (0-4096)  output level

            # LVDT Mk2 Get only
            "VDT_DSPIC_VERSION"                 : 0x45F,	# Gets DWORD value of for dsPIC firmware version 104 = v0.01.04

            # LVDT Mk2 Set/Get
            "VDT_INVERT_A"        				: 0x460,	# Sets/Gets DWORD (0 or 1)  for OutA
            "VDT_INVERT_B"                      : 0x461,    # Sets/Gets DWORD (0 or 1)  for OutB
            "VDT_PHASE_TRACKING"			    : 0x462,	# 'TP' Phase tracking mode on or off  -CALIBRATION ONLY
            "VDT_SAMPLE_LOAD"				    : 0x463,	# Sets DWORD comprises of Top 16 bits is GAIN (0-100) and lower 16 frequency (300-20000 Hz)
            "VDT_INPUT_FREQ_HI_RES"             : 0x464,	# Gets DWORD value of frequency in Hz
            "VDT_LOS_THRESHOLD"                 : 0x465,	# Sets/Gets DWORD (0 to 32768) for LOS Threshold (Default = 32768)
            "VDT_SMPL_BUFFER_SIZE"              : 0x466,	# Sets/Gets DWORD (1 to 500) for Sample buffer size (Default = 500)
            "VDT_NULL_OFFSET"                   : 0x467,	# Sets/Gets WORD (0 to 100) for null offset (Default = 0)

            # LVDT Get Only
            "VDT_STATUS"                        : 0x468,    # Gets BYTE value (0x00 or 0x01) checking LOS status
            "VDT_MAX_OUT_VOLTAGE"               : 0x469,    # Gets DOUBLE value for maximum output voltage
            "VDT_MIN_OUT_VOLTAGE"               : 0x46A,    # Gets DOUBLE value for minimum output voltage
            "VDT_MAX_IN_VOLTAGE"                : 0x46B,    # Gets DOUBLE value for maximum input voltage
            "VDT_MIN_IN_VOLTAGE"                : 0x46C,    # Gets DOUBLE value for minimum input voltage

            "CARD_PCB_NUM" : 0x43D, # Card PCB Number.
            "CARD_PCB_REV_NUM" : 0x43E, # Card PCB Revision Number.
            "CARD_FW_REV_NUM" : 0x43F  # Card FPGA Firmware Revision Number.

        }

        # Vsource Range Enum
        self.TS_RANGE = {
            "AUTO" : 0,
            "LOW" : 1,
            "MED" : 2,
            "HIGH" : 3
        }

        # Current loop modes Enum
        self.CL_MODE = {
            # 4-20mA mode (set by default)
            "4_20_MA": 1,

            # 0-24mA mode
            "0_24_MA": 2,

            # +/-24mA mode
            "MINUS24_24_MA": 3,

            # 0-5V mode
            "0_5_V": 4,

            # +/- 12V mode
            "MINUS12_12_V": 5,

            # +/- 5V mode
            "MINUS5_5_V": 6
        }



    def ErrorCodeToMessage(self, code):
        string = ctypes.create_string_buffer(100)
        self.handlePLX.PIPLX_ErrorCodeToMessage(code, ctypes.byref(string), 100)
        return self._pythonString(string.value)

    def _Check(self):
        return self.session, self.card

    #region Closing/destructor

    def Close(self):
        self.disposed = True
        self.handlePLX.PIPLX_CloseSpecifiedCard(self.session, self.card)
        return

    def __del__(self):
        if not self.disposed:
            self.Close()

    #endregion

    #region Card identity/Diagnostic

    def GetCardTemperature(self, celsius=True):
        """Get card temperature. Returns in celsius unless celsius=False, returns fahrenheit instead."""
        result = ctypes.c_double()
        # If we want celsius or fahrenheit.
        if celsius:
            corf = 0
        else:
            corf = 1

        err = self.handlePLX.PIPLX_GetCardTemperature(self.session, self.card, corf, ctypes.byref(result))

        self._handlePIPLXError(err)
        return result.value

    def getStatusMessage(self):
        status_length = 100
        status_message = ctypes.create_string_buffer(status_length)
        err = self.handlePLX.PIPLX_GetStatusMessage(self.session, self.card, ctypes.byref(status_message), status_length)
        self._handlePIPLXError(err)
        return self._pythonString(status_message.value)

    def CardId(self):
        bufferLength = 100
        cardID = ctypes.create_string_buffer(bufferLength)

        err = self.handlePLX.PIPLX_CardId(self.session, self.card, ctypes.byref(cardID), bufferLength)
        self._handlePIPLXError(err)

        return self._pythonString(cardID.value)

    def CardLoc(self):
        bus = ctypes.c_uint()
        slot = ctypes.c_uint(0)

        err = self.handlePLX.PIPLX_CardLoc(self.session, self.card, ctypes.byref(bus), ctypes.byref(slot))
        self._handlePIPLXError(err)

        return int(bus.value), int(slot.value)

    def Diagnostic(self):
        diag_string = ctypes.create_string_buffer(100)
        err = self.handlePLX.PIPLX_Diagnostic(self.session, self.card, ctypes.byref(diag_string))
        self._handlePIPLXError(err)
        return err, self._pythonString(diag_string.value)

    def EnumerateSubs(self):
        ins = ctypes.c_uint(0)
        outs = ctypes.c_uint(0)
        err = self.handlePLX.PIPLX_EnumerateSubs(self.session, self.card, ctypes.byref(ins), ctypes.byref(outs))
        self._handlePIPLXError(err)
        return int(ins.value), int(outs.value)

    def ErrorCode(self):
        err_code = ctypes.c_uint(0)
        err = self.handlePLX.PIPLX_GetLastErrorCode(self.session, ctypes.byref(err_code))
        self._handlePIPLXError(err)
        return int(err_code.value)

    def ErrorMessage(self):
        errorMessage = ctypes.create_string_buffer(100)
        err = self.handlePLX.PIPLX_GetLastErrorMessage(self.session, ctypes.byref(errorMessage), 100)
        self._handlePIPLXError(err)
        return self._pythonString(errorMessage.value)

    def Status(self):
        """Obtains the current status flags for the specified card."""
        statusFlags = self.handlePLX.PIPLX_Status(self.session, self.card)
        return statusFlags

    def SubAttribute(self, subunit, code, outputSubunit=True):
        attr = ctypes.c_uint32()
        err = self.handlePLX.PIPLX_SubAttribute(self.session,
                                                self.card,
                                                int(subunit),
                                                int(outputSubunit),
                                                int(code),
                                                ctypes.byref(attr))
        self._handlePIPLXError(err)
        return int(attr.value)

    def SubInfo(self, subunit, outputSubunit=True):
        sub_type = ctypes.c_uint(0)
        rows = ctypes.c_uint(0)
        cols = ctypes.c_uint(0)

        err = self.handlePLX.PIPLX_SubInfo(self.session,
                                           self.card,
                                           int(subunit),
                                           bool(outputSubunit),
                                           ctypes.byref(sub_type),
                                           ctypes.byref(rows),
                                           ctypes.byref(cols))
        self._handlePIPLXError(err)
        return sub_type.value, rows.value, cols.value

    def SubSize(self, sub, out_not_in):
        subtype, rows, columns = self.SubInfo(sub, out_not_in)
        bits = rows * columns
        dwords = self._calc_dwords(bits)
        return dwords, bits

    def SubStatus(self, subunit):
        status = self.handlePLX.PIPLX_SubStatus(self.session, self.card, int(subunit))
        return status

    def SubType(self, subunit, outputSubunit=True):
        subTypeString = ctypes.create_string_buffer(100)
        err = self.handlePLX.PIPLX_SubType(self.session,
                                           self.card,
                                           int(subunit),
                                           bool(outputSubunit),
                                           ctypes.byref(subTypeString),
                                           100)
        self._handlePIPLXError(err)
        return self._pythonString(subTypeString.value)

    #endregion

    #region Switching Functions
    def ClearCard(self):
        err = self.handlePLX.PIPLX_ClearCard(self.session, self.card)
        self._handlePIPLXError(err)

        return

    def ClearSub(self, subunit):

        err = self.handlePLX.PIPLX_ClearSub(self.session, self.card, int(subunit))
        self._handlePIPLXError(err)
        return

    def ClearMask(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        err = self.handlePLX.PIPLX_ClearSub(self.session, self.card, subunit)
        self._handlePIPLXError(err)
        return

    def ClosureLimit(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        limit = ctypes.c_uint(0)

        err = self.handlePLX.PIPLX_ClosureLimit(self.session, self.card, subunit, ctypes.byref(limit))
        self._handlePIPLXError(err)
        return int(limit.value)

    def MaskBit(self, subunit, bit, action):
        subunit = ctypes.c_uint32(subunit)
        bit = ctypes.c_uint32(bit)
        action = ctypes.c_bool(action)

        err = self.handlePLX.PIPLX_MaskBit(self.session, self.card, subunit, bit, action)
        self._handlePIPLXError(err)
        return

    def MaskCrosspoint(self, subunit, row, column, action):
        subunit = ctypes.c_uint32(subunit)
        row = ctypes.c_uint32(row)
        column = ctypes.c_uint32(column)
        action = ctypes.c_bool(action)

        err = self.handlePLX.PIPLX_MaskCrosspoint(self.session, self.card, subunit, row, column, action)
        self._handlePIPLXError(err)
        return

    def OpBit(self, subunit, bit, action):
        err = self.handlePLX.PIPLX_OpBit(self.session, self.card, int(subunit), int(bit), bool(action))
        self._handlePIPLXError(err)
        return

    def OpCrosspoint(self, subunit, row, column, state):
        err = self.handlePLX.PIPLX_OpCrosspoint(self.session,
                                                self.card,
                                                int(subunit),
                                                int(row),
                                                int(column),
                                                bool(state))
        self._handlePIPLXError(err)
        return

    def OpSwitch(self, subunit, switchFunc, segNum, switchNum, subswitch, action, state):
        state = ctypes.c_bool(state)

        err = self.handlePLX.PIPLX_OpSwitch(self.session,
                                            self.card,
                                            int(subunit),
                                            int(switchFunc),
                                            int(segNum),
                                            int(switchNum),
                                            int(subswitch),
                                            int(action),
                                            ctypes.byref(state))
        self._handlePIPLXError(err)
        return bool(state.value)

    def ReadBit(self, subunit, bit):
        state = ctypes.c_uint(0)
        err = self.handlePLX.PIPLX_ReadBit(self.session, self.card, int(subunit), int(bit), ctypes.byref(state))
        self._handlePIPLXError(err)
        return bool(state.value)

    def ReadSub(self, subunit):
        # get size of subunit and create an array to hold the data
        subType, rows, cols = self.SubInfo(subunit, outputSubunit=False)
        dwords = self._calc_dwords(rows * cols)

        # Array should be sized to hold number of DWORDs
        data = (ctypes.c_uint32 * dwords)()

        err = self.handlePLX.PIPLX_ReadInputSub(self.session, self.card, int(subunit), ctypes.byref(data), dwords)
        self._handlePIPLXError(err)
        return [dword for dword in data]

    def GetSubState(self, subunit):
        subType, rows, columns = self.SubInfo(subunit)
        stateData = self.ViewSub(subunit)

        state = _SubState(rows, columns, subunit, stateData)
        return state

    def GetBlankSubState(self, subunit):
        subType, rows, columns = self.SubInfo(subunit)
        stateData = [0] * self._calc_dwords(rows * columns)

        state = _SubState(rows, columns, subunit, stateData)
        return state

    def WriteSubState(self, subunit, subunitState):
        self.WriteSub(subunit, subunitState.stateData)
        return

    def SetCrosspointRange(self, subunit, row, start_col, end_col, state):
        """ 
        Sets all outputs on a row within a given range
        subunit         - Subunit to be controlled
        row         - row of the matrix to be controlled.
        start_col   - starting value of the crosspoint range
        end_col     - ending value of the crosspoint range 
        state       - 1 (energized), 0 (de-energized)
        
        This functionality IMPLEMENTED ONLY IN PYTHON WRAPPER, NOT IN THE DRIVER
        """

        subState = self.GetSubState(subunit)

        for column in range(start_col, end_col + 1):
            subState.PreSetCrosspoint(row, column, state)

        self.WriteSubState(subunit, subState)

        return

    def SettleTime(self, subunit):
        """Returns subunit relay settle time in microseconds"""
        time = ctypes.c_uint32()
        err = self.handlePLX.PIPLX_SettleTime(self.session, self.card, int(subunit), ctypes.byref(time))
        self._handlePIPLXError(err)
        return int(time.value)

    def ViewBit(self, subunit, bit):
        state = ctypes.c_bool()
        err = self.handlePLX.PIPLX_ViewBit(self.session, self.card, int(subunit), int(bit), ctypes.byref(state))
        self._handlePIPLXError(err)
        return state.value

    def ViewCrosspoint(self, subunit, row, column):
        state = ctypes.c_bool()
        err = self.handlePLX.PIPLX_ViewCrosspoint(self.session,
                                                  self.card,
                                                  int(subunit),
                                                  int(row),
                                                  int(column),
                                                  ctypes.byref(state))
        self._handlePIPLXError(err)
        return state.value

    def ViewMask(self, subunit):
        # get size of subunit and create an array to hold the data
        t, rows, cols = self.SubInfo(subunit)
        dwords = self._calc_dwords(rows * cols)
        data = (ctypes.c_uint32 * dwords)()

        err = self.handlePLX.PIPLX_ViewMask(self.session, self.card, int(subunit), ctypes.byref(data), dwords)
        self._handlePIPLXError(err)
        return [dword for dword in data]

    def ViewMaskBit(self, subunit, bit):
        state = ctypes.c_bool()
        err = self.handlePLX.PIPLX_ViewMaskBit(self.session, self.card, int(subunit), int(bit), ctypes.byref(state))
        self._handlePIPLXError(err)
        return state.value

    def ViewMaskCrosspoint(self, subunit, row, column):
        state = ctypes.c_bool()
        err = self.handlePLX.PIPLX_ViewMaskCrosspoint(self.session,
                                                      self.card,
                                                      int(subunit),
                                                      int(row),
                                                      int(column),
                                                      ctypes.byref(state))
        self._handlePIPLXError(err)
        return state.value

    def ViewSub(self, subunit):
        # get size of subunit and create an array to hold the data
        t, rows, cols = self.SubInfo(subunit)
        dwords = self._calc_dwords(rows * cols)
        data = (ctypes.c_uint32 * dwords)()

        err = self.handlePLX.PIPLX_ViewSub(self.session, self.card, int(subunit), ctypes.byref(data), dwords)
        return [dword for dword in data]

    def WriteMask(self, subunit, data):
        datalen = len(data)
        data = (ctypes.c_uint32 * datalen)(*data)

        err = self.handlePLX.PIPLX_WriteMask(self.session, self.card, int(subunit), ctypes.byref(data), datalen)
        self._handlePIPLXError(err)
        return

    def WriteSub(self, subunit, data):
        datalen = len(data)
        data = (ctypes.c_uint32 * datalen)(*data)

        err = self.handlePLX.PIPLX_WriteSub(self.session, self.card, int(subunit), ctypes.byref(data), datalen)
        self._handlePIPLXError(err)
        return

    #endregion

    #region Attenuator card functions

    def AttenType(self, subunit):
        string = ctypes.create_string_buffer(100)
        err = self.handlePLX.PIPLX_AttenType(self.session, self.card, int(subunit), ctypes.byref(string), 100)
        self._handlePIPLXError(err)
        return self._pythonString(string.value)

    def AttenInfo(self, subunit):
        size = ctypes.c_float(0.0)
        steps = ctypes.c_uint(0)
        sub_type = ctypes.c_uint(0)

        err = self.handlePLX.PIPLX_AttenInfo(self.session,
                                             self.card,
                                             int(subunit),
                                             ctypes.byref(sub_type),
                                             ctypes.byref(steps),
                                             ctypes.byref(size))
        self._handlePIPLXError(err)
        return sub_type.value, steps.value, size.value

    def SetAttenuation(self, subunit, attenuation):
        err = self.handlePLX.PIPLX_AttenSetAttenuation(self.session, self.card, int(subunit), float(attenuation))
        self._handlePIPLXError(err)
        return

    def GetAttenuation(self, subunit):
        attenuation = ctypes.c_float(0.0)
        err = self.handlePLX.PIPLX_AttenGetAttenuation(self.session, self.card, int(subunit), ctypes.byref(attenuation))
        self._handlePIPLXError(err)
        return attenuation.value

    def PadValue(self, subunit, padNum):
        attenuation = ctypes.c_float(0.0)
        err = self.handlePLX.PIPLX_AttenPadValue(self.session, self.card, int(subunit), int(padNum), ctypes.byref(attenuation))
        self._handlePIPLXError(err)
        return attenuation.value

    #endregion

    #region Calibration functions

    def ReadCal(self, subunit, index):
        data = ctypes.c_uint32()
        subunit= ctypes.c_uint32(subunit)
        index = ctypes.c_uint32(index)

        err = self.handlePLX.PIPLX_ReadCal(self.session, self.card, subunit, index, ctypes.byref(data))
        self._handlePIPLXError(err)

        return int(data.value)


    def WriteCal(self, subunit, index, data):
        subunit = ctypes.c_uint32(subunit)
        index = ctypes.c_uint32(index)
        data = ctypes.c_uint32(data)

        err = self.handlePLX.PIPLX_WriteCal(self.session, self.card, subunit, index, data)
        self._handlePIPLXError(err)

        return

    def ReadCalFP(self, subunit, store, offset, numValues):
        subunit = ctypes.c_uint32(subunit)
        store = ctypes.c_uint32(store)
        offset = ctypes.c_uint32(offset)
        numValues = ctypes.c_uint32(numValues)

        data = (ctypes.c_double * numValues)()

        err = self.handlePLX.PIPLX_ReadCalFP(self.session,
                                             self.card,
                                             subunit,
                                             store,
                                             offset,
                                             numValues,
                                             ctypes.byref(data))
        self._handlePIPLXError(err)

        return [val.value for val in data]

    def WriteCalFP(self, subunit, store, offset, data):
        subunit = ctypes.c_uint32(subunit)
        store = ctypes.c_uint32(store)
        offset = ctypes.c_uint32(offset)
        numValues = ctypes.c_uint32(len(data))

        data = (ctypes.c_double * numValues.value)(*data)

        err = self.handlePLX.PIPLX_WriteCalFP(self.session,
                                              self.card,
                                              subunit,
                                              store,
                                              offset,
                                              numValues,
                                              data)
        self._handlePIPLXError(err)

        return

    def WriteCalDate(self, subunit, store, interval):
        subunit = ctypes.c_uint32(subunit)
        store = ctypes.c_uint32(store)
        interval = ctypes.c_uint32(interval)

        err = self.handlePLX.PIPLX_WriteCalDate(self.session,
                                                self.card,
                                                subunit,
                                                store,
                                                interval)
        self._handlePIPLXError(err)

        return

    def ReadCalDate(self, subunit, store):
        subunit = ctypes.c_uint32(subunit)
        store = ctypes.c_uint32(store)

        year = ctypes.c_uint32()
        day = ctypes.c_uint32()
        interval = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_ReadCalDate(self.session,
                                               self.card,
                                               subunit,
                                               store,
                                               ctypes.byref(year),
                                               ctypes.byref(day),
                                               ctypes.byref(interval))
        self._handlePIPLXError(err)

        return year.value, day.value, interval.value

    def SetCalPoint(self, subunit, index):
        subunit = ctypes.c_uint32(subunit)
        index = ctypes.c_uint32(index)

        err = self.handlePLX.PIPLX_SetCalPoint(self.session,
                                               self.card,
                                               subunit,
                                               index)
        self._handlePIPLXError(err)

        return 

    #endregion

    #region PSU card functions

    def PsuType(self, subunit):
        string = ctypes.create_string_buffer(100)
        err = self.handlePLX.PIPLX_PsuType(self.session, self.card, int(subunit), ctypes.byref(string), 100)
        self._handlePIPLXError(err)
        return self._pythonString(string.value)

    def PsuInfo(self, subunit):
        sub_type = ctypes.c_uint(0)
        volts = ctypes.c_double(0.0)
        amps = ctypes.c_double(0.0)
        precis = ctypes.c_uint(0)
        capb = ctypes.c_uint(0)

        err = self.handlePLX.PIPLX_PsuInfo(self.session,
                                           self.card,
                                           int(subunit),
                                           ctypes.byref(sub_type),
                                           ctypes.byref(volts),
                                           ctypes.byref(amps),
                                           ctypes.byref(precis),
                                           ctypes.byref(capb))
        self._handlePIPLXError(err)
        return sub_type.value, volts.value, amps.value, precis.value, capb.value

    def PsuGetVoltage(self, subunit):
        volts = ctypes.c_double(0.0)

        err = self.handlePLX.PIPLX_PsuGetVoltage(self.session, self.card, subunit, ctypes.byref(volts))
        self._handlePIPLXError(err)
        return volts.value

    def PsuSetVoltage(self, subunit, voltage):
        voltage = ctypes.c_double(voltage)
        err = self.handlePLX.PIPLX_PsuSetVoltage(self.session, self.card, int(subunit), voltage)
        self._handlePIPLXError(err)
        return

    def PsuEnable(self, subunit, enable):
        err = self.handlePLX.PIPLX_PsuEnable(self.session, self.card, int(subunit), bool(enable))
        self._handlePIPLXError(err)
        return
    #endregion

    #region Battery Simulator Functions

    def BattSetVoltage(self, subunit, voltage):
        voltage = ctypes.c_double(voltage)
        err = self.handlePLX.PIPLX_BattSetVoltage(self.session, self.card, int(subunit), voltage)
        self._handlePIPLXError(err)
        return

    def BattGetVoltage(self, subunit):
        volts = ctypes.c_double(0.0)
        err = self.handlePLX.PIPLX_BattGetVoltage(self.session, self.card, int(subunit), ctypes.byref(volts))
        self._handlePIPLXError(err)
        return volts.value

    def BattSetCurrent(self, subunit, current):
        current = ctypes.c_double(current)
        err = self.handlePLX.PIPLX_BattSetCurrent(self.session, self.card, int(subunit), current)
        self._handlePIPLXError(err)
        return

    def BattGetCurrent(self, subunit):
        current = ctypes.c_double(0.0)
        err = self.handlePLX.PIPLX_BattGetCurrent(self.session, self.card, int(subunit), ctypes.byref(current))
        self._handlePIPLXError(err)
        return current.value

    def BattSetEnable(self, subunit, state):
        subunit = ctypes.c_uint32(subunit)
        state = ctypes.c_uint32(state)
        err = self.handlePLX.PIPLX_BattSetEnable(self.session, self.card, subunit, state)
        self._handlePIPLXError(err)
        return

    def BattGetEnable(self, subunit):
        state = ctypes.c_uint(0)
        err = self.handlePLX.PIPLX_BattGetEnable(self.session, self.card, int(subunit), ctypes.byref(state))
        self._handlePIPLXError(err)
        return bool(state.value)

    def BattReadInterlockState(self, subunit):
        state = ctypes.c_bool()
        err = self.handlePLX.PIPLX_BattReadInterlockState(self.session, self.card, int(subunit), ctypes.byref(state))
        self._handlePIPLXError(err)
        return state.value

    def BattMeasureVoltage(self, subunit):
        """Measures actual voltage value on supported Battery Simulator cards."""

        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        voltage = ctypes.c_double(0)

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.VOLTAGE_V,
                                                ctypes.byref(voltage), ctypes.sizeof(voltage))
        self._handlePIPLXError(err)

        return voltage.value

    def BattMeasureCurrentmA(self, subunit):
        """Measures actual current value in milliamps on supported Battery Simulator cards."""

        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        currentmA = ctypes.c_double()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.CURRENT_MA,
                                                ctypes.byref(currentmA), ctypes.sizeof(currentmA))
        self._handlePIPLXError(err)

        return currentmA.value

    def BattMeasureCurrentA(self, subunit):
        """Measures actual current value in amps on supported Battery Simulator cards."""

        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        current = ctypes.c_double()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.CURRENT_A,
                                                ctypes.byref(current), ctypes.sizeof(current))
        self._handlePIPLXError(err)

        return current.value

    def BattSetMeasureConfig(self,
                             subunit,
                             numOfSamples,
                             VConversionTimePerSample,
                             IConversionTimePerSample,
                             ModeOfOperation):

        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)

        measureConfig = ((numOfSamples & 0x7)
                         | ((IConversionTimePerSample & 0x7) << 6)
                         | ((VConversionTimePerSample & 0x7) << 9)
                         | ((ModeOfOperation & 0xF) << 12))

        measureConfig = ctypes.c_uint32(measureConfig)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.MEASURE_CONFIG,
                                                ctypes.byref(measureConfig), ctypes.sizeof(measureConfig))
        self._handlePIPLXError(err)

        return

    def BattSetMeasureSet(self, subunit, enabled):

        subunit = ctypes.c_uint32(subunit)
        enabled = ctypes.c_bool(enabled)
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.C_SET_MEASURE_SET,
                                                ctypes.byref(enabled), ctypes.sizeof(enabled))
        self._handlePIPLXError(err)

        return

    def BattQuerySetMeasureSet(self, subunit):

        subunit = ctypes.c_uint32(subunit)
        enabled = ctypes.c_bool(0)
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.C_SET_MEASURE_SET,
                                                ctypes.byref(enabled), ctypes.sizeof(enabled))
        self._handlePIPLXError(err)

        return enabled.value

    def BattSetLoad(self, subunit, load):

        subunit = ctypes.c_uint32(subunit)
        load = ctypes.c_uint32(load)
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.LOAD,
                                                ctypes.byref(load), ctypes.sizeof(load))
        self._handlePIPLXError(err)

        return

    #endregion

    #region Resistor Functions

    def ResSetResistance(self, subunit, resistance, mode=RES_Mode.SET):
        resistance = ctypes.c_double(resistance)
        subunit = ctypes.c_uint32(subunit)
        mode = ctypes.c_uint32(mode)

        err = self.handlePLX.PIPLX_ResSetResistance(self.session, self.card, subunit, mode, resistance)
        self._handlePIPLXError(err)
        return

    def ResGetResistance(self, subunit):
        resistance = ctypes.c_double(0.0)

        err = self.handlePLX.PIPLX_ResGetResistance(self.session, self.card, int(subunit), ctypes.byref(resistance))
        self._handlePIPLXError(err)
        return resistance.value

    def ResInfo(self, subunit):
        min_res = ctypes.c_double(0.0)
        max_res = ctypes.c_double(0.0)
        ref_res = ctypes.c_double(0.0)
        prec_pc = ctypes.c_double(0.0)
        prec_delta = ctypes.c_double(0.0)
        int1 = ctypes.c_double(0.0)
        int1_delta = ctypes.c_double(0.0)
        caps = ctypes.c_uint32(0)

        err = self.handlePLX.PIPLX_ResInfo(self.session,
                                           self.card,
                                           int(subunit),
                                           ctypes.byref(min_res),
                                           ctypes.byref(max_res),
                                           ctypes.byref(ref_res),
                                           ctypes.byref(prec_pc),
                                           ctypes.byref(prec_delta),
                                           ctypes.byref(int1),
                                           ctypes.byref(int1_delta),
                                           ctypes.byref(caps))

        self._handlePIPLXError(err)
        return {"MinRes": min_res.value,
                "MaxRes": max_res.value,
                "RefRes": ref_res.value,
                "PrecPC": prec_pc.value,
                "PrecDelta": prec_delta.value,
                "Int1": int1.value,
                "IntDelta": int1_delta.value,
                "Capabilities": caps.value}
    #endregion

    #region Voltage Source (VSOURCE type) specific functions

    def VsourceSetVoltage(self, subunit, voltage):
        voltage = ctypes.c_double(voltage)
        err = self.handlePLX.PIPLX_VsourceSetVoltage(self.session, self.card, subunit, voltage)
        self._handlePIPLXError(err)
        return

    def VsourceGetVoltage(self, subunit):
        voltage = ctypes.c_double(0.0)
        err = self.handlePLX.PIPLX_VsourceGetVoltage(self.session, self.card, int(subunit), ctypes.byref(voltage))
        self._handlePIPLXError(err)
        return voltage.value

    def VsourceSetRange(self, subunit, ts_range):
        err = self.ERRORCODE["ER_BAD_RANGE"]
        isoutsub = True
        if ts_range in self.TS_RANGE.values():
            tsrng = ctypes.c_uint(ts_range)
            err = self.handlePLX.PIPLX_SetAttribute(self.session, self.card, int(subunit), isoutsub,
                                                    self.ATTR["TS_SET_RANGE"], ctypes.byref(tsrng), ctypes.sizeof(tsrng))
        self._handlePIPLXError(err)
        return

    def VsourceGetRange(self, subunit):
        isoutsub = True
        ts_range = ctypes.c_uint(0)
        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, int(subunit), isoutsub,
                                                self.ATTR["TS_SET_RANGE"], ctypes.byref(ts_range), ctypes.sizeof(ts_range))
        self._handlePIPLXError(err)
        return ts_range.value

    def VsourceInfo(self, subunit):
        is_output = True
        subunit = int(subunit)


        low_range_min = ctypes.c_double(0.0)
        low_range_med = ctypes.c_double(0.0)
        low_range_max = ctypes.c_double(0.0)
        low_range_max_dev = ctypes.c_double(0.0)
        low_range_prec_pc = ctypes.c_double(0.0)
        low_range_prec_delta = ctypes.c_double(0.0)

        med_range_min = ctypes.c_double(0.0)
        med_range_med = ctypes.c_double(0.0)
        med_range_max = ctypes.c_double(0.0)
        med_range_max_dev = ctypes.c_double(0.0)
        med_range_prec_pc = ctypes.c_double(0.0)
        med_range_prec_delta = ctypes.c_double(0.0)

        high_range_min = ctypes.c_double(0.0)
        high_range_med = ctypes.c_double(0.0)
        high_range_max = ctypes.c_double(0.0)
        high_range_max_dev = ctypes.c_double(0.0)
        high_range_prec_pc = ctypes.c_double(0.0)
        high_range_prec_delta = ctypes.c_double(0.0)

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_LOW_RANGE_MIN"],
                                                ctypes.byref(low_range_min),
                                                ctypes.sizeof(low_range_min)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_LOW_RANGE_MED"],
                                                ctypes.byref(low_range_med),
                                                ctypes.sizeof(low_range_med)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_LOW_RANGE_MAX"],
                                                ctypes.byref(low_range_max),
                                                ctypes.sizeof(low_range_max)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_LOW_RANGE_MAX_DEV"],
                                                ctypes.byref(low_range_max_dev),
                                                ctypes.sizeof(low_range_max_dev)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_LOW_RANGE_PREC_PC"],
                                                ctypes.byref(low_range_prec_pc),
                                                ctypes.sizeof(low_range_prec_pc)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_LOW_RANGE_PREC_DELTA"],
                                                ctypes.byref(low_range_prec_delta),
                                                ctypes.sizeof(low_range_prec_delta)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_MED_RANGE_MIN"],
                                                ctypes.byref(med_range_min),
                                                ctypes.sizeof(med_range_min)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_MED_RANGE_MED"],
                                                ctypes.byref(med_range_med),
                                                ctypes.sizeof(med_range_med)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_MED_RANGE_MAX"],
                                                ctypes.byref(med_range_max),
                                                ctypes.sizeof(med_range_max)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_MED_RANGE_MAX_DEV"],
                                                ctypes.byref(med_range_max_dev),
                                                ctypes.sizeof(med_range_max_dev)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_MED_RANGE_PREC_PC"],
                                                ctypes.byref(med_range_prec_pc),
                                                ctypes.sizeof(med_range_prec_pc)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_MED_RANGE_PREC_DELTA"],
                                                ctypes.byref(med_range_prec_delta),
                                                ctypes.sizeof(med_range_prec_delta)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_HIGH_RANGE_MIN"],
                                                ctypes.byref(high_range_min),
                                                ctypes.sizeof(high_range_min)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_HIGH_RANGE_MED"],
                                                ctypes.byref(high_range_med),
                                                ctypes.sizeof(high_range_med)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_HIGH_RANGE_MAX"],
                                                ctypes.byref(high_range_max),
                                                ctypes.sizeof(high_range_max)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_HIGH_RANGE_MAX_DEV"],
                                                ctypes.byref(high_range_max_dev),
                                                ctypes.sizeof(high_range_max_dev)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_HIGH_RANGE_PREC_PC"],
                                                ctypes.byref(high_range_prec_pc),
                                                ctypes.sizeof(high_range_prec_pc)
                                                )

        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, subunit,
                                                is_output,
                                                self.ATTR["TS_HIGH_RANGE_PREC_DELTA"],
                                                ctypes.byref(high_range_prec_delta),
                                                ctypes.sizeof(high_range_prec_delta)
                                                )

        self._handlePIPLXError(err)
        return {"LOW_RANGE_MIN": low_range_min.value,
                "LOW_RANGE_MED": low_range_med.value,
                "LOW_RANGE_MAX": low_range_max.value,
                "LOW_RANGE_MAX_DEV": low_range_max_dev.value,
                "LOW_RANGE_PREC_PC": low_range_prec_pc.value,
                "LOW_RANGE_PREC_DELTA": low_range_prec_delta.value,
                "MED_RANGE_MIN": med_range_min.value,
                "MED_RANGE_MED": med_range_med.value,
                "MED_RANGE_MAX": med_range_max.value,
                "MED_RANGE_MAX_DEV": med_range_max_dev.value,
                "MED_RANGE_PREC_PC": med_range_prec_pc.value,
                "MED_RANGE_PREC_DELTA": med_range_prec_delta.value,
                "HIGH_RANGE_MIN": high_range_min.value,
                "HIGH_RANGE_MED": high_range_med.value,
                "HIGH_RANGE_MAX": high_range_max.value,
                "HIGH_RANGE_MAX_DEV": high_range_max_dev.value,
                "HIGH_RANGE_PREC_PC": high_range_prec_pc.value,
                "HIGH_RANGE_PREC_DELTA": high_range_prec_delta.value}

    def VsourceGetTemperature(self, unit):
        err = self.ERRORCODE["ER_BAD_ATTR_CODE"]
        is_output = True
        sub = 1
        temperatures = (ctypes.c_double * 4)(0.0, 0.0, 0.0, 0.0)
        if unit == self.ATTR["TS_TEMPERATURES_C"] or unit == self.ATTR["TS_TEMPERATURES_F"]:
            err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, sub,
                                                    is_output,
                                                    unit,
                                                    ctypes.byref(temperatures),
                                                    ctypes.sizeof(temperatures))

        self._handlePIPLXError(err)
        return [temp for temp in temperatures]
    #endregion

    #region VDT/Resolver Functions

    def GetCurrentmA(self, subunit):
        current = ctypes.c_double()
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.CURRENT_MA,
                                                ctypes.byref(current))
        self._handlePIPLXError(err)

        return current.value

    def SetVoltageV(self, subunit, voltage):
        voltage = ctypes.c_uint32(voltage)
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VOLTAGE_V"],
                                                ctypes.byref(voltage),
                                                ctypes.sizeof(voltage))
        self._handlePIPLXError(err)

        return

    def GetVoltageV(self, subunit):
        voltage = ctypes.c_uint32()
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VOLTAGE_V"],
                                                ctypes.byref(voltage),
                                                ctypes.sizeof(voltage))
        self._handlePIPLXError(err)
        return float(voltage.value)

    def ResolverSetStartStopRotate(self, subunit, state):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)

        if state:
            state = ctypes.c_uint32(1)
        else:
            state = ctypes.c_uint32(0)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.RESOLVER_START_STOP_ROTATE,
                                                ctypes.byref(state),
                                                ctypes.sizeof(state))
        self._handlePIPLXError(err)

        return

    def ResolverGetStartStopRotate(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        result = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.RESOLVER_START_STOP_ROTATE,
                                                ctypes.byref(result),
                                                ctypes.sizeof(result))

        self._handlePIPLXError(err)

        return bool(result.value)

    def ResolverSetNumOfTurns(self, subunit, turns):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        turns = ctypes.c_uint16(turns)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.RESOLVER_NUM_OF_TURNS,
                                                ctypes.byref(turns),
                                                ctypes.sizeof(turns))
        self._handlePIPLXError(err)

        return

    def ResolverGetNumOfTurns(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        turns = ctypes.c_uint16()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.RESOLVER_NUM_OF_TURNS,
                                                ctypes.byref(turns),
                                                ctypes.sizeof(turns))
        self._handlePIPLXError(err)

        return float(turns.value)

    def ResolverSetRotateSpeed(self, subunit, speed):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        speed = ctypes.c_double(speed)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.RESOLVER_ROTATE_SPEED,
                                                ctypes.byref(speed),
                                                ctypes.sizeof(speed))
        self._handlePIPLXError(err)

        return

    def ResolverGetRotateSpeed(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        speed = ctypes.c_double()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.RESOLVER_ROTATE_SPEED,
                                                ctypes.byref(speed),
                                                ctypes.sizeof(speed))
        self._handlePIPLXError(err)

        return float(speed.value)

    def ResolverSetPosition(self, subunit, position):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        position = ctypes.c_double(position)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.RESOLVER_POSITION,
                                                ctypes.byref(position),
                                                ctypes.sizeof(position))
        self._handlePIPLXError(err)

        return

    def ResolverGetPosition(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        position = ctypes.c_double()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.RESOLVER_POSITION,
                                                ctypes.byref(position),
                                                ctypes.sizeof(position))
        self._handlePIPLXError(err)

        return float(position.value)

    def ResolverSetPosition0To360(self, subunit, position):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        position = ctypes.c_double(position)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.RESOLVER_POSITION_0_360,
                                                ctypes.byref(position),
                                                ctypes.sizeof(position))
        self._handlePIPLXError(err)

        return

    def ResolverGetPosition0To360(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        position = ctypes.c_double()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                Attributes.RESOLVER_POSITION_0_360,
                                                ctypes.byref(position),
                                                ctypes.sizeof(position))
        self._handlePIPLXError(err)

        return position.value

    def VDTSetInputAtten(self, subunit, attenuation):
        attenuation = ctypes.c_uint32(attenuation)
        is_output = True

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                int(subunit),
                                                is_output,
                                                self.ATTR["VDT_AUTO_INPUT_ATTEN"],
                                                ctypes.byref(attenuation),
                                                ctypes.sizeof(attenuation))
        self._handlePIPLXError(err)
        return

    def VDTGetInputAtten(self, subunit):
        attenuation = ctypes.c_uint32()
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_AUTO_INPUT_ATTEN"],
                                                ctypes.byref(attenuation),
                                                ctypes.sizeof(attenuation))
        self._handlePIPLXError(err)
        return int(attenuation.value)

    def VDTSetABSPosition(self, subunit, position):
        position = ctypes.c_uint32(position)
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_ABS_POSITION"],
                                                ctypes.byref(position),
                                                ctypes.sizeof(position))
        self._handlePIPLXError(err)
        return

    def VDTGetABSPosition(self, subunit):
        position = ctypes.c_uint32()
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_ABS_POSITION"],
                                                ctypes.byref(position),
                                                ctypes.sizeof(position))
        self._handlePIPLXError(err)
        return int(position.value)

    def VDTSetABSPositionB(self, subunit, position):
        position = ctypes.c_uint32(position)
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_ABS_POSITION_B"],
                                                ctypes.byref(position),
                                                ctypes.sizeof(position))
        self._handlePIPLXError(err)
        return

    def VDTGetABSPositionB(self, subunit):
        position = ctypes.c_uint32()
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_ABS_POSITION_B"],
                                                ctypes.byref(position),
                                                ctypes.sizeof(position))
        self._handlePIPLXError(err)
        return int(position.value)

    def VDTSetPercentPosition(self, subunit, position):
        position = ctypes.c_double(position)
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_PERCENT_POSITION"],
                                                ctypes.byref(position),
                                                ctypes.sizeof(position))
        self._handlePIPLXError(err)
        return

    def VDTGetPercentPosition(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        position = ctypes.c_double()
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_PERCENT_POSITION"],
                                                ctypes.byref(position),
                                                ctypes.sizeof(position))
        self._handlePIPLXError(err)
        return int(position.value)

    def VDTSetPercentPositionB(self, subunit, position):
        position = ctypes.c_double(position)
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_PERCENT_POSITION_B"],
                                                ctypes.byref(position),
                                                ctypes.sizeof(position))
        self._handlePIPLXError(err)
        return

    def VDTGetPercentPositionB(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        position = ctypes.c_double()
        is_output = ctypes.c_uint32(1)

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_PERCENT_POSITION_B"],
                                                ctypes.byref(position),
                                                ctypes.sizeof(position))
        self._handlePIPLXError(err)
        return int(position.value)

    def VDTSetVsum(self, subunit, vsum):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        vsum = ctypes.c_double(vsum)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_VOLTAGE_SUM"],
                                                ctypes.byref(vsum),
                                                ctypes.sizeof(vsum))
        self._handlePIPLXError(err)
        return

    def VDTGetVsum(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        vsum = ctypes.c_double()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_VOLTAGE_SUM"],
                                                ctypes.byref(vsum),
                                                ctypes.sizeof(vsum))
        self._handlePIPLXError(err)
        return float(vsum.value)

    def VDTSetVdiff(self, subunit, vdiff):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        vdiff = ctypes.c_double(vdiff)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_VOLTAGE_DIFF"],
                                                ctypes.byref(vdiff),
                                                ctypes.sizeof(vdiff))
        self._handlePIPLXError(err)
        return

    def VDTGetVdiff(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        vdiff = ctypes.c_double()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_VOLTAGE_DIFF"],
                                                ctypes.byref(vdiff),
                                                ctypes.sizeof(vdiff))
        self._handlePIPLXError(err)
        return float(vdiff.value)

    def VDTSetOutGain(self, subunit, outgain):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        outgain = ctypes.c_uint32(outgain)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_OUT_GAIN"],
                                                ctypes.byref(outgain),
                                                ctypes.sizeof(outgain))
        self._handlePIPLXError(err)
        return

    def VDTGetOutGain(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        outgain = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_OUT_GAIN"],
                                                ctypes.byref(outgain),
                                                ctypes.sizeof(outgain))
        self._handlePIPLXError(err)
        return int(outgain.value)

    def VDTSetManualInputAtten(self, subunit, attenuation):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        attenuation = ctypes.c_uint32(attenuation)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_MANUAL_INPUT_ATTEN"],
                                                ctypes.byref(attenuation),
                                                ctypes.sizeof(attenuation))
        self._handlePIPLXError(err)
        return

    def VDTGetManualInputAtten(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        attenuation = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_MANUAL_INPUT_ATTEN"],
                                                ctypes.byref(attenuation),
                                                ctypes.sizeof(attenuation))
        self._handlePIPLXError(err)
        return int(attenuation.value)

    def VDTSetMode(self, subunit, mode):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        mode = ctypes.c_uint32(mode)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_MODE"],
                                                ctypes.byref(mode),
                                                ctypes.sizeof(mode))
        self._handlePIPLXError(err)
        return

    def VDTGetMode(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        mode = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_MODE"],
                                                ctypes.byref(mode),
                                                ctypes.sizeof(mode))
        self._handlePIPLXError(err)
        return int(mode.value)

    def VDTSetDelayA(self, subunit, delay):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        delay = ctypes.c_uint32(delay)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_DELAY_A"],
                                                ctypes.byref(delay),
                                                ctypes.sizeof(delay))
        self._handlePIPLXError(err)
        return

    def VDTGetDelayA(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        delay = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_DELAY_A"],
                                                ctypes.byref(delay),
                                                ctypes.sizeof(delay))
        self._handlePIPLXError(err)
        return int(delay.value)

    def VDTSetDelayB(self, subunit, delay):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        delay = ctypes.c_uint32(delay)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_DELAY_B"],
                                                ctypes.byref(delay),
                                                ctypes.sizeof(delay))
        self._handlePIPLXError(err)
        return

    def VDTGetDelayB(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        delay = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_DELAY_B"],
                                                ctypes.byref(delay),
                                                ctypes.sizeof(delay))
        self._handlePIPLXError(err)
        return int(delay.value)

    def VDTSetInputLevel(self, subunit, level):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        level = ctypes.c_uint32(level)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_INPUT_LEVEL"],
                                                ctypes.byref(level),
                                                ctypes.sizeof(level))
        self._handlePIPLXError(err)
        return

    def VDTGetInputLevel(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        level = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_INPUT_LEVEL"],
                                                ctypes.byref(level),
                                                ctypes.sizeof(level))
        self._handlePIPLXError(err)
        return int(level.value)

    def VDTSetInputFreq(self, subunit, freq):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        freq = ctypes.c_uint32(freq)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_INPUT_FREQ"],
                                                ctypes.byref(freq),
                                                ctypes.sizeof(freq))
        self._handlePIPLXError(err)
        return

    def VDTGetInputFreq(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        freq = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_INPUT_FREQ"],
                                                ctypes.byref(freq),
                                                ctypes.sizeof(freq))
        self._handlePIPLXError(err)
        return int(freq.value)

    def VDTSetOutLevel(self, subunit, level):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        level = ctypes.c_uint32(level)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_OUT_LEVEL"],
                                                ctypes.byref(level),
                                                ctypes.sizeof(level))
        self._handlePIPLXError(err)
        return

    def VDTGetOutLevel(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        level = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_OUT_LEVEL"],
                                                ctypes.byref(level),
                                                ctypes.sizeof(level))
        self._handlePIPLXError(err)
        return int(level.value)

    # LVDT mk2 Get only
    def VDTGetDSPICVersion(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        version = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_DSPIC_VERSION"],
                                                ctypes.byref(version),
                                                ctypes.sizeof(version))
        self._handlePIPLXError(err)
        return int(version.value)

    # LVDT mk2 Set/Get
    def VDTSetInvertA(self, subunit, state):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        state = ctypes.c_uint32(state)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_INVERT_A"],
                                                ctypes.byref(state),
                                                ctypes.sizeof(state))
        self._handlePIPLXError(err)
        return

    def VDTGetInvertA(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        state = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_INVERT_A"],
                                                ctypes.byref(state),
                                                ctypes.sizeof(state))
        self._handlePIPLXError(err)
        return int(state.value)

    def VDTSetInvertB(self, subunit, state):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        state = ctypes.c_uint32(state)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_INVERT_B"],
                                                ctypes.byref(state),
                                                ctypes.sizeof(state))
        self._handlePIPLXError(err)
        return

    def VDTGetInvertB(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        state = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_INVERT_B"],
                                                ctypes.byref(state),
                                                ctypes.sizeof(state))
        self._handlePIPLXError(err)
        return int(state.value)

    def VDTSetPhaseTracking(self, subunit, state):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        state = ctypes.c_uint32(state)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_PHASE_TRACKING"],
                                                ctypes.byref(state),
                                                ctypes.sizeof(state))
        self._handlePIPLXError(err)
        return

    def VDTGetPhaseTracking(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        state = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_PHASE_TRACKING"],
                                                ctypes.byref(state),
                                                ctypes.sizeof(state))
        self._handlePIPLXError(err)
        return int(state.value)

    def VDTSetSampleLoad(self, subunit, dword):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        dword = ctypes.c_uint32(dword)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_SAMPLE_LOAD"],
                                                ctypes.byref(dword),
                                                ctypes.sizeof(dword))
        self._handlePIPLXError(err)
        return

    def VDTGetInputFreqHiRes(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        freq = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_INPUT_FREQ_HI_RES"],
                                                ctypes.byref(freq),
                                                ctypes.sizeof(freq))
        self._handlePIPLXError(err)
        return int(freq.value)

    def VDTSetLOSThreshold(self, subunit, threshold):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        threshold = ctypes.c_uint32(threshold)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_LOS_THRESHOLD"],
                                                ctypes.byref(threshold),
                                                ctypes.sizeof(threshold))
        self._handlePIPLXError(err)
        return

    def VDTGetLOSThreshold(self, subunit, threshold):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        threshold = ctypes.c_uint32()


        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_LOS_THRESHOLD"],
                                                ctypes.byref(threshold),
                                                ctypes.sizeof(threshold))
        self._handlePIPLXError(err)
        return int(threshold.value)

    def VDTSetSampleBufferSize(self, subunit, size):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        size = ctypes.c_uint32(size)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_SMPL_BUFFER_SIZE"],
                                                ctypes.byref(size),
                                                ctypes.sizeof(size))
        self._handlePIPLXError(err)
        return

    def VDTGetSampleBufferSize(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        size = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_SMPL_BUFFER_SIZE"],
                                                ctypes.byref(size),
                                                ctypes.sizeof(size))
        self._handlePIPLXError(err)
        return int(size.value)

    def VDTSetNullOffset(self, subunit, offset):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        offset = ctypes.c_uint16(offset)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_NULL_OFFSET"],
                                                ctypes.byref(offset),
                                                ctypes.sizeof(offset))
        self._handlePIPLXError(err)
        return

    def VDTGetNullOffset(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        offset = ctypes.c_uint16()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_NULL_OFFSET"],
                                                ctypes.byref(offset),
                                                ctypes.sizeof(offset))
        self._handlePIPLXError(err)
        return int(offset.value)

    # LVDT Get only
    def VDTGetStatus(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        status = ctypes.c_uint8()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_STATUS"],
                                                ctypes.byref(status),
                                                ctypes.sizeof(status))
        self._handlePIPLXError(err)
        return int(status.value)

    def VDTGetMaxOutputVoltage(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        voltage = ctypes.c_double()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_MAX_OUT_VOLTAGE"],
                                                ctypes.byref(voltage),
                                                ctypes.sizeof(voltage))
        self._handlePIPLXError(err)
        return float(voltage.value)

    def VDTGetMinOutputVoltage(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        voltage = ctypes.c_double()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_MIN_OUT_VOLTAGE"],
                                                ctypes.byref(voltage),
                                                ctypes.sizeof(voltage))
        self._handlePIPLXError(err)
        return float(voltage.value)

    def VDTGetMaxInputVoltage(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        voltage = ctypes.c_double()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_MAX_IN_VOLTAGE"],
                                                ctypes.byref(voltage),
                                                ctypes.sizeof(voltage))
        self._handlePIPLXError(err)
        return float(voltage.value)

    def VDTGetMinInputVoltage(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        is_output = ctypes.c_uint32(1)
        voltage = ctypes.c_double()

        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                is_output,
                                                self.ATTR["VDT_MIN_IN_VOLTAGE"],
                                                ctypes.byref(voltage),
                                                ctypes.sizeof(voltage))
        self._handlePIPLXError(err)
        return float(voltage.value)

    #endregion

    #region Get/Set attributes

    # Gets value for certain attributes (Integer only)
    def GetAttribute(self, subunit, outputSubunit, attrCode):
        """Obtain the value of a specific attribute"""
        attr = ctypes.c_uint(0)
        attr_length = ctypes.sizeof(attr)
        err = self.handlePLX.PIPLX_GetAttribute(self.session,
                                                self.card,
                                                int(subunit),
                                                bool(outputSubunit),
                                                int(attrCode),
                                                ctypes.byref(attr),
                                                attr_length)
        self._handlePIPLXError(err)
        return attr.value

    def SetAttribute(self, subunit, outputSubunit, attrCode, attr):
        """Sets the value of a specific attribute"""
        attribute = ctypes.c_uint(attr)
        attr_length = ctypes.sizeof(attribute)
        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                int(subunit),
                                                bool(outputSubunit),
                                                int(attrCode),
                                                ctypes.byref(attribute),
                                                attr_length)
        self._handlePIPLXError(err)
        return

    #endregion

    #region Current Loop Simulator functions

    def CLSetMode(self, subunit, mode):
        mode = ctypes.c_uint32(mode)
        subunit = ctypes.c_uint32(subunit)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                1,
                                                0x401,
                                                ctypes.byref(mode),
                                                ctypes.sizeof(mode))
        self._handlePIPLXError(err)

        return

    def CLSetCurrent(self, subunit, current):
        current = ctypes.c_double(current)
        subunit = ctypes.c_uint32(subunit)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                1,
                                                0x440,
                                                ctypes.byref(current),
                                                ctypes.sizeof(current))
        self._handlePIPLXError(err)

        return

    def CLSetVoltage(self, subunit, voltage):
        voltage = ctypes.c_double(voltage)
        subunit = ctypes.c_uint32(subunit)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                1,
                                                0x441,
                                                ctypes.byref(voltage),
                                                ctypes.sizeof(voltage))
        self._handlePIPLXError(err)

        return

    def CLSetSlewRate(self, subunit, slewRate):
        slewRate = ctypes.c_uint8(slewRate)
        subunit = ctypes.c_uint32(subunit)

        err = self.handlePLX.PIPLX_SetAttribute(self.session,
                                                self.card,
                                                subunit,
                                                1,
                                                0x442,
                                                ctypes.byref(slewRate),
                                                ctypes.sizeof(slewRate))
        self._handlePIPLXError(err)

        return

    #endregion

    #region DIO card functions

    def DioCheckPortDisabled(self, subunit):
        subunit = ctypes.c_uint32()
        portDisabled = ctypes.c_bool()

        err = self.handlePLX.PIPLX_DioCheckPortDisabled(self.session,
                                                        self.card,
                                                        subunit,
                                                        ctypes.byref(portDisabled))
        self._handlePIPLXError(err)

        return portDisabled.value

    def DioDownloadPatternFile(self, filename):
        filename = self._stringToStr(filename)

        err = self.handlePLX.PIPLX_DioDownloadPatternFile(self.session,
                                                          self.card,
                                                          filename)
        self._handlePIPLXError(err)

        return

    def DioGetChannelDirection(self, subunit, channel):
        subunit = ctypes.c_uint32(subunit)
        channel = ctypes.c_uint32(channel)
        direction = ctypes.c_bool()

        err = self.handlePLX.PIPLX_DioGetChannelDirection(self.session,
                                                          self.card,
                                                          subunit,
                                                          channel,
                                                          ctypes.byref(direction))
        self._handlePIPLXError(err)

        return direction.value

    def DioGetPatternFileValidationResult(self):
        bufferSize = ctypes.c_uint32(100)
        buffer = ctypes.create_string_buffer(bufferSize.value)

        err = self.handlePLX.PIPLX_DioGetPatternFileValidationResult(self.session,
                                                                     self.card,
                                                                     ctypes.byref(buffer),
                                                                     bufferSize)
        self._handlePIPLXError(err)

        return self._pythonString(buffer.value)

    def DioGetPortDirection(self, subunit):
        subunit = ctypes.c_uint32(subunit)
        direction = ctypes.c_uint32()

        err = self.handlePLX.PIPLX_DioGetPortDirection(self.session,
                                                       self.card,
                                                       subunit,
                                                       ctypes.byref(direction))
        self._handlePIPLXError(err)

        return direction.value

    def DioPortReEnable(self, subunit):
        subunit = ctypes.c_uint32(subunit)

        err = self.handlePLX.PIPLX_DioPortReEnable(self.session,
                                                   self.card,
                                                   subunit)
        self._handlePIPLXError(err)

        return

    def DioSetChannelDirection(self, subunit, channel, direction):
        subunit = ctypes.c_uint32(subunit)
        channel = ctypes.c_uint32(channel)
        direction = ctypes.c_bool(direction)

        err = self.handlePLX.PIPLX_DioSetChannelDirection(self.session,
                                                          self.card,
                                                          subunit,
                                                          channel,
                                                          direction)
        self._handlePIPLXError(err)

        return

    def DioSetPortDirection(self, subunit, direction):
        subunit = ctypes.c_uint32(subunit)
        direction = ctypes.c_uint32(direction)

        err = self.handlePLX.PIPLX_DioSetPortDirection(self.session,
                                                       self.card,
                                                       subunit,
                                                       direction)
        self._handlePIPLXError(err)

        return

    def DioValidatePatternFileDi(self, filename):
        filename = self._stringToStr(filename)

        err = self.handlePLX.PIPLX_DioValidatePatternFileDi(self.session,
                                                            self.card,
                                                            filename)
        self._handlePIPLXError(err)

        return

    def DioUploadPatternFile(self, filename):
        filename = self._stringToStr(filename)

        err = self.handlePLX.PIPLX_DioUploadPatternFile(self.session,
                                                        self.card,
                                                        filename)
        self._handlePIPLXError(err)

        return

    #endregion


class Pi_Card_ByAlias(Pi_Card_Base):
    """Pi_Card_ByAlias class opens a session and card by resource"""
    def __init__(self, alias, resourceDatabase="", accessType=1, timeout=5000):

        Pi_Card_Base.__init__(self)

        alias = self._stringToStr(alias)
        resourceDatabase = self._stringToStr(resourceDatabase)
        self.card = ctypes.c_uint32()
        self.session = ctypes.c_ulong()
        self.disposed = False

        error = self.handlePLX.PIPLX_Init(alias,
                                          resourceDatabase,
                                          int(accessType),
                                          ctypes.byref(self.session),
                                          ctypes.byref(self.card),
                                          int(timeout))
        self._handlePIPLXError(error)

        self.bus, self.slot = self.CardLoc()

    def __del__(self):
        if not self.disposed:
            self.Close()

    def Close(self):
        self.disposed = True
        err = self.handlePLX.PIPLX_CloseSpecifiedCard(self.session, self.card)
        self._handlePIPLXError(err)

        err = self.handleCMLX.PICMLX_Disconnect(self.session)
        self._handlePICMLXError(err)


class Pi_Card_ByDevice(Pi_Card_Base):
    """Pi_Card_ByDevice opens a card using bus, device (device) numbers"""
    def __init__(self, session, bus, slot):

        Pi_Card_Base.__init__(self)

        self.card = ctypes.c_uint32()
        self.session = session

        error = self.handlePLX.PIPLX_OpenSpecifiedCard(self.session, bus, slot, ctypes.byref(self.card))
        self._handlePIPLXError(error)

        self.bus, self.slot = self.CardLoc()

        return


class Pi_Card_ByID(Pi_Card_Base):
    """Pi_Card_ByID opens a card using card number and access type"""
    def __init__(self, session, cardNum, accessType):

        Pi_Card_Base.__init__(self)

        self.session = session

        error = self.handleCMLX.PICMLX_UseCard(self.session, 0, int(cardNum), int(accessType))
        self._handlePICMLXError(error)

        self.card = ctypes.c_uint32(cardNum)

