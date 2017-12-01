# Uitwerking opdracht
| Opdracht      | Sterke wachtwoorden |
|---------------|---------------------|
| Weeknummer    | 3                   |
| Studentnummer | S1094204            |
| Naam student  | Owain van Brakel    |
| Specialisatie | FICT                |
| Pogingnummer  | 1                   |

## 1. Vraagstelling
Zie: https://dodona.ugent.be/nl/exercises/417422714/

> Steeds meer van ons dagelijks leven speelt zich online af. Om onze identiteit te bevestigen vragen online diensten vaak om een wachtwoord op te geven. Deze diensten zijn vaak echter niet zomaar tevreden met eender welk wachtwoord. Dit geheel terecht. Meestal worden enkele voorwaarden opgelegd om te verhinderen dat wachtwoorden makkelijk zouden kunnen geraden worden. Een wachtwoord geeft een sterke bescherming als elk van de volgende voorwaarden voldaan zijn
> 
> het wachtwoord is minstens 8 karakters lang,
> het wachtwoord bevat minstens één hoofdletter,
> het wachtwoord bevat minstens één kleine letter,
> het wachtwoord bevat minstens één cijfer,
> het wachtwoord bevat minstens één speciaal karakter dat geen letter of cijfer is.
> 
> Indien drie of vier van deze voorwaarden gelden, geeft het wachtwoord een matige bescherming, en als er minder dan drie voorwaarden voldaan zijn, dan geeft het wachtwoord een zwakke bescherming.



## 2. Specificatie
#### Invoer
> De eerste regel van de invoer bevat een natuurlijk getal t(1≤t≤100) dat aangeeft hoeveel testgevallen er zijn. Daarna volgen t regels die elk één wachtwoord bevatten.

Bijvoorbeeld:
```
3
wachtwoord
Prog2011
vijf+1=ZES
```

#### Uitvoer
> Voor elk wachtwoord moet één van de woorden sterk, matig of zwak uitgeschreven worden, als aanduiding van de sterkte van bescherming van het wachtwoord.

Bijvoorbeeld:
```
zwak
matig
sterk
```

### **Verbanden in en uitvoer**
> De invoer wordt verwerkt en aan de hand daarvan wordt de output gegenereerd

### **Beperkingen**
> De input wordt niet gevalideerd

## Voorbeelden
#### Invoer
```
3
wachtwoord
Prog2011
vijf+1=ZES
```
#### Uitvoer
```
zwak
matig
sterk
```

### Voorbeelden van ongeldige invoer
```
a
wachtwoord
Prog2011
vijf+1=ZES
```

## 3. Ontwerp
> Eerst wordt er gevraagd om het aantal wachtwoorden die gecontrleerd moeten worden
> Vervolgens worden eerst alle wachtwoorden gevraagd
> Hierna wordt de sterkte van elk wachtwoord berekend en teruggeven

## 4. Pseudocode
```
Vraag aantal

Voor aantal in Vraag aantal
    vraag wachtwoord

voor elk wachtwoord
    bereken wachtwoord
```

## 5. Code
```python
from string import punctuation

def calculate(password: str) -> str:
    """
    Bereken wachtwoord sterkte

    :param password: wachtwoord

    :return: zwak / matig / sterk
    """
    strenght = 0

    if len(password) > 8:  # Langer dan 8 chars?
        strenght += 1

    if any(x.isupper() for x in password):  # hoofdletter
        strenght += 1

    if any(x.islower() for x in password):  # normale letter
        strenght += 1

    if any(x.isnumeric() for x in password):  # numeriek
        strenght += 1

    if any(x in punctuation for x in password):  # leestekens
        strenght += 1

    if strenght < 3:
        return 'zwak'
    elif strenght < 5:
        return 'matig'
    else:
        return 'sterk'

def main() -> None:
    lst = []
    amount = int(input('Aantal wachtwoorden: '))

    for i in range(0, amount):
        lst.append(input('{count}e wachtwoord: '.format(count=i + 1)))

    for password in lst:
        print(calculate(password))

if __name__ == "__main__":
    main()

```

## 6. Test
```python
from unittest import TestCase
import Sterkewachtwoorden

class test_levensverwachting(TestCase):
    def velify(self):
        self.assertTrue(Sterkewachtwoorden.calculate('wachtwoord') == 'zwak')
        self.assertTrue(Sterkewachtwoorden.calculate('Prog2011') == 'matig')
        self.assertTrue(Sterkewachtwoorden.calculate('vijf+1=ZES') == 'sterk')
```