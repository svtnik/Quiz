import time

print("Willkommen zum Quiz!")

playing = input("Möchtest du mitmachen? ")

if playing.lower() == "ja":
    print("Ok!")
else:
    quit()

time.sleep(1)

print("Zuvor noch eine Frage:")
name = input("Wie soll ich dich nennen?: ")

time.sleep(1)

score = 0

answer = input("Ok " + str(name) + ", erste frage: Was ist umgangssprachlich H2O? ")
if answer.lower() == "wasser":
    print("Richtig!")
    score += 1
else:
    print("Falsch!")

answer = input(str(name) + ", in welchem Land wohnen die meisten Menschen? ")
if answer.lower() == "china":
    print("Richtig!")
    score += 1
else:
    print("Falsch!")

answer = input(str(name) + ", auf welchem Kontinent liegt die Wüste Sahara? ")
if answer.lower() == "afrika":
    print("Richtig!")
    score += 1
else:
    print("Falsch!")

answer = input(str(name) + ", Lichtwellen bewegen sich schneller als Schallwellen. Richtig oder falsch? ")
if answer.lower() == "richtig":
    print("Super!")
    score += 1
else:
    print("Falsch!")

answer = input(str(name) + ", die Freiheitsstatue in New York war ein Geschenk von: ")
if answer.lower() == "frankreich":
    print("Richtig!")
    score += 1
else:
    print("Falsch!")

answer = input(str(name) + ", wann ging der Erste Weltkrieg zu Ende? ")
if answer == "1918":
    print("Richtig!")
    score += 1
else:
    print("Falsch!")

answer = input(str(name) + ", welches Instrument hat Tasten, Pedale und Saiten? ")
if answer.lower() == "klavier":
    print("Richtig!")
    score += 1
else:
    print("Falsch!")

answer = input(str(name) + ", kann man im Weltraum Geräusche hören? ")
if answer.lower() == "nein":
    print("Richtig!")
    score += 1
else:
    print("Falsch!")

print(str(name) + ", du hast " + str(score) + " Punkte erreicht!")
print("Das sind " + str((score / 8) * 100) + "%")