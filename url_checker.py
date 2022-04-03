import re, requests, http_checker, similarty_check
headers = {'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'}


def url_check(url):
    url = http_checker.http_check(url)
    regex = r"(@)"
    if re.search(regex, url):
        return("@")
    try:    
        r = requests.get(url, allow_redirects=False, headers=headers)
    except:
        return("error")
    if ((str(r.status_code))[0]) == "3":
        if similarty_check.percentage(url,r.next.url) < 70:
            return("redirect")
    if len(url) >= 127:
        return("length")
    regex = r"(%[1234567890abcdef][1234567890abcdef])"
    hex_encode_ammount = len(re.findall(regex, url))
    if ((hex_encode_ammount)*3)/len(url) >= 0.5:
        return("hex")

