""" Sample program for Pickering PXI/PCI Battery Simulator cards using the PILPXI driver Python wrapper """

from __future__ import print_function
import pilpxi
import sys

if __name__ == "__main__":

    # Set the Bus and Device (device) address here for this session
    # can be found from Device Manager or Pickering General SFP
    # on Windows systems, or lspci on Linux systems.
    bus = 16
    device = 14

    # To access the first subunit of a card, set subunit to 1
    subunit = 1

    print("Sample program for Pickering PXI/PCI Battery Simulator cards using the PILPXI Python Wrapper")
    print()

    # Open a specific card using Pi_Card()
    try:
        card = pilpxi.Pi_Card(bus, device)
    except pilpxi.Error as ex:
        print("Error occurred opening card: {}".format(ex.message))
        exit()

    # This function returns information about the card,
    # Model name, Serial number and Firmware revision
    cardId = card.CardId()

    print("Successfully connected to specified card.")
    print("Card ID: ", cardId)
    print()

    # Functions to control Battery Simulator:

    inputMessage = "Please enter the voltage value in Volts: "

    input_var = input(inputMessage)
    volts = float(input_var)

    inputMessage = "Please enter the current value in Amps: "

    input_var = input(inputMessage)
    current = float(input_var)

    try:

        # Set Voltage
        card.BattSetVoltage(subunit, volts)

        volts = card.BattGetVoltage(subunit)
        print(f"Set {volts} volts on channel {subunit}")

        # Set Current
        card.BattSetCurrent(subunit, current)

        current = card.BattGetCurrent(subunit)
        print(f"Set {current} A limit on channel {subunit}")

        # Enable Output
        card.BattSetEnable(subunit, True)

        # Check the interlock state
        interlock  = card.BattReadInterlockState(subunit)

        if interlock:
            print("Interlock is enabled.")

        # Get Output state
        state = card.BattGetEnable(subunit)

        if state:
            print("Output is enabled.")
        else:
            print("Output is disabled.")

    except pilpxi.Error as ex:
        print(f"Error operating battery simulator: {ex.message}")
        print(f"Error code: {ex.errorCode}")
        exit()

    try:
        # Measure channel voltage and current on supported battery simulator cards
        # e.g. 41-752A-01x models. Please consult your product manual for your
        # card's specific capabilities.

        # 41-752A-01x: Enable set-measure-set mode.
        card.BattSetMeasureSet(subunit, True)

        # 41-752A-01x: Change measurement device accuracy.
        card.BattSetMeasureConfig(subunit,                              # Subunit to configure
                                  pilpxi.BattNumSamples.SAMPLES_128,    # Average values after 128 samples
                                  pilpxi.BattConversionTime.T_1052us,   # 1052 us voltage sample time
                                  pilpxi.BattConversionTime.T_540us,    # 540 us current sample time
                                  pilpxi.BattOperationMode.CONTINUOUS)  # Measure continuously (no wait for trigger)

        # The battery simulator (41-752A-01x) has the capability to take into consideration the load
        # at which the voltage must be provided. Calculated data for voltage at different loads are
        # used to provide this functionality.
        load = 100  # units: mA
        card.BattSetLoad(subunit, load)

        volts = card.BattMeasureVoltage(subunit)
        print(f"Measured voltage: {volts}")

        current = card.BattMeasureCurrentmA(subunit)
        print(f"Measured {current} mA")

        current = card.BattMeasureCurrentA(subunit)
        print(f"Measured {current} A")

    except pilpxi.Error as ex:
        print(f"Error operating special battery simulator functionality: {ex.message}")
        print(f"Error code: {ex.errorCode}")
        exit()


