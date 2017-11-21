# Uitwerking opdracht
| Opdracht      | Slaapkwaliteit   |
|---------------|------------------|
| Weeknummer    | 2                |
| Studentnummer | S1094204         |
| Naam student  | Owain van Brakel |
| Specialisatie | FICT             |
| Pogingnummer  | 1                |

## 1. Vraagstelling
Zie:  https://dodona.ugent.be/nl/exercises/1795071955/

> Je biologische klok — of circadiaanse klok van het Latijnse circa voor ongeveer en dies voor dag — is een biologisch ritme waarvan de cyclus ongeveer één dag duurt. Deze klok wordt gereguleerd door processen in de hersenen die reageren op de tijd dat je reeds wakker bent en de wisselingen tussen licht en donker. 's Nachts reageert je lichaam op het gebrek aan daglicht door het aanmaken van melatonine, een hormoon waarvan je slaperig wordt. Overdag zet het zonlicht je hersenen ertoe aan om de aanmaak van melatonine te blokkeren, waardoor je je wakker en alert voelt.

> De interne klok van de mens kan door verschillende factoren verstoord worden: nachtwerk, reizen over verschillende tijdszones of onregelmatige slaappatronen. Dit kan ervoor zorgen dat je je groggy, gedesoriënteerd of slaperig voelt op momenten waarop dit ongelegen komt. De productie van melatonine kan ook verstoord raken bij gebrek aan zonlicht gedurende de dag of overmatige blootstelling aan kunstlicht tijdens de nacht, en dan vooral het licht van elektronische apparaten zoals tv's, computers, tablets en mobiele telefoons.

> Je zou kunnen vermoeden dat als je eenmaal naar bed bent gegaan, je weldra in een diepe slaap valt die zowat de hele nacht aanhoudt, en in de ochtend overgaat in een lichte slaap totdat het moment van opstaan is aangebroken. De slaapcyclus is echter een stuk gecompliceerder dan dat. Tijdens de nacht volgt je slaap een voorspelbaar patroon, dat heen en weer beweegt tussen een diep slaap en meer alertere momenten waarin je aan het dromen bent (REM slaap). De fasen van de REM slaap en niet-REM slaap vormen samen een volledige slaapcyclus. Elke slaapcyclus duurt typisch zo'n 90 minuten, en herhaalt zich idealiter vier tot zes keer tijdens de nacht. Hoe lang je doorbrengt in elke slaaptoestand wijzigt naarmate de nacht vordert. Het grootste gedeelte van de diepe slaap komt bijvoorbeeld voor tijdens het eerste deel van de slaap. Verder in de slaap worden de periodes van de REM slaap langer, afgewisseld met fase2 slaapperiodes. Dit verklaart waarom je eerder wakker wordt in de vroege uurtjes, als je gevoelig bent aan wakker worden in het midden van de nacht, eerder dan dat het zich voordoet kort nadat je bent ingeslapen.

