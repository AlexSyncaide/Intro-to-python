#Define a list
lines=['this is line A', 'this is line B', 'this is line C']
lines
#write the list to the file
with open('/users/alpa/PycharmProjects/WriteToFile1.txt', "w") as writefile:
    for line in lines:
        print(line)
        writefile.write(line)

#check the file content has changed
with open('/users/alpa/PycharmProjects/WriteToFile1.txt', "r") as readfile:
    print('The file text is: '+readfile.read())

#add another line to the file
with open('/users/alpa/PycharmProjects/WriteToFile1.txt', "a") as addfile:
    addfile.write("this is line D")

#read the file as list, make sure it's a list by printing the file content type√
with open('/users/alpa/PycharmProjects/WriteToFile1.txt', "r") as readfile:
    print('After adding a new line the file text is: '+readfile.read())
    file_list = readfile.readlines()
    print(type(file_list))


