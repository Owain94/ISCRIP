from math import floor


def milliseconds(sol: int) -> int:
    """
    Aantal sol in milliseconden

    :param sol: het aantal sol
    :return: het aantal sol in milliseconden
    """
    sol_milliseconds = int((3600000 * 24) + (60000 * 39) + (1000 * 35) + 244)  # Één sol in ms

    return sol_milliseconds * sol


def human_readable(miliseconds_sol: int) -> tuple:
    """
    Milliseconden naar dagen, uren, minuten, seconden

    :param miliseconds_sol: het aantal sol in milliseconden

    :return: Tuple met het aantal dagen, uren, minuten, seconden
    """
    x = miliseconds_sol / 1000
    seconds = x % 60
    x /= 60
    minutes = x % 60
    x /= 60
    hours = x % 24
    x /= 24
    days = x

    return floor(days), floor(hours), floor(minutes), floor(seconds)


def main() -> None:
    # Verifieer input
    while True:
        sol_input = input('Geef het aantal sol in:\n')

        try:
            sol = int(sol_input)
            break
        except ValueError:
            continue

    time = human_readable(milliseconds(sol))
    print('{sol} sol = {dys:.0f} dagen, {hrs:.0f} uren, {min:.0f} minuten en {sec:.0f} seconden'.format(
        sol=sol,
        dys=time[0],
        hrs=time[1],
        min=time[2],
        sec=time[3])
    )


if __name__ == '__main__':
    main()
