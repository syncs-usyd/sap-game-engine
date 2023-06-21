from enum import Enum

from engine.game.petabilities import PetAbilities
from engine.game.abilitytype import AbilityType


class PetConfig:
    def __init__(self,
                 pet_name,
                 tier,
                 base_attack,
                 base_health,
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

    
    PetType.FISH: PetConfig(pet_name = "Fish",
                        tier = 1,
                        base_attack = 2,
                        base_health = 3,
                        ability_type = AbilityType.LEVEL_UP,
                        ability_func = PetAbilities.fish_ability),
    PetType.BEAVER: PetConfig(pet_name = "Beaver",
                        tier = 1,
                        base_attack = 3,
                        base_health = 2,
                        ability_type= AbilityType.SELL,
                        ability_func= PetAbilities.beaver_ability),
    PetType.PIG: PetConfig(pet_name = "Pig",
                        tier = 1,
                        base_attack = 4,
                        base_health = 1,
                        ability_type = AbilityType.BUY_ROUND_START,
                        ability_func = PetAbilities.pig_ability,),
    PetType.ANT: PetConfig(pet_name = "Ant",
                        tier = 1,
                        base_attack = 2,
                        base_health = 2,
                        ability_type= AbilityType.FAINTED,
                        ability_func= PetAbilities.ant_ability),
    
    PetType.MOZZIE: PetConfig(pet_name = "Mosquito",
                        tier = 1,
                        base_attack = 2,
                        base_health = 2,
                        ability_type= AbilityType.BATTLE_ROUND_START,
                        ability_func= PetAbilities.mosquito_ability),
    

    PetType.CRICKET: PetConfig(pet_name = "Cricket",
                        tier = 1,
                        base_attack = 1,
                        base_health = 2,
                        ability_type= AbilityType.FAINTED,
                        ability_func= PetAbilities.cricket_ability),
    
    PetType.HORSE: PetConfig(pet_name = "Horse",
                        tier = 1,
                        base_attack = 2,
                        base_health = 1,
                        ability_type= AbilityType.FRIEND_SUMMONED,
                        ability_func= PetAbilities.horse_ability),
    
    PetType.CRAB: PetConfig(pet_name = "Crab",
                        tier = 2,
                        base_attack = 4,
                        base_health = 1,
                        ability_type= AbilityType.BATTLE_ROUND_START,
                        ability_func= PetAbilities.crab_ability),
 
    PetType.SWAN: PetConfig(pet_name = "Swan",
                        tier = 2,
                        base_attack = 1,
                        base_health = 2,
                        ability_type= AbilityType.BUY_ROUND_START,
                        ability_func= PetAbilities.swan_ability),
    
    # Animal: Hedgehog 

    # Implementation: Faint ability is mostly battle, but need to cover pill usage
    PetType.HEDGEHOG: PetConfig(pet_name = "Hedgehog",
                        tier = 2,
                        base_attack = 3,
                        base_health = 2,
                        ability_type= AbilityType.FAINTED,
                        ability_func= PetAbilities.hedgehog_ability),
    
    # Animal: Peacock 
    
    # Implementation: In-battle number changing; will have edge case where someone pills a pet with a hurting faint
    PetType.PEACOCK: PetConfig(pet_name = "Peacock",
                        tier = 2,
                        base_attack = 2,
                        base_health = 5,
                        ability_type= AbilityType.HURT,
                        ability_func= PetAbilities.peacock_ability),
    
    # Animal: Flamingo 
    
    # Implementation: Faint ability is mostly battle, but need to cover pill usage
    PetType.FLAMINGO: PetConfig(pet_name = "Flamingo",
                        tier = 2,
                        base_attack = 3,
                        base_health = 2,
                        ability_type= AbilityType.FAINTED,
                        ability_func= PetAbilities.flamingo_ability),
    
    # Animal: Kangaroo 
    
    # Implementation: After every attack, check if it is at the second position (Only position where friend in front would attack)
    PetType.KANGAROO: PetConfig(pet_name = "Kangaroo",
                        tier = 2,
                        base_attack = 2,
                        base_health = 3,
                        ability_type= AbilityType.FRIEND_AHEAD_ATTACK,
                        ability_func= PetAbilities.kangaroo_ability),

    # Animal: Spider 
    
    # Implementation: Faint ability is mostly battle, but need to cover pill usage. 
                     # May need to create a new pet from Pet_config since he stats are different
    PetType.SPIDER: PetConfig(pet_name = "Spider",
                        tier = 2,
                        base_attack = 2,
                        base_health = 2,
                        ability_type= AbilityType.FAINTED,
                        ability_func= PetAbilities.spider_ability),

    # Animal: Dodo 
    # Ability: Start of battle, give 0.5L attack to the nearest friend ahead
    # Implementation: Just to the attack valuie to Position - 1, unless they're at the start of the lime
    PetType.DODO: PetConfig(pet_name = "Dodo",
                        tier = 3,
                        base_attack = 4,
                        base_health = 2,
                        ability_type= AbilityType.BATTLE_ROUND_START,
                        ability_func= PetAbilities.dodo_ability),
    # Animal: Badger 
    # Ability: Before faint, deal 0.5L attack damage to the adjacent pets
    # Implementation: Attack the pet behind it and do a normal attack on the pet at the start of the other team; mayber pretend to have an instance of thi pet on the other side attacking?
    PetType.BADGER: PetConfig(pet_name = "Badger",
                        tier = 3,
                        base_attack = 6,
                        base_health = 3,
                        ability_type= AbilityType.FAINTED,
                        ability_func= PetAbilities.badger_ability),
    
    # Animal: Dolphin 
    # Ability: Start of battle, deal 3 damage to L random pets on the other team
    # Implementation: Pre round ability, should be straightforward
    PetType.DOLPHIN: PetConfig(pet_name = "Dolphin",
                        tier = 3,
                        base_attack = 4,
                        base_health = 3,
                        ability_type= AbilityType.BATTLE_ROUND_START,
                        ability_func= PetAbilities.dolphin_ability),
    
    # Animal: Giraffe 
    # Ability: End of turn (buy phase), give 1 health and attack to L friends in front of it
    # Implementation: Can give position - [1:L] the stats
    PetType.GIRAFFE: PetConfig(pet_name = "Giraffe",
                        tier = 3,
                        base_attack = 1,
                        base_health = 3,
                        ability_type= AbilityType.BUY_ROUND_END, 
                        ability_func= PetAbilities.giraffe_ability),
    
    # Animal: Elephant 
    # Ability: After attack, deal 1 damage to the friend behind L times
    # Implementation: Loop the times you attack by the level of the elephant and maybe treat it as an attack to the pet behind. Need to check if it is alive after every fight. and then do the effect
    PetType.ELEPHANT: PetConfig(pet_name = "Elephant",
                        tier = 3,
                        base_attack = 3,
                        base_health = 7,
                        ability_type= AbilityType.AFTER_ATTACK,
                        ability_func= PetAbilities.elephant_ability),

    # Animal: Camel 
    # Ability: When hurt, give nearest friend 2L attack and health
    # Implementation: Save the old helath temporarily. After every battle/attack, check and see if there is a negative change. Also do the ability on faint. Shouldn't have a case during buy period
    PetType.CAMEL: PetConfig(pet_name = "Camel",
                        tier = 3,
                        base_attack = 1,
                        base_health = 3,
                        ability_type= AbilityType.HURT,
                        ability_func= PetAbilities.camel_ability),
    
    # Animal: Bunny 
    # Ability: When a friendly eats food, give them +1 health (THIS CAN CHANGE)
    # Implementation: When giving food, check if there is a bunny in the roster
    PetType.BUNNY: PetConfig(pet_name = "Bunny",
                        tier = 3,
                        base_attack = 1,
                        base_health = 2,
                        ability_type= AbilityType.FRIEND_ATE_FOOD,
                        ability_func= PetAbilities.bunny_ability),
    
    # Animal: Dog 
    # Ability: When a friend is summoned, gain 2L attack and L health until end of battle (stacking and unlimited)
    # Implementation: Need to check for when summoning in buy phase as well as during battle. Can remove the extra stats every start of buy round
    PetType.DOG: PetConfig(pet_name = "Dog",
                        tier = 3,
                        base_attack = 2,
                        base_health = 3,
                        ability_type= AbilityType.FRIEND_SUMMONED,
                        ability_func= PetAbilities.dog_ability),
    # Animal: Sheep 
    # Ability: On faint, summon 2 rams with 2L health and attack
    # Implementation: Faint ability is mostly battle, but need to cover pill usage. You will always be able to spwan one ram in, need to check if the amount on the lineup is <= 3 for second one
    PetType.SHEEP: PetConfig(pet_name = "Sheep",
                        tier = 3,
                        base_attack = 2,
                        base_health = 3,
                        ability_type= AbilityType.FAINTED,
                        ability_func= PetAbilities.sheep_ability)

}

TIER_PETS = [
    [PetType.FISH, PetType.BEAVER, PetType.HORSE, PetType.PIG, PetType.ANT, PetType.MOZZIE, PetType.CRICKET],
    [PetType.CRAB, PetType.SWAN, PetType.HEDGEHOG, PetType.FLAMINGO, PetType.KANGAROO, PetType.SPIDER],
    [PetType.DODO, PetType.BADGER, PetType.DOLPHIN, PetType.GIRAFFE, PetType.ELEPHANT, PetType.CAMEL, PetType.BUNNY, PetType.DOG, PetType.SHEEP],
    []
]