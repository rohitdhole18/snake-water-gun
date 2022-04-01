
# for random number generation
import random 

# working function
def game(c,y):
    if c =="s":
       if y == "w":
         return False
       elif y == "g":
         return True
       else:
        print("ERROR : Enter valid key")         
    if c =="w":
       if y == "g":
         return False
       elif y == "s":
         return True
       else:
        print("ERROR : Enter valid key")
    if c =="g":
       if y == "s":
         return False
       elif y == "w":
         return True
       else:
        print("ERROR : Enter valid key")

# generates random number between 1 to 30
randNo = random.randint(1,30)

if (randNo < 10):
    comp = "s"
elif(randNo > 10 and randNo < 20):
    comp = "w"
elif(randNo>20):
    comp = "g"

you = input("Please select from : Snake(s) || Water(w) || Gun(g) = ")

# function calling
win = game(comp,you)

# reason of result
if(you=="s" or you =="w" or you == "g"):
 print("You chooses :",you)
 print("Computer chooses : ",comp)

 # result
 if win == None:
    print("Game DRAW")
 elif win == True:
    print("You WIN!")
 else:
    print("You LOOSE")