import datetime

class sak:
    def __init__(self, prioritet, title, beskrivelse):
        self.prioritet = prioritet
        self.title = title
        self.beskrivelse = beskrivelse
        self.dato = datetime.date.today()