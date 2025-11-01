import random

words= ["python", "developer", "keyboard", "aesthetic", "machine", "coding", "project", "function" ]

print("Welcome to the world of Jumble Game !")
print("Unscramble the letters to form a valid word. Type 'exit' to quit. \n")

score = 0

while True:
    word = random.choice(words)
    jumbled = " ".join(random.sample(word, len(word)))

    print(f"word: {jumbled}")
    guess = input("Your guess: "). lower().strip()

    if guess == "exit":
        print("\n Thanls for playing!")
        break

    if guess == word:
        print(" Correct! +1 point. \n")
        score += 1
    else:
        print(f"Wrong ! The correct woed was : {word}\n")

    print(f"Your current score is: {score}\n")
