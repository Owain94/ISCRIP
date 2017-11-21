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
