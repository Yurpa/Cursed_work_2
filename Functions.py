import json

with open('operations.json', 'rt') as data:
    List_of_logs = json.load(data)

def Checkout(list):
    for item in list:
        if item["state"] == "EXECUTED":
            print(item["id"])

