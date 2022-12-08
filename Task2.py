
set1 = [3, 1, 7, 9]
set2 = [2, 4, 1, 9, 3]
distinct =[]
flag=0

#Saving elements of first set
for element1 in set1:
    flag=0
    for element2 in set2:
        if element1 == element2:
            flag=0
            break 
        else:
            flag=1
    if flag ==1:
        distinct.append(element1)
#Saving elements of second set        
for element2 in set2:
    flag=0
    for element1 in set1:
        if element1 == element2:
            flag=0
            break 
        else:
            flag=1
    if flag ==1:
        distinct.append(element2)
        
print(distinct)

#Getting sum
sums=0
for element in distinct:
    sums+=element
print(sums)