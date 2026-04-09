import pprint
naam = input("Wat is je naam?")
leeftijd = int(input("Hoe oud ben je?"))

print(naam + " is " + str(leeftijd) + " jaar oud")

if leeftijd < 18:
    print("Je bent minderjarig")
else:
    print("Je bent meerderjarig")
