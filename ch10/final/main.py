from AdviceAPI import AdviceAPI
from UselessFactAPI import UselessFactAPI
from TriviaAPI import TriviaAPI


def main():
  ufapi = UselessFactAPI()
  useless_fact = ufapi.get()

  aapi = AdviceAPI()
  advice = aapi.get()
  
  question = TriviaAPI()
  results = question.get()

  if results:
    for trivia in results:
      answers = trivia['incorrect_answers'] + [trivia['correct_answer']]
    print(f"Select the correct answer and get some advice:\n--{trivia['question']}--\n*********")

    for i, answer in enumerate(answers):
      print(f"{i}) {answer}")


    choice = int(input("Your answer:"))
    if answers[choice] == trivia['correct_answer']:
      print("correct! here's some advice:", advice) 
    else:
      for answer in trivia['incorrect_answers']:
        if answers[choice] == answer:
          print("incorrect:( instead of advice, here's a random useless fact:", useless_fact)
          break
      else:
        print("that answer is invalid.")
        

main()
