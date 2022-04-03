import re
def run_hitlist():
    word_dict = {}

    sms_database = open("datasets/sms_dataset","r")
    ammount_of_attacks = (len(sms_database.readlines()))
    sms_database.close()
    sms_database = open("datasets/sms_dataset","r")
    common_word = open("datasets/most_common_words","r")
    common_word_read = common_word.read()


    for line in sms_database:
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

    sms_database.close()
    common_word.close()

    sms_phishing_word_doc = open("datasets/sms_phishing_words","w")
    word_list = sorted(word_dict, key=word_dict.get, reverse=True)

    coutner = 0
    for i in word_list:
        coutner += 1
        percentage = ((word_dict)[i])/ammount_of_attacks*100
        sms_phishing_word_doc.write(i+"\t"+(str(int(percentage)))+"\n")
        
        if coutner == 20:
            break
    sms_phishing_word_doc.close()

run_hitlist()