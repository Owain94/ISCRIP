# Uitwerking opdracht
| Opdracht      | Levensverwachting |
|---------------|-------------------|
| Weeknummer    | 3                 |
| Studentnummer | S1094204          |
| Naam student  | Owain van Brakel  |
| Specialisatie | FICT              |
| Pogingnummer  | 1                 |

## 1. Vraagstelling
Zie: https://dodona.ugent.be/nl/exercises/849566952/

> Schrijf een functie levensverwachting waaraan de volgende vijf parameters moeten doorgegegeven worden:
> 
> geslacht: een string die het geslacht van de persoon aangeeft (man of vrouw)
> roker: een Booleaanse waarde die aangeeft of de persoon rookt
> sport: een natuurlijk getal dat aangeeft hoeveel uren per week de persoon aan sport doet
> alcohol: een natuurlijk getal dat aangeeft hoeveel glazen alcohol de persoon per week drinkt
> fastfood: een Booleaanse waarde die aangeeft of de persoon vaak fastfood eet
> 
> De functie moet op basis van de doorgegeven waarden de levensverwachting voorspellen, en moet deze prognose als resultaat teruggeven. Het resultaat van de functie moet als een reëel getal teruggegeven worden.

## 2. Specificatie
#### Invoer
> Bij deze opdracht vindt geen invoer plaats

##### Uitvoer
> Bij deze opdracht is er geen uitvoer, de functies worden direct aangeroepen en de return waarde wordt weergegeven.
> 
> De levensverwachting functie geeft een int terug

### **Verbanden in en uitvoer**
> -

### **Beperkingen**
> Er is geen invoer mogelijk

## Voorbeelden
#### Invoer
```
-
```
#### Uitvoer
```
De levensverwachting functie geeft een int terug
```

### Voorbeelden van ongeldige invoer
```
-
```

## 3. Ontwerp
> De opdracht moet één fucties bevatten namelijk levensverwachting
> Deze funnctie moet de meegegeven argumenten gebruiken om een leeftijd te berekenen

## 4. Pseudocode
```
functie lenesverwachting(geslacht, roker, sport, alcohol, fastfood):
    leeftijd = 70

    als geslacht == vrouw
        leeftijd = leeftijd + 4

    als roker
        leeftijd = leeftijd - 5
    anders
        leeftijd = leeftijd + 5

    als geen sport
        leeftijd = leeftijd - 3
    anders
        plus uuren sporten
    
    als meer dan 7 alcohol
        ...
    else
        leeftijd = leeftijd + 2

    als geen fastfood
        leeftijd = leeftijd + 3
```

## 5. Code
```python
def levensverwachting(geslacht: str, roker: bool, sport: int, alcohol: int, fastfood: bool) -> int:
    """
    Bereken de levensverwachting

    :param geslacht: Geslacht
    :param roker: Roker
    :param sport: Uren van sport per week
    :param alcohol: Alcohol gebruik
    :param fastfood: Fastfood inname

    :return: levensverwachting
    """
    age = 70

    if geslacht.strip().lower() == 'vrouw':  # geslacht
        age += 4

    if roker:  # roker
        age -= 5
    else:
        age += 5

    if sport == 0:  # sport uren
        age -= 3
    else:
        age += sport

    if alcohol > 7:  # alcohol inname
        age -= (alcohol - 7) * 0.5
    else:
        age += 2

    if not fastfood:  # fastfood inname
        age += 3

    return age

def main() -> None:
    print('{age:.1f}'.format(age=levensverwachting(geslacht='man', roker=True, sport=2, alcohol=10, fastfood=True)))
    print('{age:.1f}'.format(age=levensverwachting(geslacht='man', roker=True, sport=5, alcohol=5, fastfood=True)))
    print('{age:.1f}'.format(age=levensverwachting(geslacht='vrouw', roker=False, sport=5, alcohol=0, fastfood=False)))
    print('{age:.1f}'.format(age=levensverwachting(geslacht='vrouw', roker=False, sport=3, alcohol=14, fastfood=True)))
    print('{age:.1f}'.format(age=levensverwachting(geslacht='man', roker=False, sport=4, alcohol=4, fastfood=False)))


if __name__ == "__main__":
    main()
```

## 6. Test
```python
from unittest import TestCase
import Levensverwachting

class test_levensverwachting(TestCase):
    def velify(self):
        self.assertTrue(Levensverwachting.levensverwachting(geslacht='man', roker=True, sport=2, alcohol=10, fastfood=True) == 65.5)
        self.assertTrue(Levensverwachting.levensverwachting(geslacht='man', roker=True, sport=5, alcohol=5, fastfood=True) == 89.0)
        self.assertTrue(Levensverwachting.levensverwachting(geslacht='vrouw', roker=False, sport=5, alcohol=0, fastfood=False) == 89.0)
        self.assertTrue(Levensverwachting.levensverwachting(geslacht='vrouw', roker=False, sport=3, alcohol=14, fastfood=True) == 78.5)
        self.assertTrue(Levensverwachting.levensverwachting(geslacht='man', roker=False, sport=4, alcohol=4, fastfood=False) == 82.0)
```