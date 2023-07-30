import random
import string

def generate_random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_words(num_words, word_length):
    words = [generate_random_word(word_length) for _ in range(num_words)]
    return words

if __name__ == "__main__":
    num_words = 10000
    word_length = 30

    random_words = generate_random_words(num_words, word_length)
    random_words.sort()

    # Save the words to a file
    with open("strings.txt", "w") as file:
        for word in random_words:
            file.write(word + "\n")

    print("Successfully generated and sorted {} random words in alphabetical order and placed them in strings.txt".format(num_words))
    print("You may now close this window.")
    input()

