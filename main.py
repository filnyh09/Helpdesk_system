from src.cmd import *

while True:
    cmd = input(">")
    flexcmd = cmd.strip().lower()

    if flexcmd == "newcase":
        opprettEinNySakKommando()

        