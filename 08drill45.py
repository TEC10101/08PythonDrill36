# Python 3.5.2
# Author: Tyler Corum
# Purpose: The Tech Academy Python course drill 45 of 64


# TOC:
# 1. Drill overview
# 2. Creating the method()
# 3. desc order with 3 param
# 4. range func with 3 param, 8,6,4,2
# 5. ///// TEST AREA /////


# 1. Drill overview
# Write your own version of the sorted() method in Python. This method should take a list as an argument and return a list that is sorted in ascending order. Call your method passing in the following lists as arguments and print out each sorted list to the shell. This should should be an algorithm that you write. Do not use .sort() or the sorted() methods in your method.
#  [67, 45, 2, 13, 1, 998]
#  [89, 23, 33, 45, 10, 12, 45, 45, 45]
#  Your sorted lists should look like this when displayed:
#  [1, 2, 13, 45, 67, 998]
#  [10, 12, 23, 33, 45, 45, 45, 45, 89]
#  Your specific algorithm does not need to match the solution your instructor has. It simply needs to work.
#  Once you've designed a program that meets the above qualifications, add it to your GitHub account. Then, send a link to an instructor for viewing.


# 2. Creating the method()
listToSort1 = [67, 45, 2, 13, 1, 998]               #
lengthLTS1 = len(listToSort1)                       # 6
listToSort2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]  #
lengthLTS2 = len(listToSort2)                       # 9

def tylerSort1(listToSort1,lengthLTS1):
    while lengthLTS1 > 1:
        for i in range(0,lengthLTS1-1):
            if listToSort1[i] >= listToSort1[i+1]:
                temp = listToSort1[i]
                listToSort1[i] = listToSort1[i+1]
                listToSort1[i+1] = temp
                if lengthLTS1 == 2:
                    break
            # elif listToSort1[i] == listToSort1[i+1]:
            #     lengthLTS1 = lengthLTS1-1
            else:
                lengthLTS1 = lengthLTS1-1

def tylerSort2(listToSort2,lengthLTS2):
    while lengthLTS2 > 1:
        for i in range(0,lengthLTS2-1):
            if listToSort2[i] >= listToSort2[i+1]:
                temp = listToSort2[i]
                listToSort2[i] = listToSort2[i+1]
                listToSort2[i+1] = temp
                if lengthLTS2 == 2:
                    break
            # elif listToSort2[i] == listToSort2[i+1]:
            #     lengthLTS2 = lengthLTS2-1
            else:
                lengthLTS2 = lengthLTS2-1


tylerSort1(listToSort1,lengthLTS1)
print(listToSort1)
print('\n')
tylerSort2(listToSort2,lengthLTS2)
print(listToSort2)

