from __future__ import print_function
from pilxi import *
import time
import sys

base = pi_base()

# Default listening port 9999
listeningport = 9999
#timeout in mS
timeout = 2000

err,val = base.EchoBroadcast(listeningport ,timeout)
if (err !=0):
    print ("err ", err)
    sys.exit(err)
else:
    print ("Number of LXI's availabe:  ", val)

#Get the number of LXIs available
ret = base.GetAvailableLXICount()

#Information for LXIs in the range
for x in range(0,ret):
    err, listenport, cardcount, clientcount, opencardcount, description, address = base.GetAvailableLXIEntryEx(x)
    print ("IP Address: ", address.decode("utf-8"), "Description:  ", description.decode("utf-8"))




# if (sys.version_info > (3, 0, 0)):
#     input_var = input("Please enter the IP address: ")
# else:
#     input_var = raw_input("Please enter the IP address: ")
b_input_var = address

# Initialize the comm module
comm = pi_comm(0, b_input_var, 1024, 1000)

# Gets the version of ServerBridge
ver = comm.SbVersion()
print("Serverbridge Version on LXI:", ver)

# Gets the the card count
err, count = comm.CountFreeCards()
err, bus, slot = comm.FindFreeCards(count)
print("Error:", err, "Card count:", count)

print("--------------------------------")

cardnum = 0
# If during init the value of mode is zero them the paramA and paramB can be treated as bus and slot
# If the value of mode is non-zero then ParamA will be cardnum and paramB will be accessType

mode = 0  # Last two parameters treated as bus and slot
while cardnum < count:
    card = pi_card(0, b_input_var, 1024, 1000, mode, bus[cardnum], slot[cardnum])

    err, cid = card.CardId()
    if err != 0:
        print(err)
        ret, errmsg = card.ErrorCodeToMessage(err)
        print("Error: ", errmsg, "-", err)

    print("Bus ", bus[cardnum], "Slot ", slot[cardnum])
    print("ID = ", cid.decode("utf-8"))
    e, ins, outs = card.EnumerateSubs()
    print("subunits: ", ins, "input, ", outs, "output")

    print("--------------------------------")
    sub = 1
    while sub <= outs:

        err, inf = card.SubType(sub, 1)
        if err != 0:
            print(err)
            ret, errmsg = card.ErrorCodeToMessage(err)
            print("Error: ", errmsg, "-", err)
        else:
            print("subunit ", sub, " = ", inf)

        # err, subType, rows, cols = card.SubInfo(sub, 1)
        # if err != 0:
        #     print(err)
        #     ret, errmsg = card.ErrorCodeToMessage(err)
        #     print("Error: ", errmsg, "-", err)
        # else:
        #     for y in range(1, rows + 1):
        #         for x in range(1, cols + 1):
        #             err = card.OpCrosspoint(sub, y, x, 1)
        #             if err != 0:
        #                 print(err)
        #                 ret, errmsg = card.ErrorCodeToMessage(err)
        #                 print("Error: ", errmsg, "-", err)
        #             else:
        #                 print("Connected Crosspoint X -", x, " Y -", y)
        #                 #time.sleep(0.1)
        #                 err = card.OpCrosspoint(sub, y, x, 0)
        #                 if err != 0:
        #                     print(err)
        #                     ret, errmsg = card.ErrorCodeToMessage(err)
        #                     print("Error: ", errmsg, "-", err)
        #                 else:
        #                     print("Disconnected Crosspoint X -", x, " Y -", y)
                            #time.sleep(0.1)
            sub = sub + 1

    cardnum = cardnum + 1
    card.CloseCards()

comm.Disconnect()
