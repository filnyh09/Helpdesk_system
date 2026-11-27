from src.sak import *

while True:
    cmd = input(">")
    flexcmd = cmd.strip().lower()

    if flexcmd == "newcase":
        opprettEinNySakKommando()

        