# Импорт из файла нужных нам функций
from functions import (json_encode, date_operations, five_operations, sorted_five, encrypting)


list_main = sorted_five(
    five_operations(json_encode("operations.json"), date_operations(json_encode("operations.json"))))
for every in list_main:
    try:
        date = every["date"].strftime("%d.%m.%Y")
        desc = every["description"]
        from_who = encrypting(every.get("from", ""))
        to_who = encrypting(every["to"])
        sum_oper = every["operationAmount"]["amount"]
        currency = every["operationAmount"]["currency"]["name"]
        print(f"""{date} {desc}
{from_who} -> {to_who}
{sum_oper} {currency}
""")
    except KeyError:
        continue