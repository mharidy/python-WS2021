class Student(object):
    def __init__(self, vorname, nachname, matrikelnummer, geburtsdatum, noten):
        self.vorname = vorname
        self.nachname = nachname
        self.matrikelnummer = matrikelnummer
        self.geburtsdatum = geburtsdatum
        self.noten = noten

    def __repr__(self):
        return {"Vorname": self.vorname,
                "Nachname": self.nachname,
                "Matrikelnummer": self.matrikelnummer,
                "Geburtsdatum": self.geburtsdatum,
                "Noten": self.noten
                }

    def __str__(self):
        noten_string = " "
        for kurs_name, kurs_note in self.noten.items():
            noten_string = noten_string + kurs_name + ": " + str(kurs_note)

        return 'Vorname -> ' + self.vorname + ' Nachname -> ' + self.nachname + ' Matrikelnummer -> ' + self.matrikelnummer + ' Geburtsdatum -> ' + self.geburtsdatum + \
               ' Noten -> ' + noten_string

    def note_eintragen(self, kurs_name, kurs_note):
        self.noten[kurs_name] = kurs_note

    # TODO: refactor it using __str__ and __repr
    def noten_berichten(self):
        for kurs_name, kurs_note in self.noten.items():
            print(kurs_name, ": ", kurs_note)

    def noten_schummeln(self):
        changed_counter = 0
        for kurs_name, kurs_note in self.noten.items():
            if kurs_note != 1.0:
                self.noten[kurs_name] = 1.0
                changed_counter += 1

        return changed_counter

# Aufgabe 5
newStudent = Student("mohamed", "haridy", "850367", "04/06/1994", {"math1": 2.4, "prog1": 1.0, "IOS": 4.0})
newStudent.note_eintragen("Prog2", 3.0)
newStudent.note_eintragen("Python", 1.0)

print(newStudent.__repr__())
# I used empty an empty print to add empty line between the different prints, so that i can read the console result easier
print("")
print(newStudent.__str__())
print("")

print("Noten vor schummeln: ")
newStudent.noten_berichten()
print("")

print("Anzahl der veraenderten Noten: ", newStudent.noten_schummeln())
print("")

print("Noten Nach schummeln: ")
newStudent.noten_berichten()

print("")
