__author__ = 'kwoshvick'

import re
numberlist = list()
combined_list = list()
integer_list = list()

file = input('Enter File Name:')
fhandler = open(file)

#puts all numbers in a list that contains many lists
for lines in fhandler:
    stripped_lines = lines.strip()
    number = re.findall('[0-9]+' ,stripped_lines)
    if len(number) !=0:
       number_to_int = number
       numberlist.append(number_to_int)

#reduces the masny list to one list
for i in numberlist:
    combined_list+=i

#converts strings to interger
for num in combined_list:
    num=int(num)
    integer_list.append(num)


print(sum(integer_list))

