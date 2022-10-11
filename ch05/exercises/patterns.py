
def star_pyramid():
  rows = int(input("How many rows? "))
  numstars = 0
  while numstars <= rows:
    print('*'*numstars)
    numstars += 1
star_pyramid()

def rstar_pyramid():
  rows = int(input("How many rows? "))
  numstars = rows
  while numstars >= 0:
    print('*'*numstars)
    numstars -= 1
rstar_pyramid()