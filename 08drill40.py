# python 3.5.2
# author: Tyler Corum
# purpose: The Tech Academy Python course drill 40 of 63
# http://www.wikihow.com/Create-a-Very-Simple-Program-in-Python
#
# TOC:
# 1. gather input
# 2. calc age in days min sec
# 3. print output
# 4. 
# 5. 


# 1. gather input
print('Let\'s see how long you have lived in days, minutes and seconds.')
name = input('Name: ')
print('Now enter your age.')


# 2. calc age in days min sec
age = int(input('Age: '))
days = age * 365
minutes = age * 525948
seconds = age * 31556926


# 3. print output
print(name, ' has been alive for ', days,'days ', minutes, 'minutes and ', seconds, 'seconds!  Wow!')