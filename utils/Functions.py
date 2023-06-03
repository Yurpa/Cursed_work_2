import json
from datetime import datetime, date, timedelta

with open('../operations.json', 'r', encoding="utf-8") as data:
    operations_data = json.load(data)

def Checkout():
    timelist = []
    checkeddata = []
    doublechecked = []
    for i in operations_data:
        if i != {} and i['state'] == "EXECUTED":
            datetime_str = i['date']
            timelist.append(datetime_str)
    timelist.sort()
    for item in timelist[-5:]:
        checkeddata.append(item)
    for item in operations_data:
        if item != {} and item['date'] in checkeddata:
            doublechecked.append(item['id'])
    return doublechecked

def Censored(card1):
    '''Function which censores the card digits
     working func'''
    if card1 == None:
        return 'Данные отсутствуют'
    card1 = card1.split()
    uncensored_part = " ".join(card1[:-1])
    if 'Счет' in uncensored_part:
        card1[-1] = card1[-1].replace(card1[-1][:-4], '*' * len(card1[-1][:-4]))
        censored_part1 = "".join(card1[-1][-6:])
    else:
        card1[-1] = card1[-1].replace(card1[-1][6:-4], '*' * len(card1[-1][6:-4]))
        censored_part1 = " ".join([card1[-1][i:i+4] for i in range(0, len(card1[-1]), 4)])
    finale_censored = " ".join([uncensored_part, censored_part1])
    return finale_censored

def last_struggle():
    checked = Checkout()
    for data in operations_data:
        if data != {} and data['id'] in checked:
            if data['description'] == "Открытие вклада":
                card1 = None
            else: card1 = data['from']
            card2 = data['to']
            datetime_str = data['date']
            datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%f')
            print(f"{datetime_obj.date().strftime('%d.%m.%Y')} {data['description']} \n{Censored(card1)} ==> {Censored(card2)}")
            print(f"{data['operationAmount']['amount']} {data['operationAmount']['currency']['name']}")

last_struggle()