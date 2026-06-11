
import random
import os


def scherm_wissen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def geldige_invoer(letter):
    return len(letter) == 1 and letter.isalpha()

Woorden = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]
woord=random.choice(Woorden)
geraden_letters = []
beurten=5
fout_letters = []

if beurten > 0:
    print('welkom bij galgje')
print('je hebt ' + str(beurten) + ' beurten')
print('het woord heeft ' + str(len(woord)) + ' letters')

gok = input('Geef een letter: ').lower()
if not geldige_invoer(gok):
     print('Ongeldige invoer, Voer precies een letter in (geen cijfers of symbolen).')
beurten = beurten - 1


resultaat = ''
for letter in woord:
    if letter in geraden_letters:
     resultaat += letter
else:
    resultaat += '-'
    
if resultaat == woord:
 print('gefeliciteerd je hebt het woord geraden')     

if gok in geraden_letters or gok in fout_letters:
    print('Deze letter heb je al geprobeerd probeer een andere letter.')

    
if fout_letters:
      print('Fout geraden letters:', ', '.join(sorted(fout_letters)))
if gok in woord:
        print("\033[32mGoed geraden!\033[0m")
        geraden_letters.append(gok)
        print('je hebt ' + str(beurten) + ' beurten')
   
elif beurten == 0 and resultaat != woord:
    scherm_wissen()
    print('je hebt verloren het woord was ' + woord)

else:
     print('Deze letter zit niet in het woord.')
     fout_letters.append(gok)
     beurten = beurten - 1
     print('je hebt ' + str(beurten) + ' beurten')
