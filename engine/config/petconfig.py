from enum import Enum


class PetConfig:
    def __init__(self,
                 pet_name,
                 tier,
                 base_attack,
                 base_health,):
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
    ELEPHANT = 22
    CAMEL = 23

PET_CONFIG = {
    # Abilities are scaled per level, where L = level
    
    # Animal: Fish
    # Ability: On level up, Give 2 (random) pets +1L health and +2L attack  (consider previous level)
    # Implementation: If a pet levels up and is a fish, give 2 pets that are placed the stats
    Pet.FISH: PetConfig(pet_name = "Fish",
                        tier = 1,
                        base_health = 3,
                        base_attack = 2,),
    
    # Animal: Beaver
    # Ability: On sell, give 2 (random) pets +L attack
    # Implementation: If a pet  is soldand is a beaver, give 2 pets that are placed the stats
    Pet.BEAVER: PetConfig(pet_name = "Beaver",
                        tier = 1,
                        base_health = 2,
                        base_attack = 3,),
    # Animal: Pig 
    # Ability: On sell, give L gold
    # Implementation: If a pet is sold and is a pig, give extra gold
    Pet.PIG: PetConfig(pet_name = "Pig",
                        tier = 1,
                        base_health = 1,
                        base_attack = 4,),
    # Animal: Ant 
    # Ability: On faint, give L attack and helath to a random friend
    # Implementation: Mostly a battle ability; maybe need to check if the pill is used on an ant for a special case?
    Pet.ANT: PetConfig(pet_name = "Ant",
                        tier = 1,
                        base_health = 2,
                        base_attack = 2,),
    
    # Animal: Mosquito 
    # Ability: At start of battle, deal 1 damage to L enemies
    # Implementation: Battle ability; should also be a check for all pre-round abilities?
    Pet.MOZZIE: PetConfig(pet_name = "Mosquito",
                        tier = 1,
                        base_health = 2,
                        base_attack = 2,),
    
    # Animal: Cricket 
    # Ability: On faint, spawn a zombie cricket with L attack and health
    # Implementation: In-battle summon mechanic; however need to consider when pill is used
    Pet.CRICKET: PetConfig(pet_name = "Cricket",
                        tier = 1,
                        base_health = 2,
                        base_attack = 1,),
    
    # Animal: Horse 
    # Ability: Friend summoned, give L attack
    # Implementation: In-battle summon mechanic. Also works when buying a pet during buy rounds. Need to remove the bonus by saving attack?
    Pet.HORSE: PetConfig(pet_name = "Horse",
                        tier = 1,
                        base_health = 1,
                        base_attack = 2,),
    
    # Animal: Crab 
    # Ability: Start of combat, gain 0.5L health from the healthiest friend
    # Implementation: In-battle number changing
    Pet.CRAB: PetConfig(pet_name = "Crab",
                        tier = 2,
                        base_health = 1,
                        base_attack = 4,),
 
    # Animal: Swan 
    # Ability: Start of turn (buy period), gain L hold
    # Implementation: Check at the start of each turn for swan and its level
    Pet.SWAN: PetConfig(pet_name = "Swan",
                        tier = 2,
                        base_health = 2,
                        base_attack = 1,),
    
    # Animal: Hedgehog 
    # Ability: On faint, deal 2L damage to all 
    # Implementation: Faint ability is mostly battle, but need to cover pill usage
    Pet.HEDGEHOG: PetConfig(pet_name = "Hedgehog",
                        tier = 2,
                        base_health = 2,
                        base_attack = 3,),
    
    # Animal: Peacock 
    # Ability: When hurt, gain 4L attack permanently 
    # Implementation: In-battle number changing; will have edge case where someone pills a pet with a hurting faint
    Pet.PEACOCK: PetConfig(pet_name = "Peacock",
                        tier = 2,
                        base_health = 5,
                        base_attack = 2,),
    
    # Animal: Flamingo 
    # Ability: On faint, give L health and attack to two nearest pets behind
    # Implementation: Faint ability is mostly battle, but need to cover pill usage
    Pet.FLAMINGO: PetConfig(pet_name = "Flamingo",
                        tier = 2,
                        base_health = 2,
                        base_attack = 3,),
    
    # Animal: Kangaroo 
    # Ability: Friend ahead attacks, gain L helath and damage
    # Implementation: After every attack, check if it is at the second position (Only position where friend in front would attack)
    Pet.KANGAROO: PetConfig(pet_name = "Kangaroo",
                        tier = 2,
                        base_health = 3,
                        base_attack = 2,),

    # Animal: Spider 
    # Ability: On faint, summon a tier 3 pet with L health and attack
    # Implementation: Faint ability is mostly battle, but need to cover pill usage. 
                     # May need to create a new pet from Pet_config since he stats are different
    Pet.SPIDER: PetConfig(pet_name = "Spider",
                        tier = 2,
                        base_health = 2,
                        base_attack = 2,),

    # Animal: Dodo 
    # Ability: Start of battle, give 0.5L attack to the nearest friend ahead
    # Implementation: Just to the attack valuie to Position - 1, unless they're at the start of the lime
    Pet.DODO: PetConfig(pet_name = "Dodo",
                        tier = 3,
                        base_health = 2,
                        base_attack = 4,),
    # Animal: Badger 
    # Ability: Before faint, deal 0.5L attack damage to the adjacent pets
    # Implementation: Attack the pet behind it and do a normal attack on the pet at the start of the other team; mayber pretend to have an instance of thi pet on the other side attacking?
    Pet.BADGER: PetConfig(pet_name = "Badger",
                        tier = 3,
                        base_health = 3,
                        base_attack = 6,),
    
    # Animal: Dolphin 
    # Ability: Start of battle, deal 3 damage to L random pets on the other team
    # Implementation: Pre round ability, should be straightforward
    Pet.DOLPHIN: PetConfig(pet_name = "Dolphin",
                        tier = 3,
                        base_health = 3,
                        base_attack = 4,),
    
    # Animal: Giraffe 
    # Ability: End of turn (buy phase), give 1 health and attack to L friends in front of it
    # Implementation: Can give position - [1:L] the stats
    Pet.GIRAFFE: PetConfig(pet_name = "Giraffe",
                        tier = 3,
                        base_health = 3,
                        base_attack = 1,),
    
    # Animal: Elephant 
    # Ability: After attack, deal 1 damage to the friend behind L times
    # Implementation: Loop the times you attack by the level of the elephant and maybe treat it as an attack to the pet behind. Need to check if it is alive after every fight. and then do the effect
    Pet.ELEPHANT: PetConfig(pet_name = "Elephant",
                        tier = 3,
                        base_attack = 3,
                        base_health = 7,),

    # Animal: Camel 
    # Ability: When hurt, give nearest friend 2L attack and health
    # Implementation: Save the old helath temporarily. After every battle/attack, check and see if there is a negative change. Also do the ability on faint. Shouldn't have a case during buy period
    Pet.CAMEL: PetConfig(pet_name = "Elephant",
                        tier = 3,
                        base_attack = 1,
                        base_health = 3,), 
    
    # Animal: Bunny 
    # Ability: When a friendly eats food, give them +1 health (THIS CAN CHANGE)
    # Implementation: When giving food, check if there is a bunny in the roster
    Pet.BUNNY: PetConfig(pet_name = "Bunny",
                        tier = 3,
                        base_attack = 1,
                        base_health = 2,),    
    
    # Animal: Dog 
    # Ability: When a friend is summoned, gain 2L attack and L health until end of battle (stacking and unlimited)
    # Implementation: Need to check for when summoning in buy phase as well as during battle. Can remove the extra stats every start of buy round
    Pet.DOG: PetConfig(pet_name = "Dog",
                        tier = 3,
                        base_attack = 2,
                        base_health = 3,),
    # Animal: Sheep 
    # Ability: On faint, summon 2 rams with 2L health and attack
    # Implementation: Faint ability is mostly battle, but need to cover pill usage. You will always be able to spwan one ram in, need to check if the amount on the lineup is <= 3 for second one
    Pet.SHEEP: PetConfig(pet_name = "Sheep",
                        tier = 3,
                        base_attack = 2,
                        base_health = 3,)

}

TIER_PETS = [
    [Pet.FISH, Pet.BEAVER, Pet.HORSE, Pet.PIG, Pet.ANT, Pet.MOZZIE, Pet.CRICKET],
    [Pet.CRAB, Pet.SWAN, Pet.HEDGEHOG, Pet.FLAMINGO, Pet.KANGAROO, Pet.SPIDER],
    [Pet.DODO, Pet.BADGER, Pet.DOLPHIN, Pet.GIRAFFE, Pet.ELEPHANT, Pet.CAMEL, Pet.BUNNY, Pet.DOG, Pet.SHEEP],
    []
]