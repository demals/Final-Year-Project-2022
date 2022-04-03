file1 = open("datasets/SMSSpamCollection","r")
file2 = open("datasets/no_spam_ham_dataset_for_testing","w")

for line in file1:
    x = line.split("\t" , 1)
    file2.write(str(x[1]))

file1.close()
file2.close()