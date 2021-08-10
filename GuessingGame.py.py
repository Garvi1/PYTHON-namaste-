import random 
#randint function is used to generate random number
number=random.randint(1,9)
chance=0
while chance<5:
    guess=int(input("enter your guess"))
  if guess==number:
    print("CONGO!YOU WON",guess) 
    elif guess<number:
        print("HEY")
else:
    print("YOUR GUESS WAS TO HIGH TRY TO MATCH IN NEXT CHANCE",guess) 
    chance=chance+1
    #CHECK WHETHER THE PLAYER GUESSED THE CORRECT ANSWER
    if not chance <  5:
        print("YOU LOSE THE NUMBER I GUESSED",number)