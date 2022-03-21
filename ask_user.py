import save_to_database
def ask(message):
    print ("would you like to save this attack to the database?")
    user = input ("yes/no: ")
    if user == "no":
        return(None)
    elif user == "yes":
        save_to_database.save(message)
        print("saved to database")
        return(None)