# Uitwerking opdracht
| Opdracht      | Ceasarrotatie    |
|---------------|------------------|
| Weeknummer    | 3                |
| Studentnummer | S1094204         |
| Naam student  | Owain van Brakel |
| Specialisatie | FICT             |
| Pogingnummer  | 1                |

## 1. Vraagstelling
Zie: https://dodona.ugent.be/nl/exercises/105361566/

> Het Caesarcijfer is een klassieke manier om tekstberichten te coderen (versleutelen) en te decoderen (ontsleutelen). Het is vernoemd naar Julius Caesar, die het gebruikte om te communiceren met zijn veldheren.

> De versleuteling werkt door elke letter van het alfabet te vervangen door een letter die enkele plaatsen verder in het alfabet voorkomt. Hierbij wordt een circulair alfabet beschouwd, wat betekent dat na de letter Z opnieuw de letter A volgt. Vandaar dat ook de term rotatie of verschuiving gebruikt wordt voor deze operatie. Bijvoorbeeld, bij rot3 (een rotatie over drie posities) wordt de letter B tijdens het versleutelen vervangen door de letter E.

![alt text](https://dodona.ugent.be/exercises/105361566/media/caesarrotatie.png "Rot 3")

> Het onsleutelen van een tekst gebeurt door de omgekeerde bewerking uit te voeren. In dit geval wordt er dus een rotatie of verschuiving naar links uitgevoerd, in plaats van naar rechts zoals bij de versleuteling. Bijvoorbeeld, bij rot3 wordt de letter E tijdens het ontsleutelen vervangen door de letter B.

![alt text](https://dodona.ugent.be/exercises/105361566/media/caesarrotatie2.png "Rot 3")

## 2. Specificatie
#### Invoer
> De eerste regel van de invoer bevat een getal n∈ℕ dat aangeeft over hoeveel posities er geroteerd wordt bij een Caesarrotatie. Daarna volgt een regel die een zin bevat die gecodeerd werd aan de hand van een Caesarrotatie over n posities. Hierbij werden enkel de letters van het alfabet geroteerd (zowel hoofdletters als kleine letters). Alle overige karakters (cijfers, leestekens, spaties, …) bleven ongewijzigd in de gecodeerde tekst.


Bijvoorbeeld:
```
20
Ylluly boguhog ymn.
```

#### Uitvoer
> De gedecodeerde zin.

Bijvoorbeeld:
```
Errare humanum est.
```

### **Verbanden in en uitvoer**
> De invoer wordt verwerkt en aan de hand daarvan wordt de output gegenereerd

### **Beperkingen**
> -

## Voorbeelden
#### Invoer
```
20
Ylluly boguhog ymn.
```
#### Uitvoer
```
Errare humanum est.
```

### Voorbeelden van ongeldige invoer
```
-
```

## 3. Ontwerp
> Eerst wordt er een getal gevraagd, deze wordt gebruikt om de letters een x aantal te verschuiven
> 
> Vervolgens wordt er om een string gevraagd, deze string zal vervolgens omgezet worden naar een gecodeerde zin

## 4. Pseudocode
```
invoer_nummer = nummer
invoer_tekst = tekst

gecodeerde_tekst = ''

for letter in tekst
    als letter geen speciaal teken is:
        zet letter om naar index in het alfabet
        geconverteerd = converteer_terug_naar_letter(letter - invoer nummer)
        gecodeerde_tekst += geconverteerd
```

## 5. Code
```python
def decipher(key: int, message: str) -> str:
    """
    Ontcijfer een caesarrotatie door middel van misbruik te maken van de ASCII chart

    :param key: Aantal letter verschoven
    :param message: Bericht om te ontcijveren

    :return: Oncijverde bericht
    """
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num -= key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26  # Ga terug naar het begin van het alfabet 
                elif num < ord('A'):
                    num += 26  # Ga naar het einde van het alfabet 
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26  # Ga naar het einde van het alfabet 
                elif num < ord('a'):
                    num += 26  # Ga terug naar het begin van het alfabet 

            translated += chr(num)
        else:
            translated += symbol  # Voeg charaters die geen letter zijn sowieso toe

    return translated

def main() -> None:
    pos = int(input('Posities: '))
    cipher = input('Cipher: ')

    print(decipher(pos, cipher))

if __name__ == "__main__":
    main()
```

## 6. Test
```python
from unittest import TestCase
import Caesarrotatie

class test_formule_1(TestCase):
    def velify(self):
        self.assertTrue(Caesarrotatie.encode(20, 'Ylluly boguhog ymn.') == 'Errare humanum est.')
        self.assertTrue(Caesarrotatie.encode(1, 'Testing encoding!@#$%.') == 'Sdrshmf dmbnchmf!@#$%.')
```