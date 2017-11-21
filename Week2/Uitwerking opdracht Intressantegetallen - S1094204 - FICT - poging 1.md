# Uitwerking opdracht
| Opdracht      | Intressante getallen |
|---------------|----------------------|
| Weeknummer    | 2                    |
| Studentnummer | S1094204             |
| Naam student  | Owain van Brakel     |
| Specialisatie | FICT                 |
| Pogingnummer  | 1                    |

## 1. Vraagstelling
Zie: https://dodona.ugent.be/nl/exercises/211647828/

> Voor een gegeven natuurlijk getal n, vind het kleinste natuurlijk getal dat deelbaar is door n en waarvan de som van de cijfers gelijk is aan n.

## 2. Specificatie
#### Invoer
> De invoer bestaan uit t testgevallen (t≤50). De eerste regel van de invoer bevat een natuurlijk getal t. Daarna volgen t regels die de verschillende testgevallen omschrijven. Elk geval wordt omschreven door een natuurlijke getal n (0<n≤100).

Bijvoorbeeld:
```
2
1
10
```

#### Uitvoer
> Schrijf voor elk testgeval het gevraagde natuurlijk getal uit op een afzonderlijke regel, zonder voorloopnullen.

Bijvoorbeeld:
```
1
190
```

### **Verbanden in en uitvoer**
> De invoer wordt verwerkt en aan de hand daarvan wordt de output gegenereerd

### **Beperkingen**
> De invoer wordt niet gevalideerd, tevens is het niet mogelijk om 0 in te vullen

## Voorbeelden
#### Invoer
```
2
1
10
```
#### Uitvoer
```
1
190
```

### Voorbeelden van ongeldige invoer
```
a
1
10
```
```
100
...
...
...
```
```
1
0
```

## 3. Ontwerp
> Vraag het aantal testgevallen
> 
> Vraag voor elk testgeval een natuurlijk getal
> 
> Bereken voor elk testgeval het kleinste natuurlijk getal dat deelbaar is door de invoer en waarvan de som van de cijfers gelijk is aan de invoer.

## 4. Pseudocode
```
invoer_aantal = Aantal testgevallen
voor testgeval in invoer_aantal
    nummer = 1
    zolang nummer is niet deelbaar door testgeval EN som testgeval is niet gelijk aan testgeval
    nummer += 1
```

## 5. Code
```python
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
```

## 6. Test
```python
from unittest import TestCase
import Interessantegetallen

class test_intressantegetallen(TestCase):
    def verify(self):
        self.assertTrue(Interessantegetallen.calculate(1) == 1)
        self.assertTrue(Interessantegetallen.calculate(2) == 2)
        self.assertTrue(Interessantegetallen.calculate(3) == 3)
        self.assertTrue(Interessantegetallen.calculate(4) == 4)
        self.assertTrue(Interessantegetallen.calculate(5) == 5)
        self.assertTrue(Interessantegetallen.calculate(6) == 6)
        self.assertTrue(Interessantegetallen.calculate(7) == 7)
        self.assertTrue(Interessantegetallen.calculate(8) == 8)
        self.assertTrue(Interessantegetallen.calculate(9) == 9)
        self.assertTrue(Interessantegetallen.calculate(10) == 190)
        self.assertTrue(Interessantegetallen.calculate(11) == 209)
        self.assertTrue(Interessantegetallen.calculate(12) == 48)
        self.assertTrue(Interessantegetallen.calculate(13) == 247)
```