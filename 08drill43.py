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
drillList = (0,1,2,3)
numItemsInDrillList = len(drillList)


# 2. print in order, use range() with 1 param.  i = index
# for i in range(numItemsInDrillList): # <-- need the : colon!
#     print(drillList[i])


# 3. desc order with 3 param
# for (i) in range(numItemsInDrillList,0,-1): # <-- need the : colon!
#     print(drillList[i-1])
# alt:
# for i in reversed(range(0,numItemsInDrillList,1)):
    # print(drillList[i])


# 4. range func with 3 param, 8,6,4,2
for i in reversed(range(0,numItemsInDrillList,1)):
    print(drillList[i]*2+2)



# 5. ///// TEST AREA /////
# for i in reversed(range(numItemsInDrillList)):
#     print(i)

# for i in reversed(range(0,numItemsInDrillList,1)):
#     print(drillList[i]*2+2)