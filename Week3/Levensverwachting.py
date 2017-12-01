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
