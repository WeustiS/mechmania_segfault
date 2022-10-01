from strategy.speedknight import SpeedKnight
from strategy.starter_strategy import StarterStrategy
from strategy.strategy import Strategy

from strategy.knight import Knight


"""Return the strategy that your bot should use.

:param playerIndex: A player index that can be used if necessary.

:returns: A Strategy object.
"""
def get_strategy(player_index: int) -> Strategy:  
  return SpeedKnight()

