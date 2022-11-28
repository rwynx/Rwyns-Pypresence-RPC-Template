from pypresence import Presence
import time
rpc = Presence("appid_here")
rpc.connect()
rpc.update(state="state_here",details="detail_here",party_size=[2,4],large_image="application_icon_here",start=time.time())

# rpc = presence("YOUR_APPCLIENT_ID_HERE")
# state = current activity type, example: "CO-OP"
# details = 2nd line, example: "playing XXX"
# party_size 2,4 = COOP 2/4 (can be changed)
# large_image = if you want to use an icon, you must upload it to application's Rich Presence page first,
# then use the file's name with ".ico" ext.

import datetime
now = datetime.datetime.now()
print ("App execution time: ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

input("Executed.")
input("ENTER to terminate the process - RWYN RPC.")
# input indicates that application will NOT be terminated immediately after use.
