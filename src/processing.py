from typing import Any, Iterable


def filter_by_state(dictionaries: Iterable[dict[Any, Any]], state: Any = "EXECUTED") -> list[dict[Any, Any]]:
    """Функция выведения данных по определенному значению"""
    executed_list = []
    for i in dictionaries:
        if i["state"] == state:
            executed_list.append(i)
    return executed_list


def sort_by_date(dictionaries: Iterable[dict[Any, Any]], reverse: bool = True) -> list[dict[Any, Any]]:
    """Функция для сортировки по датам"""
    list_date = sorted(dictionaries, key=lambda x: x["date"], reverse=True)
    return list_date
