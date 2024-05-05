import random

def display_title():
    print("Guessing Game")
    print()
    
def play_game(limit):
    number = random.randint(1,limit)
    print(f"I am thinking of a number from one to {limit}\n")
    count = 1
    guess = int(input("Your Guess?:  "))
    
    while(guess != number):
        if guess < number:
            print('too low')
            count += 1
        elif guess > number:
            print('too high')
            count += 1
        guess = int(input("your guess?:  "))
    print(f"you guessed the number in {count} tries.\n")
    
def main():
    display_title()
    again = "yes"
    while again.lower() == "yes":
        limit = int(input("enter the limit: "))
        play_game(limit)
        again = input("would you like to play again? enter (yes/no)")
        print()
    print("bye")
    
if __name__ == "__main__":
    main()
    
            
                                                                   
    