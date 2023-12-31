# """ Sample program for Pickering LXI/PXI Precision Resistor cards using the PILXI ClientBridge Python Wrapper """

# import pilxi

# if __name__ == "__main__":
#     print("pilxi wrapper version: {}".format(pilxi.__version__))
#     # Connect to a chassis using an IP address.
#     # The ClientBridge driver can also connect to local PXI chassis by passing
#     # 'PXI' in place of the IP.

#     IP_Address = "192.168.0.147"

#     # Default port and timeout settings in mS
#     port = 1024
#     timeout = 1000

#     # In this example we'll directly connect to the card using bus and device numbers:
#     bus = 4
#     device = 14

#     print("Sample program for Pickering LXI/PXI Precision Resistor cards using the PILXI ClientBridge Python Wrapper")

#     # Open a session with LXI
#     try:
#         session = pilxi.Pi_Session(IP_Address, port, timeout)
#     except pilxi.Error as ex:
#         print("Opening LXI session failed: {}".format(ex.message))
#         exit()

#     # Open the card
#     try:
#         card = session.OpenCard(bus, device)
#     except pilxi.Error as ex:
#         print("Opening card failed: {}".format(ex.message))
#         exit()

#     # Get the card ID
#     cardId = card.CardId()

#     print("Connected to chassis at", IP_Address)
#     print("Successfully connected to card at bus:", bus, "device:", device)
#     print("Card ID: ", cardId)

#     #use subunit 1 of the card.
#     subunit = 1

#     # Functions to control Precision Resistor:
#     try:
#         #Set Resistance
#         #       ---/ ------------
#         #       |               |
#         # ----------------R----------
#         resistance = 326
#         card.ResSetResistance(subunit, 1, resistance)

#         #Get Resistance
#         resistance = 324
#         resistance = card.ResGetResistance(subunit)
#         print("Resistance readback ", resistance)

#         #short circuit
#         #       -----------------
#         #       |               |
#         # ---------/  ----R----------
#         resistance = 138
#         card.ResSetResistance(subunit, 0, resistance)

#         # #open circuit
#         # #       ---/ ------------
#         # #       |               |
#         # # ---------/  ----R----------
#         resistance = float("inf")
#         card.ResSetResistance(subunit, 0, resistance)

#     except pilxi.Error as ex:
#         print("Error occurred operating Precision Resistor Card: {}".format(ex.message))
#         print("Error code: {}".format(ex.errorCode))
    
#     # Close the card. It is recommended to close any open cards
#     print("Closing card and exiting.")

#     card.Close()
import pilxi

if __name__ == "__main__":
    print("pilxi wrapper version: {}".format(pilxi.__version__))

    IP_Address = "192.168.0.147"
    port = 1024
    timeout = 1000

    bus = 4
    device = 14

    print("Sample program for Pickering LXI/PXI Precision Resistor cards using the PILXI ClientBridge Python Wrapper")

    try:
        session = pilxi.Pi_Session(IP_Address, port, timeout)
    except pilxi.Error as ex:
        print("Opening LXI session failed: {}".format(ex))
        exit()

    try:
        card = session.OpenCard(bus, device)
    except pilxi.Error as ex:
        print("Opening card failed: {}".format(ex))
        exit()

    cardId = card.CardId()

    print("Connected to chassis at", IP_Address)
    print("Successfully connected to card at bus:", bus, "device:", device)
    print("Card ID: ", cardId)

    subunit = 1

    try:
        resistance = 326
        card.ResSetResistance(subunit, 1, resistance)

        resistance = card.ResGetResistance(subunit)
        print("Resistance readback: ", resistance)

        resistance = 138
        card.ResSetResistance(subunit, 1, resistance)

        resistance = float("inf")
        card.ResSetResistance(subunit, 1, resistance)

    except pilxi.Error as ex:
        print("Error occurred operating Precision Resistor Card: {}".format(ex))
        print("Error code: {}".format(ex.errorCode))

    print("Closing card and exiting.")
    card.Close()
