import re

def regex_url(array):
    regex = r"([(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*))"
    for term in array:
        if re.search(regex, term):
            return(term)