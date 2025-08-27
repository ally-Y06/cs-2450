import random

def ask(prompt):
    user_input = input(prompt)
    return user_input

if (__name__ == "__main__"):
    name = ask("Hi! What is your name?  ")
    guessed = False
    guesses = 0
    while guessed != True:
        if guesses >= 5:
            print("Couldn't guess your age in 5 turns!")
            break
        guess = random.randint(15,30)
        answer = ask('Is '+ str(guess) + 'your age?(y/n)  ')
        if answer == 'y':
            print(name + " is "+str(guess) +" years old.")
            guessed = True
        else:
            print("Rats.")
            guesses += 1
        
    
   