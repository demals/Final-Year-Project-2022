def http_check(url):
    if ("http://" in url):
        return(url)
    elif ("https://" in url):
        return(url)
    else:
        url = "http://"+url
        return(url)
