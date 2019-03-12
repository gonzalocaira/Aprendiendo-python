
filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

### read mode ('r')
### write mode ('w')
### append mode ('a')
### you to read and write to the file ('r+')

with open(filename,'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
