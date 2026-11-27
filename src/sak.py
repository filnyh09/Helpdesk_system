Saksliste = []

class sak:
    def __init__(self, prioritet, title, beskrivelse, dato):
        self.prioritet = prioritet
        self.title = title
        self.beskrivelse = beskrivelse
        self.dato = dato

    def PressenterSaken(self):
        melding += f"{self.title}\n"
        melding += f"åpnet: {self.dato}\n"
        melding += f"prioritet: {self.prioritet}\n"
        melding += f"{self.beskrivelse}"

        return melding