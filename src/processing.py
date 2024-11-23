from typing import Any, Iterable


def filter_by_state(dictionaries: Iterable[dict[str, Any]], state: Any = "EXECUTED") -> list[dict[str, Any]]:
    """Функция выведения данных по определенному значению"""
    executed_of_list = []
    for i in dictionaries:
        if i["state"] == state:
            executed_of_list.append(i)
    return executed_of_list


def sort_by_date(dictionaries: Iterable[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция для сортировки по датам"""
    list_sorted_date = sorted(dictionaries, key=lambda x: x["date"], reverse = reverse)
    return list_sorted_date
