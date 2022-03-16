import user_input, message_spliter, regex_url, dataset_checker, url_checker

caller_id, message = user_input.user_input()

check = dataset_checker.dataset_check(message)

if  check == "phishing":
    print ("the following message:", message, "has appared in the database, therefore we suspect is is a phishing attack.")
    quit()

message_split = message_spliter.message_spliter(message)
url = regex_url.regex_url(message_split)
url_status = url_checker.url_check(url)
if url_status == "@":
    print(r"the url in the message contains the @ chracter, suggesting that the message is a phishing attack.")
    quit()
elif url_status == "redirect":
    print(r"the url in the message is a redirect, suggesting that the message is a phishing attack")
elif url_status == "length":
    print(r"the length of the url is over 128 characters, suggesting that the url within the message is a phishing attack")
    quit()
elif url_status == "hex":
    print(r"over 50% of the url within the message is encoded in hex, suggesting that the message is a phishing attack")
    quit()