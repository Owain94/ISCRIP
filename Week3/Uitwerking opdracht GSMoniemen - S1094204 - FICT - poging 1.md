# Uitwerking opdracht
| Opdracht      | GSMoniemen       |
|---------------|------------------|
| Weeknummer    | 3                |
| Studentnummer | S1094204         |
| Naam student  | Owain van Brakel |
| Specialisatie | FICT             |
| Pogingnummer  | 1                |

## 1. Vraagstelling
Zie: https://dodona.ugent.be/nl/exercises/1858246142/

> Schrijf een functie T9 waaraan een string moet doorgegeven worden die enkel bestaat uit letters. Deze functie moet als resultaat een string teruggeven met de cijfercombinatie die je moet ingeven op een GSM-toestel dat het T9-systeem ondersteunt. Hierbij mag de functie geen onderscheid maken tussen hoofdletters en kleine letters.

> Gebruik de functie T9 om een functie GSMoniemen te schrijven waaraan twee strings moeten doorgegeven worden. Deze functie moet als resultaat een Booleaanse waarde teruggeven die aangeeft of de gegeven strings al dan niet GSMoniemen zijn.

## 2. Specificatie
#### Invoer
> Bij deze opdracht vindt geen invoer plaats

#### Uitvoer
> Bij deze opdracht is er geen uitvoer, de functies worden direct aangeroepen en de return waarde wordt weergegeven.
> 
> De T9 functie geeft een string terug en GSMoniemen functie geeft een boolean terug

### **Verbanden in en uitvoer**
> -

### **Beperkingen**
> Er is geen invoer mogelijk

## Voorbeelden
#### Invoer
```
-
```
#### Uitvoer
```
De T9 functie geeft een string terug en GSMoniemen functie geeft een boolean terug
```

### Voorbeelden van ongeldige invoer
```
-
```

## 3. Ontwerp
> De opdracht moet twee fucties bevatten namelijk T9 en GSMoniemen
> De functie T9 moet zal woorden omzetten in de T9 variant van het woord
> De functie GSMoniemen zal kijken of twee woorden dezelfde T9 variant terug geven

## 4. Pseudocode
```
functie T9(woord)
    Voor elke letter in woord
        als letter in abc
            1
        als letter in def
            2
        etc.

fuctie GSMoniemen(woord_1, woord_2)
    als T9(woord_1) gelijk aan T9(woord_2)
```

## 5. Code
```python
# noinspection PyPep8Naming
def T9(message: str) -> str:  # Function name should be lower case (PEP8 naming conventions)
    """
    Zet een bericht om naar de T9 variant van het bericht

    :param message: Het bericht
    :return: Een nummer reeks van de T9 variant
    """
    key = ''

    for symbol in message:
        if symbol.lower() in 'abc':
            key += '2'
        if symbol.lower() in 'def':
            key += '3'
        if symbol.lower() in 'ghi':
            key += '4'
        if symbol.lower() in 'jkl':
            key += '5'
        if symbol.lower() in 'mno':
            key += '6'
        if symbol.lower() in 'pqrs':
            key += '7'
        if symbol.lower() in 'tuv':
            key += '8'
        if symbol.lower() in 'wxyz':
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
```

## 6. Test
```python
from unittest import TestCase
import GSMoniemen

class test_GSMoniemen(TestCase):
    def velify(self):
        self.assertTrue(GSMoniemen.T9('Hallo') == '42556')
        self.assertTrue(GSMoniemen.T9('aanbod') == '226263')
        self.assertTrue(GSMoniemen.T9('bamboe') == '226263')

        self.assertTrue(GSMoniemen.GSMoniemen('aanbod', 'bamboe'))
        self.assertFalse(GSMoniemen.GSMoniemen('maandag', 'vrijdag'))
```