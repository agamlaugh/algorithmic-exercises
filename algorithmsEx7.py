list1 = [3,6,9,3,5,1,0]
list2 = [4,-1,-5,7,2,8,-9]
list3 = list1 + list2
list4 = []
counter = 0
min = list3[counter]

while len(list3)>0:
    for x in list3:
        if min>list3[counter]:
            min = list3[counter]
        counter = counter + 1
    list4.append(min)
    list3.remove(min)
    counter = 0
    try:
        min = list3[counter]
    except:
        pass


print(list4)

#IT WORKS!!!!!
