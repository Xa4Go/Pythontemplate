from jinja2.nodes import Break
import random
import os

def scherm_wissen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



Woorden = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]
woord=random.choice(Woorden)
geraden_letters = []
beurten=5

if beurten > 0:
    print('welkom bij galgje')
print('je hebt ' + str(beurten) + ' beurten')
print('het woord heeft ' + str(len(woord)) + ' letters')



tekst = input("Voer een tekst in: ")


resultaat = ''
for letter in woord:
    if letter in geraden_letters:
     resultaat += letter
else:
    resultaat += '-'

    print('huidige stand van het woord ' + resultaat)
if resultaat == woord:
 print('gefeliciteerd je hebt het woord geraden')
    
 Break

 gok = input('raad een letter ')
 geraden_letters.append(gok)

 if gok in woord:
        print('goed geraden')
else:
        print('deze letter zit niet in het woord')
        beurten = beurten - 1
if beurten == 0 and resultaat != woord:
     scherm_wissen()
print('je hebt verloren het woord was ' + woord)