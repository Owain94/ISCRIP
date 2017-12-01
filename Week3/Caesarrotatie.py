def encode(key: int, message: str) -> str:
    """
    Ontcijver een caesarrotatie door middel van misbruik te maken van de ASCII chart

    :param key: Aantal letter verschoven
    :param message: Bericht om te ontcijveren

    :return: Oncijverde bericht
    """
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num -= key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26  # Ga terug naar het begin van het alfabet 
                elif num < ord('A'):
                    num += 26  # Ga naar het einde van het alfabet 
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26  # Ga naar het einde van het alfabet 
                elif num < ord('a'):
                    num += 26  # Ga terug naar het begin van het alfabet 

            translated += chr(num)
        else:
            translated += symbol  # Voeg charaters die geen letter zijn sowieso toe

    return translated


def main() -> None:
    pos = int(input('Posities: '))
    cipher = input('Cipher: ')

    print(encode(pos, cipher))


if __name__ == "__main__":
    main()
