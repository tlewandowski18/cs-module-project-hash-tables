#Print out all of the strings in the following array in alphabetical order, each on a separate line.
# ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# The expected output is:
# 'Cha Cha'
# 'Foxtrot'
# 'Jive'
# 'Paso Doble'
# 'Rumba'
# 'Samba'
# 'Tango'
# 'Viennese Waltz'
# 'Waltz'
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

#creating a variable that will hold our list
# arr = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

# #sort that list alphabetically ascending

# arr.sort()

# #loop through the array after its sorted and print each item out individually

# for i in range(len(arr)):
#     print(arr[i])

# Print out all of the strings in the following array in alphabetical order sorted by the middle letter of each string, each on a separate line. If the word has an even number of letters, choose the later letter, i.e. the one closer to the end of the string.
# ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# The expected output is:
# 'Cha Cha'
# 'Paso Doble'
# 'Viennese Waltz'
# 'Waltz'
# 'Samba'
# 'Rumba'
# 'Tango'
# 'Foxtrot'
# 'Jive'
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

#find middle letter of each word.
# arr = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive'] 
# letter_arr = []

# obj = {}

# for i in range(len(arr)):
#     string = arr[i].replace(' ', '')
#     if len(string) % 2 == 0:
#         letter = string[(len(string) // 2)]
#     else:
#         letter = string[(len(string) // 2)]
#     #Place in new dictionary with middle as key and original word as value
#     letter_arr.append(letter)


# counter = 1
# for i in range(len(letter_arr)):
#     if letter_arr[i] in obj.keys():
#         new_key = letter_arr[i] + f'{counter}'
#         letter_arr[i] = new_key
#         obj[new_key] = arr[i]
#         counter += 1
#     else:
#         obj[letter_arr[i]] = arr[i]


# letter_arr.sort()

# print(letter_arr)

# for letter in letter_arr:
#     print(obj[letter])



#catch collisions with an if statement to ensure unique key
#loop through the dictionary and print each value individually
