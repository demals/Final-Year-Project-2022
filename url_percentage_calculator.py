import re
def url_percent_cal():
    array = []
    sms_dataset_length = 0
    at_counter = 0
    file = open("datasets/sms_dataset","r")
    regex = r"([(http(s)?):\/\/(www)?a-zA-Z0-9@:%_\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*))"
    for line in file:
        sms_dataset_length += 1
        if re.search(regex, line):
            array.append(line)
    file.close()
    for item in array:
        if "@" in item:
            at_counter += 1

    return(int(((len(array)-at_counter)/sms_dataset_length)*100))