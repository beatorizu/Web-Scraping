from bs4 import BeautifulSoup
from pandas import DataFrame

from web_scraping.settings import attributes_properties


def html_to_dataframe(html):
    soup = BeautifulSoup(html, 'html.parser')
    collection = soup.find_all('li', {'class': 'info-holder'})

    dataframe = DataFrame(
        [tag_to_dict(material, attributes_properties) for material in collection])
    return dataframe

def tag_to_dict(tag, parser_settings):
    material_dict = {}

    for attribute in tag.find_all('div', {'class': 'tabela-lista-valor'}):
        attribute_key = attribute.find('p', {'class': 'outer tabela-lista-item'}).contents[0].strip()
        attribute_value = attribute.find('p', {'class': 'inner'}).contents[0]
        parser = parser_settings[attribute_key]
        material_dict[parser["field"]] = parser["parser"](attribute_value)

    return material_dict
