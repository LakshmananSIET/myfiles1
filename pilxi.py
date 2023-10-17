# Communication module header file of ClientBridge for communication with
#  LXI device.
#
#  Copyright (C) 1988 - 2018, Pickering Interfaces ltd.
#
#  Support: support@pickeringswitch.com
#  PicmlxVersion: 1.8.6
#  PiplxVersion: 1.8.0
#  Supported OS: Mac OS 10.9.2, Windows XP/7/8/10
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


from ctypes import *
import platform

PI_WRAP_PICMLX_VERSION = "1.2.0"
PI_WRAP_PIPLX_VERSION = "1.2.0"

def calc_dwords(bits):
    dwords = bits / 32
    if (bits % 32) > 0:
        dwords = dwords + 1

    return int(dwords)


class pi_base:
    def __init__(self):
        if platform.system() == "Windows":
            arch = platform.architecture()
            if "64bit" in arch:
                self.handleCMLX = windll.LoadLibrary("Picmlx_w64")
                self.handlePLX = windll.LoadLibrary("Piplx_w64")
            else:
                self.handleCMLX = windll.LoadLibrary("Picmlx_w32")
                self.handlePLX = windll.LoadLibrary("Piplx_w32")
        elif platform.system() == "Darwin":
            self.handleCMLX = cdll.LoadLibrary("Bin/libpicmlx.so")
            self.handlePLX = cdll.LoadLibrary("Bin/libpiplx.so")
        elif platform.system() == "Linux":
            self.handleCMLX = cdll.LoadLibrary("libpicmlx.so")
            self.handlePLX = cdll.LoadLibrary("libpiplx.so")

    # Discovery Functions
    def EchoDirectEx(self, address, port, timeout):
        listen_port = c_uint(0)
        card_count = c_uint(0)
        client_count = c_uint(0)
        open_card_count = c_uint(0)
        description_size = c_uint(256)
        description = create_string_buffer(description_size.value)
        lxi_address_size = c_uint(100)
        lxi_address = create_string_buffer(lxi_address_size.value)
        err = self.handleCMLX.PICMLX_EchoDirectEx(address, port, timeout,
                                                  byref(listen_port),
                                                  byref(card_count),
                                                  byref(client_count),
                                                  byref(open_card_count),
                                                  byref(description),
                                                  description_size,
                                                  byref(lxi_address),
                                                  lxi_address_size)
        return err, listen_port.value, card_count.value, client_count.value, open_card_count.value, description.value, \
               lxi_address.value

    def EchoBroadcast(self, listen_port, timeout):
        available_lxi_count = c_uint(0)
        err = self.handleCMLX.PICMLX_EchoBroadcast(listen_port, timeout, byref(available_lxi_count))
        return err, available_lxi_count.value

    def GetAvailableLXICount(self):
        ret = self.handleCMLX.PICMLX_GetAvailableLXICount()
        return ret

    def GetAvailableLXIEntryEx(self, index):
        listen_port = c_uint(0)
        card_count = c_uint(0)
        client_count = c_uint(0)
        open_card_count = c_uint(0)
        description_size = c_uint(256)
        description = create_string_buffer(description_size.value)
        lxi_address_size = c_uint(100)
        lxi_address = create_string_buffer(lxi_address_size.value)
        err = self.handleCMLX.PICMLX_GetAvailableLXIEntryEx(index,
                                                            byref(listen_port),
                                                            byref(card_count),
                                                            byref(client_count),
                                                            byref(open_card_count),
                                                            byref(description),
                                                            description_size,
                                                            byref(lxi_address),
                                                            lxi_address_size)
        return err, listen_port.value, card_count.value, client_count.value, open_card_count.value, description.value, \
               lxi_address.value

    def Version(self):
        ver1 = self.handleCMLX.PICMLX_GetVersion()
        ver2 = self.handlePLX.PIPLX_GetVersion()
        return ver1, ver2

    def WrapperVersion(self):
        return PI_WRAP_PICMLX_VERSION, PI_WRAP_PIPLX_VERSION

