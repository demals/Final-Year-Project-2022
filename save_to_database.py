def save(message):
    file = open("datasets/2022_dataset","a+")
    message_to_write = (message+"\n")
    file.write(message_to_write)
    file.close()


#user = input("message: ")
#save(user)
