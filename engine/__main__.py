from signal import SIGTERM, signal
import sys

from engine.gameengine import GameEngine


if __name__ == "__main__":
    engine = GameEngine()

    def kill_handler(a, b):
        print("Game engine killed")
        for i, player in enumerate(engine.state.players):
            engine.output_handler._write_game_log(i, engine.log.get_game_log(player))
        sys.exit(0)

    signal(SIGTERM, kill_handler)

    engine.run()
