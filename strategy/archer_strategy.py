from random import Random
from turtle import pos
from game.game_state import GameState
import game.character_class
import random 

from game.item import Item

from game.position import Position
from strategy.strategy import Strategy

from util.utility import * 

class StarterStrategy(Strategy):
    def strategy_initialize(self, my_player_index: int):
        self.aggressiveness = 0
        self.target = None
        self.last_player_positions = [None, None, None, None]
        return game.character_class.CharacterClass.ARCHER

    def move_action_decision(self, game_state: GameState, my_player_index: int): # -> Position:
        if self.last_player_positions[0] is None:
            self.last_player_positions = [(x.position.x, x.positions.y) for x in game_state]
        
        current_player_positions = [(x.position.x, x.positions.y) for x in game_state]
        predicted_player_positions = [
            (
                max(0, min(9, self.predicted_player_positions[i][0]-self.last_player_positions[i][0])), 
                max(0, min(9, self.predicted_player_positions[i][1]-self.last_player_positions[i][1]))
            )
            for i, x in enumerate(game_state) 
        ]
            
        # check if center is safe- if so, go there
        # TODO
        # check for low HP enemy/chase
        my = game_state[my_player_index]
        other_players = [x for i, x in game_state if i != my_player_index]
        players_to_target = set()
        # find targets based on current HP
        for p_idx, player in enumerate(other_players):
            if player.health < my.stat_set.damage:
                players_to_target.add(p_idx)
        # find targets based on expected HP
        # TODO - predict movements
        # if no targets find lowest HP
        if len(players_to_target) == 0:
            player_hps = [x.health for x in other_players]
            players_to_target.add(player_hps.index(min(players_to_target)))
        
        # randomly choose a plyer to target from list
        target = random.choice(tuple(players_to_target))
        self.target = target
        
        target_predicted_loc = [x for i, x in enumerate(predicted_player_positions) if i is not my_player_index][target]
        
        ideal_distance = my.stat_set.range - self.aggressiveness
        
        viable_sqaures = []
        for dx in range(-ideal_distance, ideal_distance):
            for dy in range(-ideal_distance, ideal_distance):
                pos_query = Position(target_predicted_loc[0]+dy, target_predicted_loc+dx)
                if in_bounds(pos_query) and chebyshev_distance(pos_query, target_predicted_loc) ==ideal_distance:
                    viable_sqaures.append(pos_query)
        
        if len(viable_sqaures) == 0:
            for center_sq in [Position(4,4), Position(4,5), Position(5,4), Position(5,5)]:
                if chebyshev_distance(center_sq, my.position) <= my.stat_set.speed:
                    self.target = None
                    return center_sq
            
        return random.choice(viable_sqaures)

    
    def attack_action_decision(self, game_state: GameState, my_player_index: int):# -> int:
        # set last positions
        other_players = [x for i, x in game_state if i != my_player_index]
        my = game_state[my_player_index]
        if self.target is not None: # increase aggressiveness if we miss our target  
            if chebyshev_distance(other_players[self.target], my.position) < my.stat_set.range: 
                self.aggressiveness = self.aggressiveness + 1 
        
        viable_targets = []
        for i, player in enumerate(game_state):
            if chebyshev_distance(player.position, my.position) < my.stat_set.range: 
                viable_targets.append((i, player))
        
        # Prioritize  targeting low HP players
        best_target = None
        for i, target in viable_targets:
            if i == my_player_index:
                continue 
            if target.health < my.stat_set.damage: # if multiple true, any are fine
                best_target = i
        
        # TODO: target players who will be low
        if best_target is not None:
            return best_target

        else:
            return random.choice(viable_targets)


    def buy_action_decision(self, game_state: GameState, my_player_index: int):# -> Item:
        return Item.NONE

    def use_action_decision(self, game_state: GameState, my_player_index: int):# -> bool:
        return False