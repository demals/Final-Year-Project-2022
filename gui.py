import user_input, message_spliter, regex_url, dataset_checker, url_checker, message_split_checker, similarty_check, ask_user, at_percentage_calculator,url_percentage_calculator, word_hit_list

word_hit_list.run_hitlist()

percentage = 0

message = user_input.user_input()

if  dataset_checker.dataset_check(message) == "phishing":
    print ("the following message:\n"+message+"\nhas appared in the database, therefore we suspect is is a phishing attack.")
    quit()

similarty_check_score = similarty_check.similar(message)

if similarty_check_score != 0:
    print ("the following message;\n"+message+"\n"+r"was found to be at least 50% similar to",str(similarty_check_score),"other message(s) found in the dataset, therefore this message is likley to be a phishing attack.")
    ask_user.ask(message)
    quit()

message_split = message_spliter.message_spliter(message)

url = regex_url.regex_url(message_split)

url_per = url_percentage_calculator.url_percent_cal() 
at_per = at_percentage_calculator.at_percentage_cal()

alert = None

if url != None:
    url_status = url_checker.url_check(url)
    if url_status == "error":
        percentage += url_per
    elif url_status == "@":
        percentage += at_per
    elif url_status == "redirect":
        alert = "amber"   
    elif url_status == "length":
        print(r"the length of the url is over 128 characters, suggesting that the url within the message is a phishing attack")
        ask_user.ask(message)
        quit()    
    elif url_status == "hex":
        print(r"over 50% of the url within the message is encoded in hex, suggesting that the message is a phishing attack")
        ask_user.ask(message)
        quit()    
 
percentage += message_split_checker.message_split_check(message_split)

if (percentage >= 80) or (percentage >= 50 and alert == "amber") :
    print ("the following message: "+message,"is",str(percentage)+"%","likley to be a phishing attack.")
    ask_user.ask(message)
    quit() 
else:
    print ("the message is very unlikley to be a phishing attack")
    quit()

