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