class pi_comm(pi_base):
    def __init__(self, board, address, port, timeout):
        pi_base.__init__(self)
        self.session = c_uint(0)
        self.card = c_uint(0)
        self.bus = (c_uint32 * 40)()
        self.slot = (c_uint32 * 40)()
        self.c = (c_uint32 * 100)()
        self.handleCMLX.PICMLX_Connect(board, address, port, timeout, byref(self.session))
    
    def __del__(self):
        self.Disconnect()

    def CountFreeCards(self):
        count = c_uint(0)
        err = self.handlePLX.PIPLX_CountFreeCards(self.session, byref(count))
        return err, count.value

    def FindFreeCards(self, count):
        err = self.handlePLX.PIPLX_FindFreeCards(self.session, count, byref(self.bus), byref(self.slot))
        return err, self.bus, self.slot

    def Disconnect(self):
        err = self.handleCMLX.PICMLX_Disconnect(self.session)
        return err

    def SbVersion(self):
        ver = self.handleCMLX.PICMLX_SbVersion(self.session)
        return ver

    def WrapperVersion(self):
        return PI_WRAP_PICMLX_VERSION

    def GetUsableCards(self, card_type):
        car = (c_uint32 * 100)()
        num_cards = c_uint(100)
        err = self.handleCMLX.PICMLX_GetUsableCards(self.session, card_type, byref(car), byref(num_cards))
        return err, car, num_cards.value

    def GetUsedCards(self, card_type):
        car = (c_uint32 * 100)()
        num_cards = c_uint(100)
        err = self.handleCMLX.PICMLX_GetUsedCards(self.session, card_type, byref(car), byref(num_cards))
        return err, car, num_cards.value

    def GetTotalCardsCount(self):
        count = c_uint32(0)
        err = self.handleCMLX.PICMLX_GetTotalCardsCount(self.session, byref(count))
        return err, count.value

    def GetTotalCardsOpenedCards(self):
        count = c_uint32(0)
        err = self.handleCMLX.PICMLX_GetTotalOpenedCards(self.session, byref(count))
        return err, count.value

    """............................."""

    """ SESSION RELATED FUNCTIONS """

    def GetSessionsCount(self):
        """Pointer to variable to receive a number of all live sessions."""
        count = c_uint32(0)
        err = self.handleCMLX.PICMLX_GetSessionsCount(self.session, byref(count))
        return err, count.value

    def GetCardSessionsCount(self, card_types, card):
        """Pointer to variable to receive a number of all live sessions."""
        count = c_uint32(0)
        err = self.handleCMLX.PICMLX_GetCardSessionsCount(self.session, card_types, card, byref(count))
        return err, count.value

    def UseForeignSession(self, session):
        """Pointer to variable to unique confirmation token"""
        length = c_int(100)
        token = create_string_buffer(length.value)
        err = self.handleCMLX.PICMLX_UseForeignSession(self.session, session, byref(token), length)
        return err, token

    def ReleaseForeignSession(self, session):
        err = self.handleCMLX.PICMLX_ReleaseForeignSession(self.session, session)
        return err

    def GetActiveSession(self):
        session = c_uint32(0)
        length = c_int(100)
        token = create_string_buffer(length.value)
        err = self.handleCMLX.PICMLX_GetActiveSession(self.session, byref(session), byref(token), length)
        return err, session.value, token.value

