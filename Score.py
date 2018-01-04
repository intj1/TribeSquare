class Score:

  def __init__(self, player_name):
    self.__player = player_name
    self.__c_score = 0
    self.__c_multiplier = 1

  def add_points(self, amount):      
      self.__c_score += amount
      return self.__c_score
    
  def subtract_points(self, amount):
    self.__c_score -= (amount)
    self.__c_multiplier = 1
    
  def get_multiplier(self):
    return self.__c_multiplier #accessor

  def increment_multiplier(self, amount):
    self.__c_multiplier *= amount
    return self.__c_multiplier
   
  def get_score(self):
    return self.__c_score #accessorS