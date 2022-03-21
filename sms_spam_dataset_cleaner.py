f1 = open("datasets/SMSSpamCollection","r")
f2 = open("datasets/sms_dataset","a")

for line in f1:
    x = line.split("\t" , 1)
    if x[0] == ("spam"):
        f2.write(str(x[1]))
        print (x[1])

f1.close()
f2.close()


