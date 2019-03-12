

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    #print(contents)
    ### If you want to remove the extra blank line
    print(contents.rstrip())

print('\n')

""" READING LINE BY LINE"""
filename = 'pi_digits.txt'

with open(filename) as file_object2:
    for line in file_object2:
        #print(line)
        print(line.rstrip())

print('\n')       
""" Making a list of lines from a file """

with open(filename) as file_object:
   lines = file_object.readlines()

for line in lines:
        print(line.rstrip())
