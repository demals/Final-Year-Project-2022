def at_percentage_cal():
    file = open("datasets/sms_dataset","r")
    at_count = 0
    line_counter = 0
    for message in file:
        line_counter += 1
        if "@" in message:
            at_count += 1
    file.close()
    percentage = ((at_count/line_counter)*100)
    return(int(percentage))