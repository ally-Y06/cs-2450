import random

def ask(prompt):
    user_input = input(prompt)
    return user_input

if (__name__ == "__main__"):
    name = ask("Hi! What is your name?  ")
    guessed = False
    while guessed != True:
        guess = random.randint(15,30)
        answer = ask('Is '+ guess + 'your age?(y/n)  ')
        if answer == 'y':
            guessed = True
        else:
            print("Rats.")
    print(name + " is "+guess +" years old.")
   