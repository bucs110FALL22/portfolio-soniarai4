import pygame

n=101
while (n != 1 ): 
  if n%2 ==0:
     n = n//2
     print (n)
  else: 
     n = n*3 +1
     print(n)

n=101
count=0

while (n != 1):
    if n%2 ==0:
       n = n//2
    else: 
       n = n*3 +1
    count +=1
    print ("count: ", count)

start = (n)
n=101
upper_limit=20 

iters ={}
for start in range(2, upper_limit +1 ,1):
  count=0
  while (n != 1): 
      if n%2 ==0:
        n = n//2
      else: 
        n = n*3 +1

        count +=1

        iters[start] = count
      
        print(iters)

pygame.init()
window= pygame.display.set_mode()
window.fill("aliceblue")
pygame.display.flip()

font= pygame.font.Font(None,50)
pygame.font.init()

upper_limit=20
iters={}
max_so_far=0
max_val =25
scale=5



for n in range(2, upper_limit +1 ,1):
  n=101
  count=0
  
  while (n != 1): 
      if n%2 ==0:
        n = n//2
        
      else: 
        n = n*3 +1
        count += 1
        iters[start] = count
        print(iters)
        iters_items=(iters, count)

coords = (iters_items)

if coords in range(2):
  pygame.draw.lines(window, "black", False, coords)
  pygame.transform.flip()

elif max_so_far< count:
  max_so_far +=1
  max_val +=1
  
msg=font.render("Largest number of iterations", True, "purple")


pygame.display.flip()