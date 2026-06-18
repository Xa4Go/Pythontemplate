import random #dit importeert de random-module
import os  # Dit importeert de os-module


def scherm_wissen(): #dit zorgt ervoor dat het scherm wordt gewist
    if os.name == 'nt': # Voor Windows
        os.system('cls') # Voor andere besturingssystemen
    else:
        os.system('clear')  

def geldige_invoer(letter):
    return len(letter) == 1 and letter.isalpha()

Woorden = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]
woordjes=random.choice(Woorden) #kiest random woord uit de lijst
woord = ['_'] * len(woordjes)
geraden_letters = []
beurten=5
fout_letters = []

while beurten > 0 and "_" in woord : #dit zorgt ervoor dat de loop stopt als je geen beurten meer hebt of als je het woord hebt geraden
    print('welkom bij galgje')
    print('je hebt ' + str(beurten) + ' beurten')
    print('het woord heeft ' + str(len(woord)) + ' letters') #dit zorgt ervoor dat het aantal letters in het woord wordt weergegeven
    print(woord)
    

    gok = input('Geef een letter: ').lower()
    print("\n")  # Dit voegt een lege regel toe
    if not geldige_invoer(gok):
     print('Ongeldige invoer, Voer precies een letter in (geen cijfers of symbolen).')
     beurten=beurten-1 #als je een ongeldige invoer doet verlies je een beurt


    resultaat = ''
    for letter in woord:
      if letter in geraden_letters:
         resultaat += letter #dit zorgt ervoor dat de letters die je al hebt geraden niet meer worden vervangen door een streepje
    else:
     resultaat += '-'
    
    if resultaat == woord:
     print('gefeliciteerd je hebt het woord geraden')     

    if gok in geraden_letters or gok in fout_letters: #dit zorgt ervoor dat je niet dezelfde letter twee keer kan raden
     print('Deze letter heb je al geprobeerd probeer een andere letter.')
     beurten= beurten -1
    
    if fout_letters:
          print('Fout geraden letters:', ', '.join(sorted(fout_letters))) #dit zorgt ervoor dat de fout geraden letters worden weergegeven
    if gok in woordjes:
        print("\033[32mGoed geraden!\033[0m")
        geraden_letters.append(gok)
        for i, letter in enumerate(woordjes): #dit zorgt ervoor dat de letter op de plek komt van een wit streepje
            if letter == gok:
                woord[i] = gok
        print('je hebt ' + str(beurten) + ' beurten')
      
    else:
     print('Deze letter zit niet in het woord.')
     fout_letters.append(gok) #dit zorgt ervoor dat de fout geraden letters worden toegevoegd aan de lijst
     beurten = beurten -1
     print('je hebt ' + str(beurten) + ' beurten')
     if beurten == 0 and resultaat != woord: #als je geen beurten meer hebt verlies je
        scherm_wissen()
        print('je hebt verloren het woord was ' + str(woordjes))


opnieuw = input('Wil je nog een spel spelen? (ja/nee): ').lower()
if opnieuw=="ja":
    scherm_wissen()
    print("Goed gedaan!")
    import main #dit zorgt ervoor dat het programma opnieuw begint
else:
        print('Bedankt voor het spelen van Galgje!')
    