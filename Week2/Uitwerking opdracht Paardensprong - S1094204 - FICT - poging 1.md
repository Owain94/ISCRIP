# Uitwerking opdracht
| Opdracht      | Paardensprong    |
|---------------|------------------|
| Weeknummer    | 2                |
| Studentnummer | S1094204         |
| Naam student  | Owain van Brakel |
| Specialisatie | FICT             |
| Pogingnummer  | 1                |

## 1. Vraagstelling
Zie: https://dodona.ugent.be/nl/exercises/56374393/

> Een schaakbord bestaat uit 64 vierkanten die gerangschikt zijn in een rooster van 8 rijen en 8 kolommen. De vierkanten hebben afwisselend een lichte en een donkere kleur. De rijen van het bord worden van onder naar boven aangeduid met de cijfers 1-8 en de kolommen worden van links naar rechts aangeduid met de letters a-h. Op die manier heeft elk vierkant op het bord een naam die bestaat uit de letter van de kolom en het cijfer van de rij waarop het vierkant gelegen is.

![alt text](https://dodona.ugent.be/exercises/56374393/media/knight.png "Paardensprong")

> Het paard is één van de zes verschillende stukken van het schaakspel. De manier waarop een paard kan bewegen over het schaakbord — de paardensprong — is ongebruikelijk onder de schaakstukken. Als het paard beweegt, dan verplaatst het zich naar een positie die twee vierkanten horizontaal en één vierkant verticaal, of één vierkant horizontaal en twee vierkanten verticaal verwijderd is van zijn oorspronkelijke positie. Daardoor heeft de volledige beweging de vorm van de letter L en springt het paard afwisselend naar lichte en donkere vierkanten.

> In tegenstelling tot de andere schaakstukken kan een paard over alle andere schaakstukken springen naar een nieuwe positie, ongeacht hun kleur. Het vangt een vijandelijk stuk door het te vervangen op zijn nieuwe positie. Het vermogen van het paard om over andere stukken te springen, betekent dat het meest tot zijn recht komt in ingesloten posities, in tegenstelling tot bijvoorbeeld de loper.

> De paardensprong is al meer dan zeven eeuwen een vast onderdeel van het schaakspel, en is daarmee één van de langste overlevende bewegingen in het spel. Daardoor komt het ook voor in de meeste lokale varianten van het schaakspel.

## 2. Specificatie
#### Invoer
> De invoer bestaat uit twee regels, die elk de naam van een vierkant op het schaakbord bevatten.

Bijvoorbeeld:
```
d4
e6
```

#### Uitvoer
> De uitvoer bestaat uit één regel die aangeeft of het paard al dan niet van het eerste vierkant naar het tweede vierkant op het schaakbord kan springen. Bekijk onderstaande voorbeelden om te zien in welk formaat de uitvoer moet opgemaakt worden.

Bijvoorbeeld:
```
het paard kan springen van d4 naar e6
```

### **Verbanden in en uitvoer**
> De invoer wordt verwerkt en aan de hand daarvan wordt de output gegenereerd

### **Beperkingen**
> Als de invoer van de begin positie met een hoofdletter is dan moet de invoer van de eindpositie ook met een hoofletter zijn (geldt ook voor kleine letters)

## Voorbeelden
#### Invoer
```
d4
e6
```
#### Uitvoer
```
Het paard kan springen van d4 naar e6
```

#### Invoer
```
h1
c2
```
#### Uitvoer
```
Het paard kan niet springen van h1 naar c2
```

### Voorbeelden van ongeldige invoer
```
D4
e6
```
```
h1
C2
```

## 3. Ontwerp
> Vraag het startpunt
> 
> Vraag het eindpunt
> 
> Bereken alle mogelijke posities vanaf het startpunt
>
> Kijk of het eindpunt in alle mogelijkheden zit

## 4. Pseudocode
```
invoer_startpunt = startpunt
invoer_eindpunt = eindpunt

zet de letter van het startpunt om naar een getal
zet de letter van het enidpunt om naar een getal

bereken alle mogelijke posities
mogelijkheden = []
mogelijkheid += startpunt[0] + 1 en startpunt[1] + 2
mogelijkheid += startpunt[0] - 1 en startpunt[1] + 2
mogelijkheid += startpunt[0] + 2 en startpunt[1] + 1
etc...

for mogelijkheid in mogelijkheden
    als mogelijkheid is buiten het bord -> verwijder mogenlijkheid

return als eindpunt in mogelijkheden
```

## 5. Code
```python
from string import ascii_lowercase

def step(pos_one: str, pos_two: str) -> bool:
    """
    Kijk of de pardensprong mogelijk is

    :param pos_one: Begin positie
    :param pos_two: Eind positie

    :return: Boolean of de sprong wel of niet mogelijk is
    """
    return (ascii_lowercase.index(pos_two[0].lower()) + 1, int(pos_two[1])) \
           in horse_jump(ascii_lowercase.index(pos_one[0].lower()) + 1, int(pos_one[1]))

def horse_jump(x: int, y: int) -> list:
    """
    Bereken alle mogelijke posities voor de paardensprong

    :param x: x positie van het startpunt
    :param y: y positie van het startpunt

    :return: List met alle mogelijke posities voor de paardensprong
    """
    positions = []

    # Alle mogelijke pardenspongen die mogelijk zijn
    for i in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
        x = x + i[0]
        y = y + i[1]

        # Het paard kan niet buiten het bord gaan
        if x >= 9 or x < 1 or y >= 9 or y < 1:
            continue
        else:
            positions.append((x, y))

    return positions

def main() -> None:
    start = input('Startpunt: ')
    end = input('Eindpunt: ')

    print('het paard kan{tf} springen van {start} naar {end}'.format(
        tf=[' niet', ''][step(start, end)],  # Python heeft geen fatsoenlijke ternary operator (val ? 'niet' : '')
        start=start,
        end=end)
    )

if __name__ == '__main__':
    main()
```

## 6. Test
```python
from unittest import TestCase
import Paardensprong

class test_paardensprong(TestCase):
    def verify(self):
        self.assertTrue(Paardensprong.step('d4', 'e6'))
        self.assertFalse(Paardensprong.step('d4', 'd6'))

        self.assertFalse(Paardensprong.step('h1', 'c2'))
        self.assertTrue(Paardensprong.step('h1', 'f2'))
```