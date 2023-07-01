from typing import Optional

from engine.config.petconfig import PET_CONFIG
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

def spawner(health_inp : int, attack_inp: int, pet_config_inp : 'PET_CONFIG[PetType]', player_inp : PlayerState, state_inp : GameState, sub_level_inp : int):
    new_pet = PetState(health_inp, attack_inp, pet_config_inp, player_inp, state_inp)
    
    new_pet.sub_level = sub_level_inp
    
    return new_pet

player_a = PlayerState(0, state)
player_a.pets = [
    spawner(
        health_inp=7,
        attack_inp=4,
        pet_config_inp=PET_CONFIG[PetType.PEACOCK],
        player_inp=player_a,
        state_inp=state,
        sub_level_inp=1
    ),
    spawner(
        health_inp=3,
        attack_inp=2,
        pet_config_inp=PET_CONFIG[PetType.KANGAROO],
        player_inp=player_a,
        state_inp=state,
        sub_level_inp=0
    ),
    spawner(
        health_inp=4,
        attack_inp=4,
        pet_config_inp=PET_CONFIG[PetType.SHEEP],
        player_inp=player_a,
        state_inp=state,
        sub_level_inp=0
    ),
    spawner(
        health_inp=4,
        attack_inp=5,
        pet_config_inp=PET_CONFIG[PetType.HORSE],
        player_inp=player_a,
        state_inp=state,
        sub_level_inp=3
    ),
    spawner(
        health_inp=5,
        attack_inp=4,
        pet_config_inp=PET_CONFIG[PetType.DOG],
        player_inp=player_a,
        state_inp=state,
        sub_level_inp=2
    ),
]

player_b = PlayerState(1, state)
player_b.pets = [
    spawner(
        health_inp=4,
        attack_inp=4,
        pet_config_inp=PET_CONFIG[PetType.ANT],
        player_inp=player_b,
        state_inp=state,
        sub_level_inp=2
    ),
    spawner(
        health_inp=5,
        attack_inp=3,
        pet_config_inp=PET_CONFIG[PetType.CAMEL],
        player_inp=player_b,
        state_inp=state,
        sub_level_inp=0
    ),
    spawner(
        health_inp=10,
        attack_inp=5,
        pet_config_inp=PET_CONFIG[PetType.PEACOCK],
        player_inp=player_b,
        state_inp=state,
        sub_level_inp=0
    ),
    spawner(
        health_inp=5,
        attack_inp=3,
        pet_config_inp=PET_CONFIG[PetType.GIRAFFE],
        player_inp=player_b,
        state_inp=state,
        sub_level_inp=2
    ),
    spawner(
        health_inp=3,
        attack_inp=4,
        pet_config_inp=PET_CONFIG[PetType.SPIDER],
        player_inp=player_b,
        state_inp=state,
        sub_level_inp=0
    ),

]


battle = Battle(player_a, player_b, state, log)
player_a.battle = battle
player_b.battle = battle
battle.run()