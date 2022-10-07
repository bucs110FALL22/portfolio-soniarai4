import pygame
import random
import math



pygame.init()
window = pygame.display.set_mode(size = (500,300))
windowsize = pygame.display.get_window_size()
radius = int(windowsize[0]/2)
center_of_screen = (windowsize[0]/2, windowsize[1]/2)
print(center_of_screen[0])



#choosing between players
redbox = pygame.Rect(0, 0 , windowsize[0]/2, windowsize[1])
bluebox = pygame.Rect(0, 0 , windowsize[0]/2, windowsize[1])
bluebox.topleft = redbox.topright
player1 = pygame.draw.rect(window,'crimson', redbox)
player2 = pygame.draw.rect(window,'dodgerblue', bluebox)
pygame.display.flip()
print("Who will win? Red or Blue?")

winner = 0
while winner == 0:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_click_pos = event.pos
      print(mouse_click_pos)
      if redbox.collidepoint(mouse_click_pos):
        print("You chose Player 1.")
        winner = 1
      if bluebox.collidepoint(mouse_click_pos):
        winner = 2
        print("You chose Player 2.") 

        
#dartboard
window.fill("palevioletred")
pygame.display.flip()
pygame.draw.circle(window, 'aliceblue',center_of_screen, radius)
pygame.draw.line(window, 'black', (center_of_screen[0]-radius,center_of_screen[1]), (center_of_screen[0]+radius, center_of_screen[1]))
pygame.draw.line(window, 'black', (center_of_screen[0],center_of_screen[1]-radius), (center_of_screen[0], center_of_screen[1]+radius))

pygame.display.flip()

player1_points = 0
player2_points = 0

#game
for i in range(10):
  print("* Round", i+1,"*")
  for j in range(2):
    xcoord = random.randrange(0, windowsize[0])
    ycoord = random.randrange(0, windowsize[1])
    distance_from_center = math.hypot(xcoord - windowsize[0] / 2, ycoord - windowsize[1] / 2) 
    is_in_circle = distance_from_center <= windowsize[0]/2
    if is_in_circle:
      if j == 0:
        pygame.draw.circle(window, 'crimson', (xcoord, ycoord),3)
        player1_points += 1
        print("Player 1 has scored a point. Total points:", str(player1_points))
      elif j == 1:
        pygame.draw.circle(window, 'dodgerblue', (xcoord, ycoord),3)
        player2_points += 1
        print("Player 2 scored a point. Total points:", str(player2_points),)
    else:
      pygame.draw.circle(window, 'gray', (xcoord, ycoord), 3)
      print("Player ", j+1, "missed. No points earned")

    pygame.display.flip()
    pygame.time.wait(1000)
pygame.time.wait(3000)

print(f"Player 1 has {player1_points} points.")
print(f"Player 1 has {player2_points} points.")

actualwinner = 0
if player1_points > player2_points:
  actualwinner = 1
  print("Player 1 won")
elif player1_points < player2_points:
  actualwinner = 2
  print("Player 2 won")
else:
  print("No players won")

if actualwinner == winner:
  print("Your guess was correct.")
else:
  print("Your guess was incorrect.")





