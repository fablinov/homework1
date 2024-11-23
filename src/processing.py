from typing import Iterable
from typing import Any


def filter_by_state(filter_state: Iterable, state="EXECUTED") -> Any and Iterable:
    """Функция принимает список словарей и возвращает новый список словарей содержащий только
    те словари, у которых ключ state соответствует указанному значению"""
    new_filter_state = []

    for dictionary_state in filter_state:
        if dictionary_state["state"] == state:
            new_filter_state.append(dictionary_state)

    return new_filter_state


def sort_by_date(sort_state: list[dict[str, Any]], reverse=False) -> list[dict[str, Any]]:
    """Функция возвращает новый список отсортированный по дате"""
    sorted_state_date = sorted(sort_state, key=lambda sort_state: sort_state["date"], reverse=reverse)
    return sorted_state_date