# Reading Files

dil_file = open("dil.txt", "r")
# print(dil_file.readlines()[1])
for dil in dil_file.readlines():
    print(dil)
 #print(dil_file.readline())
 #print(dil_file.readline())

dil_file.close()
