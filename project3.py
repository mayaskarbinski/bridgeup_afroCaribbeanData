import sqlite3

# After your database is complete and ready to use,
# Fill in the blanks (the underlined areas) with your
# information.
# From there, follow the instructions from comments
#  with three hashtags ### to add your own code


# Some lines, like these, are not in a function!
# Don't change this code, but think about it for a minute.
# What does that mean?
conn = sqlite3.connect('cuba_anthro.db')
c = conn.cursor()


def menu():
	dbName = "AfroCaribbean" #name your database here
	partner1 = "Maya" #one of your names here
	partner2 = "Makoyan" #one of your names here
	print "Welcome to the "+ dbName + " database,"
	print "By " + partner2 + " and " + partner1 + ".\n"

	user_choice = options()

	# We have never seen this 'while' word before!
	# What do you think it does?
	while user_choice != "Q":
		if user_choice == "0":
			exampleQuestion()
		elif user_choice == "1":
			question1()
		elif user_choice == "2":
			question2()
		elif user_choice == "3":
			question3()
		elif user_choice == "4":
			question4()
		elif user_choice == "5":
			question5()
		### If you get to creating your own question/s,
		### don't forget to add other elifs here!
		else:
			print "We're sorry, that is not an option."
			print "Please try again"

		print "\n\n"
		user_choice = options()

	print "\nThank you for using our program!"
	print "Have a great day."

def options():
	print "Which question would you like answered (enter the number below)?"
	print "0. Example Question: How many donors have given to this collection?"
	print "1. What techniques were used to create a Potsherd?"
	print "2. Which donors have we exchanged items with, and where did those items come from (what locale)?"
	print "3. What objects were made with clay, outside of Northeast coast of Cuba, Baracoa?"
	print "4. What are the dimentions of each object from the Northeast coast of Cuba, Baracoa?"
	print "5. What locale has objects made of stone?"
	### If you get to creating your own question/s,
	### don't forget to tell the user about it here!
	print "\nPress 'Q' to quit"
	choice = raw_input()
	return choice

def exampleQuestion():
	print "You have chosen to look up how many donors"
	print "have given to this collection.\n"

	query = c.execute("SELECT COUNT(DISTINCT donor) FROM Donor")
	for row in query:
		print "There are "+ str(row[0]) + " donors in this collection."

def question1():
	print "You have chosen to discover:"
	print "Which techniques have been used to"
	print "create a 'Potsherd'?"

	query = c.execute('''SELECT DISTINCT obj,technique FROM Object WHERE obj="POTSHERD"''')
	for row in query:
		print row
	### Add code here to answer each question

def question2():
	print "You have chosen to discover:"
	print "Which donors have we exchanged items with, and where did those items come from (what locale)?"
	
	query= c.execute('''SELECT DISTINCT donor,class,locale FROM Donor JOIN Object ON Donor.accession_no = Object.accession_no JOIN Place ON Object.locale_id = Place.locale_id WHERE class = "EXCHANGE"''')
	for row in query:
		print row
	### Add code here to answer each question

def question3():
	print "You have chosen to discover:"
	print "What objects were made with clay, outside of Northeast coast of Cuba, Baracoa?"
	
	query = c.execute('''SELECT DISTINCT obj, locale, material FROM Object JOIN Place ON Object.locale_id = Place.locale_id WHERE locale!="NORTHEAST COAST OF CUBA BARACOA" and material="CLAY"''')

	for row in query:
		print row
	### Add code here to answer each question

def question4():
	print "You have to choose to discover:"
	print "What are the dimentions of each object from the Northeast coast of Cuba, Baracoa?"

	query = c.execute('''SELECT DISTINCT obj,dimensions,locale FROM Object JOIN Place ON Object.locale_id = Place.locale_id WHERE locale="NORTHEAST COAST OF CUBA BARACOA" and dimensions!=""''')
	for row in query:
		print row

def question5():
	print "You have to choose to discover:"
	print "What locale has objects made of stone?"

	query = c.execute('''SELECT DISTINCT locale,obj,material FROM Object JOIN Place ON Object.locale_id = Place.locale_id WHERE material LIKE "STONE%"''') #WHERE obj="%STONE%"
	for row in query:
		print row
### If you get to creating your own question/s,
### make sure to add a new function for each question!



menu()
# Don't forget to close the connection to the database!
# (We don't have to save what we did because we aren't
#  updating our database.)
conn.close()
