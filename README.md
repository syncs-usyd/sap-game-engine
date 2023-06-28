# (not so) Super Auto Pets Game Engine
This repository contains the game engine for SYNCS x SIG Bot Battle 2023. This year, we're playing the auto-battler game [Super Auto Pets](https://teamwood.itch.io/super-auto-pets). If you've never heard of it, the game is free to play on the browser and is great fun. In particular, we're playing the Versus mode, which pits players against eachother in real-time until there is only one player left standing.

## High-level Strategy and Game Overview
Please checkout our high-level [(not so) Super Auto Pets game rundown](https://syncs.notion.site/SYNCS-BOT-BATTLE-2023-GAME-RUNDOWN-baad74bdc74a4efea01cb18efebf6046?pvs=4). 

## How to Run
### Prereqs
- We recommend Python 3.8.x
- The scripts have been designed for Unix environments (note: they work on WSL2)

### Scripts
To run the game engine, all you have to do is execute the `run_test_env.sh` script. Without any flags, it will copy the `tutorialsubmission.py` for each player and run the game engine to completion. It does this by creating a testing subdirectory `testing_environment` where all the necessary files and directories will be created and copied.

To debug the engine or submission code, you can add optional flags. *Warning*: the game engine has strict timeouts so, before debugging and running the script, update the timeout values in `engine/config/ioconfig.py`.  
- Executing `./run_test_env.sh -e` will setup the test environment and start the submissions but wont start the game engine. This allows you to run the `testing_environment/engine` Python module with a debugger. Note: it is recommended to make your working directory `testing_environment` and use the provided `debug_engine.py` script to easily debug without needing to execute the module itself.

- Executing `./run_test_env.sh -s {submission_num}` will setup the test environment and start the other submissions/game engine. Similar to above, this allows you to run the debugger on your submission.

### Output
After executing `run_test_env.sh` to completion, the output files will be created in `testing_environment/output`.
- `results.json` tells you whether the game succeeded and who the winner/at fault player was.
- `game_{submission_num}.md` is a human-readable markdown representation of the game for each submission.
- `submission_{submission_num}.err` is the stderr for each submission.
- `submission_{submission_num}.log` is the stdout for each submission.

## Core Components
### `engine`
The `engine` Python module is where everything to do with the game engine exists. It contains the game state, input handlers, output helpers and config.

### `submissionhelper`
The `submissionhelper` Python module is an API to make communicating with the game engine easier for submissions. It provides the `BotBattle` class, which has helper methods for getting game information and playing moves. It also has helpful info classes for the various game information the engine provides.

### `tutorialsubmission.py`
The `tutorialsubmission.py` is an example submission that is meant to help explain how to create a bot and use the `submissionhelper` module. It is a super useful place to start to write your first bot.

### `run_test_env.sh`
The `run_test_env.sh` script is the easiest way to test your submission locally. Update the `$submission_file` bash variable to use your submission. See the [How to Run](#how-to-run) section to learn how to use it. 