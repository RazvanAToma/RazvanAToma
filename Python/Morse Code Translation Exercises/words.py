
# empty list
words_in_the_English_dictionary = []

# Path to the file
path = "C:/Users/razva/Documents/GitHub/RazvanAToma/Python/Morse Code Translation Exercises/words_alpha.txt"


def getting_words_into_list():
	with open (path, "r") as file:

		# reading each line
		for line in file:

			# reading each word
			for word in line.split():
									
				# adding the words to a list
				words_in_the_English_dictionary.append(word)
	
	return words_in_the_English_dictionary

words_in_the_English_dictionary = getting_words_into_list()