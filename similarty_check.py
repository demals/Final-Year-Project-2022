from difflib import SequenceMatcher

def percentage(message,line):
    return ((SequenceMatcher(None, message, line).ratio())*100)

def similar(message):
    dataset = open("datasets/sms_dataset","r")
    counter = 0
    for line in dataset:
        per = percentage(message,line)
        #print(str(per))
        if per >= 50:
            counter += 1
    return counter

#message1 = ("Royal Mail: Your package has a £2.99 shipping fee, to pay this now visit royalmail-redelivery.support. Actions will be taken if you do not pay this fee")
#message2 = ()
#print(percentage(message1, message2))
#print (similar(message1))