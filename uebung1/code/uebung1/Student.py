class Student(object):
    def __init__(self, vorname, nachname, matrikelnummer, geburtsdatum, noten=[]):
        self.vorname = vorname
        self.nachname = nachname
        self.matrikelnummer = matrikelnummer
        self.geburtsdatum = geburtsdatum
        self.noten = noten

    def note_eintragen(self, kurs_name, kurs_note):
        self.noten.append({"kurs_name": kurs_name, "kurs_note": kurs_note})

    # TODO: refactor it using __str__ and __repr
    def noten_berichten(self):
        print("self.noten-->", self.noten)

    # TODO: Implement __str__

    # TODO: Implement __repr__

    def noten_schummeln(self):
        for note in self.noten:
            if note.kurs_note != 1.0:
                note.kurs_note=1.0
            



