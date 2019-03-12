

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

""" Working with a File's Contents """
print('\n')
    
with open(filename) as file_object:
   lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    #pi_string += line.strip()

print(pi_string[4:]+"...")
print(pi_string[:15]+"...")
print(len(pi_string))


