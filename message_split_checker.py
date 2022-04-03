def message_split_check(message):
    word_dict = {}
    percnetage = 0
    file = open("datasets/sms_phishing_words","r")
    for line in file:
        word_dict[line.split("\t")[0]] = int(line.split("\t")[1])
    for word in word_dict:
        if word in message:
            percnetage += word_dict[word]
    return(percnetage)