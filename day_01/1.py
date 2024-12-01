list1 = []
list2 = []

with open("input.txt", "r") as f:
    lines  = f.readlines()
               
for line in lines:
    num1, num2 = line.split()
    list1.append(int(num1))
    list2.append(int(num2))

list1.sort()
list2.sort()

#part 1
sum = 0

for i in range(len(list1)):
    if list1[i] > list2[i]:
        sum += list1[i] - list2[i]
    else:
        sum += list2[i] - list1[i]

print(sum)

#part 2
dict = {}
sum1 = 0

for i in list2:
    dict[i] = dict.get(i, 0) + 1

for i in list1:
    sum1 += i * dict.get(i, 0)

print(sum1)