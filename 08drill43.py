# python 3.5.2
# author: Tyler Corum
# purpose: The Tech Academy Python course drill 43 of 63
# working with a list, index, range, reverse range
# 
# TOC:
# 1. create list and length of list
# 2. print in order, use range() with 1 param.  i = index
# 3. desc order with 3 param
# 4. range func with 3 param, 8,6,4,2
# 5. ///// TEST AREA /////


# 1. create list and length of list



# 2. print in order, use range() with 1 param.  i = index
print("This is in order, 0,1,2,3")
for i in range(4): # <-- need the : colon!
    print(i)

print("\n")


# 3. desc order with 3 param
print("This is in rev-order, 3,2,1,0")
for (i) in range(3,-1,-1): # <-- need the : colon!
    print(i)

print("\n")



# 4. range func with 3 param, 8,6,4,2
print("This is in rev-order, 8,6,4,2")
for i in range(8,0,-2):
    print(i)




# 5. ///// TEST AREA /////
# for i in reversed(range(4)):
#     print(i)

# for i in reversed(range(0,4,1)):
#     print([i]*2+2)