class pi_card(pi_base):

    # Constructor
    # If during init the value of mode is zero them the param_a and param_b can be treated as bus and slot
    # If the value of mode is non-zero then param_a will be card_num and param_b will be accessType

    def __init__(self, board, address, port, timeout, mode, param_a, param_b):
        pi_base.__init__(self)
        self.session = c_uint(0)
        self.card = c_uint(0)
        self.str_length = c_int(100)
        self.path_length = c_int(260)
        self.string = create_string_buffer(self.str_length.value)
        self.alias = create_string_buffer(self.str_length.value)
        self.storage = create_string_buffer(self.path_length.value)
        self.data_length = c_int(40)
        self.data = (c_uint32 * self.data_length.value)()
        self.bus = None
        self.slot = None
        self.handleCMLX.PICMLX_Connect(board, address, port, timeout, byref(self.session))
        if mode == 0:
            err = self.OpenSpecifiedCard(param_a, param_b)
        else:
            err = self.handleCMLX.PICMLX_UseCard(self.session, 0, param_a, param_b)
            if err == 0:
                self.card.value = param_a

    def __del__(self):
        self.CloseSpecifiedCard()

    # Non-card specific functions

    def Check(self):
        return self.session, self.card

    def SbVersion(self):
        ver = self.handleCMLX.PICMLX_SbVersion(self.session)
        return ver

    def WrapperVersion(self):
        return PI_WRAP_PIPLX_VERSION

    # Card specific functions

    # Shared Access Functions

    def UseCard(self, card_type, card_num, access_type):
        err = self.handleCMLX.PICMLX_UseCard(self.session, card_type, card_num, access_type)
        if err == 0:
            self.card.value = card_num
        return err

    def IsCardUsed(self, card_type, card, owner_type):
        is_used = c_uint(0)
        err = self.handleCMLX.PICMLX_IsCardUsed(self.session, card_type, card, owner_type, byref(is_used))
        return err, bool(is_used.value)

    # Open/Close

    def OpenCards(self):
        err = self.handlePLX.PIPLX_OpenCards(self.session)
        return err

    def OpenSpecifiedCard(self, bus, slot):
        if bus is None:
            bus = self.bus
        if slot is None:
            slot = self.slot
        if self.card.value != 0:
            self.CloseSpecifiedCard()
        err = self.handlePLX.PIPLX_OpenSpecifiedCard(self.session, bus, slot, byref(self.card))
        if err == 0:
            self.bus = bus
            self.slot = slot
        return err, self.card.value

    def OpenAliasCard(self, alias, storage, access, timeout):
        if alias == None:
            alias = self.alias
        if type(alias) is str:
            alias = alias.encode("ascii")

        if storage == None:
            storage = self.storage
        if type(storage) is str:
            storage = storage.encode("ascii")

        if self.card.value != 0:
            self.CloseSpecifiedCard()

        session = self.session
        card = self.card

        err = self.handlePLX.PIPLX_Init(alias, storage, access, byref(session), byref(card), timeout)
        if err == 0:
            err, bus, slot= self.CardLoc()
            if err == 0:
                self.bus = bus
                self.slot = slot
                self.alias = alias
                self.storage = storage
                self.session = session
                self.card = card
        return err, self.card.value

    def CloseCards(self):
        err = self.handlePLX.PIPLX_CloseCards(self.session)
        if (self.session != 0):
            err = self.handleCMLX.PICMLX_Disconnect(self.session)
        return err

    def CloseSpecifiedCard(self):
        err = self.handlePLX.PIPLX_CloseSpecifiedCard(self.session, self.card)
        self.card.value = 0
        if (self.session != 0):
            err = self.handleCMLX.PICMLX_Disconnect(self.session)
        return err, self.card.value

    # Card identity

    def CardId(self):
        err = self.handlePLX.PIPLX_CardId(self.session, self.card, byref(self.string), self.str_length)
        return err, self.string.value

    def CardLoc(self):
        bus = c_uint(0)
        slot = c_uint(0)
        err = self.handlePLX.PIPLX_CardLoc(self.session, self.card, byref(bus), byref(slot))
        return err, bus.value, slot.value

    def ClearCard(self):
        err = self.handlePLX.PIPLX_ClearCard(self.session, self.card)
        return err

    def ClearSub(self, sub):
        err = self.handlePLX.PIPLX_ClearSub(self.session, self.card, sub)
        return err

    def ClearMask(self, sub):
        err = self.handlePLX.PIPLX_ClearSub(self.session, self.card, sub)
        return err

    def ClosureLimit(self, sub):
        limit = c_uint(0)
        err = self.handlePLX.PIPLX_ClosureLimit(self.session, self.card, sub, byref(limit))
        return err, limit.value

    def Diagnostic(self):
        diag_string = create_string_buffer(100)
        err = self.handlePLX.PIPLX_Diagnostic(self.session, self.card, byref(diag_string))
        return err, diag_string.value

    def EnumerateSubs(self):
        ins = c_uint(0)
        outs = c_uint(0)
        err = self.handlePLX.PIPLX_EnumerateSubs(self.session, self.card, byref(ins), byref(outs))
        return err, ins.value, outs.value

    def ErrorCode(self):
        err_code = c_uint(0)
        err = self.handlePLX.PIPLX_GetLastErrorCode(self.session, byref(err_code))
        return err, err_code.value

    def ErrorMessage(self):
        err = self.handlePLX.PIPLX_GetLastErrorMessage(self.session, byref(self.string), self.str_length)
        return err, self.string.value

    def ErrorCodeToMessage(self, code):
        err = self.handlePLX.PIPLX_ErrorCodeToMessage(code, byref(self.string), self.str_length)
        return err, self.string.value

    def MaskBit(self, sub, bit, action):
        err = self.handlePLX.PIPLX_MaskBit(self.session, self.card, sub, bit, action)
        return err

    def MaskCrosspoint(self, sub, row, column, action):
        err = self.handlePLX.PIPLX_MaskCrosspoint(self.session, self.card, sub, row, column, action)
        return err

    def OpBit(self, sub, bit, action):
        err = self.handlePLX.PIPLX_OpBit(self.session, self.card, sub, bit, action)
        return err

    def OpCrosspoint(self, sub, row, column, action):
        err = self.handlePLX.PIPLX_OpCrosspoint(self.session, self.card, sub, row, column, action)
        return err

    def OpSwitch(self, sub, func, seg, sw, sub_sw, act):
        state = c_uint(0)
        err = self.handlePLX.PIPLX_OpSwitch(self.session, self.card, sub, func, seg, sw, sub_sw, act, byref(state))
        return err, bool(state.value)

    def ReadBit(self, sub, bit):
        state = c_uint(0)
        err = self.handlePLX.PIPLX_ReadBit(self.session, self.card, sub, bit, byref(state))
        return err, state.value

    def ReadCal(self, sub, index):
        data = c_uint(0)
        err = self.handlePLX.PIPLX_ReadCal(self.session, self.card, sub, index, byref(data))
        return err, data.value

    def ReadSub(self, sub):
        # get size of subunit and create an array to hold the data
        e, t, rows, cols = self.SubInfo(sub, 0)
        dwords = calc_dwords(rows * cols)
        err = self.handlePLX.PIPLX_ReadInputSub(self.session, self.card, sub, byref(self.data), self.data_length)
        return err, dwords, self.data

    def SetMode(self, mode):
        old_mode = self.handlePLX.PIPLX_SetMode(self.session, mode)
        return old_mode

    def SettleTime(self, sub):
        time = c_uint(0)
        err = self.handlePLX.PIPLX_SettleTime(self.session, self.card, sub, byref(time))
        return err, time.value

    def Status(self):
        err = self.handlePLX.PIPLX_Status(self.session, self.card)
        return err

    def SubAttribute(self, sub, out_not_in, code):
        attr = c_uint(0)
        err = self.handlePLX.PIPLX_SubAttribute(self.session, self.card, sub, out_not_in, code, byref(attr))
        return err, attr.value

    def SubInfo(self, sub, out_not_in):
        sub_type = c_uint(0)
        rows = c_uint(0)
        cols = c_uint(0)
        err = self.handlePLX.PIPLX_SubInfo(self.session, self.card, sub, out_not_in, byref(sub_type), byref(rows),
                                           byref(cols))
        return err, sub_type.value, rows.value, cols.value

    def SubSize(self, sub, out_not_in):
        e, t, r, c = self.SubInfo(sub, out_not_in)
        bits = r * c
        dwords = calc_dwords(bits)
        return dwords, bits

    def SubStatus(self, sub):
        status = self.handlePLX.PIPLX_SubStatus(self.session, self.card, sub)
        return status

    def SubType(self, sub, out_not_in):
        err = self.handlePLX.PIPLX_SubType(self.session, self.card, sub, out_not_in, byref(self.string), self.str_length)
        return err, self.string.value

    def ViewBit(self, sub, bit):
        state = c_uint(0)
        err = self.handlePLX.PIPLX_ViewBit(self.session, self.card, sub, bit, byref(state))
        return err, state.value

    def ViewCrosspoint(self, sub, row, column):
        state = c_uint(0)
        err = self.handlePLX.PIPLX_ViewCrosspoint(self.session, self.card, sub, row, column, byref(state))
        return err, state.value

    def ViewMask(self, sub):
        # get size of subunit and create an array to hold the data
        e, t, rows, cols = self.SubInfo(sub, 1)
        dwords = calc_dwords(rows * cols)
        err = self.handlePLX.PIPLX_ViewMask(self.session, self.card, sub, byref(self.data), self.data_length)
        return err, dwords, self.data

    def ViewMaskBit(self, sub, bit):
        state = c_uint(0)
        err = self.handlePLX.PIPLX_ViewMaskBit(self.session, self.card, sub, bit, byref(state))
        return err, state.value

    def ViewMaskCrosspoint(self, sub, row, column):
        state = c_uint(0)
        err = self.handlePLX.PIPLX_ViewMaskCrosspoint(self.session, self.card, sub, row, column, byref(state))
        return err, state.value

    def ViewSub(self, sub):
        # get size of subunit and create an array to hold the data
        e, t, rows, cols = self.SubInfo(sub, 1)
        dwords = calc_dwords(rows * cols)
        err = self.handlePLX.PIPLX_ViewSub(self.session, self.card, sub, byref(self.data), self.data_length)
        return err, dwords, self.data

    def WriteCal(self, sub, index, data):
        err = self.handlePLX.PIPLX_WriteCal(self.session, self.card, sub, index, data)
        return err

    def WriteMask(self, sub, data):
        mask_len = len(data)
        mask_arr = (c_uint32 * mask_len)()
        for idx in range(mask_len):
            mask_arr[idx] = c_uint32(data[idx])

        err = self.handlePLX.PIPLX_WriteMask(self.session, self.card, sub, mask_arr, mask_len)
        return err

    def WriteSub(self, sub, data):
        write_len = len(data)
        write_arr = (c_uint32 * write_len)()
        for idx in range(write_len):
            write_arr[idx] = c_uint32(data[idx])

        err = self.handlePLX.PIPLX_WriteSub(self.session, self.card, sub, write_arr, write_len)
        return err

    # Attenuator card functions

    def AttenType(self, sub):
        err = self.handlePLX.PIPLX_AttenType(self.session, self.card, sub, byref(self.string), self.str_length)
        return err, self.string.value

    def AttenInfo(self, sub):
        size = c_float(0.0)
        steps = c_uint(0)
        sub_type = c_uint(0)
        err = self.handlePLX.PIPLX_AttenInfo(self.session, self.card, sub, byref(sub_type), byref(steps), byref(size))
        return err, sub_type.value, steps.value, size.value

    def SetAttenuation(self, sub, atten):
        err = self.handlePLX.PIPLX_AttenSetAttenuation(self.session, self.card, sub, atten)
        return err

    def GetAttenuation(self, sub):
        atten = c_float(0.0)
        err = self.handlePLX.PIPLX_AttenGetAttenuation(self.session, self.card, sub, byref(atten))
        return err, atten.value

    def PadValue(self, sub, pad):
        atten = c_float(0.0)
        err = self.handlePLX.PIPLX_AttenPadValue(self.session, self.card, sub, pad, byref(atten))
        return err, atten.value

    # PSU card functions

    def PsuType(self, sub):
        err = self.handlePLX.PIPLX_PsuType(self.session, self.card, sub, byref(self.string), self.str_length)
        return err, self.string.value

    def PsuInfo(self, sub):
        sub_type = c_uint(0)
        volts = c_double(0.0)
        amps = c_double(0.0)
        precis = c_uint(0)
        capb = c_uint(0)
        err = self.handlePLX.PIPLX_PsuInfo(self.session, self.card, sub, byref(sub_type), byref(volts), byref(amps),
                                           byref(precis), byref(capb))
        return err, sub_type.value, volts.value, amps.value, precis.value, capb.value

    def PsuGetVoltage(self, sub):
        volts = c_double(0.0)
        err = self.handlePLX.PIPLX_PsuGetVoltage(self.session, self.card, sub, byref(volts))
        return err, volts.value

    def PsuSetVoltage(self, sub, v):
        volts = c_double(v)
        err = self.handlePLX.PIPLX_PsuSetVoltage(self.session, self.card, sub, volts)
        return err

    def PsuEnable(self, sub, enable):
        err = self.handlePLX.PIPLX_PsuEnable(self.session, self.card, sub, enable)
        return err

    # Battery Simulator Functions

    def BattSetVoltage(self, sub, v):
        volts = c_double(v)
        err = self.handlePLX.PIPLX_BattSetVoltage(self.session, self.card, sub, volts)
        return err

    def BattGetVoltage(self, sub):
        volts = c_double(0.0)
        err = self.handlePLX.PIPLX_BattGetVoltage(self.session, self.card, sub, byref(volts))
        return err, volts.value

    def BattSetCurrent(self, sub, curr):
        current = c_double(curr)
        err = self.handlePLX.PIPLX_BattSetVoltage(self.session, self.card, sub, current)
        return err

    def BattGetCurrent(self, sub):
        current = c_double(0.0)
        err = self.handlePLX.PIPLX_BattGetVoltage(self.session, self.card, sub, byref(current))
        return err, current.value

    def BattSetEnable(self, sub, pattern):
        err = self.handlePLX.PIPLX_BattSetEnable(self.session, self.card, sub, pattern)
        return err

    def BattGetEnable(self, sub):
        pattern = c_uint(0)
        err = self.handlePLX.PIPLX_BattGetEnable(self.session, self.card, sub, byref(pattern))
        return err, pattern.value

    def BattReadInterlockState(self, sub):
        state = c_uint(0)
        err = self.handlePLX.PIPLX_BattReadInterlockState(self.session, self.card, sub, byref(state))
        return err, bool(state.value)

    # Resistor Functions

    def ResSetResistance(self, sub, mode, resistance):
        is_out_sub = c_uint32(1)
        md = c_uint(mode)
        res = c_double(resistance)
        err = self.handlePLX.PIPLX_ResSetResistance(self.session, self.card, sub, md, res)
        return err

    def ResGetResistance(self, sub):
        resistance = c_double(0.0)
        err = self.handlePLX.PIPLX_ResGetResistance(self.session, self.card, sub, byref(resistance))
        return err, resistance.value

    def ResInfo(self, sub):
        min_res = c_double(0.0)
        max_res = c_double(0.0)
        ref_res = c_double(0.0)
        prec_pc = c_double(0.0)
        prec_delta = c_double(0.0)
        int1 = c_double(0.0)
        int1_delta = c_double(0.0)
        caps = c_uint32(0)

        err = self.handlePLX.PIPLX_ResInfo(self.session, self.card, sub,
                                           byref(min_res),
                                           byref(max_res),
                                           byref(ref_res),
                                           byref(prec_pc),
                                           byref(prec_delta),
                                           byref(int1),
                                           byref(int1_delta),
                                           byref(caps))
        return err, min_res.value, max_res.value, ref_res.value, prec_pc.value, prec_delta.value,\
               int1.value, int1_delta.value, caps.value

    # Voltage Source (VSOURCE type) specific functions

    def VsourceSetRange(self, sub, r):
        range = c_double(r)
        err = self.handlePLX.PIPLX_VsourceSetRange(self.session, self.card, sub, range)
        return err

    def VsourceGetRange(self, sub):
        range = c_double(0.0)
        err = self.handlePLX.PIPLX_VsourceGetRange(self.session, self.card, sub, byref(range))
        return err, range.value

    def VsourceSetVoltage(self, sub, v):
        volts = c_double(v)
        err = self.handlePLX.PIPLX_VsourceSetVoltage(self.session, self.card, sub, volts)
        return err

    def VsourceGetVoltage(self, sub):
        volts = c_double(0.0)
        err = self.handlePLX.PIPLX_VsourceGetVoltage(self.session, self.card, sub, byref(volts))
        return err, volts.value

    def VsourceSetEnable(self, sub, pattern):
        err = self.handlePLX.PIPLX_VsourceSetEnable(self.session, self.card, sub, pattern)
        return err

    def VsourceGetEnable(self, sub):
        pattern = c_uint(0)
        err = self.handlePLX.PIPLX_VsourceGetEnable(self.session, self.card, sub, byref(pattern))
        return err, pattern.value

    def getStatusMessage(self):
        status_length = c_uint(100)
        status_message = create_string_buffer(status_length.value)
        err = self.handlePLX.PIPLX_GetStatusMessage(self.session, self.card, byref(status_message), status_length)
        return err, status_message.value

    # Gets value for certain attributes (Integer only)
    def GetAttribute(self, sub, out_not_in, code):
        attr = c_uint(0)
        attr_length = c_uint(100)
        err = self.handlePLX.PIPLX_GetAttribute(self.session, self.card, sub, out_not_in, code, byref(attr), attr_length)
        return err, attr.value

    def SetAttribute(self, sub, out_not_in, code, attr):
        attribute = c_uint(attr)
        attr_length = c_uint(100)
        err = self.handlePLX.PIPLX_SetAttribute(self.session, self.card, sub, out_not_in, code, byref(attribute), attr_length)
        return err

class pi_card_alias(pi_card):
    def __init__(self, alias, storage, access, timeout):
        pi_base.__init__(self)
        self.session = c_uint(0)
        self.card = c_uint(0)
        self.str_length = c_int(100)
        self.path_length = c_int(260)
        self.string = create_string_buffer(self.str_length.value)
        self.alias = create_string_buffer(self.str_length.value)
        self.storage = create_string_buffer(self.path_length.value)
        self.data_length = c_int(40)
        self.data = (c_uint32 * self.data_length.value)()
        self.bus = None
        self.slot = None
        self.OpenAliasCard(alias, storage, access, timeout)
