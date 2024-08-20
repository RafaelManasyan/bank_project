from generators import filter_by_currency


user_filtered_trans = [
    {
        "id": "134341",
        "state": "CANCELED",
        "date": "2022-03-03T08:41:08Z",
        "amount": "13642",
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Visa 9770850749183268",
        "to": "American Express 0522499169905654",
        "description": "Перевод с карты на карту",
    },
    {
        "id": "2177828",
        "state": "EXECUTED",
        "date": "2022-04-14T15:14:21Z",
        "amount": "24853",
        "currency_name": "Yuan Renminbi",
        "currency_code": "CNY",
        "from": "Счет 38577962752140632721",
        "to": "Счет 47657753885349826314",
        "description": "Перевод со счета на счет",
    },
    {
        "id": "4137938",
        "state": "EXECUTED",
        "date": "2023-01-04T13:13:34Z",
        "amount": "15560",
        "currency_name": "Real",
        "currency_code": "BRL",
        "from": "",
        "to": "Счет 38164279390569873521",
        "description": "Открытие вклада",
    },
    {
        "id": "4699552",
        "state": "EXECUTED",
        "date": "2022-03-23T08:29:37Z",
        "amount": "23423",
        "currency_name": "Peso",
        "currency_code": "PHP",
        "from": "Discover 7269000803370165",
        "to": "American Express 1963030970727681",
        "description": "Перевод с карты на карту",
    },
]

fl = filter_by_currency(user_filtered_trans, code='')
print(fl)
