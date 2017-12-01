from string import punctuation


def calculate(password: str) -> str:
    """
    Bereken wachtwoord sterkte

    :param password: wachtwoord

    :return: zwak / matig / sterk
    """
    strenght = 0

    if len(password) > 8:  # Langer dan 8 chars?
        strenght += 1

    if any(x.isupper() for x in password):  # hoofdletter
        strenght += 1

    if any(x.islower() for x in password):  # normale letter
        strenght += 1

    if any(x.isnumeric() for x in password):  # numeriek
        strenght += 1

    if any(x in punctuation for x in password):  # leestekens
        strenght += 1

    if strenght < 3:
        return 'zwak'
    elif strenght < 5:
        return 'matig'
    else:
        return 'sterk'


def main() -> None:
    lst = []
    amount = int(input('Aantal wachtwoorden: '))

    for i in range(0, amount):
        lst.append(input('{count}e wachtwoord: '.format(count=i + 1)))

    for password in lst:
        print(calculate(password))


if __name__ == "__main__":
    main()
