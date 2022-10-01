from game.game_state import GameState
from game.item import Item
from game.player_state import PlayerState
from game.position import Position
from strategy.strategy import Strategy
from game.character_class import CharacterClass
from util.utility import *
import random 

class SpeedKnight(Strategy):    

    '''check if at the spawn point'''
    def isInSpawn(self,game_state:GameState, my_player_index:int):# -> bool:
        state = self.myState(game_state,my_player_index)
        return (state.position.x == 0 and state.position.y == 0) or (state.position.x == 9 and state.position.y == 0) or (state.position.x == 0 and state.position.y == 9) or (state.position.x == 9 and state.position.y == 9)
        return False    

    '''check whether or not the given player is in center'''
    def isInCenter(self, ps:PlayerState):# -> bool:
        if (ps.position.x, ps.position.y) in self.centerlist:
            return True
        return False

    '''Return my current player state'''
    def myState(self, game_state:GameState, my_player_index:int):# -> PlayerState:
        return game_state.player_state_list[my_player_index]

    '''Check if there are any other knights on the board
        return true if there is, false if none
    '''
    def otherKnight(self, game_state:GameState, my_player_index: int):# -> bool:
        playerlist = game_state.player_state_list
        for i in playerlist:
            if i == my_player_index:
                continue
            if i.character_class == CharacterClass.KNIGHT:
                return True
        return False
    
    def strategy_initialize(self, my_player_index: int):# -> None:
        self.centerlist = [(4,4), (4,5), (5,4), (5,5)]
        self.spawnlist = [Position(0,0), Position(9, 0), Position(9,9), Position(0,9)]
        
        self.status = "moving"
        self.approaches = [
            ('lr', 'd', 'ud', 'd'),
                           ('lr', 'lr', 'ud', 'ud'),
                           ('lr', 'ud', 'lr', 'ud')
                           ]
        
        self.approach_idx = 0 
        self.move_idx = 0
        self.got_hit = False
        return CharacterClass.KNIGHT

    def use_action_decision(self, game_state: GameState, my_player_index: int):# -> bool:
        state = self.myState(game_state,my_player_index)
        if state.item == Item.HUNTER_SCOPE:
            return False
        if state.item == Item.SPEED_POTION and self.move_idx == 2:
            self.fast = True
            return True
        self.fast = False
        return False

    def move_action_decision(self, game_state: GameState, my_player_index: int):# -> Position:
        my = game_state.player_state_list[my_player_index]
        if self.isInSpawn(game_state,my_player_index):
            if my.gold >= 8 and my.item == Item.NONE:
                return self.spawnlist[my_player_index]
            self.status = "moving"
            self.move_idx = 0
            if self.got_hit:
                self.approach_idx = (self.approach_idx + 1)%3
            self.got_hit = False
            
        if self.isInCenter(game_state.player_state_list[my_player_index]):
            self.status = "holding"
            self.move_idx = 0
        if self.move_idx <= 2 and my.health< my.stat_set.max_health:
            self.got_hit = True
            # self.approach_idx = (self.approach_idx + 1)%3
            
        if self.status == "moving":
            
            curr_pos = game_state.player_state_list[my_player_index].position
            dx = 0
            dy = 0
            
            dir = self.approaches[self.approach_idx][self.move_idx]
            
            if dir == 'ud':
                dy = -2 if curr_pos.y > 4.5 else 2 
            if dir == 'lr':
                dx = -2 if curr_pos.x > 4.5 else 2 
            if dir == 'd':
                dx = -1 if curr_pos.x > 4.5 else 1 
                dx = -1 if curr_pos.x > 4.5 else 1 
            
            if self.move_idx == 2 and self.fast:
                next_dir = self.approaches[self.approach_idx][self.move_idx+1]
                if next_dir == 'ud':
                    dy += -2 if curr_pos.y > 4.5 else 2 
                if next_dir == 'lr':
                    dx += -2 if curr_pos.x > 4.5 else 2 
                if next_dir == 'd':
                    dx += -1 if curr_pos.x > 4.5 else 1 
                    dx += -1 if curr_pos.x > 4.5 else 1 
                
                return Position(curr_pos.x+dx, curr_pos.y+dy)
            
            self.move_idx = self.move_idx + 1
            if dir == 'ud': # move up/down
                return Position(curr_pos.x, curr_pos.y+dy)
            
            if dir == 'lr':
                return Position(curr_pos.x+dx, curr_pos.y)
            
            
        else:
            return random.choice([Position(4,4), Position(4,5), Position(5,4), Position(5,5)])

    def attack_action_decision(self, game_state: GameState, my_player_index: int):# -> int:

        state = self.myState(game_state, my_player_index)
        playerlist = game_state.player_state_list
        #lowest_hp = 10
        #index_hp = 0
        highest_sc = -1
        index_sc = 0
        for i,player in enumerate(playerlist):
            if i == my_player_index:
                continue
            if chebyshev_distance(state.position,player.position) <= state.stat_set.range:
                if player.score > highest_sc:
                    highest_sc = player.score
                    index_sc = i
        return index_sc

    def buy_action_decision(self, game_state: GameState, my_player_index: int):# -> Item:
        state = self.myState(game_state, my_player_index)
        if self.isInSpawn(game_state,my_player_index):
            if state.gold >= 8:
                return Item.HUNTER_SCOPE
        return Item.NONE
