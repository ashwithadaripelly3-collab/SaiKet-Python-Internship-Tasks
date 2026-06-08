import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    clear_screen()
    print("=" * 40)
    print("   GUESS THE NUMBER GAME - SaiKet Task 2")
    print("=" * 40)
    
    print("\nSelect Difficulty:")
    print("1. Easy   - 1 to 50")
    print("2. Medium - 1 to 100") 
    print("3. Hard   - 1 to 500")
    
    while True:
        try:
            choice = int(input("\nEnter 1/2/3: "))
            if choice == 1:
                max_num = 50
                break
            elif choice == 2:
                max_num = 100
                break
            elif choice == 3:
                max_num = 500
                break
            else:
                print("Please enter 1, 2, or 3 only")
        except ValueError:
            print("Invalid input. Enter a number 1-3")
    
    secret_number = random.randint(1, max_num)
    attempts = 0
    max_attempts = 10
    
    clear_screen()
    print(f"\nI picked a number between 1 and {max_num}")
    print(f"You have {max_attempts} attempts. Good luck!\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Your guess: "))
            attempts += 1
            
            if guess < 1 or guess > max_num:
                print(f"⚠️  Please guess between 1 and {max_num}")
                attempts -= 1
                continue
                
            if guess < secret_number:
                print("📈 Higher! Try a bigger number\n")
            elif guess > secret_number:
                print("📉 Lower! Try a smaller number\n")
            else:
                clear_screen()
                print("🎉" * 20)
                print(f"CONGRATULATIONS! You guessed it!")
                print(f"The number was {secret_number}")
                print(f"You took {attempts} attempts")
                print("🎉" * 20)
                return attempts
                
        except ValueError:
            print("⚠️  Please enter a valid number!\n")
    
    clear_screen()
    print("💔" * 20)
    print("GAME OVER! Out of attempts")
    print(f"The number was {secret_number}")
    print("💔" * 20)
    return None

def main():
    best_score = None
    
    while True:
        score = play_game()
        
        if score is not None:
            if best_score is None or score < best_score:
                best_score = score
                print(f"\n🏆 NEW BEST SCORE: {best_score} attempts!")
            else:
                print(f"\nYour best score: {best_score} attempts")
        
        play_again = input("\nWant to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Task 2 Complete ✅")
            print("Made for SaiKet Systems Internship")
            break

if __name__ == "__main__":
    main()