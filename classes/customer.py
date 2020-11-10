class Customer:

    def __init__(self, name, cash):

        #instance variables - all needs to be prefixed by "self."
        self.name = name
        self.cash = cash

        # A new customer has no pets (that we have sold to them) yet. So, only an empty list is created.
        self.pets = []


    # Remember to ALWAYS pass in "self" - even if no other parms!!!
    def pet_count(self):
        return len(self.pets)

