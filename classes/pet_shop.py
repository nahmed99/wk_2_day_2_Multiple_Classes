class PetShop:

    def __init__(self, name, stock, cash):
        self.name = name
        self.stock = stock
        self.total_cash = cash

        # Instance variables
        self.pets_sold = 0


    #REMEMBER to add "self" to parm list, even if no other parms exist!!!
    #REMEMBER to add "self" to parm list, even if no other parms exist!!!
    #REMEMBER to add "self" to parm list, even if no other parms exist!!!
    #REMEMBER to add "self" to parm list, even if no other parms exist!!!
    #REMEMBER to add "self" to parm list, even if no other parms exist!!!


    def stock_count(self):
        return len(self.stock)


    def increase_pets_sold(self):
        self.pets_sold += 1


    def increase_total_cash(self, amount):
        self.total_cash += amount

    
    def add_pet(self, new_pet):
        self.stock.append(new_pet)


    def remove_pet(self, pet_gone):
        self.stock.remove(pet_gone)


    def find_pet_by_name(self, name):
        for pet in self.stock:
            if pet.name == name:
                return pet


    def sell_pet_to_customer(self, pet_name, customer):
        customer.add_pet(pet_name)
        pet_sold = self.find_pet_by_name(pet_name)
        self.remove_pet(pet_sold)
        self.increase_pets_sold()
        self.increase_total_cash(pet_sold.price)
        