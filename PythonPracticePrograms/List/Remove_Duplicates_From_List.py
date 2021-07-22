# WAP to remove to find duplicates elements in list

list1 = [78,"Green",33,"Green",78,33,78]
#list1 = ['A','B','C','B','A']
print(list1)
for i in list1:
    count = 0
    for j in range(0, len(list1)):
        if i == list1[j]:
            count += 1
        if count > 1:
            list1.pop(j)
            break
print(list1)