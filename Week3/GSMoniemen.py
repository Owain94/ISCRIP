# noinspection PyPep8Naming
def T9(message: str) -> str:  # Function name should be lower case (PEP8 naming conventions)
    """
    Zet een bericht om naar de T9 variant van het bericht

    :param message: Het bericht
    :return: Een nummer reeks van de T9 variant
    """
    key = ''

    for symbol in message.lower():
        if symbol in 'abc':
            key += '2'
        if symbol in 'def':
            key += '3'
        if symbol in 'ghi':
            key += '4'
        if symbol in 'jkl':
            key += '5'
        if symbol in 'mno':
            key += '6'
        if symbol in 'pqrs':
            key += '7'
        if symbol in 'tuv':
            key += '8'
        if symbol in 'wxyz':
            key += '9'
        if symbol == ' ':
            key += '0'

    return key


# noinspection PyPep8Naming
def GSMoniemen(message_one: str, message_two: str) -> bool:  # Function name should be lower case (PEP8 naming conventions)
    """
    Kijk of de T9 variant van beide berichten gelijk is

    :param message_one: Het eerste bericht
    :param message_two: Het tweede bericht

    :return: Boolean of de T9 variant gelijk zijn
    """
    return T9(message_one) == T9(message_two)


def main() -> None:
    print(T9('Hallo'))
    print(T9('aanbod'))
    print(T9('bamboe'))

    print(GSMoniemen('aanbod', 'bamboe'))
    print(GSMoniemen('maandag', 'vrijdag'))


if __name__ == "__main__":
    main()
