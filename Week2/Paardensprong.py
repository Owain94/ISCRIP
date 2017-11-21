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
