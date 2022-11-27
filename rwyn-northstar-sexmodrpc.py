from pypresence import Presence
import time
import pyfiglet
from colorama import Fore, Style, init
from termcolor import colored

from sys import stdout
init()
# convert: needed for cmd color
init(convert=True)

rpc = Presence("1039931364411183174")
rpc.connect()
rpc.update(state="CO-OP",details="Having an intense sex",party_size=[2,4],large_image="northstar-rwyn-icon",start=time.time())

result = pyfiglet.figlet_format("RWYN'S RPC", font = "slant"  )
print(result)

import datetime
now = datetime.datetime.now()
print(f"{Fore.GREEN}App execution time:{Style.RESET_ALL}")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print(f"\n{Fore.GREEN}Online Status:{Style.RESET_ALL} RWYN Northstar SexMod RPC v2.7 started without an issue.\n{Fore.GREEN}Current Activity:{Style.RESET_ALL} You are currently having sex with {Fore.RED}one (1){Style.RESET_ALL} person.\n\n------------------------------------------------------------------\nI wrote this code in like 30 secs or something soo yeah don't expect too much lmao cya.\nAlso check your {Fore.BLUE}Discord{Style.RESET_ALL} activity to see *elapsed_time*")
# inputtan sonrası printlenmeyecek
print(f"------------------------------------------------------------------\n")
input("If you wanna contact me for some weird reason: rwyn#9860")
input('Press ENTER to terminate the process - Rwyn RPC.')

# color test 2;;
print(colored('peekaabooo mf rwyn#9860','magenta'))
