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
        increase_pets_sold()
        

    customer = Customer("Jack Jarvis", 1000)
        self.pet_shop.sell_pet_to_customer("Sir Percy", customer)
        self.assertEqual(1, customer.pet_count())
        self.assertEqual(1, self.pet_shop.stock_count())
        self.assertEqual(1, self.pet_shop.pets_sold)
        self.assertEqual(1500, self.pet_shop.total_cash)