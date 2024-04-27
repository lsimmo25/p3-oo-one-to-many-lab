class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name: str, pet_type: str, owner=""):
        self.name = name
        self.owner = owner
        self.pet_type = pet_type
        if pet_type not in self.PET_TYPES:
            raise Exception("Pet must be in approved list")
        self.all.append(self)

class Owner:
    def __init__(self, name: str):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        pet.owner = self
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda x: x.name)