![alt text](https://dodona.ugent.be/exercises/1795071955/media/hypnogram.png "Hypnogram")

> Zelfs wanneer je van een lange slaap hebt genoten, kan het toch moeilijk zijn om uit bed te komen wanneer de wekker afgaat temidden een diepe slaapfase (fase 3). Als je het opstaan minder pijnlijk wilt maken — of als je weet dat je maar korte tijd kunt slapen — probeer je wekker dan zo in te stellen dat je een veelvoud van 90 minuten slaapt, aangezien dit de lengte is van een gemiddelde slaapcyclus. Als je bijvoorbeeld om 22:00 naar bed gaat, zet dan je alarm om 05:30 (na zevenenhalf uur slaap) eerder dan om 06:00 of 06:30. Het zou wel eens kunnen dat je je om 05:30 veel uitgeruster voelt dan wanneer je nog een half uur of een uur was blijven doorslapen, omdat je dan opstaat op het einde van een slaapcyclus wanneer je lichaam en hersenen toch al dicht bij een waaktoestand waren. Er zijn zelfs ook al mobiele apps beschikbaar die heel nauwkeurig je slaapcycli opvolgen, en op basis daarvan bepalen wanneer de wekker best afgaat.

## 2. Specificatie
#### Invoer
> De invoer bestaat uit vier natuurlijke getallen, elk op een afzonderlijke regel. De eerste twee getallen stellen het uur en de minuut voor van het tijdstip waarop je in slaap valt (of denkt te vallen), en de laatste twee getallen stellen het uur en de minuut voor van het tijdstip waarop je ten vroegste wilt opstaan. Beide tijdstippen worden uitgedrukt volgens een 24-uursklok, dus met uren tussen 0 en 23 en minuten tussen 0 en 59.

Bijvoorbeeld:
```
22
37
6
0
```

#### Uitvoer
> Als uitvoer moet je een regel uitschrijven met het ideale tijdstip om op te staan. Dit is het eerstvolgende tijdstip vanaf het tijdstip waarop je ten vroegste wilt opstaan, dat je een slaapduur oplevert die een veelvoud is van 90 minuten. Dit tijdstip moet worden uitgedrukt op een 24-uursklok, dus met uren tussen 0 en 23 en minuten tussen 0 en 59. De uren en minuten van het tijdstip moeten van elkaar gescheiden worden met een dubbelpunt, en beide getallen moeten weergegeven worden met twee cijfers door indien nodig een voorloopnul aan het getal toe te voegen.

Bijvoorbeeld:
```
06:07
```

### **Verbanden in en uitvoer**
> De invoer wordt verwerkt en aan de hand daarvan wordt de output gegenereerd

### **Beperkingen**
> De invoer wordt niet gevalideerd, tevens is het is niet mogelijk om op dezelfde dag te gaan slapen als wakker te worden, denk aan: 00:12 slapen 8:00 wakker worden of 13:12 slapen 20:00 wakker

## Voorbeelden
#### Invoer
```
22
37
6
0
```
#### Uitvoer
```
06:07
```

### Voorbeelden van ongeldige invoer
```
00
37
6
0
```

```
00
377
6
0
```

```
a
377
b
0
```

## 3. Ontwerp
> Vraag om het uur van in slaap vallen
> 
> Vraag om de minuten van in slaap vallen
> 
> Vraag om het uur van wakker worden
> 
> Vraag om de minuten van wakker worden
> 
> Bereken het eerste 90 minuten moment na de ingevoerde wakker worden tijdstip

## 4. Pseudocode
```
invoer_slapen_uur = slapen_uur
invoer_slapen_minuten = slapen_minuten
invoer_wakker_uur = wakker_uur
invoer_wakker_minuten = wakker_minuten

datum_slapen = datum(invoer_slapen_uur = slapen_uur, invoer_slapen_minuten)
datum_wakker = datum(invoer_wakker_uur = slapen_uur, invoer_wakker_minuten)

tijdverschil = datum_wakker - datum_slapen

rest = tijdverschil % 90

datum_wakker + rest
```

## 5. Code
```python
from datetime import datetime, timedelta
from time import mktime

def calculate(sleep_hour: int, sleep_minute: int, awake_hour: int, awake_minute: int) -> str:
    """
    Bereken de beste tijd om wakker te worden

    :param sleep_hour: het uur van in slaap vallen
    :param sleep_minute: de minuut van in slaap vallen
    :param awake_hour: het uur van wakker worden
    :param awake_minute: de minuten van wakker worden

    :return: De beste tijd om wakker te worden
    """
    s1 = '01/01/1970 {}:{}'.format(sleep_hour, sleep_minute)  # Zet de gegevens om naar een datum
    s2 = '02/01/1970 {}:{}'.format(awake_hour, awake_minute)  # Zet de gegevens om naar een datum
    fmt = '%d/%m/%Y %H:%M'  # Format van de datum

    minutes = int(mktime(datetime.strptime(s2, fmt).timetuple()) - mktime(datetime.strptime(s1, fmt).timetuple())) / 60

    # Eerste 90 minuten punt na de wekker
    return (datetime.strptime(s2, fmt) + timedelta(minutes=90 - minutes % 90)).strftime('%H:%M')

def main() -> None:
    sleep_hour = int(input('Uur van in slaap vallen: '))
    sleep_minute = int(input('Minuten van in slaap vallen: '))
    awake_hour = int(input('Uur van in wakker worden: '))
    awake_minute = int(input('Minuten van wakker worden: '))

    print(calculate(sleep_hour, sleep_minute, awake_hour, awake_minute))

if __name__ == '__main__':
    main()

```

## 6. Test
```python
from unittest import TestCase
import Slaapkwaliteit

class test_slaapkwaliteit(TestCase):
    def verify(self):
        self.assertTrue(Slaapkwaliteit.calculate(22, 37, 6, 0) == '06:07')
        self.assertTrue(Slaapkwaliteit.calculate(23, 44, 9, 15) == '10:14')
```