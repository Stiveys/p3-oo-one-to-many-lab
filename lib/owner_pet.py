# lib/owner_pet.py

class Pet:
    # Class variable to store valid pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    # Class variable to store all instances of Pet
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        if owner is not None:
            owner.add_pet(self)  # Automatically add the pet to the owner's list

    def set_owner(self, owner):
        if isinstance(owner, Owner):
            if self.owner != owner:
                self.owner = owner
                owner.add_pet(self)  # Add the pet to the owner's list
        else:
            raise Exception("Owner must be an instance of Owner class")

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            if pet.owner != self:
                pet.set_owner(self)  # Ensure the pet's owner is set correctly
            if pet not in self._pets:
                self._pets.append(pet)
        else:
            raise Exception("Pet must be an instance of Pet class")

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)