def dataset_check(message):
    f = open("datasets/sms_dataset","r")
    file = f.read()
    if message in file:
        return ("phishing")

