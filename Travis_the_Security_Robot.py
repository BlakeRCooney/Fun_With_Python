# List of known users, will be allowing user input to be stored in the known_users array at a later date.
known_users = ["Alice", "Jimmy", "Sam", "Dean", "Bailey", "Olive"]

while True:
    print("Hello! My name is Travis your crappy Security Robot: ")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()

        if remove == "y" or remove == "yes":
            known_users.remove(name)
            print("You have been removed")
        elif remove == "n" or remove == "no":
            print("No problem, I didn't want you to be removed anyway!")

    else:
        print("Name Entered in not in the system.")
        add_user = input("Would you like to be added to the system (y/n)?: ").strip().lower()

        if add_user == "y" or add_user == "yes":
            print(known_users)
            known_users.append(name)
            print(known_users)
        elif add_user == "n" or add_user == "no":
            print("Not a problem, see you later!")
