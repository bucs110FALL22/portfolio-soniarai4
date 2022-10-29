class Player:
	def __init__(self, pnum):
		“””
			Initialize the player object
               
               args: pnum [int] the player's id number  
		“””
          self.player_num = pnum
          self.lives = 3 # players always start with 3 lives
          self.is_large = False # player always starts small