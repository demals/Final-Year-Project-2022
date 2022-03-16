def message_spliter(message):
    message_array = []
    word = ""
    for i in message:
        if i != " ":
            word += i
        elif i == " ":
            message_array.append(word)
            word = ""
    message_array.append(word)
    return(message_array)