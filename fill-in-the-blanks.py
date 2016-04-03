easy_quiz = """For 2016 Presidential Election race, the leading female Democratic candidate's
first name is ____1____ and her last name is ____2____. The other leading male Democratic
candidate's first name is ____3____ and his last name is ____4____."""

medium_quiz = """For 2016 Presidential Election race, there are 4 remaining republican
candidates. Donald Trump is Chairman of The ____1____ Organization, Marco Rubio is
a Senator from ____2____, John Kasich is a Governor from ____3____, and Ted Cruz is
a Senator from ____4____."""

hard_quiz = """While they withdrew pretty quickly, there were 4 other dem candidates
for 2016 US Presidential Election. They are Martin ____1____, Lawrence ____2____,
Lincoln ____3____, and Jim ____4____."""

blank  = ["____1____", "____2____", "____3____", "____4____"]
level = ["Easy", "Medium", "Hard"]
quiz_sentence = [easy_quiz, medium_quiz, hard_quiz]
answer_list = [["Hillary", "Clinton", "Bernie", "Sanders"], ["Trump", "Florida", "Ohio", "Texas"], ["O'Malley", "Lessig", "Chafee", "Webb"]]
quiz_title = "2016 Election Quiz"

def word_in_pos(word, parts_of_speech):
	""" Takes a string and a list of strings. Return the string with the first letter capitalized if word is
	in fact in the list (parts_of_speech). If not, it will return None"""
	parts_of_speech = [x.lower() for x in parts_of_speech] # lowercasing the comparison list
	word = word.lower() # lowercasing the word to compare
	for e in parts_of_speech:
		if e in word:
			e = e.title() # Capitalizing the found word
			return e
	return None

def header_format(word):
	"""Takes a string, and format it as a header for easy readability like ==== example ===="""
	title_length = len(word)
	word = word.title()	# Makig the first letter of every word to be capitalized automatically
	full_length = 60
	symbol_needed = full_length - title_length
	if symbol_needed % 2 == 0:	# Fixing one character being off sometimes
		header_left = symbol_needed / 2
		header_right = header_left
	else:
		header_left = symbol_needed / 2
		header_right = header_left + 1
	header = "=" * header_left + " " + word + " " + "=" * header_right
	print " "
	print header
	return

def level_selection():
	"""Prompt user to select the game level. If invalid input, re-prompt.
	If valid, return the index number of the level list"""
	index = 0
	while index == 0:
		header_format("Level Selection")
		print "Welcome to " + quiz_title + "!"
		user_input = raw_input("Select your level: Easy, Medium, Hard: ")
		level_selected = word_in_pos(user_input, level)
		if level_selected == None:
			print "Not a valid level. Choose again"
		else:
			print "You chose " + level_selected + "! Good Luck!"
			index += 1
			level_index = level.index(level_selected)
	return level_index

def replace_with_answer2(quiz, blank, answer): # holy cow, this is so much simpler
	"""takes a quiz sentence, blank to be filled, an answer, and retry limit. Prompt user to provide and answer and
	check if the provided answer matches the correct answer. if the user hits the retry limit, it breaks
	out from the function"""
	print quiz
	index = 0
	while index == 0:
		user_input = raw_input("What should go in " + blank + "?: ").lower()
		if user_input == answer.lower():
			print "Correct!"
			print ""
			quiz = quiz.replace(blank, answer)
			index += 1
		else:
			print "Incorrect! Try again!"
			print ""
	return quiz


def play_game():
	"""when ran, it asks for a difficulty level, and spit out a pre-defined quiz for the given level.
	User is prompted to fill in the blanks until they successfully finish the quiz"""
	level_index = level_selection()
	selected_quiz = quiz_sentence[level_index]
	header_format("Quiz: " + level[level_index])
	index = 0
	while index < len(blank):
		corresponding_answer = answer_list[level_index][index]
		corresponding_blank = blank[index]
		selected_quiz = replace_with_answer2(selected_quiz, corresponding_blank, corresponding_answer)
		index += 1
	header_format("You successfully answered all questions!")
	print selected_quiz
	print ""
	return

play_game()

