

###################################loops intro######################################
# queue videos
#what is iteration?
#what are for loops?


# For Loops Practice #1
# Using For loops, greet all members of a class, printing "Hello" + their name.

# For example: "Hello Norville"

students = ["Norville", "Fred", "Velma", "Daphne"]




# For Loops Practice #2
# Given the following list of numbers, calculate the sum of all the numbers using For loops and store the result of the sum in a variable called sum_numbers:

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
# sum_numbers = 





# For Loops Practice #3
# Given the following list of numbers, perform the sum of all even and odd* numbers separately in the variables sum_even and sum_odd respectively:

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

# *Recall from previous days: the modulus (or remainder) of a number divided by 2 is zero when said value is even, and 1 when it is odd

# num % 2 == 0 (even values)

# num % 2 == 1 (odd values)

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

# sum_even = 

# sum_odd = 




########################################loops############################################################
# while Loops
# The while statement in Python is one of most general ways to perform iteration. A while statement will repeatedly execute a single statement or group of statements as long as the condition is true. The reason it is called a 'loop' is because the code statements are looped through over and over again until the condition is no longer met.

# The general format of a while loop is:

# while condition:
#     code statements
# else:
#     final code statements

# so a while loop is basically a way for python to loop through code several times until a condtion is met
# Let’s look at a few simple while loops in action.
#queue video about loops
# i = 1
# while i < 10:
#   print(i)
#   i = i + 1
#   # or i += 1

# print("done with loop")


# we can use a while loop to continually ask the user to guess a word until they guess it correctly
# secret_word ="giraffe"
# guess= ""

# while guess != secret_word:
#   guess = input("enter a guess: ")

# print("you win")


# While Loops Practice #1
# Create a While Loop that prints the numbers 10 to 0 on the screen, one at a time.

number = 10



# While Loops Practice #2
# Create a While Loop that subtracts one by one the numbers from 50 to 0 (both numbers included) with the following additional conditions:

# If the number is divisible by 5, show that number on the screen (remember that here you can use the modulus operation dividing by 5 and checking the remainder!)

# If the number is not divisible by 5, continue executing the loop without showing the value on the screen (don't forget to continue subtracting so that the program doesn't run infinitely).

number = 50



# Loop Interruption Statements Practice
# Create a For loop through the following list of numbers, printing each of its elements to the screen, and interrupt the flow when you find a negative value:

# list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

# You must not change the order of the list.

list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]




##############################dictionaries and loops##############################################
#We've been learning about sequences in Python but now we're going to switch gears and learn about mappings in Python. If you're familiar with other languages you can think of these Dictionaries as hash tables.

# This section will serve as a brief introduction to dictionaries and consist of:

# 1.) Constructing a Dictionary
# 2.) Accessing objects from a dictionary
# 3.) Nesting Dictionaries
# 4.) Basic Dictionary Methods

# So what are mappings? Mappings are a collection of objects that are stored by a key, unlike a sequence that stored objects by their relative position. This is an important distinction, since mappings won't retain order since they have objects defined by a key.

# A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.


#sample dictionary
monthConversions = {
    "JAN" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun": "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct"  : "October"

}
# print(monthConversions["Sep"])
# #add more months
# monthConversions['Nov'] ="November"
# monthConversions['Dec'] = "December"
# print(monthConversions)
#print(monthConversions.keys())
# so structure of a dictionary
 #is the title of the dictionary = {"key": "value"}

# challenge 1
#how do we get data from our dictionary?
# test for understanding
#create a dictionary filled with your favorite actors and movies.
#call the dictionary favActors_Movies
# call the dictionary twice finding at least two movies

#######################loops challenge#####################
# Challenge: Print all even numbers from 1 to 100 using a for loop.

# Loop through numbers 1 to 100
####################################################################################
#while loops = execute some code WHILE some conditions remain true

# name = input("Enter your name ")
# #interation = loop
# #interate (verb) = looping over something
# while name == "":
#     print("You did not enter your name. ")
#     name = input("Enter you name: ")
# print(f"Hello {name}.")

# age = int(input("enter your age "))

# while age < 0:
#     print("age cannot be negative")
#     age = int(input("enter your age "))
# print(f"you are {age} years old")

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"you like {food}.")
#     food = input("Enter another food you like (q to quit): ")

# print("bye!")

# num = int(input("Enter a # between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))

# print(f"your number is {num}")
###############################################################################
#for loops = execute a block of code a fixed number of times.
#           you can iterate over a range, sequence, string, etc.

# for x in range (1, 11):
#     print(x)
# #counting to ten but we add eleven cause thats the first number that's excluded
#     #for loops works for a limit, but while loops work forever

# print("HAPPY NEW YEAR")

# for x in reversed(range(1, 11)):
#     print(x)
# #counting to ten but we add eleven cause thats the first number that's excluded
#     #for loops works for a limit, but while loops work forever

# print("HAPPY NEW YEAR")

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

#continue means skip over
# for x in range (1,21):
#     if x == 13:
#         continue
#     else:
#         print(x)

#break stops loop
# for x in range (1,21):
    # if x == 13:
    #     break
    # else:
    #     print(x)

#create a list of famous horror movie characters
# horror_characters= ["Freddy Krueger", "Jason Voorhees","Micheal Myers", "Pennywise", "Chucky" ]
# #iterate through the list and print each character

# for character in horror_characters:
#     if character == "Jason Voorhees":
#         continue
# print(character)

# if character == "Micheal Myers":
#         character = "Dracula"
# print(character)

# if character == "Pennywise":
#         character = "Ghostface"
# print(character)

horror_movies = ["Terrifer", "Smile", "Halloween", "The Conjuring", "Scream", "The Exorcist"]
for movie in horror_movies:
    if movie == "Terrifer":
        break
print(horror_movies)

for movie in horror_movies:
    if movie == "Smile":
        movie = "Annabelle"
print(horror_movies)

