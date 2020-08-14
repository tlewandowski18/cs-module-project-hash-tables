# Your code here
import re

def word_histo(filepath):
    #create histo index
    histo_index = {}
    #open the file and save string to variable
    f = open(filepath).read()
    #split string at spaces
    f = re.split(' |\n|\n\n', f)
    #loop through strings
    for word in f:
        #replace ignored characters with nothing
        alphanumeric_list = [char for char in word if char.isalnum()]
        alphanumeric = "".join(alphanumeric_list)
        #check if word is in histo index
        if alphanumeric in histo_index:
            #if so add a hashmark
            histo_index[alphanumeric] += "#"
        else:
            histo_index[alphanumeric] = "#"
            #else create key with value of one hash mark
    sorted_keys = sorted(histo_index, key=len, reverse=True)
    space_default = len(sorted_keys[0]) + 2
    sorted_index = sorted(histo_index.items(), key=lambda x:x[1], reverse=True)
    for item in sorted_index:
        additional_spaces = " " * (space_default - len(item[0]))
        word = item[0] + additional_spaces
        print(f'{word}  {item[1]}')
    #sort histo_index by values (longest string to shortest)
    #find longest string in histo index and add two spaces to it
    #find number of characters of each key and add enough spaces to equal longest string plus two spaces


file = 'applications/histo/robin.txt'
word_histo(file)

