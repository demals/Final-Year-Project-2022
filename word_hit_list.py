import re

word_dict = {}

file = open("sms_dataset","r")
common_word = open("most_common_words","r")
common_word_read = common_word.read()


for line in file:
    line_split = re.split('\s+',line[:-2])
    for word in line_split:
        if len(word) == 1:
            continue
        elif word.lower() in common_word_read:
            continue
        elif word.lower() in word_dict:
            word_dict[word.lower()] = int(word_dict[word.lower()])+1
        else:
            word_dict[word.lower()] = 1
file.close()
common_word.close()

sms_phishing_word_doc = open("sms_phishing_words","a")
word_list = sorted(word_dict, key=word_dict.get, reverse=True)

coutner = 0
for i in word_list:
    coutner += 1
    sms_phishing_word_doc.write(i+"\n")
    print(i,word_dict[i])
    if coutner == 20:
        break
sms_phishing_word_doc.close()