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
pgraph = pgraph.upper()
# print(pgraph)
new_pgraph = ''

replaced_letters = (('A', '4'), ('E', '3'), ('G', '6'), ('I', '1'), ('O', '0'), ('S', '5'), ('T', '7'))

for letter in pgraph:
    for old_string, new_string in replaced_letters:
        if letter == old_string:
            letter = new_string
    new_pgraph += letter
print(new_pgraph)

#first attempt, close but no cigar
# for old_string, new_string in replaced_letters:
#     leek = pgraph.replace(old_string, new_string)
#     #print(old_string, new_string)
#     print(leek)

#print(leek)
