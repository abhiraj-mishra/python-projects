import random
guesed_no = random.randint(0,99)

user_no = -1
guess = 0

while(guesed_no != user_no):
    guess += 1
    user_no = int(input("guess the no.: "))
    if (user_no > guesed_no):
        print("guess lower number please")
    if(user_no < guesed_no):
        print("guess higher number please")
    else:
        print("there was an problem")

print(f'''You won the number was {guesed_no} , and you guessed {guess} times 
      thank you for playing''')



