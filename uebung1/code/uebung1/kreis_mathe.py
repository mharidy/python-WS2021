import math


def flaeche_berechnen(radius):
    return math.pi * math.sqrt(radius)


print("Kreis flaesche fuer radius 5 -> ", flaeche_berechnen(5))


def umfang_berechnen(radius):
    return 2 * math.pi * radius


print("Kreis umfang fuer radius 5 -> ", umfang_berechnen(5))
