# Uitwerking opdracht
| Opdracht      | Dronken mier     |
|---------------|------------------|
| Weeknummer    | 4                |
| Studentnummer | S1094204         |
| Naam student  | Owain van Brakel |
| Specialisatie | FICT             |
| Pogingnummer  | 1                |

## 1. Vraagstelling
Zie: https://dodona.ugent.be/nl/exercises/276629077/

> In deze opgave simuleren we het gedrag van een mier die op basis van een verstoord feromonenspoor de weg naar zijn nest probeert terug te vinden. De omgeving waarin de mier zich beweegt, wordt voorgesteld als een vierkant n×n rooster met n rijen en n kolommen. De mier bevindt zich initieel in de linkeronderhoek van het rooster en zijn nest bevindt zich in de rechterbovenhoek van het rooster. Elke cel van het rooster bevat een feromonenspoor dat wijst naar boven, onder, links of rechts. Bij elke simulatiestap verplaatst de mier zich naar de naburige cel die wordt aangegeven door het feromonenspoor, waarna de richting van het spoor op de cel die wordt verlaten 90° in wijzerzin gedraaid wordt. Indien de mier niet in de aangegeven richting kan bewegen omdat ze tegen de rand van het rooster aanloopt, blijft ze op haar huidige positie staan, maar wordt de richting van het spoor op de cel wel nog 90° in wijzerzin gedraaid.

## 2. Specificatie
#### Invoer
> Bij deze opdracht vindt geen invoer plaats

#### Uitvoer
> Bij deze opdracht is er geen uitvoer, de functies worden direct aangeroepen en de return waarde wordt weergegeven.

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
-
```

### Voorbeelden van ongeldige invoer
```
-
```

## 3. Ontwerp
> -

## 4. Pseudocode
```
functie rooster(size, track)
    als size * size != aan lengte van track
        Gooi een error

    Loop door de de track heen per size:
        Voeg de string toe aan per letter

    Geef de track terug

functie tekst(vierkant)
    Loop door de eerste lijst heen
        Loop door de tweede lijst heen
            Voeg elk karakter toe aan nieuwe string
        Voeg een newline
    Geef nieuwe string terug


functie doe_stap(vierkant, positie)
    Haal de richtig op van de huidige positie
    Draai de richting 90 graden
    Loop in de richting

fucntie stap(vierkant positie)
    Voer de fucntie doe stap uit
    Kijk na of de mier niet buiten het vierkant is gelopen

    Geef nieuwe positie terug

functie stappen(vierkant)
    Begin linksonderin
    Endig rechtsbovenin

    Zolang positie != eind
        Voer functie doe stap uit
```

## 5. Code
```python
from typing import List


def rooster(size: int, track: str) -> list:
    """
    Maak een rooster aan de hand van de param track met de hoogte en breedte van de param size

    :param size: Hoogte en breedte van het rooster
    :param track: Het spoor van de mier

    :return:
    """
    # kijk na of het spoor even lang is als size * size
    if size * size is not len(track):
        # Gooi een error op als de invoer niet klopt
        raise AssertionError("ongeldige argumenten")

    # Breek de string af per `size` vaardoor de rijen worden gemaakt, voeg vervolgens alle rijen samen in een list
    return [list(x) for x in [track[i:i + size] for i in range(0, len(track), size)]]


def tekst(vierkant: List[List[str]]) -> str:
    """
    Maak een string van het rooster die veergegeven kan worden

    :param vierkant: Het rooster

    :return: 'visuele' weergave van het rooster
    """
    # Map de lijsten naar een string, voeg elke rij samen gescheiden door een newline
    # en voeg elk karakter in de rij sames gescheiden door een spatie
    return '\n'.join(map(str, [' '.join(map(str, row)) for row in vierkant]))


def doe_stap(vierkant: List[List[str]], positie: tuple) -> tuple:
    """
    Bereken alle waardes van een enkele stap

    :param vierkant: Het rooster
    :param positie: De huidige positie van de mier

    :return: een tuple van het nieuwe rooster, de nieuwe locatie en of het eet valide stap is
    """
    # Alle mogelijke richtingen
    direction = ["<", "^", ">", "v"]
    # Alle stappen die bij de richtingen horen
    direction_index = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    # Haal de index op van de richting van de cel waarop de mier zich bevind
    index = direction.index(vierkant[positie[0]][positie[1]])

    # Draai de richting van de cel waarop de mier zich bevind met 90 graden
    vierkant[positie[0]][positie[1]] = direction[(index + 1) % len(direction)]
    # Bereken aan de hand van de richting de nieuwe locatie van de mier
    new_loc = tuple(map(sum, zip(positie, direction_index[index % len(direction_index)])))

    # Kijk na of de mier zich buiten het rooster bevind
    valid_move = -1 < new_loc[0] < len(vierkant) and -1 < new_loc[1] < len(vierkant)

    return vierkant, new_loc, valid_move


def stap(vierkant: List[List[str]], positie: tuple) -> tuple:
    """
    Laat de mier één stap zetten in het rooster

    :param vierkant: Het rooster
    :param positie: de huidige positie van de mier

    :return: De nieuwe locatie
    """
    # Dit is dus wel iets waar je een mhile True voor kan gebruiken
    while True:
        # Voer een enkele stap uit en sla de return waardes op
        _, location, valid = doe_stap(vierkant, positie)
        # Kijk na of de stap valide is
        if valid:
            # Geef de nieuwe locatie terug
            return location


def stappen(vierkant: List[List[str]]) -> list:
    """
    Laat de mier vanaf de beginpositie (linksonderin) naar z'n hol lopen (rechtsbovenin)

    :param vierkant: Het rooster

    :return: Een lijst met alle locaties waar de mier is geweest
    """
    # Begin positie
    pos = (len(vierkant) - 1, 0)
    # Eind positie
    end_pos = (0, len(vierkant) - 1)
    # Een lijst waarin alle stappen worden bijgehouden
    lst = []

    # Zolang de mier niet bij z'n hol is
    while pos != end_pos:
        # Voer een enkele stap uit en sla de return waardes op
        vierkant, location, valid = doe_stap(vierkant, pos)
        # Kijk na of de stap valide is
        if valid:
            # Sla de nieuwe positie van de mier op
            pos = location
        # Voeg de locatie van de mier toe aan de stappen lijst
        lst.append(pos)

    # Geef de hele lijst met stappen terug
    return lst


def main() -> None:
    vierkant = rooster(4, '>>>>^<^v^v^^>>v>')
    print(vierkant)
    print(tekst(vierkant))

    print(stap(vierkant, (3, 0)))
    print(tekst(vierkant))

    print(stap(vierkant, (3, 1)))
    print(tekst(vierkant))

    vierkant = rooster(4, '>>>>^<^v^v^^>>v>')
    print(tekst(vierkant))

    print(stappen(vierkant))
    print(tekst(vierkant))

    # Deze geeft een error zoals in de opdracht beschreven staat
    # rooster(4, '>>>>^<^v^v^>>v>')


if __name__ == "__main__":
    main()
```