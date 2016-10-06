# Python 3.5.2
# author: tyler corum
# about: Course: Python, Step 36 of 64

# // start instructions //
# DRILL: 
        
# Write a program in Python 2.7 using IDLE that demonstrates the following concepts. 

# Use comments in your program to denote where you demonstrate each step. If you cannot demonstrate any of these comments, research them online first. If you still have trouble, then ask an Instructor for assistance. 

# 1. Assign an integer to a variable

# 2. Assign a string to a variable

# 3. Assign a float to a variable

# 4. Use the print function and .format() notation to print out the variable you assigned

# 5. Use each of these operators +, ­ , * , / , +=, ­= , %

# 6. Use of logical operators and, or , not

# 7. Use of conditional statements: if, elif, else

# 8. Use of a while loops

# 9. Use of a for loop

# 10. Creating a list and iterate through that list using a for loop to print each item out on a new line

# 11. Create a tuple and iterate through it using a for loop to print each item out on a new line

# 12. Defining a function that returns a string variable

# 13. Call the function you defined above and print the result to the shell

# Once this is completed, email what you wrote to an Instructor.
# // end instructions //

# // start drill //
# step 1:
stepOneIntVar = 5


# step 2:
stepTwoStringVar = "sample string"


# step 3:
stepThreeFloatVar = float(stepOneIntVar)


# step 4a (Python 2.7.12):
# print "These are the variables: \nstepOneIntVar = {}\nstepTwoStringVar = {}\nstepThreeFloatVar = {}".format(stepOneIntVar,stepTwoStringVar,stepThreeFloatVar)

# step 4b (Python 3.5):
print("These are the variables: \nstepOneIntVar = {}\nstepTwoStringVar = {}\nstepThreeFloatVar = {}".format(stepOneIntVar,stepTwoStringVar,stepThreeFloatVar))


# step 5:
x = stepOneIntVar #5
print(5 + x) #10
print(5 - x) #0
print(5 * x) #25
print(5 / x) #1

x += 11
print(x) #16

x -= 2
print(x) #14

if (x % 2 == 0):
    print("x is currently even\n")
else:
    print("x is currently odd\n")


# step 6:
y = 100
z = 14
if (y > x and z > x):
    print('the value of x is pretty small')
elif (y > x or z > x):
    print('don\'t know what to tell you...\neither y is greater than x or z is greater than x')
elif not(y == x):
    print('y does not equal x')
else:
    print('You broke it.')


# step 7:
print('Look up, I accidentally created step 7 already in step 6.')


# step 8:
allowedIn = False
while allowedIn == False:
    ageInputByCustomer = int(input('How old are you? '))
    if (ageInputByCustomer >= 18):
        allowedIn = True
    else:
        print('You\'re not old enough to enter')
        break


# step 9:
for seatForStudent in range(1,31):
    print('You\'re going on the field trip.  Sit in seat #{}'.format(seatForStudent))


# step 10:
horseInfo = {'THIS IS A':'DICTIONARY-LIST\n','name':'freddy','age':15,'type':'mustang',
             'riderName':'danny','wins':11,'losses':2}

for horseInfoKey, horseInfoValue in horseInfo.items():
  print(horseInfoKey, horseInfoValue)


# step 11
horseNamesTuple = ('\nNOW FOR TUPLE:\n','freddy','bonny','charlie','danny','edward','frank')

for index, listEachHorsesNameTuple in enumerate(horseNamesTuple):
  print(listEachHorsesNameTuple)


# step 12
def addTwoNumbers(x,y):
    resultOfAddition = x + y
    convertToString = str(resultOfAddition)
    return convertToString


# step 13
print ('x, {} + stepOneIntVar, {} == {}'.format(x,stepOneIntVar,addTwoNumbers(x, stepOneIntVar)))
