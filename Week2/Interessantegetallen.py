def calculate(test: int) -> int:
    """
    Het kleinste getal dat deelbaar is door en waarvan de som van de cijfers gelijk is aan

    :param test: testgeval

    :return: Het kleinste natuurlijk getal
    """
    num = 1

    while True:
        # Controlleer of de test deelbaar is door en de som gelijk is aan
        if num % test == 0 and sum(list(map(int, str(num)))) == test:
            break
        num += 1

    return num


def main() -> None:
    test = 51  # Fucking goor maar het werkt wel
    tests = []

    while 0 < test > 50:
        test = int(input('Aantal testgevallen: '))

    for i in range(0, test):
        given_test = int(input('Testgeval {count}: '.format(count=i + 1)))

        while 0 < given_test > 100:
            given_test = int(input('Testgeval {count}: '.format(count=i + 1)))

        tests.insert(i, given_test)

    for i in tests:
        print(calculate(i))


if __name__ == "__main__":
    main()
