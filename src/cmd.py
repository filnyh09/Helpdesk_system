import datetime, pick
from sak import *

def opprettEinNySakKommando():
    title = input("Title på saken: ")
    beskrivelse = input("Beskriv saken: ")
    # på prioritetsvalg er [1] indexen og [0] selve valget
    prioritetsvalg = pick.pick(['1', '2', '3', '4', '5'], 'Velg prioritetsnivå fra 1(notering) til 5(kritisk): ')

    Saksliste.append(sak(prioritetsvalg[1] + 1, title, beskrivelse, datetime.date.today()))