import random

num = random.randrange(1,11)
num_guesses = 0

for i in range(5):
  guess_num = int(input("Enter a guess:"))
  #num_guesses = num_guesses +1
  num_guesses += 1
  if guess_num > num:
    print ("your guess was too high!")
  elif guess_num < num:
    print("your guess was too low")
  else:
    print("correct!")
    correct_guess= True

  if guess_num == num:
    break

print("It took", num_guesses, "tries to get the correct number.")