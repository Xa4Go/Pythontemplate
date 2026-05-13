def bereken_prijs(aantal, prijs_per_stuk):
    return aantal * prijs_per_stuk

aantal = int(input("Hoeveel stuks wil je? "))
prijs_per_stuk = float(input("Wat is de prijs per stuk? "))

totaal = bereken_prijs(aantal, prijs_per_stuk)
print("De totale prijs is: " + str(totaal))
