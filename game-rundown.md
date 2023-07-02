# What is SYNCS Bot Battle?

Bot Battle is a programming competition that forces students to systematically solve a video game with an automated solution while competing with other students. The goal is to challenge student’s programming ability and devise clever solutions to complex problems in a competitive and fun environment.

# Game Outline

The game is heavily based on the video game *Super Auto Pets* (If you’d like to check out the original game in your spare time, it is very fun and free! More importantly, it will definitely help you with getting a stronger feel of the game and the strategies involved). [https://teamwood.itch.io/super-auto-pets](https://teamwood.itch.io/super-auto-pets)

The game is an auto-battler that has players field a team of pets that will battle each other. As the rounds progress, players lose lives based on the performance of their team and gain access to more pets. A player’s goal is to be the last one standing. 

## Turn Overview

There are 2 stages per round.

### Buy Stage

- A player starts off with a set income of 10 coins, which will determine the extent of actions they can take.
- The player is then presented with a shop that has a random selection of pets and food. The options change as the rounds progress with stronger and more varied options unlocked.
    - The shop can be rerolled to refresh the pet and food selection at the cost of one coin.
    - Elements within the shop can be frozen to be kept in subsequent refreshes or rounds

#### Actions that can be taken are:

##### Buy pets
- Buy pets will have three requirements 
	- You have enough coins (3) to buy the pet 
	- You have an empty slot to place the new pet into 
	- You have a duplicate of the pet that you will put in to level up.
		- Pets are levelled up through buying copies of the same pet, giving stats and enhancing their abilities.
- Buying pets will trigger 
	- A buy trigger
	- A friend summoned trigger

##### Sell pets
- Selling a pet will give you their level back in gold, 
- This will also activate any ability with a sell trigger

##### Buy food to feed to pets
- All food must be bought with enough currency 
	- For food that can be targeted
		- Has to be given to a valid pet in the team 

##### Move the positions of pets
- Given a valid index, two pets can be swapped in position
	- If a pet is moved into a duplicate of another step, the pets will merge and increase sub levels

##### Refresh 
- A refresh will generate new pets and food in the shop
	- All pets have an equal change to appear regardless of tier 

##### Freeze/Unfreeze
- Valid items can be frozen
	- Frozen items and pets will remain in the shop after new rounds and after refreshes 


### Battle Stage
- The pets attack each other simultaneously based on their respective attack values and are knocked out once they run out of health.
- The player who has the last pet(s) standing wins, and their opponent loses lives.
    - If both players have no pets, the round is drawn and no one loses a life.

## Battle Stage order
The engine will conduct the battle stage abilities in a fixed order:

- Round start abilities are activated
	- A scan is done to check for hurt and fainted pets 
- While both teams have at least one member 
	- Trigger before attack abilities 
	- Both pets at the front of each team will attack each other
		- The pets lose health respective of the attack of the other pet
	- Trigger any after attack abilities 
	- Trigger any friend ahead attacked abilities 
	- Trigger any knockout abilities
	- Trigger any faint or hurt abilities 
		- Note that after the ability triggers there will be a clean up of dead pets 
			- Pets who have hurt or faint triggers will not be removed until they have their ability triggered 

For ability priority within the ability activations 
- Level of pet > sub-level difference > stat total (sum of health and attack)


# Pets

Out of the cast of pets available to be bought, all have an ability that is triggered through different mechanisms.
- All pets have a flat cost of 3 coins

| Ability types | Context |
| --- | --- |
| Hurt  | During battle, when the pet is hurt from any form of damage |
| Faint | During battle, when the pet faints |
| Buy/Sell | When a pet is bought or sold. |
| Level Up | When a pet levels up. |
| Friend Ahead Attacks | During battle, when the friend in the position in front of them attacks. |
| Buy Stage Start/End | When the buy round begins, and after the player declares the end of their own buy round.  |
| Friend Summoned | When a pet is summoned into the team line up. Note that this also triggers when a pet is bought and introduced into the line-up after the shop. |
| Battle Stage Start | Before the pets begin to attack each other. |
| Before/After attack | During battle, before and after an attack. |
| Knock-out | During battle, when the pet manages to knock out an opposing pet after attacking them |
| Friend eats food | When a friend is given food or has their stats increased based on a food purchased. |

## Levelling

- Levels are determined by the sub-level 
	- Sub level 2 (1 pet + 2 duplicates) == Level 2 
	- Sub level 5 (Level 2 pet + 3 duplicates) == Level 3

## All pets

>Abilities are enhanced through the level of the pet. The scaling is denoted by L.

### Tier 1 

| Pet  | Trigger | Ability |
| --- | --- | --- |
| Ant  | Faint | Give L attack and health to a random friend |
| Fish | Level up | Give 2 (random) pets +1L health and +1L attack |
| Pig | Sell | Give L gold |
| Mosquito | Battle stage start | Deal 1 damage to L enemies |
| Cricket | Faint | Spawn a zombie cricket with L attack and health |
| Horse | Friend summoned | Give L attack until the end of combat |
| Beaver | Sell | Give 2 (random) pets +L attack | 

### Tier 2

| Pet | Trigger | Ability |
| --- | --- | --- |
| Crab | Battle stage start | Gain 0.5L health from the healthiest friend |
| Swan | Buy stage start | Gain L gold |
| Hedgehog | Faint | Deal 2L damage to all |
| Peacock | Hurt | Gain 4L attack |
| Flamingo | Faint | Give L health and attack to two nearest pets behind | 
| Spider | Faint | Summon a tier 3 pet with 2L health and attack |
| Kangaroo | Friend ahead attacks | Gain L health and damage |

### Tier 3

| Pet | Trigger | Ability |
| --- | --- | --- |
| Dodo | Battle stage end | Give 0.5L attack to the nearest friend ahead |
| Badger | Faint | Deal 0.5L attack damage to the adjacent pets. Includes your own pets |
| Dolphin | Battle stage end | Deal 3 damage to the lowest health enemy. Triggers L times |
| Giraffe |  Buy stage end | Give 1 health and attack to L friends in front of it |
| Camel | Hurt | Give nearest friend behind 2L attack and health | 
| Elephant | After attack | Deal 1 damage to the friend behind L times |
| Bunny | Friendly eats food | Give them +L health |
| Dog | Friend Summoned | Gain 2L attack and L health until end of battle |
| Sheep | Faint | Summon 2 rams with 2L health and attack | 
### Tier 4

| Pet | Trigger |  Ability |
| --- | --- | --- |
| Skunk | Battle stage start | Reduce the highest health enemy's health by 0.33\*L |
| Hippo | Knock Out | Gain 3L health and attack |
| Bison  | Buy stage end | If this has a level 3 friend, gain L attack and 2L health|
| Blowfish | Hurt | Deal 3L damage to one random enemy |
| Squirrel | Buy stage start | Discount all shop food by 1 coin | 
| Penguin | Buy stage end | Give two level 2+ friends L health and attack |

> All pets have a limit of 50 health and attack that cannot be surpassed 

## Pet availability 
The round progression will determine the pool of pets/food available.
- Pets and Food are sorted into tiers 1 to 4
- Round 1 (starting round) will only have tier 1 available 
- Round 3 will introduce tier 2 
- Round 5 will introduce tier 3
- Round 7 will introduce tier 4 
	- As of version 1, tier 4 is the final tier and all corresponding rounds will no longer iterate 

- For each slot in the shop 
	- EVERY AVAILIABLE PET/FOOD ITEM WILL HAVE AN EQUAL CHANCE TO APPEAR IN THAT SLOT

# Food 
- Foods can be split into 2 categories 
	- Consumed food 
		- Disappears post effect
	- Held items
		- Given as an attribute of the pet, and will persist across rounds
		- Will be gone if the pet is sold
- Unless specified, all food will need to be given to a target pet
- Foods will have a flat cost of 3 coins

### Tier 1

| Food | Duration |  Ability |
| --- | --- | --- |
| Apple | Consumed | Increase the health and attack of a pet by 1 |
| Honey | Held | Spawn a 1/1 bee after faint |
### Tier 2

| Food | Duration |  Ability |
| --- | --- | --- |
| Meat Bone | Held | Non-ability attacks will now deal +3 damage |
| Cupcake | Temporary | Give target pet +3 health and attack until end of battle |
### Tier 3

| Food | Duration |  Ability |
| --- | --- | --- |
| Garlic | Held | Pet will take 2 less damage from all sources |
| Salad Bowl | Temporary | Give 2 random pets +1 health and attack |
### Tier 4 

| Food | Duration |  Ability |
| --- | --- | --- |
| Canned Food | Consumed | Give all current and future shop pets +1 attack and health (will not need target pet) |
| Pear | Consumed | Give target pet +2 health and attack |

# Main differences from main game + known bugs
- The pet roster is reduced compared to the normal game. 
- Sleeping pill has been removed via executive decision 
	- All hurt and faint effects can only occur during battle
- As of iteration 1: Repeated actions will not occur 
	- Elephant and Dolphin upgrade abilities are notably affected
- Applications of animal abilities will not be exactly like the game, but will consistently occur
	- Can be clarified through exploring game engine for specifics