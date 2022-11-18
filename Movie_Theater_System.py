# This is where all of the movies available are defined, what age restrictions there would be, and how many tickets are available
films = {
    "Finding Dory":[3,5],
    "Jeepers Creepers":[18,5],
    "Pandora":[12,5],
    "Bolt":[10,5]
    }

# Asking the user to input the movie they would like to watch
while True:
    choice = input("What Film would you like to watch? ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        # Check users age
        
        if age >= films[choice][0]:

            num_seats = films[choice][1]
            
            # Check the amount of seats in theater
            
            if films[choice][1] > 0:
                
                print("Enjoy the film!")
                films[choice][1] = films[choice][1]-1

            else:
                print("Sorry, that film is sold out!")
        else:
            print("You are to young to view this film, please select another film.")
        
    else:
        print("We do not currently have that film.....")
