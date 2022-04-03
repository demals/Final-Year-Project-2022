import gui_mod_testing
file1 = open("datasets/no_spam_ham_dataset_for_testing","r")
file2 = open("datasets/post_mod_dataset2","w") 
for line in file1:
    val = gui_mod_testing.testing(line)
    if val == True:
        file2.write(line)
file1.close()
file2.close()