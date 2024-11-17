from typing import Any, Iterable


list_of_dict = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

def filter_by_state(dictionaries: Iterable[dict[str, Any]], state: Any = "EXECUTED") -> list[dict[str, Any]]:
    """Функция выведения данных по определенному значению"""
    executed_of_list = []
    for i in dictionaries:
        if i["state"] == state:
            executed_of_list.append(i)
    return executed_of_list

print(filter_by_state(list_of_dict))


def sort_by_date(dictionaries: Iterable[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция для сортировки по датам"""
    list_sorted_date = sorted(dictionaries, key=lambda x: x["date"], reverse = reverse)
    return list_sorted_date

print(sort_by_date(list_of_dict))