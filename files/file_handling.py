"""

    r = read
    w = write(overwrite)
    a = append (append on exsiting)
    r+ = read and write(append)

"""

# fileObject = open('workfile.txt', 'r')
# readData = fileObject.readline()
# fileObject.close()
# print(fileObject.closed)


# This operation will read your data from existing file
# with open('workfile.txt', 'r') as readObject:
#     readData = readObject.read()
#     print(readData)


# # this operation will opverwrite your data on existing file
# with open('workfile.txt', 'w') as writeObject:
#     writeObject.write('My name is suresh')


# This operation will append your data on existing file content
# with open('workfile.txt', 'a') as appendObject:
#     appendObject.write(' I am python developer')


with open('workfile.txt', 'r+') as fileObject:
    readData = fileObject.read()
    print(readData)
    fileObject.truncate(0)
    fileObject.seek(0)
    fileObject.write('Hello')
