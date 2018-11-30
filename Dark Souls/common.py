#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from typing import List, Tuple
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def get_links_location(url_location: str) -> List[Tuple[str, str]]:
    """
    Функция для поиска переходов из локации

    """

    rs = requests.get(url_location)
    root = BeautifulSoup(rs.content, 'html.parser')

    locations = []

    table_locations = root.select_one('table.pi-horizontal-group')
    if not table_locations or 'Переходы:' not in table_locations.text:
        return locations

    for a in table_locations.select('a'):
        url = urljoin(rs.url, a['href'])
        title = a.text.strip().title()

        locations.append((title, url))

    return locations


def find_locations(url_locations: str, log=True) -> (List[str], List[Tuple[str, str]]):
    visited_locations = set()
    links = set()

    rs = requests.get(url_locations)
    root = BeautifulSoup(rs.content, 'html.parser')

    for a in root.select('.category-page__member-link'):
        abs_url = urljoin(rs.url, a['href'])

        locations = get_links_location(abs_url)
        if not locations:
            continue

        title = a.text.strip().title()
        log and print(title, abs_url)

        visited_locations.add(title)

        for x_title, x_url in locations:
            log and print('    {} -> {}'.format(x_title, x_url))

            # Проверяем что локации с обратной связью не занесены
            if (x_title, title) not in links:
                links.add((title, x_title))

        log and print()

    visited_locations = sorted(visited_locations)
    links = sorted(links)

    return visited_locations, links


def find_locations_ds1(log=True) -> (List[str], List[Tuple[str, str]]):
    url = "http://ru.darksouls.wikia.com/wiki/Категория:Локации_(Dark_Souls)"
    return find_locations(url, log)


def find_locations_ds2(log=True) -> (List[str], List[Tuple[str, str]]):
    url = "http://ru.darksouls.wikia.com/wiki/Категория:Локации_(Dark_Souls_II)"
    return find_locations(url, log)


def find_locations_ds3(log=True) -> (List[str], List[Tuple[str, str]]):
    url = "http://ru.darksouls.wikia.com/wiki/Категория:Локации_(Dark_Souls_III)"
    return find_locations(url, log)


def find_links_ds1(log=True) -> List[Tuple[str, str]]:
    return find_locations_ds1(log)[1]


def find_links_ds2(log=True) -> List[Tuple[str, str]]:
    return find_locations_ds2(log)[1]


def find_links_ds3(log=True) -> List[Tuple[str, str]]:
    return find_locations_ds3(log)[1]


if __name__ == '__main__':
    visited_locations, links = find_locations_ds1()

    # Выведем итоговый список
    print(len(visited_locations), visited_locations)
    print(len(links), links)

    print()

    links = find_links_ds1(log=False)
    print(len(links), links)
