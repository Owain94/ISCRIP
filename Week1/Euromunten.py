def calculate(inp: tuple) -> tuple:
    """
    Berekent het totaal aantal munten en het totale bedrag

    :param inp: Tuple met alle euromunten waardes

    :return: tuple met het totaal aantal munten en het totale bedrag
    """
    return (
               (inp[0] * 1) +
               (inp[1] * 2) +
               (inp[2] * 5) +
               (inp[3] * 10) +
               (inp[4] * 20) +
               (inp[5] * 50) +
               (inp[6] * 100) +
               (inp[7] * 200)
            ) / 100, sum(inp)


def main() -> None:
    one = int(input('Aantal 1 cent munten: '))
    two = int(input('Aantal 2 cent munten: '))
    five = int(input('Aantal 5 cent munten: '))
    ten = int(input('Aantal 10 cent munten: '))
    twenty = int(input('Aantal 20 cent munten: '))
    fifty = int(input('Aantal 50 cent munten: '))
    hunderd = int(input('Aantal 1 euro munten: '))
    twohunderd = int(input('Aantal 2 euro munten: '))

    cents, total = calculate((one, two, five, ten, twenty, fifty, hunderd, twohunderd))

    print('{total}\n{cents:.2f}'.format(total=total, cents=cents))


if __name__ == '__main__':
    main()
