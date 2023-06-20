from enum import Enum

from engine.game.abilities import Abilities
from engine.game.abilitytype import AbilityType


class PetConfig:
    def __init__(self,
                 pet_name,
                 tier,
                 base_health,
                 base_attack,
                 ability_type,
                 ability_func,):
        self.PET_NAME = pet_name
        self.TIER = tier
        self.BASE_HEALTH = base_health
        self.BASE_ATTACK = base_attack
        self.ABILITY_TYPE = ability_type
        self.ABILITY_FUNC = ability_func

class PetType(Enum):
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
    # Ability: On level up, Give 2 (random) pets +1L health and +1L attack  (consider previous level)
    # Implementation: If a pet levels up and is a fish, give 2 pets that are placed the stats
    PetType.FISH: PetConfig(pet_name = "Fish",
                        tier = 1,
                        base_health = 3,
                        base_attack = 2,
                        ability_type = AbilityType.LEVEL_UP,
                        ability_func = Abilities.fish_ability),
    
    # Animal: Beaver
    # Ability: On sell, give 2 (random) pets +L attack
    # Implementation: If a pet  is soldand is a beaver, give 2 pets that are placed the stats
    PetType.BEAVER: PetConfig(pet_name = "Beaver",
                        tier = 1,
                        base_health = 2,
                        base_attack = 3,),
    # Animal: Pig 
    # Ability: On sell, give L gold
    # Implementation: If a pet is sold and is a pig, give extra gold
    PetType.PIG: PetConfig(pet_name = "Pig",
                        tier = 1,
                        base_health = 1,
                        base_attack = 4,
                        ability_type = AbilityType.BUY_ROUND_START,
                        ability_func = Abilities.pig_ability,),
    # Animal: Ant 
    # Ability: On faint, give L attack and helath to a random friend
    # Implementation: Mostly a battle ability; maybe need to check if the pill is used on an ant for a special case?
    PetType.ANT: PetConfig(pet_name = "Ant",
                        tier = 1,
                        base_health = 2,
                        base_attack = 2,),
    
    # Animal: Mosquito 
    # Ability: At start of battle, deal 1 damage to L enemies
    # Implementation: Battle ability; should also be a check for all pre-round abilities?
    PetType.MOZZIE: PetConfig(pet_name = "Mosquito",
                        tier = 1,
                        base_health = 2,
                        base_attack = 2,),
    
    # Animal: Cricket 
    # Ability: On faint, spawn a zombie cricket with L attack and health
    # Implementation: In-battle summon mechanic; however need to consider when pill is used
    PetType.CRICKET: PetConfig(pet_name = "Cricket",
                        tier = 1,
                        base_health = 2,
                        base_attack = 1,),
    
    # Animal: Horse 
    # Ability: Friend summoned, give L attack
    # Implementation: In-battle summon mechanic. Also works when buying a pet during buy rounds. Need to remove the bonus by saving attack?
    PetType.HORSE: PetConfig(pet_name = "Horse",
                        tier = 1,
                        base_health = 1,
                        base_attack = 2,),
    
    # Animal: Crab 
    # Ability: Start of combat, gain 0.5L health from the healthiest friend
    # Implementation: In-battle number changing
    PetType.CRAB: PetConfig(pet_name = "Crab",
                        tier = 2,
                        base_health = 1,
                        base_attack = 4,),
 
    # Animal: Swan 
    # Ability: Start of turn (buy period), gain L hold
    # Implementation: Check at the start of each turn for swan and its level
    PetType.SWAN: PetConfig(pet_name = "Swan",
                        tier = 2,
                        base_health = 2,
                        base_attack = 1,),
    
    # Animal: Hedgehog 
    # Ability: On faint, deal 2L damage to all 
    # Implementation: Faint ability is mostly battle, but need to cover pill usage
    PetType.HEDGEHOG: PetConfig(pet_name = "Hedgehog",
                        tier = 2,
                        base_health = 2,
                        base_attack = 3,),
    
    # Animal: Peacock 
    # Ability: When hurt, gain 4L attack permanently 
    # Implementation: In-battle number changing; will have edge case where someone pills a pet with a hurting faint
    PetType.PEACOCK: PetConfig(pet_name = "Peacock",
                        tier = 2,
                        base_health = 5,
                        base_attack = 2,),
    
    # Animal: Flamingo 
    # Ability: On faint, give L health and attack to two nearest pets behind
    # Implementation: Faint ability is mostly battle, but need to cover pill usage
    PetType.FLAMINGO: PetConfig(pet_name = "Flamingo",
                        tier = 2,
                        base_health = 2,
                        base_attack = 3,),
    
    # Animal: Kangaroo 
    # Ability: Friend ahead attacks, gain L helath and damage
    # Implementation: After every attack, check if it is at the second position (Only position where friend in front would attack)
    PetType.KANGAROO: PetConfig(pet_name = "Kangaroo",
                        tier = 2,
                        base_health = 3,
                        base_attack = 2,),

    # Animal: Spider 
    # Ability: On faint, summon a tier 3 pet with L health and attack
    # Implementation: Faint ability is mostly battle, but need to cover pill usage. 
                     # May need to create a new pet from Pet_config since he stats are different
    PetType.SPIDER: PetConfig(pet_name = "Spider",
                        tier = 2,
                        base_health = 2,
                        base_attack = 2,),

    # Animal: Dodo 
    # Ability: Start of battle, give 0.5L attack to the nearest friend ahead
    # Implementation: Just to the attack valuie to Position - 1, unless they're at the start of the lime
    PetType.DODO: PetConfig(pet_name = "Dodo",
                        tier = 3,
                        base_health = 2,
                        base_attack = 4,),
    # Animal: Badger 
    # Ability: Before faint, deal 0.5L attack damage to the adjacent pets
    # Implementation: Attack the pet behind it and do a normal attack on the pet at the start of the other team; mayber pretend to have an instance of thi pet on the other side attacking?
    PetType.BADGER: PetConfig(pet_name = "Badger",
                        tier = 3,
                        base_health = 3,
                        base_attack = 6,),
    
    # Animal: Dolphin 
    # Ability: Start of battle, deal 3 damage to L random pets on the other team
    # Implementation: Pre round ability, should be straightforward
    PetType.DOLPHIN: PetConfig(pet_name = "Dolphin",
                        tier = 3,
                        base_health = 3,
                        base_attack = 4,),
    
    # Animal: Giraffe 
    # Ability: End of turn (buy phase), give 1 health and attack to L friends in front of it
    # Implementation: Can give position - [1:L] the stats
    PetType.GIRAFFE: PetConfig(pet_name = "Giraffe",
                        tier = 3,
                        base_health = 3,
                        base_attack = 1,),
    
    # Animal: Elephant 
    # Ability: After attack, deal 1 damage to the friend behind L times
    # Implementation: Loop the times you attack by the level of the elephant and maybe treat it as an attack to the pet behind. Need to check if it is alive after every fight. and then do the effect
    PetType.ELEPHANT: PetConfig(pet_name = "Elephant",
                        tier = 3,
                        base_attack = 3,
                        base_health = 7,),

    # Animal: Camel 
    # Ability: When hurt, give nearest friend 2L attack and health
    # Implementation: Save the old helath temporarily. After every battle/attack, check and see if there is a negative change. Also do the ability on faint. Shouldn't have a case during buy period
    PetType.CAMEL: PetConfig(pet_name = "Elephant",
                        tier = 3,
                        base_attack = 1,
                        base_health = 3,), 
    
    # Animal: Bunny 
    # Ability: When a friendly eats food, give them +1 health (THIS CAN CHANGE)
    # Implementation: When giving food, check if there is a bunny in the roster
    PetType.BUNNY: PetConfig(pet_name = "Bunny",
                        tier = 3,
                        base_attack = 1,
                        base_health = 2,),
    
    # Animal: Dog 
    # Ability: When a friend is summoned, gain 2L attack and L health until end of battle (stacking and unlimited)
    # Implementation: Need to check for when summoning in buy phase as well as during battle. Can remove the extra stats every start of buy round
    PetType.DOG: PetConfig(pet_name = "Dog",
                        tier = 3,
                        base_attack = 2,
                        base_health = 3,),
    # Animal: Sheep 
    # Ability: On faint, summon 2 rams with 2L health and attack
    # Implementation: Faint ability is mostly battle, but need to cover pill usage. You will always be able to spwan one ram in, need to check if the amount on the lineup is <= 3 for second one
    PetType.SHEEP: PetConfig(pet_name = "Sheep",
                        tier = 3,
                        base_attack = 2,
                        base_health = 3,)

}

TIER_PETS = [
    [PetType.FISH, PetType.BEAVER, PetType.HORSE, PetType.PIG, PetType.ANT, PetType.MOZZIE, PetType.CRICKET],
    [PetType.CRAB, PetType.SWAN, PetType.HEDGEHOG, PetType.FLAMINGO, PetType.KANGAROO, PetType.SPIDER],
    [PetType.DODO, PetType.BADGER, PetType.DOLPHIN, PetType.GIRAFFE, PetType.ELEPHANT, PetType.CAMEL, PetType.BUNNY, PetType.DOG, PetType.SHEEP],
    []
]