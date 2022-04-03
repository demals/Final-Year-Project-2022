import message_spliter, regex_url, dataset_checker, url_checker, message_split_checker, similarty_check, at_percentage_calculator,url_percentage_calculator

def testing(message):
    percentage = 0
    if  dataset_checker.dataset_check(message) == "phishing":    
        return(True)

    if similarty_check.similar(message) != 0:        
        return(True)

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
            return(True)                     
        elif url_status == "hex":                 
            return(True)                

    percentage += message_split_checker.message_split_check(message_split)

    if (percentage >= 80) or (percentage >= 50 and alert == "amber"):             
        return(True)
    else:
        return()


