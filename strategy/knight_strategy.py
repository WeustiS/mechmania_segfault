from game.game_state import GameState
from game.item import Item
from game.player_state import PlayerState
from game.position import Position
from strategy.strategy import Strategy
from game.character_class import CharacterClass

from util.utility import *


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
         
        pass
    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        curr_state = self.myState(game_state, my_player_index)
        curr_position = curr_state.position
        curr_speed = curr_state.stat_set.speed
        
        '''
        curr_health = curr_state.health
        curr_item = curr_state.item
        curr_range = curr_state.stat_set.range 
        curr_damage = curr_state.stat_set.damage
        '''
        
        centers_x = [5, 4, 4, 5]
        centers_y = [5, 5, 4, 4]
        centers = [Position(x, y) for x,y in zip(centers_x,centers_y)]
        
        x = curr_position.x
        y = curr_position.y
        direction_x = [1, -1, -1, 1]
        direction_y = [1, 1, -1, -1]
        
        goal_x = centers_x[my_player_index]
        goal_y = centers_y[my_player_index]
        
        enemies = [game_state.player_state_list[i] for i in range(4) if i != my_player_index]
        other_postions = [enemy.position for enemy in enemies]

        if curr_position == centers[my_player_index] :
            return curr_position
        else:
            # find next move to the goal
            move_x = 1 if goal_x > x else -1
            move_y = 1 if goal_y > y else -1
            step_x = random_enum(list([range(curr_speed+1)]))
            step_y = curr_speed - step_x
            x = x + move_x*step_x
            y = y + move_y*step_y
            return Position(x, y)
        
        '''
        spawn_x = [0, 9, 9, 0]
        spawn_y = [0, 0, 9, 9]
        spawn_point = Position(spawn_x[my_player_index], spawn_y[my_player_index])
        

        # possible destinations
        squares = []
        for i in range(10):
            for j in range(10):
                if manhattan_distance(curr_position, Position(i,j)) <= curr_speed:
                    squares.append(Position(i,j))
        possible_dests = [squares[i] for i in range()]
        
        possible_attack = []
        
        enemies_range = []
        for enemy in enemies:
         
        
        
        
        distances = [manhattan_distance(p, curr_position) for p in other_postions]
        
        enemies_target = []
        enemies_fatal = []
        for enemy in enemies:
            if enemy.stat_set.damage >= curr_health:
                if curr_position in enemy:
        
        if         
        # is in attack ranges
                
                # is one turn to die
                    
                    # go to people closest to you
                    
                # else
                
        dangers = []
        for enemy in enemies:
            for center in centers:
                
        
        
        healths = [game_state.player_state_list[i].health for i in range(4) if i != my_player_index]
        
        
        
        '''

    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        pass
    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        pass
    def path(self):
        game_state: GameState, my_player_index: int