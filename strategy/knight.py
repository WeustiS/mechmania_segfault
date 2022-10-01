from game.game_state import GameState
from game.item import Item
from game.player_state import PlayerState
from game.position import Position
from strategy.strategy import Strategy
from game.character_class import CharacterClass
from util.utility import chebyshev_distance


class Knight(Strategy):    

    '''check if at the spawn point'''
    def isInSpawn(self,game_state:GameState, my_player_index:int) -> bool:
        state = self.myState(game_state,my_player_index)
        if my_player_index == 0:
            if state.position == Position(0,0):
                return True
        elif my_player_index == 1:
            if state.position == Position(0,9):
                return True
        elif my_player_index == 2:
            if state.position == Position(9,0):
                return True
        else:
            if state.position == Position(9,9):
                return True
        return False    

    '''check whether or not the given player is in center'''
    def isInCenter(self, ps:PlayerState) -> bool:
        if ps.position in self.centerlist:
            return True
        return False

    '''Return my current player state'''
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
        self.centerlist = [Position(4,4),Position(4,5),Position(5,4),Position(5,5)]
        return CharacterClass.KNIGHT

    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        state = self.myState(game_state,my_player_index)
        #if state.item == Item.SPEED_POTION:
        #    if self.otherKnight(game_state, my_player_index):
        #        return True
        if state.item == Item.HUNTER_SCOPE:
            return True
        return False

    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        curr_state = self.myState(game_state, my_player_index)
        curr_position = curr_state.position
        '''
        curr_health = curr_state.health
        curr_item = curr_state.item
        curr_range = curr_state.stat_set.range
        curr_speed = curr_state.stat_set.speed
        curr_damage = curr_state.stat_set.damage
        '''
        
        centers_x = [4, 5, 5, 4]
        centers_y = [4, 4, 5, 5]
        centers = [Position(x, y) for x,y in zip(centers_x,centers_y)]
        
        x = curr_position.x
        y = curr_position.y
        direction_x = [1, -1, -1, 1]
        direction_y = [1, 1, -1, -1]
        
        enemies = [game_state.player_state_list[i] for i in range(4) if i != my_player_index]
        other_postions = [enemy.position for enemy in enemies]

        if curr_position in centers:
            return curr_position
        else:
            
            return(Position(x+direction_x[my_player_index], y+direction_y[my_player_index]))
        
        '''
        spawn_x = [0, 9, 9, 0]
        spawn_y = [0, 0, 9, 9]
        spawn_point = Position(spawn_x[my_player_index], spawn_y[my_player_index])
        
        
                
        for
        
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
        state = self.myState(game_state, my_player_index)
        playerlist = game_state.player_state_list
        #lowest_hp = 10
        #index_hp = 0
        highest_sc = 0
        index_sc = 0
        for i in playerlist:
            if i == my_player_index:
                continue
            if chebyshev_distance(state.position,playerlist[i].position) <= state.stat_set.range:
                #if playerlist[i].health < lowest_hp:
                #    lowest_hp = playerlist[i].health
                #    index_hp = i
                if playerlist[i].score > highest_sc:
                    highest_sc = playerlist[i].score
                    index_sc = i
        #if playerlist[index_hp] <= state.stat_set.damage:
        #    return index_hp
        #else:
        return index_sc

    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        state = self.myState(game_state, my_player_index)
        if self.isInSpawn(game_state,my_player_index):
            if state.gold >= 8:
                return Item.HUNTER_SCOPE
        return Item.NONE
