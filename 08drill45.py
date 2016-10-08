# Python 3.5.2
# Author: Tyler Corum
# Purpose: The Tech Academy Python course drill 45 of 64


# TOC:
# 1. Drill overview
# 2. Creating two lists to be sorted
# 3. define function to sort list in ascending order
# 4. processing the output
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


# 2. Creating two lists to be sorted
listToSort1 = [67, 45, 2, 13, 1, 998]
listToSort2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]


# 3. define function to sort list in ascending order
def sortList_Asc(listIndex):
    lengthOfList = len(listIndex)

    for eachPass in range(lengthOfList-1):
        for i in range(0,lengthOfList-1):
            if listIndex[i] >= listIndex[i+1]:
                temp = listIndex[i]
                listIndex[i] = listIndex[i+1]
                listIndex[i+1] = temp
                if lengthOfList == 2:  #once only a pair left, break so not get stuck in loop
                    break
            else:
                lengthOfList = lengthOfList-1


# 4. processing the output
sortList_Asc(listToSort1)
print(listToSort1)
print('\n')
sortList_Asc(listToSort2)
print(listToSort2)