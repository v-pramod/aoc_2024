list1 = []
list2 = []
isFirst = True

with open("input.txt", "r") as f:
   for line in f:
        # Process each line
        for num in line.strip().split("   "):
            if isFirst:
                list1.append(int(num))
                isFirst = not isFirst
            else:
                list2.append(int(num))
                isFirst = not isFirst

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

for i in list2:
    dict[i] = dict.get(i, 0) + 1

sum1 = 0
for i in list1:
    sum1 += i * dict.get(i, 0)

print(sum1)