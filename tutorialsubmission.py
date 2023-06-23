from submissionhelper.botbattle import BotBattle
from submissionhelper.info.gameinfo import GameInfo


# Core class for the submission helper
# Use this to make moves and get game info
bot_battle = BotBattle()

# Core game loop
# Each iteration you will be expected to make one move
prev_round_num = 0
while True:
    # This function will pause until the game engine
    # is ready for you to make a move. Always call it
    # before making a move. It provides the information
    # required to make a sensible move
    game_info = bot_battle.get_game_info()

    # How to detect whether it is a new round
    new_round = prev_round_num != game_info.round_num
    if new_round:
        prev_round_num = game_info.round_num

    # Now let's go through a very simple (and poorly written!)
    # example submission
    def make_move(game_info: 'GameInfo'):
        # This loop runs through the available pets in the shop.
        # It then checks whether you have an empty slot in your pet lineup.
        # If you do, then it checks that you can afford to buy the pet from
        # the shop.
        # At a minimum, you will now atleast get a full pet lineup!
        for shop_pet in game_info.player_info.shop_pets:
            for i, pet in enumerate(game_info.player_info.pets):
                if pet == None and shop_pet.cost <= game_info.player_info.coins:
                    # Always return after playing a move as
                    # you can only make one move at a time!
                    bot_battle.buy_pet(shop_pet, i)
                    return

        # If we get here, there are two possibilities
        # 1. We're out of cash... yikes. Let's just end if thats the case
        # Note: your bot can be a lot smarter! Why not freeze some shop pets/foods?
        # Potentially rearrange your lineup to be more effective (think ability composition)
        # If you've got one or two coins laying around, do a reroll and freeze the goodies
        if game_info.player_info.coins < 3:
            # Note: you have to end your turn once you're finished otherwise your submission
            # will get banned and you'll have to resubmit to keep playing!
            bot_battle.end_turn()
            return

        # 2. We have a full pet lineup. That's not toooo bad,
        # but why not check if there's a better pet in the shop
        for shop_pet in game_info.player_info.shop_pets:
            for i, pet in enumerate(game_info.player_info.pets):
                if pet.health < shop_pet.health and pet.attack < shop_pet.attack and shop_pet.cost <= game_info.player_info.coins:
                    # We can't just immediately buy the pet because we have no free slots :(
                    # First we have to sell the mediocre pet AND THEN we can buy the shop pet

                    # This requires two remaining moves so let's check that first
                    if game_info.remaining_moves < 2:
                        bot_battle.end_turn()
                        return

                    bot_battle.sell_pet(pet)
                    # We always have to call get_game_info() before making a second move
                    _ = bot_battle.get_game_info()
                    bot_battle.buy_pet(shop_pet, i)
                    return

        # And, for this simple example, if we get here, there's no more moves to make
        bot_battle.end_turn()

    # Last but not least, don't forget to call the function!
    make_move(game_info)

    # Now, you might be asking, where do I go from here?
    # Well, here's a few ideas to get you started:

    # 1. We didn't look at what type of pet we were buying AT ALL
    #    How are you going to make the best lineup possible without having some sort of heuristic for which pet is best?
    #    In the game engine, we have a ton of config listed. You could always leverage that!
    
    # 2. What about the shop foods? Eating food is a quick way to get better pets. AND don't forget about garlic + meat bone

    # 3. We didn't even rearrange our pets! bot_battle.swap_pets() is crucial to making an effective lineup

    # 4. What about rerolling!?!!?! Time to start decided when it is most effective to reroll versus eating food

    # 5. LEVEL YOUR PETS UP! Once you start getting a lineup you like, leveling up a pet can gurantee a victory.

    # This only scratches the surface and there's a lot of clever tricks you can do in the game
    # (HINT: For example, sleeping pill often causes permanent changes and potentially upgrades)

    # If you have any problems or questions, remember to hit us up on the discord.
