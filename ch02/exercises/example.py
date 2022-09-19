num = int(input("Enter a number between 2 and 1000: "))

for i in range(1, num):
  if i % 3 == 0 and i % 5 ==0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  
  

