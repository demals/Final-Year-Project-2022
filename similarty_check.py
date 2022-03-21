from difflib import SequenceMatcher

def percentage(message,line):
    return ((SequenceMatcher(None, message, line).ratio())*100)

def similar(message):
    dataset = open("datasets/sms_dataset","r")
    counter = 0
    for line in dataset:
        if percentage(message,line) >= 70:
            counter += 1
    return counter
