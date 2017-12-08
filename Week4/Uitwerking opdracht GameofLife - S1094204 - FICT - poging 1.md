# Uitwerking opdracht
| Opdracht      | Game of life     |
|---------------|------------------|
| Weeknummer    | 4                |
| Studentnummer | S1094204         |
| Naam student  | Owain van Brakel |
| Specialisatie | FICT             |
| Pogingnummer  | 1                |

## 1. Vraagstelling
Zie: https://dodona.ugent.be/nl/exercises/511272034/

> Schrijf een functie toonGeneratie die de toestand van een gegeven generatie afdrukt. Deze functie heeft één verplicht argument: een lijst van lijsten die een rechthoekig rooster voorstelt. De geneste lijsten hebben allemaal dezelfde lengte en bevatten enkel Booleaanse waarden. Een generatie wordt dus voorgesteld door een lijst van rijen, waarbij elke rij zelf ook door een lijst wordt voorgesteld. Op positie n staat er True als de cel op kolom n in die rij leeft. Anders staat er False. De levende cellen worden bij het afdrukken voorgesteld door de letter X en de dode cellen worden voorgesteld door de letter O (niet het cijfer nul!!).

> Schrijf een functie aantalBuren die voor een gegeven generatie en een gegeven cel teruggeeft hoeveel levende buren die cel heeft. Deze functie heeft drie verplichte argumenten: het eerste argument is de gegeven generatie, het tweede argument de rij en het derde argument de kolom van de cel waarvan de buren worden opgevraagd.

> Gebruik de functie aantalBuren om een functie volgendeGeneratie te schrijven, dat de volgende generatie teruggeeft voor een gegeven generatie. Deze nieuwe generatie wordt op dezelfde manier voorgesteld als de gegeven generatie, namelijk als een lijst van lijsten. De gegeven generatie wordt als argument aan de functie doorgegeven, en wordt door de functie ook niet gewijzigd.

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
functie aantal buren(generatie, rij, kolom)
    Loop door elke rij heen
        Loop door elk karakter heen
            Kijk of de cel buurt aan de gegeven cel
                Kijk of de cel leeft
                    Buur = buur + 1

    Geef buur terug

functie toon generatie(generatie)
    Loop door elke rij heen
        Loop deer elke kolom heen
            Zet een boolen om naar X of O
            Voeg de letter toe aan nieuwe string
        Voeg een new line toe aan nieuwe string
   Geef nieuwe string terug

functie volgende generatie(generatie)
    Loop door elke rij heen
        Loop door elke kolom heen
            Kijk het aantal buren na
                Als de cel levend is en 2 of 3 buren heeft
                    Nieuwe cel levend
                Als de cel dood is en 3 buren heeft
                    Nieuwe cel levend
                Anders
                    Nieuwe cel dood
            Voeg de nieuwe cel toe
        Voeg de rij toe
    Geef nieuwe generatie terug
```

## 5. Code
```python
from typing import List


def aantalBuren(generatie: List[List[bool]], rij: int, kolom: int) -> int:
    """
    Geei het aantal buren vaan een cel terug

    :param generatie: De hele ganeratie
    :param rij: De rij van de cel
    :param kolom: de kolom van de cel

    :return: het aantal buren
    """
    nieuwe_rij = rij - 1
    nieuwe_kolom = kolom - 1
    buren = 0

    # Loop door alle kolommen om de cel heen
    for y in range(nieuwe_kolom, nieuwe_kolom + 3):
        # Loop door elke rij hom de cel heen
        for x in range(nieuwe_rij, nieuwe_rij + 3):
            # Kijk of de cel zich in binnen het rooster bevind
            if not (x < 0 or y < 0) and y < len(generatie) and x < len(generatie[0]):
                # Kijk of het niet de cel zelf is
                if rij != x or kolom != y:
                    # Kijk of de cel levend is
                    if generatie[y][x]:
                        # Voeg 1 toe aan het aantal buren
                        buren += 1

    # Geef het aantal buren terug
    return buren


def toonGeneratie(generatie: List[List[bool]]) -> str:
    """
    Zet de generatie om naar een 'visuele' string

    :param generatie: de hele generatie

    :return: Een visuele weergave van de generatie
    """
    # Voeg alle rijen samen gescheiden door een newline
    # voeg elk karakter in de rij samen gescheiden door een spatie (O of X)
    return "\n".join([str(" ".join([['O', 'X'][x] for x in row])) for row in generatie])


def volgendeGeneratie(generatie: List[List[bool]]) -> List[List[bool]]:
    """
    Bouw de volgende generatie op

    :param generatie: de huidige generatie

    :return: De nieuwe generati
    """
    # MAak een lege lijst aan om de nieuwe generatie in op te lsaan
    nieuwe_generatie = []

    # Loop door de rijen van de genaratie heen
    for y, rij in enumerate(generatie):
        # Maak een lege loop om de rij in op te slaan
        nieuwe_rij = []

        # Loop door alle cellen van een rij heen
        for x, cel in enumerate(rij):
            # Zet de cel standaard op dood
            nieuw_cel = False

            if not nieuw_cel:
                # Bekijk het aantal buren
                if cel and aantalBuren(generatie, x, y) in [2, 3]:
                    # Zet de cel op levend
                    nieuw_cel = True

            if not nieuw_cel:
                # Bekijk het aantal buren
                if not cel and aantalBuren(generatie, x, y) is 3:
                    # Maak de cel levend
                    nieuw_cel = True

            # Voeg de cel toe aan de rij
            nieuwe_rij.append(nieuw_cel)
        # Voeg elke rij toe aan de nieuwe geneartie
        nieuwe_generatie.append(nieuwe_rij)

    return nieuwe_generatie


def main() -> None:
    generatie = [[True] + [False] * 7 for _ in range(6)]

    print(aantalBuren(generatie, 0, 0))
    print(aantalBuren(generatie, 1, 1))
    print(aantalBuren(generatie, 2, 2))

    volgende = volgendeGeneratie(generatie)
    print(toonGeneratie(volgende))
    print()

    volgende = volgendeGeneratie(volgende)
    print(toonGeneratie(volgende))
    print()

    volgende = volgendeGeneratie(volgende)
    print(toonGeneratie(volgende))
    print()

    volgende = volgendeGeneratie(volgende)
    print(toonGeneratie(volgende))


if __name__ == '__main__':
    main()
```