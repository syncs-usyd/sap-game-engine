from engine.state.gamestate import GameState
from engine.state.playerstate import PlayerState
from engine.state.petstate import PetState
from engine.config.petconfig import PET_CONFIG
from engine.config.pettype import PetType
from engine.game.battle import Battle
from engine.output.gamelog import GameLog

state = GameState()
log = GameLog(state)
log.write_battle_stage_log = lambda x, y, z, k: print("Battle done!")

player_a = PlayerState(0, state)
player_a.pets = [
    PetState(
        health=2,
        attack=2,
        pet_config=PET_CONFIG[PetType.ANT],
        player=player_a,
        state=state
    ),
    PetState(
        health=2,
        attack=2,
        pet_config=PET_CONFIG[PetType.ANT],
        player=player_a,
        state=state
    ),
    PetState(
        health=2,
        attack=2,
        pet_config=PET_CONFIG[PetType.ANT],
        player=player_a,
        state=state
    ),
    PetState(
        health=2,
        attack=2,
        pet_config=PET_CONFIG[PetType.ANT],
        player=player_a,
        state=state
    ),
    PetState(
        health=2,
        attack=2,
        pet_config=PET_CONFIG[PetType.ANT],
        player=player_a,
        state=state
    ),
]

player_b = PlayerState(1, state)
player_b.pets = [
    PetState(
        health=2,
        attack=2,
        pet_config=PET_CONFIG[PetType.ANT],
        player=player_b,
        state=state
    ),
    PetState(
        health=2,
        attack=2,
        pet_config=PET_CONFIG[PetType.ANT],
        player=player_b,
        state=state
    ),
    PetState(
        health=2,
        attack=2,
        pet_config=PET_CONFIG[PetType.ANT],
        player=player_b,
        state=state
    ),
    PetState(
        health=2,
        attack=2,
        pet_config=PET_CONFIG[PetType.ANT],
        player=player_b,
        state=state
    ),
    PetState(
        health=2,
        attack=2,
        pet_config=PET_CONFIG[PetType.ANT],
        player=player_b,
        state=state
    ),
]


battle = Battle(player_a, player_b, state, log)
player_a.battle = battle
player_b.battle = battle
battle.run()