import datetime
Saksliste = []

class sak:
    def __init__(self, prioritet, title, beskrivelse, dato):
        self.prioritet = prioritet
        self.title = title
        self.beskrivelse = beskrivelse
        self.dato = dato

def opprettEinNySakKommando():
    title = input("Title på saken: ")
    beskrivelse = input("Beskriv saken: ")
    
    Saksliste.append(sak(None, title, beskrivelse, datetime.date.today()))