class Customer:

    def __init__(self, name, cash):

        #instance variables - all needs to be prefixed by "self."
        self.name = name
        self.cash = cash

        # A new customer has no pets (that we have sold to them) yet. So, only an empty list is created.
        self.pets = []


    # Remember to ALWAYS pass in "self" to a method - even if no other parms!!!
    # Remember to ALWAYS pass in "self" to a method - even if no other parms!!!
    # Remember to ALWAYS pass in "self" to a method - even if no other parms!!!


    def pet_count(self):
        return len(self.pets)


    def add_pet(self, new_pet):
        self.pets.append(new_pet)


    def get_total_value_of_pets(self):
        total_value = 0

        for pet in self.pets:
            # Access the price property of the pet object
            total_value += pet.price

        return total_value

    
