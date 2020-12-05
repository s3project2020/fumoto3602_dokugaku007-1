for i in range(1,3):
    print(i)
    for letter in ["a","b","c"]:
        print(letter)
# 1
# a
# b
# c
# 2
# a
# b
# c

list1 = [1,2,4,8]
list2 = [5,6,7,8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)
# [6, 7, 8, 9, 7, 8, 9, 10, 9, 10, 11, 12, 13, 14, 15, 16]

while input('y or n?') != 'n':
    for i in range(1,6):
        print(i)

# y or n?y
# 1
# 2
# 3
# 4
# 5
# y or n?y
# 1
# 2
# 3
# 4
# 5
# y or n?n