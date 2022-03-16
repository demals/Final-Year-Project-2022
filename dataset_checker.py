def dataset_check(message):
    f = open("sms_dataset","r",encoding='utf8')
    file = f.read()
    if message in file:
        return ("phishing")