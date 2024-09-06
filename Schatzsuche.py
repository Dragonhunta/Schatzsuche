from random import randint

zahl = int(input("Gib die Größe des Felds ein: "))
print("Erstellung des Feldes...")

# Erstellung des Feldes
feld = []
for i in range(zahl):
  feld.append(["O"] * zahl)
for i in feld:
  print(i)

# Verstecken des Schatzes (X)
reiheSchatz = zahl - 1
spalteSchatz = 0

reiheSchatz = randint(0, len(feld) - 1)
print(reiheSchatz)
spalteSchatz = randint(0, len(feld[0]) - 1)
print(spalteSchatz)
feld[reiheSchatz][spalteSchatz] = "X"


for i in feld:
  print(i)

print()

# Erstellen des Läufers
positionY = zahl - 1
positionX = 0
feld[positionY][positionX] = "+"

print("Erstellung abgeschlossen!")
print("-" * 10)

for i in feld:
  print(i)

print()

# Bewegen des Läufers
vorher = ""
while ((positionY == reiheSchatz) and (positionX == spalteSchatz)) == False:
    print(positionY, positionX, reiheSchatz, spalteSchatz)
    # richtung = randint(0, 3)
    richtung = int(input("Gib 0 für Norden, 1 für Osten, 2 für Süden und 3 für Westen ein: "))
    if richtung == 0: # Norden
        if vorher != "süden":
            positionY -= 1
            print("ok")
            if positionY < 0:
                positionY = zahl - 1
            vorher = "norden"
    elif richtung == 1: # Osten
        if vorher != "westen":
            positionX += 1
            print("ok")
            if positionX > zahl - 1:
                positionX = 0
            vorher = "osten"
    elif richtung == 2: # Süden
        if vorher != "norden":
            print("ok")
            positionY += 1
            if positionY > zahl - 1:
                positionY = 0
            vorher = "süden"
    elif richtung == 3: # Westen
        if vorher != "osten":
            print("ok")
            positionX -= 1
            if positionX < 0:
                positionX = zahl - 1
            vorher = "westen"
    print(vorher)
    feld[positionY][positionX] = "+"
    for i in feld:
        print(i)
    print()

print(positionY, positionX, reiheSchatz, spalteSchatz)
print("Der Läufer hat den Schatz gefunden!")
