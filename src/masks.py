from typing import Iterable

card_number = ()


def get_mask_card_number(card_number: Iterable[int]) -> str:

    """Функция  принимает на вход номер карты и возвращает ее маску."""
    attempts = 0
    while attempts < 3:

        card_number = input("Введите номер банковского карты:")

        attempts += 1
        if len(card_number) == 16:

            str_card_number = str(card_number)
            mask_card_number = str_card_number[:4] + " " + str_card_number[4:6] + "** **** " + str_card_number[-4:]

            return mask_card_number

        elif len(card_number) != 16 and attempts < 3:
            print("Пожалуйста, введите 16 символов номера банковского карты")
        else:
            return "Вы превысили количество попыток ввода."


masked_card_number = get_mask_card_number(card_number)
print(masked_card_number)

account_number = ()


def get_mask_account(account_number: Iterable[int]) -> str:

    """Функция принимает на вход номер счета и возвращает его маску."""

    attempts = 0
    while attempts < 3:
        account_number = input("Введите номер банковского счета: ")
        attempts += 1
        if len(account_number) == 20:
            str_account_number = str(account_number)
            mask_account_number = "**" + str_account_number[-4:]
            return mask_account_number
        elif len(account_number) != 20 and attempts < 3:
            print("Пожалуйста, введите 20 символов для номера банковского счета")

        else:
            return "Вы превысили количество попыток ввода."


masked_account = get_mask_account(account_number)
print(masked_account)
