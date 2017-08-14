#This is a template for the python story
def begin_story():
	user_response = 0
	print("This is the beginning of the story. Pick a response")
	user_response = int(input("1.option one\n2.option two\n3.option three"))
	decision1(user_response)
	
def decision1(user_response):
	print("This would be the story continuing after the user's first response")
	if user_response == 1:
		print("User selected 1. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		decision2_1(user_response)
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		decision2_2(user_response)
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		decision2_3(user_response)
	
def decision2_1(user_response):
	print("This would be the story continuing after the user's second response")
	if user_response == 1:
		print("User selected 1. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))

def decision2_2(user_response):
	print("This would be the story continuing after the user's second response")
	if user_response == 1:
		print("User selected 1. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))

def decision2_3(user_response):
	print("This would be the story continuing after the user's second response")
	if user_response == 1:
		print("User selected 1. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		decision3_1(user_response)
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		decision3_2(user_response)
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.option one\n2.option two\n3.option three"))
		decision3_3(user_response)
		
def decision3_1(user_response):
  print("This would be the story continuing after the user's third response")
  if user_response == 1:
    print("User selected 1. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_1(user_response)
  elif user_response == 2:
    print("User selected 2. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_3(user_response)

def decision3_2(user_response):
  print("This would be the story continuing after the user's third response")
  if user_response == 1:
    print("User selected 1. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_1(user_response)
  elif user_response == 2:
    print("User selected 2. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_3(user_response)
    
def decision3_3(user_response):
  print("This would be the story continuing after the user's third response")
  if user_response == 1:
    print("User selected 1. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_1(user_response)
  elif user_response == 2:
    print("User selected 2. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.option three"))
    decision3_3(user_response)
	
#This runs the game
user_name = input("Enter your name")
begin_story()
