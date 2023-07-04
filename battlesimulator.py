from typing import Optional
from engine.config.foodconfig import FOOD_CONFIG, FoodConfig
from engine.config.foodtype import FoodType

from engine.config.petconfig import PET_CONFIG, PetConfig
from engine.config.pettype import PetType
from engine.game.battle import Battle
from engine.output.gamelog import GameLog
from engine.state.gamestate import GameState
from engine.state.petstate import PetState
from engine.state.playerstate import PlayerState



def write_battle_log(x, y, battle_lost: Optional[bool], k):
    if battle_lost == True:
        print("Player B won!")
    elif battle_lost is None:
        print("The battle was a tie!")
    else:
        print("Player A won!")

state = GameState()
log = GameLog(state)
log.write_battle_stage_log = write_battle_log

def spawner(health: int, attack: int, pet_config: 'PetConfig', player: 'PlayerState', state: 'GameState', sub_level: int, carried_food: Optional['FoodConfig'] = None):
    new_pet = PetState(health, attack, pet_config, player, state)
    new_pet.sub_level = sub_level
    new_pet.carried_food = carried_food

    return new_pet

player_a = PlayerState(0, state)
player_a.pets = [
    spawner(
        health=1,
        attack=2,
        pet_config=PET_CONFIG[PetType.HORSE],
        player=player_a,
        state=state,
        sub_level=0
    ),
    spawner(
        health=2,
        attack=2,
        pet_config=PET_CONFIG[PetType.MOSQUITO],
        player=player_a,
        state=state,
        sub_level=0
    ),
    spawner(
        health=2,
        attack=2,
        pet_config=PET_CONFIG[PetType.ANT],
        player=player_a,
        state=state,
        sub_level=0
    ),
    spawner(
        health=1,
        attack=4,
        pet_config=PET_CONFIG[PetType.PIG],
        player=player_a,
        state=state,
        sub_level=0
    ),
    spawner(
        health=3,
        attack=2,
        pet_config=PET_CONFIG[PetType.FISH],
        player=player_a,
        state=state,
        sub_level=0
    ),
]

player_b = PlayerState(1, state)
player_b.pets = [
    spawner(
        health=1,
        attack=2,
        pet_config=PET_CONFIG[PetType.HORSE],
        player=player_b,
        state=state,
        sub_level=0,
        carried_food=FOOD_CONFIG[FoodType.HONEY]
    ),
    spawner(
        health=1,
        attack=2,
        pet_config=PET_CONFIG[PetType.HORSE],
        player=player_b,
        state=state,
        sub_level=0
    ),
    spawner(
        health=2,
        attack=2,
        pet_config=PET_CONFIG[PetType.MOSQUITO],
        player=player_b,
        state=state,
        sub_level=0
    ),
    spawner(
        health=1,
        attack=2,
        pet_config=PET_CONFIG[PetType.HORSE],
        player=player_b,
        state=state,
        sub_level=0
    ),
    spawner(
        health=3,
        attack=2,
        pet_config=PET_CONFIG[PetType.FISH],
        player=player_b,
        state=state,
        sub_level=0
    ),
]


battle = Battle(player_a, player_b, state, log)
player_a.battle = battle
player_b.battle = battle
battle.run()