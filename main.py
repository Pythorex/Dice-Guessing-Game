import random

totalscore = 0

totaldice = [1, 2, 3, 4, 5, 6]
possiblediceside = [1, 2, 3, 4, 5, 6]

numberofdice = random.choice(totaldice)

for x in range(numberofdice):
  value = random.choice(possiblediceside)
  totalscore = totalscore + value


print("The total score is ", totalscore, ".")

guess = input("How many dice are there? (1-6) ")
guessint = int(guess)

if guessint == numberofdice:
  print("Correct, you win!")
else:
  print("Inncorect! You lose.")