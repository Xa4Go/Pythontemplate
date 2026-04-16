leeftijd = int(input("Voer je leeftijd in: "))

if leeftijd < 18:
    print("Jij moet naar school")
elif leeftijd >= 65:
    print("Woon je al in een bejaardenhuis?")
else:
    print("Jij moet elke dag werken")