from engine.input.movetype import MoveType


class PlayerInput:
    def __init__(self, move_type: 'MoveType', input_dict: dict) -> 'PlayerInput':
        self.move_type = move_type

        if move_type == MoveType.BuyPet:
            self._parse_buy_pet(input_dict)
        elif move_type == MoveType.BuyItem:
            self._parse_buy_item(input_dict)
        elif move_type == MoveType.UpgradePet:
            self._parse_upgrade_pet(input_dict)
        elif move_type == MoveType.SellPet:
            self._parse_sell_pet(input_dict)
        elif move_type == MoveType.Reroll:
            self._parse_reroll(input_dict)
        elif move_type == MoveType.FreezePet:
            self._parse_freeze_pet(input_dict)
        elif move_type == MoveType.FreezeItem:
            self._parse_freeze_item(input_dict)
        elif move_type == MoveType.SwapPet:
            self._parse_swap_pet(input_dict)
        elif move_type == MoveType.EndTurn:
            self._parse_end_turn(input_dict)
        else:
            raise Exception(f'Invalid move type: {move_type}')

    def _parse_buy_pet(self, input_dict):
        pass

    def _parse_buy_item(self, input_dict):
        pass

    def _parse_upgrade_pet(self, input_dict):
        pass

    def _parse_sell_pet(self, input_dict):
        pass

    def _parse_reroll(self, input_dict):
        pass

    def _parse_freeze_pet(self, input_dict):
        pass

    def _parse_freeze_item(self, input_dict):
        pass

    def _parse_swap_pet(self, input_dict):
        pass

    def _parse_end_turn(self, input_dict):
        pass