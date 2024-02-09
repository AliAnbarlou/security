import random ,os

os.system('clear') and os.system('cls')
def guess_word(target_word):
    words = int(0)
    x = ""
    while True:
        random_word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(len(target_word)))
        words += 1
        x=random_word
        if random_word == target_word:
            return f"guessed word : {x} , code tried over {words} times"


target = input("Enter the target word: ")
guessed_words = guess_word(target)
print("Guessed words:", guessed_words)
