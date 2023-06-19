from engine.input.movetype import MoveType


class PlayerInput:
    self.index_from: int
    self.index_to: int

    def __init__(self, move_type: 'MoveType', input_dict: dict):
        self.move_type = move_type
        self.index_from

        if move_type == MoveType.BUY_PET:
            self._parse_buy_pet(input_dict)
        elif move_type == MoveType.BUY_ITEM:
            self._parse_buy_item(input_dict)
        elif move_type == MoveType.UPGRADE_PET:
            self._parse_upgrade_pet(input_dict)
        elif move_type == MoveType.SELL_PET:
            self._parse_sell_pet(input_dict)
        elif move_type == MoveType.REROLL:
            self._parse_reroll(input_dict)
        elif move_type == MoveType.FREEZE_PET:
            self._parse_freeze_pet(input_dict)
        elif move_type == MoveType.FREEZE_ITEM:
            self._parse_freeze_item(input_dict)
        elif move_type == MoveType.SWAP_PET:
            self._parse_swap_pet(input_dict)
        elif move_type == MoveType.END_TURN:
            self._parse_end_turn(input_dict)
        else:
            raise Exception(f'Invalid move type: {move_type}')

    def _parse_buy_pet(self, input_dict):
        self.index_from = input_dict["buy_pet_position"]
        self.index_to = input_dict["place_pet_position"]

    def _parse_buy_item(self, input_dict):
        self.index_from = input_dict["buy_item_position"]
        self.index_to = input_dict["use_item_position"]

    def _parse_upgrade_pet(self, input_dict):
        self.index_from = input_dict["buy_pet_position"]
        self.index_to = input_dict["upgrade_pet_position"]

    def _parse_sell_pet(self, input_dict):
        self.index_from = input_dict["sell_pet_position"]

    def _parse_reroll(self, input_dict):
        pass

    def _parse_freeze_pet(self, input_dict):
        self.index_from = input_dict["freeze_pet_position"]

    def _parse_freeze_item(self, input_dict):
        self.index_from = input_dict["freeze_item_position"]

    def _parse_swap_pet(self, input_dict):
        self.index_from = input_dict["swap_pet1_position"]
        self.index_to = input_dict["swap_pet2_position"]

    def _parse_end_turn(self, input_dict):
        self.index_to = input_dict
