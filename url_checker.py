import re, requests
headers = {'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'}


def url_check(url):
    regex = r"(@)"
    if re.search(regex, url):
        print ("has @")
        return("@")
    r = requests.get(url, allow_redirects=False, headers=headers)
    if ((str(r.status_code))[0]) == "3":
        return("redirect")
    print (str(r.status_code))
    if len(url) >= 127:
        return("length")
    regex = r"(%[1234567890abcdef][1234567890abcdef])"
    hex_encode_ammount = len(re.findall(regex, url))
    if ((hex_encode_ammount)*3)/len(url) >= 0.5:
        return("hex")