import json
import datetime

#with open('../operations.json', 'r') as data:
    #list_of_logs = json.load(data)

def Checkout(list):
    '''Beta ver of printing the last 5 op
    does not work yet'''
    list_of_executed_op = []
    for item in list:
        if item["state"] == "EXECUTED":
            list_of_executed_op.append(item["id"])
            print(item["date"].strftime("%Y/%m/%d %H/%M/%S"))

def Censored(card1):
    '''Function which censores the card digits
     working func'''
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

c1 = Censored('Visa Gold 3589276410671603')
print(c1)


