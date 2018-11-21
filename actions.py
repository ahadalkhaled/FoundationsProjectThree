# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Ahad"
my_age = 22
my_bio = "I love sports"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)



def options():
    # your code goes here!
    print()
    print("Would you like to:")
    print("1)Create a new club.")
    print("2)Browse and join clubs.")
    print("3)View existing clubs.")
    print("4)Display members of club.")
    print("-1)Close application.")
    user_option = input("> ")
    return user_option
 
def print_population():
	print()
	index = 1
	for person in population:
		print("[%s] %s" % (index, person.name))
		index += 1


def create_club():
    # your code goes here!
    
    club_name = input("Pick a name for your new club:")

    club_description = input("Tell us more about your club:")

    club = Club(club_name, club_description)
    club.recruit_member(myself)
    club.assign_president(myself)

    # get the members to recruit to the club
    print("Enter the number of the people you would like to recruit:")
    print_population()
    person_recruited = ""
    while person_recruited != "-1":
    	person_recruited = input("> ")
    	if person_recruited.isdigit() and int(person_recruited) <= len(population):
    		club.recruit_member(population[int(person_recruited)-1])

    print("Here's your new club:")
    print(club.name)
    print(club_description)
    club.print_member_list()
    clubs.append(club)	

    

def view_clubs():
    # your code goes here!
    for club in clubs:
    	print("\tNAME: %s\n\tDESCRIPTION: %s\n\tMEMBERS: %s\n" % (club.name, club.description, len(club.members)))
    

def view_club_members():
    # your code goes here!
    view_clubs() 
    club_found = False
    while not club_found:
    	club_name = input("Enter club name of the members you would like to view: ")
    	for club in clubs:
    		if club.name.lower() == club_name.lower():
    			club.print_member_list()
    		club_found = True

    

def join_clubs():
    # your code goes here!
    view_clubs()
    club_found = False
    while not club_found:
    	club_name = input("Enter the club name you would like to join: ")
    	for club in clubs:
    		if club.name.lower() == club_name.lower():
    			club.recruit_member(myself)
    		club_found = True

    

def application():
    introduction()
    # your code goes here!
    #this fundtion is used to call the functions from the options
    option = ""
    while option != "-1":
    	option = options()
    	if option == "1":
    		create_club()
    	elif option == "2":
    		join_clubs()
    	elif option == "3":
    		view_clubs()
    	elif option == "4":	
    		view_club_members()
    	elif option == "-1":
    		break









    
