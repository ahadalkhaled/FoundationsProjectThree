# CLASSES AND METHODS
class Person(): #this is a class for only one person not the clubs
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.members = []
        self.presedent = None


    def assign_president(self, person):
        # your code goes here!
        if person in self.members:
            self.president = person



    def recruit_member(self, person):
        # your code goes here!
        if not person in self.members:
            self.members.append(person)


    def print_member_list(self):
        # your code goes here!
        # "is" is the same as ==
        for member in self.members:
            if member is self.president:
                print("- %s (%s years old, president) - %s" % (member.name, member.age, member.bio))
            else:
                print("- %s (%s years old) - %s" % (member.name, member.age, member.bio))


