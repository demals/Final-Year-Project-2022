def save(message):
    file = open("datasets/sms_dataset","a+")
    message_to_write = (message+"\n")
    file.write(message_to_write)
    file.close()


