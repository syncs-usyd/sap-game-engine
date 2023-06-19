from enum import Enum


class PetConfig:
    def __init__(self,
                 pet_name,
                 tier,
                 base_health,
                 base_attack,):
        self.PET_NAME = pet_name
        self.TIER = tier
        self.BASE_HEALTH = base_health
        self.BASE_ATTACK = base_attack

class Pet(Enum):
    FISH = 1
    BEAVER = 2
    PIG = 3
    ANT = 4
    MOZZIE = 5
    CRICKET = 6
    HORSE = 7
    CRAB = 8
    SWAN = 9
    HEDGEHOG = 10
    PEACOCK = 11
    FLAMINGO = 12
    KANGAROO = 13
    SPIDER = 14
    DODO = 15
    BADGER = 16
    DOLPHIN = 17
    GIRAFFE = 18
    BUNNY = 19 
    DOG = 20
    SHEEP = 21
    

PET_CONFIG = {
    # Abilities are scaled per level, where L = level
    
    # Animal: Fish
    # Ability: On level up, Give 2 (random) pets +1L health and +2L attack  (consider previous level)
    # Implementation: If a pet levels up and is a fish, give 2 pets that are placed the stats
    Pet.FISH: PetConfig(pet_name = "Fish",
                        tier = 1,
                        base_health = 3,
                        base_attack = 3,),
    
    # Animal: Beaver
    # Ability: On sell, give 2 (random) pets +L attack
    # Implementation: If a pet  is soldand is a beaver, give 2 pets that are placed the stats
    Pet.BEAVER: PetConfig(pet_name = "Beaver",
                        tier = 1,
                        base_health = 3,
                        base_attack = 2,),
    # Animal: Pig 
    # Ability: On sell, give L gold
    # Implementation: If a pet is sold and is a pig, give extra gold
    Pet.PIG: PetConfig(pet_name = "Pig",
                        tier = 1,
                        base_health = 4,
                        base_attack = 1,),
    # Animal: Ant 
    # Ability: On faint, give L attack and helath to a random friend
    # Implementation: Mostly a battle ability; maybe need to check if the pill is used on an ant for a special case?
    Pet.ANT: PetConfig(pet_name = "Ant",
                        tier = 1,
                        base_health = 2,
                        base_attack = 2,),
    
    # Animal: Mosquito 
    # Ability: At start of battle, deal 1 damage to L enemies
    # Implementation: Battle ability; check for all pre-round abilities?
    Pet.MOZZIE: PetConfig(pet_name = "Mosquito",
                        tier = 1,
                        base_health = 2,
                        base_attack = 2,),
    
    # Animal: Cricket 
    # Ability: On faint, spawn a zombie cricket with L attack and health
    # Implementation: In-battle summon mechanic; however need to consider when pill is used
    Pet.CRICKET: PetConfig(pet_name = "Cricket",
                        tier = 1,
                        base_health = 1,
                        base_attack = 2,),
    
    # Animal: Horse 
    # Ability: Friend summoned, gain L attack
    # Implementation: In-battle summon mechanic
    Pet.HORSE: PetConfig(pet_name = "Horse",
                        tier = 1,
                        base_health = 1,
                        base_attack = 2,),
    
    # Animal: Crab 
    # Ability: Start of combat, gain 0.5L health from the healthiest friend
    # Implementation: In-battle number changing
    Pet.CRAB: PetConfig(pet_name = "Crab",
                        tier = 2,
                        base_health = 4,
                        base_attack = 1,),
 
    # Animal: Swan 
    # Ability: Start of turn (buy period), gain L hold
    # Implementation: Check at the start of each turn for swan and its level
    Pet.SWAN: PetConfig(pet_name = "Swan",
                        tier = 2,
                        base_health = 1,
                        base_attack = 2,),
    
    # Animal: Hedgehog 
    # Ability: On faint, deal 2L damage to all 
    # Implementation: Faint ability is mostly battle, but need to cover pill usage
    Pet.HEDGEHOG: PetConfig(pet_name = "Hedgehog",
                        tier = 2,
                        base_health = 3,
                        base_attack = 2,),
    
    # Animal: Peacock 
    # Ability: When hurt, gain 4L attack
    # Implementation: In-battle number changing; will have edge case where someone pills a poet with a hurting faint
    Pet.PEACOCK: PetConfig(pet_name = "Peacock",
                        tier = 2,
                        base_health = 2,
                        base_attack = 5,),
    
    # Animal: Flamingo 
    # Ability: On faint, give L health and attack to two nearest pets behind
    # Implementation: Faint ability is mostly battle, but need to cover pill usage
    Pet.FLAMINGO: PetConfig(pet_name = "Flamingo",
                        tier = 2,
                        base_health = 4,
                        base_attack = 1,),
    
    # Animal: Kangaroo 
    # Ability: Friend ahead attacks, gain L helath and damage
    # Implementation: After every attack, check if it is at the second position (Only position where friend in front would attack)
    Pet.KANGAROO: PetConfig(pet_name = "Kangaroo",
                        tier = 2,
                        base_health = 2,
                        base_attack = 3,),

    # Animal: Spider 
    # Ability: On faint, summon a tier 3 pet with L health and attack
    # Implementation: Faint ability is mostly battle, but need to cover pill usage. 
                     # May need to create a new pet from Pet_config since he stats are different
    Pet.SPIDER: PetConfig(pet_name = "Spider",
                        tier = 2,
                        base_health = 2,
                        base_attack = 2,)


    
    
        
}

TIER_PETS = [
    [Pet.FISH, Pet.BEAVER, Pet.HORSE, Pet.PIG, Pet.ANT, Pet.MOZZIE, Pet.CRICKET],
    [Pet.CRAB, Pet.SWAN, Pet.HEDGEHOG, Pet.FLAMINGO, Pet.KANGAROO, Pet.SPIDER],
    [],
    []
]