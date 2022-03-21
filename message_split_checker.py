
from email import message


def message_split_check(message):
    word_dict = {}
    percnetage = 0
    file = open("datasets/sms_phishing_words","r")
    for line in file:
        word_dict[line.split(",")[0]] = int(line.split(",")[1])
    for word in message:
        if word in word_dict:
            percnetage += word_dict[word]

    return(percnetage)

