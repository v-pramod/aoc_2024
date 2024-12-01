list1 = []
list2 = []
isFirst = True

with open("input.txt", "r") as f:
    lines  = f.readlines()
               
for line in lines:
    num1, num2 = line.split()
    list1.append(int(num1))
    list2.append(int(num2))

# #part 2


