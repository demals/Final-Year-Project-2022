import user_input, message_spliter, regex_url, dataset_checker

caller_id, message = user_input.user_input()

check = dataset_checker.dataset_check(message)
print (check)

if  check == "phishing":
    print ("the following message:", message, "has appared in the database, therefore we suspect is is a phishing attack.")
    quit()

message_split = message_spliter.message_spliter(message)
regex_url.regex_url(message_split)
