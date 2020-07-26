import random
def equationPartSwitcher(arg):  
      switcher = {
        1: "*", 
        2: "+",
        3: "+2 *",
        4: "^"
      }
      return switcher[arg]
name = input ("Welcome to the sequence guesser game. \nWhat is your name?\n")
ready = input("Welcome %s. I am going to generate a sequence of numbers, then you have to enter the next number in the sequence. \nReady? (y/n) \n" % name)
while True:
  if (ready == "y"):
    x = random.randint(1,2)
    y = random.randint(1,4)
    equation = ("x = x %s x" % (equationPartSwitcher(y)))
    print("Okay, here's a sequence:")
    for i in range(7):
      exec(equation)
      if i != 5:
        
        print("%i " % x, end = '')
      else:
        answer = x
        print("? ", end = '')

    while True:
      userGuess = input("\nWhat's the missing number?\n")
      if (userGuess.isdigit()):
        if int(userGuess) == answer:
          print("You got it!")
          break
        else:
          print("Incorrect! Try again. ")
      else: 
        print("Please enter a digit.\n")
        continue
    ready = input("Want to play again? (y/n)")
    continue

  else:
    print ("Thanks for playing.")
    break