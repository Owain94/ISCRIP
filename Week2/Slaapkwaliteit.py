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
