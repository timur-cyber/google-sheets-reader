import requests
import xml.etree.ElementTree as ET

EXCHANGE_DATA_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def get_currency():
    """
    Функция для получения курса 1 Доллара США к Российскому Рублю c сайта ЦБ РФ
    :return: float
    """
    result = requests.get(EXCHANGE_DATA_URL)
    myroot = ET.fromstring(result.text)
    for i in myroot:
        if i.attrib.get('ID') == 'R01235':
            for k in i:
                if k.tag == 'Value':
                    currency = float(k.text.replace(',', '.'))
                    return currency


def make_exchange(sum: int):
    """
    Функция для конвертации суммы в долларах к рублю
    :param sum: int
    :return: int
    """
    curr = get_currency()
    return round(sum * curr)
