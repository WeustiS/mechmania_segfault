from game.game_state import GameState
from game.item import Item
from game.player_state import PlayerState
from game.position import Position
from strategy.strategy import Strategy
from game.character_class import CharacterClass


class Knight(Strategy):
    '''Return the my current player state'''
    def myState(self, game_state:GameState, my_player_index:int) -> PlayerState:
        return game_state.player_state_list[my_player_index]

    '''Check if there are any other knights on the board
        return true if there is, false if none
    '''
    def otherKnight(self, game_state:GameState, my_player_index: int) -> bool:
        playerlist = game_state.player_state_list
        for i in playerlist:
            if i == my_player_index:
                continue
            if i.character_class == CharacterClass.KNIGHT:
                return True
        return False

    def strategy_initialize(self, my_player_index: int) -> None:
        return CharacterClass.KNIGHT
    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        if self.otherKnight(game_state, my_player_index):
            
        pass
    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        pass
    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        pass
    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        pass
