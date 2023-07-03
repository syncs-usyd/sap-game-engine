from submissionhelper.botbattle import BotBattle
from submissionhelper.info.gameinfo import GameInfo
from submissionhelper.info.playerinfo import PlayerInfo
import random

bot_battle = BotBattle()

game_info = bot_battle.get_game_info

player_info = game_info.player_info


class Moveset:
    endTurn = "end turn"
    buyPet = "buy pet"
    buyFood = "buy food"
    freezeFood = "freeze food"
    freezePet = "freeze Pet"
    reroll = "reroll"



def play_moves(bot_battle: 'BotBattle', 
               game_info: 'GameInfo', 
               player_info: 'PlayerInfo', 
               move):

    if move == Moveset.buyPet:
        return buy_pet(bot_battle, game_info, player_info)
    elif move  == Moveset.buyFood:
        return buy_food(bot_battle, game_info, player_info)
    elif move == Moveset.endTurn:
        bot_battle.end_turn()
        return True
    elif move == Moveset.reroll:
        if player_info.coins() < 1:
            return False
        bot_battle.reroll_shop()
        return True
    elif move  ==  Moveset.freezeFood:
        food_to_freeze = player_info.shop_foods()[0]
        if food_to_freeze.is_frozen == True:
            return False
        bot_battle.freeze_food(food_to_freeze)
    elif move  ==  Moveset.freezePet:
        pet_to_freeze = player_info.shop_pets()[0]
        if pet_to_freeze.is_frozen == True:
            return False
        bot_battle.freeze_pet(pet_to_freeze)
    else:
        return False


def buy_pet(bot_battle: 'BotBattle', game_info: 'GameInfo', player_info: 'PlayerInfo'):
    if player_info.coins < 3:
        return False
    player_team_slot_index = random.randint(0,4)

    if player_info.pets[player_team_slot_index] is not None:
        return False
    
    pet_shop_index = random.randint(0,len(player_info.shop_pets()) - 1)
    pet_to_buy = player_info.shop_pets()[pet_shop_index]
    bot_battle.buy_pet(pet_to_buy, player_team_slot_index)
    return True

def buy_food(bot_battle: 'BotBattle', game_info: 'GameInfo', player_info: 'PlayerInfo'):
    if player_info.coins < 3:
        return False
    
    shop_food = player_info.shop_foods()[0]
    pet_to_feed = player_info.pets()[0]
    bot_battle.buy_food(shop_food, pet_to_feed)
    return True



while True:

    game_info = bot_battle.get_game_info()

    moveset = [Moveset.buyPet, Moveset.reroll, Moveset.buyFood, Moveset.freezeFood, Moveset.freezePet]

    #Always buy a pet first if possible 
    play_moves(bot_battle, game_info, Moveset.buyPet)

    outcome = False
    while outcome == False:
        selectedMove = random.sample(moveset, 1)[0]

        outcome = play_moves(bot_battle, game_info, selectedMove)    

    



