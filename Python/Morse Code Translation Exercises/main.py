import random
from words import getting_words_into_list, words_in_the_English_dictionary

getting_words_into_list()

random_word = random.choice(words_in_the_English_dictionary)

def pose_question():
    print("-.-.-.-.-.-.-.-.-.-.-.-.-")
    print(f"Your word to translate is {random_word}")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-")
    user_input = input()

    return user_input


user_input = pose_question()

morse_translations = {
    "a": ".-",
    "b": "-..."
}


print(morse_translations)