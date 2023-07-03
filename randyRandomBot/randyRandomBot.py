from submissionhelper.botbattle import BotBattle
from submissionhelper.info.gameinfo import GameInfo
import random

bot_battle = BotBattle()

game_info = bot_battle.get_game_info

player_info = game_info.player_info


class Moveset:
    endTurn = "end turn"
    buyPet = "buy pet"
    reroll = "reroll"


def play_moves(bot_battle: 'BotBattle', game_info: 'GameInfo', move):

    if move == Moveset.buyPet:
        if player_info.coins < 3:
            return False
        player_team_slot_index = random.randint(0,4)

        if player_info.pets[player_team_slot_index] is not None:
            return False
        
        pet_shop_index = random.randint(0,len(player_info.shop_pets()) - 1)
        pet_to_buy = player_info.shop_pets()[pet_shop_index]

        bot_battle.buy_pet(pet_to_buy, player_team_slot_index)

    elif move == Moveset.endTurn:
        bot_battle.end_turn()

    elif move == Moveset.reroll:
        if player_info.coins() < 1:
            return False
        bot_battle.reroll_shop()
    else:
        return False


while True:

    game_info = bot_battle.get_game_info()

    moveset = [Moveset.buyPet, Moveset.reroll]

    outcome = False
    while outcome == False:
        selectedMove = random.sample(moveset, 1)[0]

        outcome = play_moves(bot_battle, game_info, selectedMove)    

    



