# Python104, medium, exercise 1
# translate user input into leet speak
# A = 4
# E = 3
# G = 6
# I = 1
# O = 0
# S = 5
# T = 7

# #GET SENTENCE FROM USER
pgraph = input('Enter a sentence: ')
#make sure naswer is in all caps
pgraph = pgraph.upper()
#declare var to hold the edited paragraph
new_pgraph = ''

#list of letters to be replaced/switched
replaced_letters = (('A', '4'), ('E', '3'), ('G', '6'), ('I', '1'), ('O', '0'), ('S', '5'), ('T', '7'))

# '''for loops nested to 1st declare letters and iterate thru pgraph. 
# 2nd declare old & new_string + iterate thru replaced_letters'''
for letters in pgraph:
    for old_string, new_string in replaced_letters:
        #if statement checks to see if var letters equals old_string... 
        if letters == old_string:
            #..if so letters is assigned to new_string
            letters = new_string
    #new_pgraph var receives the new string with replaced letters
    new_pgraph += letters
#prints sentence in Leek Speak!
print(new_pgraph)

#first attempt, close but no cigar
# for old_string, new_string in replaced_letters:
#     leek = pgraph.replace(old_string, new_string)
#     #print(old_string, new_string)
#     print(leek)

#print(leek)
