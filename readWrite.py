#Reading file
file=open('text.txt')
print(file.read(10))
print(file.readline())
print(file.readline())


line=file.readline()
while line!="":
    print(line)
    line=file.readline()


for line in file.readlines():
    print(line)
file.close()

#Writing to a file

#read the file and store all the lines in list
#reverse the list
#write the list back to the file

with open('text.txt','r') as reader:
    content=reader.readlines()
    reversed(content)
    with open('text.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)
