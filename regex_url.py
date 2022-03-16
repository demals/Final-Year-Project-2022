import re

def regex_url(array):
    regex = r"([(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]\.[a-z]\b([-a-zA-Z0-9@:%_\+.~#?&//=]*))"
    for term in array:
        if re.search(regex, term):
            print (term)
            