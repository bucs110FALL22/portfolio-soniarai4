scoreValue = float(input("Input your score: "))

score1 = scoreValue >= 90
score2 = scoreValue >=80 and scoreValue <90
score3 = scoreValue >70 and scoreValue <80
score4 = scoreValue >60 and scoreValue <70
score5 = scoreValue >= 60

def percentage_to_letter(score=0):
  if score1:
    print("A Grade")
    return True
  if score2:
    print("B Grade")
    return True
  if score3:
    print("C Grade")
    return True
  if score4:
    print("D Grade")
    return False
  if score5:
    print("F Grade")
    return False
print(percentage_to_letter())


