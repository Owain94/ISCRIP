# Uitwerking opdracht
| Opdracht      | Formule 1        |
|---------------|------------------|
| Weeknummer    | 2                |
| Studentnummer | S1094204         |
| Naam student  | Owain van Brakel |
| Specialisatie | FICT             |
| Pogingnummer  | 1                |

## 1. Vraagstelling
Zie: https://dodona.ugent.be/nl/exercises/1236821040/

> Bij Formule 1 wordt het aantal ronden dat tijdens een grote prijs wordt afgelegd bepaald als het kleinste aantal volledige ronden waardoor een afstand van 305 kilometer wordt overschreden. De enige uitzondering op deze regel wordt gevormd door de grote prijs van Monaco waarbij slechts 78 ronden afgelegd worden, goed voor een totaal van 260.52 kilometer. Bij uitzonderlijke omstandigheden kan een wedstrijd vroegtijdig afgebroken worden. Zo is er de bijkomende regel dat een wedstrijd niet langer kan duren dan twee uur. Indien deze tijdslimiet wordt overschreden, dan wordt de wedstrijd beëindigd op het einde van de ronde die momenteel bezig is.

## 2. Specificatie
#### Invoer
> Drie regels met daarop respectievelijk de naam van de grote prijs, de afstand a∈ℝ (in kilometer) van één enkele ronde, en de gemiddelde tijd t∈ℝ (in minuten) voor het afleggen van één enkele ronde onder de huidige omstandigheden.

Bijvoorbeeld:
```
Brazilië
5.031
1.54178
```

#### Uitvoer
> Een regel die aangeeft hoeveel ronden er moeten verreden worden voor de grote prijs die wordt beschreven in de invoer. Gebruik de tekst "De grote prijs van naam wordt verreden over r ronden (k km)." als template voor de omschrijving. Hierbij moeten de cursieve fragmenten ingevuld worden op basis van de gegeven en berekende informatie.

Bijvoorbeeld:
```
De grote prijs van Brazilië wordt verreden over 61 ronden (306.891 km).
```

### **Verbanden in en uitvoer**
> De invoer wordt verwerkt en aan de hand daarvan wordt de output gegenereerd

### **Beperkingen**
> De invoer is heel simpel en er zijn makkelijk fouten in te maken

## Voorbeelden
#### Invoer
```
Brazilië
5.031
1.54178
```
#### Uitvoer
```
De grote prijs van Brazilië wordt verreden over 61 ronden (306.891 km).
```

#### Invoer
```
België
7.004
2.88772
```
#### Uitvoer
```
De grote prijs van België wordt verreden over 42 ronden (294.168 km).
```

#### Invoer
```
Monaco
3.340
1.13895
```
#### Uitvoer
```
De grote prijs van Monaco wordt verreden over 78 ronden (260.52 km).
```

### Voorbeelden van ongeldige invoer
```
Naam van de grote prijs: 21
Afstand: test
Gemiddelde tijd: test
```

## 3. Ontwerp
> Vraag het land
> 
> Vraag de afstand van de ronde in km
>
> Vraag de gemiddelde tijd per ronde in minuten
> 
> Zoek uit wat eerder is -> afstand limiet of tijd limiet
> 
> Kijk vervolgens of het land Monaco is -> zoja worden er maar 78 rondes gereden
> 
> Geef vervolgens het aantal rondes terug
> 
> Voor de output wordt het aantal rondes vermenigvuldigd met de afstand van elke ronde

## 4. Pseudocode
```
invoer = naam grote prijs
invoer = Afstand ronde
invoer = Gemiddelde tijd ronde

ronde_tijd = 120 / gemiddelde tijd
ronde_afstand = 305 / afstand

als naam gelijk is aan monaco -> rondes = 78
als ronde_tijd kleiner is dan ronde ronde_afstand -> rondes = ronde_tijd
anders -> rondes = ronde_afstand
```

## 5. Code
```python
from math import ceil

def calculate(country: str, distance: float, average: float) -> int:
    """
    Bereken het aantal rondes

    :param country: Het land vn de grote prijs
    :param distance: De afstand van een ronde
    :param average: De gemiddelde tijd vn een ronde

    :return: Het aantal rondes
    """
    rounds_time = ceil(120 / average)
    rounds_distance = ceil(305 / distance)

    if country.lower() == 'monaco':
        rounds = 78
    elif rounds_time < rounds_distance:
        rounds = rounds_time
    else:
        rounds = rounds_distance

    return rounds

def main() -> None:
    country = input('Naam van de grote prijs: ')
    distance = float(input('Afstand: '))
    average = float(input('Gemiddelde tijd: '))

    rounds = calculate(country, distance, average)

    print('De grote prijs van {country} wordt verreden over {rounds} ronden ({km:.3f} km)'.format(
        country=country,
        rounds=rounds,
        km=rounds * distance)
    )

if __name__ == '__main__':
    main()
```

## 6. Test
```python
from unittest import TestCase
import Formule1

class test_formule_1(TestCase):
    def velify(self):
        self.assertTrue(Formule1.calculate('Brazilië', 5.031, 1.54178) == 61)
        self.assertTrue(Formule1.calculate('België', 7.004, 2.88772) == 42)
        self.assertTrue(Formule1.calculate('Monaco', 3.340, 1.13895) == 78)
```